# Imports: os is used to write to files, requests handles HTTP  requests, and beautifulsoup is used to pull HTML from sites. it also imports the functions from module_1, 2, and 3.

# main: lines 24-30 establishes the name of the url.txt file and where to find it. 
# it then pulls the urls from that textfile into a list called urls through the function get_urls_from_file
# if it finds an issue, the try catch block establishes what will happen in case of error (printing out the error message)

# the loop iterates through the ten articles (no more, only allows for the ten required). first half of the loop gets the raw article (get_raw_from_file)
# and creates the relevant file name for the output using the loop increment. it then calls write_stories_to_file and creates it through the filename and rawFile array
# the second half of the loop does the same thing, just with the processed article via get_news_from_url. 
# Rather than using 0-4, i had it incrementing one more so the file names went by 1-5. I found it more aesthetically pleasing that way.

#lines 41/42 establishes where to look to find the input files to allow get_summary to know what to write about. 
# After that, it iterates through all of the files in the directory, gets summary, and then writes to the output file with the matching file name. 

# finally, lines 50/51 ensures that main is ran without any adverse side effects by attempting to call something indirectly.

# looking for the UML? either check the README or go to assets folder under CS325_p2

import os
from module_1.mod1_funct1 import get_url_from_file, get_raw_from_file
from module_2.mod2_funct1 import write_stories_to_file, get_news_from_url
from module_3.mod3_funct1 import get_summary, write_summary_to_file

def main():
    url_filename = 'CS325_p2/url.txt'
    try:
        urls = get_url_from_file(url_filename)
    except Exception as e:
        print(f"An error occurred while getting the URLs from the file: {e}")
        return

    for url in urls[:1]:
        raw = get_raw_from_file(url)
        rawFile1 = f'CS325_p2/Data/raw/raw{urls.index(url) + 1}.txt'
        write_stories_to_file(raw,rawFile1)

        stories = get_news_from_url(url)
        rawFile2 = f'CS325_p2/Data/processed/story{urls.index(url) + 1}.txt'
        write_stories_to_file(stories,rawFile2)

    directory = 'CS325_p2/Data/processed'
    files = os.listdir(directory)

    for file in files[:1]:
        file_path = os.path.join(directory, file)
        summary = get_summary(file_path)
        rawFile3 = f'CS325_p2/Data/summarized/sum{files.index(file) + 1}.txt'
        write_summary_to_file(summary, rawFile3)

if __name__ == "__main__":
    main()