"""
ZenRows-based web scraping demo.

This script demonstrates how ZenRows can be used as a managed
access layer to fetch HTML content from a website and extract
basic structured information using BeautifulSoup.

Target site:
https://example.com
(This is a public demo domain commonly allowed by scraping services.)
"""

import os
import csv
import requests
from typing import List, Dict
from bs4 import BeautifulSoup
from dotenv import load_dotenv


class ZenRowsClient:
    """
    Handles communication with the ZenRows API.
    """

    BASE_URL = "https://api.zenrows.com/v1/"

    def __init__(self, api_key: str, js_render: bool = False, timeout: int = 30):
        self.api_key = api_key
        self.js_render = js_render
        self.timeout = timeout

    def fetch_html(self, target_url: str) -> str:
        """
        Fetch HTML content for a given URL via ZenRows.
        """
        params = {
            "apikey": self.api_key,
            "url": target_url,
            "js_render": str(self.js_render).lower(),
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.text


class ExampleParser:
    """
    Parses basic content from example.com.
    """

    def parse(self, html: str) -> List[Dict[str, str]]:
        """
        Extracts title, heading, and paragraph text.
        """
        soup = BeautifulSoup(html, "html.parser")
        results: List[Dict[str, str]] = []

        title = soup.title.get_text(strip=True) if soup.title else ""
        heading = soup.find("h1").get_text(strip=True) if soup.find("h1") else ""
        paragraph = soup.find("p").get_text(strip=True) if soup.find("p") else ""

        results.append({
            "title": title,
            "heading": heading,
            "paragraph": paragraph
        })

        return results


class CSVWriter:
    """
    Writes structured data to a CSV file.
    """

    def write(self, data: List[Dict[str, str]], file_path: str) -> None:
        if not data:
            print("No data extracted. CSV file not created.")
            return

        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


class ExampleScraper:
    """
    Orchestrates the ZenRows scraping workflow.
    """

    def __init__(
        self,
        client: ZenRowsClient,
        parser: ExampleParser,
        writer: CSVWriter
    ):
        self.client = client
        self.parser = parser
        self.writer = writer

    def run(self, url: str, output_file: str) -> None:
        html = self.client.fetch_html(url)
        parsed_data = self.parser.parse(html)
        self.writer.write(parsed_data, output_file)


def main() -> None:
    load_dotenv()

    api_key = os.getenv("ZENROWS_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "ZENROWS_API_KEY not found. Please set it in the environment variables."
        )

    zenrows_client = ZenRowsClient(
        api_key=api_key,
        js_render=False  # example.com does not require JS rendering
    )

    parser = ExampleParser()
    writer = CSVWriter()
    scraper = ExampleScraper(zenrows_client, parser, writer)

    scraper.run(
        url="https://example.com",
        output_file="example_output.csv"
    )


if __name__ == "__main__":
    main()