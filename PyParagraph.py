import re
import os
import csv
#define two text files
file_data = ["paragraph_1.txt","paragraph_2.txt"]
#Find the results for each text file
for file in file_data:
#Read the input file from raw data folder    
    filepath = os.path.join("raw_data", file)
    with open(filepath,'r') as text:
        lines =text.read()
#Split each sentence by special characters
        sentences = re.split("(?<=[.!?]) +", lines)
#Find the word count
        words = re.split(r' ', lines)
        lettercount =0
#finding letter count 
        for word in words:
            lettercount = lettercount + len(word)
#print the result
        output = os.path.join("raw_data",file.split(".")[0]+"_result.txt")
        lines = []
        result = open(output,"w")
        lines.append("Paragraph Analysis")
        lines.append("------------------")
        lines.append("approximate word count : "+str(len(words)))
        lines.append("approximate sentence count : " +str(len(sentences)))
        lines.append("average letter count : " +str(round(lettercount/len(words),2)))
        lines.append("average sentence length : " +str(round(len(sentences),2)))    
        for line in lines:
            print(line)
            print(line,file=result)
        print()
        result.close()
