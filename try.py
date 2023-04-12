import asyncio
from pyppeteer import launch

async def main():
    # Create a headless Chromium browser instance
    browser = await launch(headless=True)

    # Create a new page and navigate to a website
    page = await browser.newPage()
    url = "https://www.investing.com/equities/pre-market"
    await page.goto(url)

    # Extract data from the website
    # ...
      # Retrieve the HTML source code of the page using ISO-8859-1 encoding
    page_content = await page.content(encoding='ISO-8859-1')
    print(page_content)
    # Close the browser
    await browser.close()

# Run the event loop
asyncio.get_event_loop().run_until_complete(main())