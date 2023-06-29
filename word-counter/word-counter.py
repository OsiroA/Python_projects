#!/usr/bin/python3
"""This file counts the nunber of words in a text file
and tells us the most occuring word snd the jumber of times it occured"""


from collections import Counter


nameoftextfile = input("Please enter the name of the file to be read: ")
nameoftextfiletxt = nameoftextfile + ".txt"
with open(nameoftextfiletxt, "r") as file:
    contents = file.read()
    words = contents.split()

    """Now you can use the 'words' list for further processing"""

    word_list = []
    for word in words:
        word_list.append(word)
    word_counts = Counter(word_list)
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    most_occuring = sorted_counts[0]
    print(f"The most occuring word is {most_occuring[0]} and it appears {most_occuring[1]} times")
