# Imports: os is used to write to files, requests handles HTTP  requests, and beautifulsoup is used to pull HTML from sites

# get_news_from_url: function takes in a url, which is then opened and scraped by beautifulsoup commands. Very similar to get_raw_from_url, however
# the find_all narrows down what html is used, through <p> class "sc-eb7bd5f6-0 fYAfXe" which contains only the news information.
# To make it easier to handle, each sentence is put into an array for better organization. It then returns this array for run.py to use.

# write_stories_to_file: This function takes in an array of the news information as well as the anticipated output file name. 
# using os, it iterates through the array and appends it to the ouput file. 
# i also included a try/except block for error handling purposes if there is issues locating/creating the files.

# SOLID Principle: My project reflects the use of Single Responsibility Principle (SRP) by separating out each task into its own function/method.
# Each function is in charge of handling one thing alone- getting news, writing to file, getting raw, and pulling urls. 
# This made it easier to test functions independently of each other as well as reusability, 
# since I am able to reuse writing to file as it only needs an array and a file name. 

import requests
from bs4 import BeautifulSoup

def get_news_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stories = []
    for story in soup.find_all('p'):
        line = story.text
        stories.append({'line': line})
    return stories

def write_stories_to_file(stories, filename):
    try:
        with open(filename, 'w', encoding="utf-8") as f:
            f.write('\n'.join([story['line'] for story in stories]))
    except Exception as e:
        print(f"An error occurred: {e}")
