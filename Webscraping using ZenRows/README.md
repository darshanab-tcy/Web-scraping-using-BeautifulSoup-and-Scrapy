# Web Scraping using ZenRows

This module demonstrates how to use ZenRows as a managed web scraping access layer in Python. The primary objective is to understand ZenRows integration within a scraping pipeline rather than large-scale data extraction.

ZenRows is used here to handle request routing, headers, and basic anti-bot mechanisms so that the scraping logic remains clean, modular, and production-oriented.

## Why ZenRows?

ZenRows is useful when traditional scraping approaches face limitations such as IP blocking, bot detection, request fingerprinting, or aggressive rate limiting. Instead of manually managing proxies, headers, and retries, ZenRows acts as an external access layer.

## Target Website Used

https://example.com

This is a public demo domain commonly allowed by scraping services and is used here to validate ZenRows integration under trial account constraints. Some popular scraping demo sites such as quotes.toscrape.com or books.toscrape.com may be restricted or blocked under ZenRows trial plans.

## Project Structure
```
Webscraping using ZenRows/
├── scraper.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env (not committed)
```
## How the Script Works

1. Reads the ZenRows API key from environment variables  
2. Sends a request to the ZenRows API with the target URL  
3. Receives raw HTML content from ZenRows  
4. Parses the HTML using BeautifulSoup  
5. Extracts basic page information such as page title, headings, and text content  
6. Writes the extracted data to a CSV file  

## Setup Instructions

Create and activate a virtual environment:

python -m venv venv  
venv\Scripts\activate  

Install dependencies:

pip install -r requirements.txt  

Create a .env file:

ZENROWS_API_KEY=your_api_key_here  

Run the script:

python scraper.py  

## Output

example_output.csv

This confirms that the ZenRows API access is working correctly and that HTML fetching, parsing, and CSV export have executed successfully.

## Limitations and Notes

ZenRows trial accounts may restrict access to certain websites. This example focuses on validating integration and architecture rather than data volume. Parsing logic must always be customized for each target website in real-world use cases.

## Key Takeaway

ZenRows is not a replacement for BeautifulSoup, Scrapy, or Playwright. It is an access layer that becomes valuable when websites block standard scraping techniques.