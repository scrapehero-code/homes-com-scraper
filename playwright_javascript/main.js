const { chromium, firefox } = require('playwright');
const fs = require('fs');

const location = "Washington Township, OH";
const maxPagination = 2;

/**
* Save data as list of dictionaries
as json file
* @param {object} data
*/
function saveData(data) {
    let dataStr = JSON.stringify(data, null, 2)
    fs.writeFile("homesDataJS.json", dataStr, 'utf8', function (err) {
        if (err) {
            console.log("An error occurred while writing JSON Object to File.");
            return console.log(err);
        }
        console.log("JSON file has been saved.");
    });
}

function cleanData(data) {
    if (!data) {
        return;
    }
    // removing extra spaces and unicode characters
    let cleanedData = data.split(/\s+/).join(" ").trim();
    cleanedData = cleanedData.replace(/[^\x00-\x7F]/g, "");
    return cleanedData;
}

/**
* The data extraction function used to extract
necessary data from the element.
* @param {HtmlElement} innerElement
* @returns
*/
async function extractData(innerElement) {

    async function extractData(data) {
        let count = await data.count();
        if (count) {
            return await data.innerText()
        }
        return null
    };
    // intializing xpath and selectors
    const xpathSpecifications = "//ul[@class='detailed-info-container']";
    const priceSelector = "[class='price-container']";
    const propetyNameSelctor = "[class = 'property-name']";
    const descriptionSelector = "//p[@class='property-description']";


    // Extracting necessary data
    let name = innerElement.locator(propetyNameSelctor);
    name = await extractData(name);

    let price = innerElement.locator(priceSelector);
    price = await extractData(price);

    let specifications = innerElement.locator(xpathSpecifications);
    specifications = await extractData(specifications);

    let description = innerElement.locator(descriptionSelector);
    description = await extractData(description);

    // cleaning data
    name = cleanData(name)
    price = cleanData(price)
    specifications = cleanData(specifications)
    description = cleanData(description)

    extractedData = {
        'property_name': name,
        'price': price,
        'specifications': specifications,
        'description': description
    }
    console.log(extractData)

    return extractedData
}
/**
* The main function initiate a browser object and handle the navigation.
*/
async function run() {
    // intializing browser and creating new page
    const browser = await chromium.launch({ headless: false });
    const context = await browser.newContext();
    const page = await context.newPage();

    // initializing xpaths and selectors
    const xpathSearchBox = "//input[contains(@class,'search')]";
    const listingDivSelector = "[class='placard-container']";
    const totalResultsSelector = "[id='spanSearchCount']";
    const xpathNextPage = "//button[@title='Next Page']";


    // Navigating to the home page
    await page.goto('https://www.homes.com/', { waitUntil: 'load' });

    // Clicking the input field to enter the location
    await page.waitForSelector(xpathSearchBox);
    await page.click(xpathSearchBox);
    await page.fill(xpathSearchBox, location);
    await page.keyboard.press('Enter');

    // Wait until the list of properties is loaded
    await page.waitForSelector(listingDivSelector);

    const totalResultCount = await page.locator(totalResultsSelector).innerText();
    console.log(`Total results found - ${totalResultCount} for location - ${location}`);

    // to store the extracted data
    let data = [];
    // navigating through pagination
    for (let pageNum = 0; pageNum < maxPagination; pageNum++) {

        await page.waitForLoadState("load");
        await page.waitForTimeout(10);

        let allVisibleElements = page.locator(listingDivSelector);
        allVisibleElementsCount = await allVisibleElements.count()
        // going through each listing element
        for (let index = 0; index < allVisibleElementsCount; index++) {

            await page.waitForTimeout(2000);
            await page.waitForLoadState("load");
            let innerElement = await allVisibleElements.nth(index);
            await innerElement.hover();

            innerElement = await allVisibleElements.nth(index);
            let dataToSave = await extractData(innerElement);
            data.push(dataToSave);
        };
        //to load next page
        let nextPage = page.locator(xpathNextPage);
        await nextPage.hover();
        if (await nextPage.count()) {
            await nextPage.click();
        }
        else { break };
    };
    saveData(data);
    await context.close();
    await browser.close();
};

run();
