# Imports: os is used to write to files, requests handles HTTP  requests, and beautifulsoup is used to pull HTML from sites

# get_url_from_file: this function takes in and then opens the text file 'urls.txt' and reads each line of it to create a list of urls
# which is then returned to be iterated through by run.py and other functions. 

# get_raw_from_url: function takes in a url, which is then opened and scraped by beautifulsoup commands. Very similar to get_news_from_url, rather than 
# using a specific tag to limit the search, it just takes all of it and appends it to the array. it then returns this array for run.py to use.

# SOLID Principle: My project reflects the use of Single Responsibility Principle (SRP) by separating out each task into its own function/method.
# Each function is in charge of handling one thing alone- getting news, writing to file, getting raw, and pulling urls. 
# This made it easier to test functions independently of each other as well as reusability, 
# since I am able to reuse writing to file as it only needs an array and a file name. 

import requests
from bs4 import BeautifulSoup

def get_url_from_file(file):
    with open(file, 'r', encoding="utf-8") as f:
        urls = [line.strip() for line in f.readlines()]
    # Test Case #1: If it finds that there are no URLs, returns error saying so
    if not urls:
        raise ValueError("URLs not found in file- please check url.txt")
    # Test Case #8: check if we have a duplicate URL
    # ... and if so, remove it
    unique_urls = list(set(urls))

    if len(unique_urls) != len(urls):
        duplicate_urls = [url for url in urls if urls.count(url) > 1]
        print(f"Duplicate URLs found: {duplicate_urls}")

    return unique_urls

def get_raw_from_file(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    stories = []
    for story in soup:
        line = story.text
        stories.append({'line': line})
    # Test Case #5: Checking if file array has been written to correctly
    if(len(stories)==0):
        raise ValueError('No text was created- empty file')
    else:
        return stories

# Test Case #7: Check if all input URLs are from CBS Sports
# we will be calling this in run.py to ensure modularity
def ensure_cbsnews_domain(urls):
    cbsnews_domain = "https://www.cbsnews.com" # I believe we need HTTPS for Beautiful Soup to work
    for url in urls:
        if cbsnews_domain not in url:
            raise ValueError(f"URL {url} is not from CBS News")
        
# Test Case #2: Check that all URLs are accessbile using GET requests
# returns a list of failed URLs
def test_urls(urls):
    # create array to store failed URLs
    failed_urls = []
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code != 200: # 200 is the HTTP status code for "OK"
                failed_urls.append(url)
        except Exception as e:
            print(f"Error in accessing URL {url}: {e}")

    if failed_urls:
        print("The following URLs failed to load:")
        for url in failed_urls:
            print(url)
    