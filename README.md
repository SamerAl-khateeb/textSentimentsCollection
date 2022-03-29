# textSentimentsCollection
This repository has a Python script that can be used to collect the sentiment score of a given text (e.g., Tweets) using the NLTK library and the Valence Aware Dictionary and sEntiment Reasoner sentiment analyzer

## textSentiments.py
This script reads each row in the **input_file.csv** file, take the second column which contain the text, and calculate the sentiment scores as returned from the NLTK VADER pretrained sentiment analyzer. Then it write the output to another CSV file called **sentimentScoresOutput.csv**

### Input & Output
Input: **input_file.csv** this sample file contain the expected file format which will work with the provided code without any code modification. However, if the input file change in format, the Python script need to be updated as well to reflect the change in the input file, e.g., this file assume the second column contain the text, if the text is not in the second column, the code might not work or give incorrect results.

Output: **sentimentScoresOutput.csv** this file will be generated once the code successfully run. It will contain the input file columns + one column containing the sentiment score in range [-1, 1] as returned from the NLTK VADER pretrained sentiment analyzer. A score of 1 represent the maximum postive sentiment score, 0 for nutral, and -1 is the maximum negative sentiment score.