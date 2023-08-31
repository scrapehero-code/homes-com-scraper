import asyncio
import json

from playwright.async_api import Playwright, async_playwright

data = []
zip_code = "10001"
pagination_limit = 2


def save_data():
    """
    Saving the globaly stored data as json
    """
    with open("Homes_data.json", "w") as outfile:
        json.dump(data, outfile, indent=4)


async def parse_product_page(page):
    """
    Parses information from a product page and extracts relevant details.

    This function takes a browser page object and extracts various details from
    the product page using XPath locators. It waits for the DOM to be fully loaded
    before attempting to locate and retrieve the information.

    Args:
        page (Page): The browser page object representing the product page.

    """

    xpath_price = "//span[@id='price']"
    xpath_beds = "//span[contains(@class, 'beds')]/span[contains(@class, 'detail')]"
    xpath_baths = "//span[@class='property-info-feature']/span[contains(@class, 'detail')]"
    xpath_sqft = "//span[contains(@class, 'sqft')]/span[contains(@class, 'detail')]"
    xpath_hao_fee = "//span[contains(@class, 'hoaFee')]/span[contains(@class, 'detail')]"
    xpath_address_line_1 = "//h1[@class='property-info-address-main']"
    xpath_address_line_2 = "//span[@class='property-info-address-citystatezip']"
    xpath_about = "//p[@class='ldp-description-text']"

    price = await page.locator(xpath_price).inner_text()
    beds = await page.locator(xpath_beds).inner_text()
    baths = await page.locator(xpath_baths).inner_text()
    sqft = await page.locator(xpath_sqft).inner_text()
    hao_fee = await page.locator(xpath_hao_fee).inner_text()
    address_line_1 = await page.locator(xpath_address_line_1).inner_text()
    address_line_2 = await page.locator(xpath_address_line_2).inner_text()
    about = await page.locator(xpath_about).all_inner_texts()

    data_to_save = {
        "price": price,
        "beds": beds,
        "baths": baths,
        "sqft": sqft,
        "hao_fee": hao_fee,
        "address_line_1": address_line_1,
        "address_line_2": address_line_2,
        "about": " ".join(about).strip(),
    }
    data.append(data_to_save)


async def parse_listing_page(page, current_page):
    """
    Iterates through a listing page, extracts information from individual listings,
    and handles pagination to continue parsing subsequent pages.

    This function takes a browser page object, representing a listing page, and the
    current page number. It locates each individual listing element on the page, clicks
    on it to open a popup with details, parses the details using 'parse_product_page',
    and then closes the popup. After processing all listings on the current page, it
    checks for pagination, clicks the 'Next Page' button if available, and recursively
    calls itself to parse the next page.

    Args:
        page (Page): The browser page object representing the listing page.
        current_page (int): The current page number being parsed.
    """
    xpath_products = "//ul[@class='placards-list']/li//a[@title]"
    xpath_next_page = '//button[@title="Next Page"]'

    await page.wait_for_timeout(5000)

    listed_homes = page.locator(xpath_products)
    listed_homes_count = await listed_homes.count()

    for i in range(listed_homes_count):
        item_element = listed_homes.nth(i)
        async with page.expect_popup() as page_1_info:
            await item_element.click()
            page_1 = await page_1_info.value
            await page_1.wait_for_load_state(timeout=60000)
            await parse_product_page(page_1)
            await page_1.close()

    # Pagination
    next_page = page.locator(xpath_next_page)
    if await next_page.count() > 0 and current_page <= pagination_limit:
        current_page += 1
        await next_page.click()
        await parse_listing_page(page, current_page)


async def parse_search(page):
    """
    Performs a search operation on a webpage by entering a ZIP code into a search box.

    This function takes a browser page object and interacts with a search box element
    on the page. It clicks on the search box, types the provided ZIP code with a slight
    delay between keystrokes, presses the 'Enter' key, and waits for the page to finish
    loading. The resulting page is returned after the search operation is completed.

    Args:
        page (Page): The browser page object to perform the search on.

    Returns:
        Page: The updated browser page object after the search operation.
    """
    xpath_search_box = "//input[contains(@class, 'multiselect-search')]"

    await page.locator(xpath_search_box).click()
    await page.locator(xpath_search_box).type(zip_code, delay=200)
    await page.wait_for_load_state("domcontentloaded")
    await page.locator(xpath_search_box).press("Enter")
    await page.wait_for_load_state("domcontentloaded")
    return page


async def run(playwright: Playwright) -> None:
    """
    Orchestrates a web scraping process using the Playwright library.

    Launches a Chromium browser instance, navigates to a URL, performs
    parsing operations, and closes the browser after saving data.

    Args:
        playwright (Playwright): The Playwright instance for browser operations.

    Returns:
        None
    """

    # Initializing browser, context and a new pge
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    url = "https://www.homes.com/"
    await page.goto(url, wait_until="domcontentloaded")
    page = await parse_search(page=page)
    page = await parse_listing_page(page, 1)
    save_data()

    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
