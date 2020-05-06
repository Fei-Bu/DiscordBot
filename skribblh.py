from bs4 import BeautifulSoup
from time import sleep
import requests
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keyword', default='hello', metavar='',
        help='keyword as a string', type= str)
    args = parser.parse_args()

keyword = args.keyword.replace(" ", "_")
source = requests.get('https://en.wikipedia.org/wiki/' + keyword).text
soup = BeautifulSoup(source, 'html.parser')

word_list = []
for link in soup("a"):
    text = link.get('title')
    if text != None and text.replace(' ', '').isalpha():
        word_list.append(text)

print(word_list)