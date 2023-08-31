# Homes.com Scraper using Playwright Python

Step 1: Clone/download the repo to your local system.

Step 2: cd into the playwright_python directory.

Step 3: Install the requirements.txt using

     pip install -r requirements.txt

Step 4: Install the necessary browsers required for playwright

    playwright install

Step 5: Run the scraper code using

     python main.py




<br>

>:bulb: ***To collect property listing data from Homes.com on scale and without code visit [Scrapehero Cloud](https://www.scrapehero.com/marketplace/homes-com-scraper/).***

<br>

>:memo: ***More resources on scraping and other related topics can be found [here](https://www.scrapehero.com/articles/).***

The results will be stored into a HomesData.json in your project directory. Using the **search_term as Texas homes in Homes.com**, we get the sample data shown below.


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
{
    "address": "3310 Voyager Dr, Texas City, TX, 77591",
    "agent_email": "jason@frgrpllc.com",
    "agent_phone_number": "(281) 799-3598",
    "agent_url": null,
    "area": "2,212",
    "baths": "2.5",
    "beds": "4",
    "city": "Texas City",
    "days_on_market": "5",
    "description": " Welcome home to Herons Landing! This home was built in 2020 and has just undergone a full update and renovation. The all new flooring ties this open concept home together perfectly. The living room offer an abundance of natural light through the double pane windows. The kitchen is just off the living area and offers a smooth s=transition with island. It is perfect for entertaining friends and family. The primary bedroom is tucked away in the back of the home for privacy and includes a large walk in closet, double vanity and separate tub & shower. The second story provides 3 additional bedrooms, full bath and a game room. The upgrades on this home are too many to list, but include all new paint throughout, new bathroom vanities, redesign of the primary bath, all new flooring, all new fixtures, etc. Be sure to call today for a tour before this one is gone! ",
    "estimate_annual_tax": 5004.0,
    "estimate_mortgage": "",
    "exterior_features": [
        {
            "Disclosures": "Other, Seller Disclosure"
        },
        {
            "Roof": "Composition"
        },
        {
            "Fencing": "Back Yard"
        },
        {
            "Lot Features": "Subdivision"
        },
        {
            "Pool Private": "No"
        },
        {
            "Construction Type": "Brick, Wood Siding"
        },
        {
            "Direction Faces": "Southwest"
        },
        {
            "Exterior Features": "Covered Patio, Deck, Fence, Porch, Patio, Private Yard"
        },
        {
            "Foundation Details": "Slab"
        },
        {
            "Patio And Porch Features": "Covered, Deck, Patio, Porch"
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
    "hoa": 50.0,
    "images": [
        "https://images.homes.com/listings/102/2224494533-998037851-original.jpg",
        "https://images.homes.com/listings/117/9224494533-998037851-original.jpg",
        "https://images.homes.com/listings/117/7074494533-998037851-original.jpg",
        "https://images.homes.com/listings/117/0324494533-998037851-original.jpg",
        "https://images.homes.com/listings/117/9764494533-998037851-original.jpg",
        "https://images.homes.com/listings/117/0864494533-998037851-original.jpg",
        "https://images.homes.com/listings/117/1864494533-998037851-original.jpg",
        "https://images.homes.com/listings/117/2864494533-998037851-original.jpg",
        "https://images.homes.com/listings/117/3864494533-998037851-original.jpg",
        "https://images.homes.com/listings/117/4864494533-998037851-original.jpg",
        "https://images.homes.com/listings/117/5864494533-998037851-original.jpg",
        "https://images.homes.com/listings/117/6864494533-998037851-original.jpg"
    ],
    "interior_features": [
        {
            "Appliances": "Convection Oven, Dishwasher, Disposal, Gas Range, Microwave, ENERGY STAR Qualified Appliances, Refrigerator"
        },
        {
            "Full Bathrooms": "2"
        },
        {
            "Half Bathrooms": "1"
        },
        {
            "Total Bedrooms": "4"
        },
        {
            "Flooring": "Carpet, Plank, Vinyl"
        },
        {
            "Interior Amenities": "Breakfast Bar, Crown Molding, Central Vacuum, Entrance Foyer, High Ceilings, Kitchen Island, Kitchen/Family Room Combo, Pots & Pan Drawers, Pantry, Window Treatments, Ceiling Fan(s), Programmable Thermostat"
        },
        {
            "Living Area": "2212.0"
        },
        {
            "Window Features": "Low Emissivity Windows"
        },
        {
            "ResoLivingAreaSource": "PublicRecords"
        }
    ],
    "land_area": "",
    "latitude": 29.41358,
    "listing_agent": "Jason Franklin",
    "listing_date": "08/26/2023",
    "listing_details": [
        {
            "Directions": "Going South on I-45 go until you turn Left onto FM 517, then turn Right onto HWY 3, then turn Right onto Central Park Blvd, then turn Left on Sprite Ln and then Right onto Voyager Dr, the house will be on the Right."
        },
        {
            "Property Sub Type": "Detached"
        },
        {
            "Prop. Type": "Residential"
        },
        {
            "Building Stories": "2"
        },
        {
            "Year Built": "2020"
        },
        {
            "Lot Size Acres": "0.1435"
        },
        {
            "Ownership": "Full Ownership"
        },
        {
            "Cumulative Days on Market": "3"
        },
        {
            "Days On Market": "3"
        },
        {
            "Subdivision Name": "Herons Lndg Sec 2"
        },
        {
            "Architectural Style": "Traditional"
        },
        {
            "Garage Yn": "Yes"
        },
        {
            "Unit Levels": "Two"
        },
        {
            "New Construction": "No"
        },
        {
            "Efficiency": "Appliances, HVAC, Insulation, Lighting, Solar Panel(s), Thermostat, Windows"
        },
        {
            "Special Features": "None"
        },
        {
            "Stories": "2"
        }
    ],
    "listing_type": "Resale",
    "listing_url": "https://www.homes.com/texas-city-tx/p1/",
    "longitude": -95.00946,
    "mls_key": "w56x04h",
    "price": 319900.0,
    "property_count": "1",
    "property_type": "Single Family",
    "property_url": "https://www.homes.com/property/3310-voyager-dr-texas-city-tx/t8hmphj7fbzj7/",
    "utilities": [
        {
            "Laundry Features": "Washer Hookup, Electric Dryer Hookup"
        },
        {
            "Security": "Prewired, Smoke Detector(s)"
        },
        {
            "Cooling": "Central Air, Electric"
        },
        {
            "Cooling Y N": "Yes"
        },
        {
            "Heating": "Central, Gas"
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
{
    "address": "12705 S Shore Dr, Texas City, TX, 77591",
    "agent_email": "kevin4scott@hotmail.com",
    "agent_phone_number": "(713) 665-8329",
    "agent_url": "https://www.homes.com/real-estate-agents/kevin-scott/p7d7dss/",
    "area": "1,691",
    "baths": "2.0",
    "beds": "3",
    "city": "Texas City",
    "days_on_market": "1",
    "description": " 12705 S shore is a gorgeous 3BR, 2Bath brick home tucked within the sought after Lago Mar masterplanned community. Efficient floorplan, huge windows, pristine walls, and posh decorative lightings create an ambient interior ideal for relaxation. Gourmet kitchen with island and lots of storage spaces is decked with Granite countertop and subway tile. The elegant living area provides access to the covered patio and expansive backyard – with no back neighbors! Cap off the day and indulge into tranquil comfort in the Primary Bedroom with huge walk-in closet and ensuite bath with double sinks and glass-enclosed shower. Resort-style amenities including a 12-acre crystal lagoon and excellent proximity to major employment centers and entertainment venues via Interstate 45 South await you on this gem. Don’t miss out - schedule your showing today! ",
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
            "Fencing": "Back Yard"
        },
        {
            "Lot Features": "Subdivision"
        },
        {
            "Pool Private": "No"
        },
        {
            "Construction Type": "Brick, Cement Siding"
        },
        {
            "Exterior Features": "Deck, Fence, Patio"
        },
        {
            "Foundation Details": "Slab"
        },
        {
            "Patio And Porch Features": "Deck, Patio"
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
    "hoa": 108.0,
    "images": [
        "https://images.homes.com/listings/102/5620757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/4920757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/2330757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/7920757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/6330757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/1030757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/9330757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/4030757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/5941757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/7030757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/9941757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/1130757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/4051757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/6130757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/9051757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/2230757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/3151757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/5230757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/0251757533-797987851-original.jpg",
        "https://images.homes.com/listings/117/9230757533-797987851-original.jpg"
    ],
    "interior_features": [
        {
            "Appliances": "Dishwasher, Gas Cooktop, Disposal, Gas Oven, Microwave, Refrigerator"
        },
        {
            "Full Bathrooms": "2"
        },
        {
            "Possible Bedrooms": "3"
        },
        {
            "Total Bedrooms": "3"
        },
        {
            "Flooring": "Tile"
        },
        {
            "Interior Amenities": "Breakfast Bar, High Ceilings, Kitchen Island, Kitchen/Family Room Combo, Window Treatments"
        },
        {
            "Living Area": "1691.0"
        },
        {
            "ResoLivingAreaSource": "PublicRecords"
        }
    ],
    "land_area": "",
    "latitude": 29.42566,
    "listing_agent": "Kevin Scott",
    "listing_date": "08/29/2023",
    "listing_details": [
        {
            "Directions": "I-45 South to right onto Lago Mar Blvd., left onto Lago Front Dr., right onto Del Mar Dr., right onto S Shore Drive."
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
            "Year Built": "2018"
        },
        {
            "Lot Size Acres": "0.1329"
        },
        {
            "Ownership": "Full Ownership"
        },
        {
            "Subdivision Name": "Lago Mar Pod 7 Sec 3"
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
    "longitude": -95.06084,
    "mls_key": "w56x04h",
    "price": 310500.0,
    "property_count": "1",
    "property_type": "Single Family",
    "property_url": "https://www.homes.com/property/12705-s-shore-dr-texas-city-tx/tjyddnx2swkgb/",
    "utilities": [
        {
            "Laundry Features": "Washer Hookup, Electric Dryer Hookup"
        },
        {
            "Security": "Prewired"
        },
        {
            "Cooling": "Central Air, Electric"
        },
        {
            "Cooling Y N": "Yes"
        },
        {
            "Heating": "Central, Gas"
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
    "year_build": 2018
},
```

