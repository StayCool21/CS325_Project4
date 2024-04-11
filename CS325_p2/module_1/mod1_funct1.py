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
    if not urls:
        raise ValueError("URLs not found in file")
    return urls

def get_raw_from_file(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    stories = []
    for story in soup:
        line = story.text
        stories.append({'line': line})
    return stories