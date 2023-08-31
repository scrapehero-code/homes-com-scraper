import asyncio
import json
import logging

from playwright.async_api import async_playwright

location = "Washington Township, OH"
maxPagination = 2


async def extractData(page, selector) -> list:
    """
    parsing details
    from the listing page

    Args:
        page (_type_): webpage of browser
        selector : selector for the div containing
        property details

    Returns:
        list: details of hotels
    """

    # initializing selctors and xpaths
    totalResultsSelector = "[id='spanSearchCount']"
    xpathNextPage = "//button[@title='Next Page']"
    xpathSpecifications = "//ul[@class='detailed-info-container']"
    priceSelector = "[class='price-container']"
    propetyNameSelctor = "[class = 'property-name']"
    descriptionSelector = "//p[@class='property-description']"

    # no of results obtained for the location
    totalResultsCount = await (
        page.locator(totalResultsSelector).inner_text()
        )
    totalResultsCount = totalResultsCount.split()[0]
    logging.warning(
        f"Total results found for {location}- {totalResultsCount}"
        )

    # list to save the details of properties
    homesForSale = []

    # Paginating through each page
    for pageNumber in range(maxPagination):
        # Waiting to finish the loading
        await page.wait_for_load_state("load")

        # Extracting the elements
        allVisibleElements = page.locator(selector)
        allVisibleElementsCount = await allVisibleElements.count()

        for index in range(allVisibleElementsCount):
            # Hovering the element to load the price
            innerElement = allVisibleElements.nth(index=index)
            await innerElement.hover()
            # innerElement = allVisibleElements.nth(index=index)
            # Extracting necessary data
            name = innerElement.locator(propetyNameSelctor)
            name = await name.inner_text() if await name.count() else None

            price = innerElement.locator(priceSelector)
            price = await price.inner_text() if await price.count() else None

            specifications = innerElement.locator(xpathSpecifications)
            specifications = await (
                specifications.inner_text() if await specifications.count() else None
            )
            description = innerElement.locator(descriptionSelector)
            description = await (
                description.inner_text() if await description.count() else None
            )

            specifications = ",".join(specifications.split("\n"))
            # Removing extra spaces and unicode characters
            price = cleanData(price)
            name = cleanData(name)
            description = cleanData(description)
            specifications = cleanData(specifications)

            DatatoSave = {
                "property_name": name,
                "price": price,
                "specificaitons": specifications,
                "description": description,
            }

            homesForSale.append(DatatoSave)

        nextPage = page.locator(xpathNextPage)
        await nextPage.hover()
        if not await nextPage.count():
            break

        # Clicking the next page button
        await nextPage.click()

    saveData(homesForSale, "HomesData.json")


async def run(playwright) -> None:
    # Initializing browser and creating new page.
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    await page.set_viewport_size({"width": 1920, "height": 1080})
    page.set_default_timeout(120000)
    # Navigating to homepage
    await page.goto("https://www.homes.com/", wait_until="domcontentloaded")
    await page.wait_for_load_state(timeout=60000)

    # intializing xpath and selector
    xpath_search_box = "//input[contains(@class,'search')]"
    listing_div_selector = "[class='placard-container']"

    # Clicking the input filed to enter the location and
    # navigates to lisiting page
    await page.locator(xpath_search_box).click()
    await page.locator(xpath_search_box).fill(location)
    await page.locator(xpath_search_box).press("Enter")

    # wait until the list of properties loaded
    await page.wait_for_selector(listing_div_selector)

    await extractData(page, listing_div_selector)

    await context.close()
    await browser.close()


def cleanData(data: str) -> str:
    """
    Cleaning data by removing extra
    white spaces in between and Unicode
    characters

    Args:
        data (str): data to be cleaned

    Returns:
        str: cleaned string
    """
    if not data:
        return
    cleanedData = " ".join(data.split()).strip() if data else None
    cleanedData = cleanedData.encode("ascii", "ignore").decode("ascii")
    return cleanedData


def saveData(product_page_data: list, filename: str):
    """converting list of dictionary to json format

    Args:
        product_page_data (list): details of each
        products
        filename (str): name of json file
    """
    with open(filename, "w") as outfile:
        json.dump(product_page_data, outfile, indent=4)


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == "__main__":
    asyncio.run(main())

