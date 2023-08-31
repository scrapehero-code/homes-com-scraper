# Homes.com Scraper using Playwright Javascript

Step 1:  Clone/download the repo to your local system.

Step 2: cd into the `playwright_javascript` directory.

Step 3: Install the dependencies mentioned in the `package.json` file using the command.
>`npm install`

Step 4: Install the necessary browsers required for playwright 
>`playwright install`

Step 5: Run the scraper code using
>` node main.js`


<br>

>:bulb: ***To collect property listing data from Homes.com on scale and without code visit [Scrapehero Cloud](https://www.scrapehero.com/marketplace/homes-com-scraper/).***

<br>

>:memo: ***More resources on scraping and other related topics can be found [here](https://www.scrapehero.com/articles/).***

The results will be stored into a `homesDataJS.json` in your project directory.
Using the search_term as `Texas Homes for Sale` in Homes.com, we get the sample data shown below.

```json
{
    "address": "2705 Bayrose Dr, La Marque, TX, 77568",
    "agent_email": "vernardlewis1414@gmail.com",
    "agent_phone_number": "(713) 489-8130",
    "agent_url": "https://www.homes.com/real-estate-agents/vernard-lewis/rmvbx03/",
    "area": "1,651",
    "baths": "2.0",
    "beds": "3",
    "city": "La Marque",
    "days_on_market": "3",
    "description": " Absolutely stunning new condition home in master planned Lago Mar! gated community, 3 bedroom, 2 bathroom Residents enjoy top-notch amenities that include the two fitness centers, resort-style pools, parks, a splash pad, a soccer field, golf cart/walking trails, & a 12-acre lagoon with beach club access! ",
    "estimate_annual_tax": null,
    "estimate_mortgage": "",
    "exterior_features": [
        {
            "Disclosures": "Municipal Utility District Disclosure, Seller Disclosure"
        },
        {
            "Roof": "Composition"
        },
        {
            "Lot Features": "Subdivision"
        },
        {
            "Pool Private": "No"
        },
        {
            "Construction Type": "Brick, Other"
        },
        {
            "Foundation Details": "Slab"
        }
    ],
    "garage_or_parking": [
        {
            "Attached Garage": "Yes"
        },
        {
            "Non Garaged Spaces": "2.0"
        },
        {
            "Parking Features": "Attached, Garage"
        }
    ],
    "hoa": 150.0,
    "images": [
        "https://images.homes.com/listings/102/3759465533-345357851-original.jpg",
        "https://images.homes.com/listings/117/0220565533-345357851-original.jpg",
        "https://images.homes.com/listings/117/8420565533-345357851-original.jpg",
        "https://images.homes.com/listings/117/2220565533-345357851-original.jpg",
        "https://images.homes.com/listings/117/3520565533-345357851-original.jpg",
        "https://images.homes.com/listings/117/4220565533-345357851-original.jpg",
        "https://images.homes.com/listings/117/0620565533-345357851-original.jpg",
        "https://images.homes.com/listings/117/5220565533-345357851-original.jpg",
        "https://images.homes.com/listings/117/7220565533-345357851-original.jpg",
        "https://images.homes.com/listings/117/8220565533-345357851-original.jpg",
        "https://images.homes.com/listings/117/2320565533-345357851-original.jpg",
        "https://images.homes.com/listings/117/6320565533-345357851-original.jpg",
        "https://images.homes.com/listings/117/1420565533-345357851-original.jpg",
        "https://images.homes.com/listings/117/4420565533-345357851-original.jpg"
    ],
    "interior_features": [
        {
            "Appliances": "Dishwasher, Disposal, Microwave, Trash Compactor"
        },
        {
            "Full Bathrooms": "2"
        },
        {
            "Total Bedrooms": "3"
        },
        {
            "Living Area": "1651.0"
        },
        {
            "ResoLivingAreaSource": "PublicRecords"
        }
    ],
    "land_area": "",
    "latitude": 29.40765,
    "listing_agent": "Vernard Lewis",
    "listing_date": "08/28/2023",
    "listing_details": [
        {
            "Directions": "From Houston, take I-45S to exit 19. Merge onto Gulf Fwy, then turn right onto Lago Mar Blvd. Turn right onto Gales Point Dr, then turn right onto Bayrose Dr."
        },
        {
            "Property Sub Type": "Detached"
        },
        {
            "Prop. Type": "Residential"
        },
        {
            "Building Stories": "1"
        },
        {
            "Year Built": "2020"
        },
        {
            "Lot Size Acres": "0.152"
        },
        {
            "Cumulative Days on Market": "110"
        },
        {
            "Subdivision Name": "Lago Mar Pod 6 Sec 2"
        },
        {
            "Architectural Style": "Traditional"
        },
        {
            "Garage Yn": "Yes"
        },
        {
            "Unit Levels": "One"
        },
        {
            "New Construction": "No"
        },
        {
            "Special Features": "None"
        },
        {
            "Stories": "1"
        }
    ],
    "listing_type": "Resale",
    "listing_url": "https://www.homes.com/texas-city-tx/p1/",
    "longitude": -95.05066,
    "mls_key": "w56x04h",
    "price": 315000.0,
    "property_count": "1",
    "property_type": "Single Family",
    "property_url": "https://www.homes.com/property/2705-bayrose-dr-la-marque-tx/0ltx9stgmpmh6/",
    "utilities": [
        {
            "Cooling": "Central Air, Electric"
        },
        {
            "Cooling Y N": "Yes"
        },
        {
            "Heating": "Central, Electric"
        },
        {
            "Heating Yn": "Yes"
        },
        {
            "Sewer": "Public Sewer"
        },
        {
            "Water Source": "Public"
        }
    ],
    "year_build": 2020
},

```
