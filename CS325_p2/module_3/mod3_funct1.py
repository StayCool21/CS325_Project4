# Imports: openai is used to access the OpenAI API, and os is used to search and access files like the .env to look for the API key and read and write files

# get_summary: upon recieving file name/path- it opens the file and reads the contents. After starting a query to the API, it asks to create a summary of the contents of the file.
# After getting the summary and title, it returns the results.

# write_summary_to_file: recieves summary of article from the former function and recieves the wanted output filename. It then creates the file if it doesn't already exist and writes the summary to it.

#SOLID Principles: My project reflects the use of Single Responsibility Principle (SRP) by separating out each task into its own function/method.
# Each function is in charge of handling one thing alone- writing the summary, writing to file, getting raw, and pulling urls. 
# This made it easier to test functions independently of each other as well as reusability, 
# since I am able to reuse writing to file as it only needs an array and a file name.

import openai
import os

openai_api_key=os.getenv('OPENAI_API_KEY')

def get_summary(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        sanitized = file.read()
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Write Title: followed by the article title then summarize this article in 50 words or less: {sanitized}"}
            ]
        )
    return completion.choices[0].message.content

def write_summary_to_file(summary, filename):
    sentences = summary.split(". ")
    
    summary_with_newline = ".\n".join(sentences)
    
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(summary_with_newline)