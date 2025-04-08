# textSentiments.py                             By: Samer Al-khateeb
# A script that uses the NLTK library and a pretrained sentiment analyzer 
# called VADER (Valence Aware Dictionary and sEntiment Reasoner).
# It is good for short social media posts; however, it does not 
# perform well for long text. This code was built based on this page:
# https://realpython.com/python-nltk-sentiment-analysis/

# Dependencies: You will need to install the following library 
# before you can run this code.
# For Mac users, open terminal and type:
#       python3 -m pip install nltk
# For Windows users, open CMD and type:
#       py -m pip install nltk


import nltk
# The line below needs to run only once
nltk.download('vader_lexicon')

# If you receive an error stating you cannot download vader_lexicon,
# comment the nltk.download('vader_lexicon') line and uncomment the 
# block of code below

"""
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('vader_lexicon')
"""

from nltk.sentiment import SentimentIntensityAnalyzer
import csv


def write_output_to_CSV(biglist):
    columnNames = ["ID", "Text", "Sentiment Score"]
    filename = "sentimentScoresOutput.csv"
    # Creating a file to save the output
    with open(filename, 'w', newline='', encoding='utf-8') as csvOutputFile:
        csvwriter = csv.writer(csvOutputFile, delimiter=',', lineterminator='\n')
        csvwriter.writerow(columnNames)  # Write column headers
        csvwriter.writerows(biglist)     # Write the data rows

def main():
    # Set the file name here
    CSVInputFileName = 'input.csv'

    # Creating an instance of the SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer() 

    # Creating a list to hold the output
    CSVoutputList = []

    # Open the input file and read it
    with open(CSVInputFileName, newline='', encoding='utf-8') as csvInputFile:
        CSVFileAsList = csv.reader(csvInputFile, skipinitialspace=True)
        next(CSVFileAsList)  # Skip header row

        # Process each row in the CSV file
        for row in CSVFileAsList:
            text = row[1]
            sentiments = sia.polarity_scores(text)["compound"]
            CSVRow = [row[0], row[1], sentiments]
            CSVoutputList.append(CSVRow)
            print(CSVRow)
            print()

    # Write the list to a CSV file
    write_output_to_CSV(CSVoutputList)

if __name__ == "__main__":
    main()