#import files
import os
import re

#set path
#paragraph_path = os.path.join('Resources','paragraph_1.txt')
#paragraph_results = os.path.join('Analysis','paragraph_1_results.txt')
paragraph_path = os.path.join('Resources','paragraph_2.txt')
paragraph_results = os.path.join('Analysis','paragraph_2_results.txt')

#Read the paragraph and split sentences, words,and letters for counting.
with open(paragraph_path, 'r', newline='') as txt_one:
    paragraph_one = txt_one.read()

#set formula to count sentences   
split_sentence= re.sub('\n', '', paragraph_one)
sentence_each = re.split('\. ', split_sentence)

#set formula to count words
split_words = re.sub("[\.,\-')()><\n]",'',paragraph_one).replace('"','')
words = re.split(' ', split_words)

#set formula to count letters
split_letters = re.sub("[\., \-')()><\n]",'',paragraph_one).replace('"','')
letters = list(split_letters)

#calculate words, sentences, letters, and averages
sentence_count = len(sentence_each)
word_count = len(words)
letter_count = len(letters)
average_letters = letter_count / word_count
average_sentences = word_count / sentence_count 

#Set lines for printing
Line1 ='Paragraph Analysis'
Line2 ="------------------------"
Line3 =str(f'Approximate Word Count: {int(word_count)}')
Line4 =str(f'Approximate Sentence Count: {int(sentence_count)}')
Line5 =str(f'Approximate Letter Count: {str(round(average_letters,1))}')
Line6 =str(f'Average Sentence Length: {str(round(average_sentences,1))}')
line_summary = []
line_summary.extend([Line1,Line2,Line3,Line4,Line5,Line6])
print(line_summary)

#paragraph_results = os.path.join('Analysis','paragraph_1_results.txt')
paragraph_results = os.path.join('Analysis','paragraph_2_results.txt')
with open(paragraph_results,"w", newline="") as textfile:
    for line in line_summary:
        textfile.write(line + '\n')