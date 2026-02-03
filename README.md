# Web Scraping using BeautifulSoup and Scrapy

This repository demonstrates web scraping techniques using **BeautifulSoup** and **Scrapy** in Python.  
The project focuses on extracting structured data from a publicly available website and exporting it to CSV format.

---

## Objectives
- Demonstrate static web scraping using BeautifulSoup.
- Implement pagination handling across multiple pages.
- Demonstrate scalable scraping using Scrapy.
- Demonstrate JavaScript-rendered scraping using Playwright.
- Explore CAPTCHA-aware scraping workflows.
- Store scraped data in structured CSV files.

---

## Website Used
- https://quotes.toscrape.com  
This website is intended for scraping practice and does not require authentication.
---

## Tools & Libraries
- Python
- BeautifulSoup
- Requests
- Scrapy
- Playwright
- Pandas
- Jupyter Notebook

---

## Project Structure 
```
Web-scraping-using-BeautifulSoup-and-Scrapy/
│
├── Web scraping using BeautifulSoup/
│   ├── Web scraping using BeautifulSoup.ipynb
│   └── data/
│       ├── quotes.csv
│       └── quotes_bs4.csv
│
├── Web scraping using Scrapy/
│   ├── scrapy.cfg
│   ├── requirements.txt
│   ├── quotes_project/
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders/
│   │       ├── __init__.py
│   │       └── quotes_spider.py
│   └── data/
│       └── quotes_scrapy.csv
│
├── Captcha solver scraper/
│   ├── Web scraping using Captcha solver.ipynb
│   └── README.md
├── Web scraping using Playwright/
│   ├── playwright_scraper.py
│   ├── requirements.txt
│   ├── data/
│   │   └── quotes_playwright.csv
│   └── README.md
├── README.md
└── .gitignore
```
---

## BeautifulSoup Scraping
- Sends HTTP requests to static web pages.
- Parses HTML using BeautifulSoup.
- Extracts quote text, author, and tags.
- Handles pagination by detecting "Next" links.
- Saves results to CSV using Pandas.

---

## Scrapy Scraping
- Uses Scrapy spider for structured crawling.
- Automatically handles pagination.
- Faster and more scalable than manual scraping.
- Outputs data directly to CSV.

---

## Output Data
- Quote text
- Author name
- Associated tags

---

## Notes
- This project focuses on **static web scraping**.
- No browser automation was used.

---

## Key Takeaways
- BeautifulSoup is suitable for simple to medium scraping tasks.
- Scrapy is preferred for larger, scalable scraping pipelines.
- Proper project structure and version control are essential.

## CAPTCHA-Aware Scraping (Exploratory)

This repository also includes an **exploratory CAPTCHA-aware scraping module** located in:

`Captcha solver scraper/`

This module demonstrates:
- CAPTCHA detection in scraping workflows
- Integration points for third-party solver services (e.g., 2Captcha)
- Request retry logic after CAPTCHA resolution

📄 Detailed documentation for this module is available in the  
**README inside the `Captcha solver scraper` folder**.

## Playwright Scraping
- Used for scraping JavaScript-rendered web pages.
- Executes a real browser to allow JavaScript to run.
- Extracts data from the rendered DOM.
- Handles pagination through browser interactions.
- Suitable for dynamic websites where static scraping fails.

## Tool Selection Summary
- **BeautifulSoup** is used for static and exploratory scraping.
- **Scrapy** is used for scalable and structured crawling pipelines.
- **Playwright** is used for JavaScript-rendered and interactive websites.
- **CAPTCHA-aware logic** demonstrates handling protected scraping scenarios.

Tool selection is based on how the website delivers content, not just the data being extracted.

## Legal & Ethical Disclaimer
This repository contains web scraping examples using BeautifulSoup, Scrapy, and Playwright for educational and demonstration purposes only.

All examples operate on publicly accessible demo data and do not involve scraping private, sensitive, or authenticated content.  
This project does not encourage or support bypassing website security mechanisms or violating terms of service.

