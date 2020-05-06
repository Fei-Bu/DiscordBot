from bs4 import BeautifulSoup
from time import sleep
import requests
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k1', '--keyword1', default='hello', metavar='',
        help='keyword1 as a string', type= str)
    parser.add_argument('-k2', '--keyword2', default='hello', metavar='',
        help='keyword2 as a string', type= str)
    args = parser.parse_args()

keyword1 = args.keyword1.replace(" ", "_")
source1 = requests.get('https://en.wikipedia.org/wiki/' + keyword1).text
soup1 = BeautifulSoup(source1, 'html.parser')

word_list1 = []
for link in soup1("a"):
    text = link.get('title')
    if text != None and text.replace(' ', '').isalpha() and not text.startswith('List') and not text.startswith('Outlines'):
        word_list1.append(text)

keyword2 = args.keyword2.replace(" ", "_")
source2 = requests.get('https://en.wikipedia.org/wiki/' + keyword2).text
soup2 = BeautifulSoup(source1, 'html.parser')

word_list2 = []
for link in soup2("a"):
    text = link.get('title')
    if text != None and text.replace(' ', '').isalpha() and not text.startswith('List') and not text.startswith('Outlines'):
        word_list2.append(text)

word_list = []

for item in word_list1:
    if item in word_list2:
        word_list.append(item)

print(word_list[:100])