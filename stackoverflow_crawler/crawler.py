"""Crawler."""

import os
import csv
from lxml import html
import requests

def _get_page_and_tree(url):
    """Return app's page from google play."""
    page = requests.get(url)
    tree = html.fromstring(page.content)
    return page, tree

def get_results_count(query):
    "Get number of results from query."
    url = "https://stackoverflow.com/search?q={}".format(query)
    page, tree = _get_page_and_tree(url)
    results_count = tree.xpath('//div[@class="subheader results-header"]/h2')
    if len(results_count):
        return int(results_count[0].text.replace(',',''))
    else:
        print ("Could not fetch results for {}.".format(query))
        return 0

if __name__ == "__main__":
    get_results_count('amen')

