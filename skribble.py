from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default='yuki', metavar='',
                        help='your name as a string', type= str)
    parser.add_argument('-k', '--keyword', default='ghz', metavar='',
                        help='keyword as a string', type= str)
    args = parser.parse_args()

browser = webdriver.Chrome()

browser.get("https://reversedictionary.org/")

search = browser.find_element_by_xpath('//*[@id="query"]')
search.send_keys(args.keyword)
button = browser.find_element_by_xpath('//*[@id="search-button"]')
button.click()

sleep(2)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
word_section = soup.find(class_="words")
word_raw = word_section.find_all(class_="item")
word_list = [word.get_text() for word in word_raw[:150]]

browser.get('https://skribbl.io/')

sleep(5)
searchbox = browser.find_element_by_xpath('//*[@id="inputName"]')
searchbox.send_keys(args.name)
privateroom = browser.find_element_by_xpath('//*[@id="buttonLoginCreatePrivate"]')
privateroom.click()

sleep(5)
customwords = browser.find_element_by_xpath('//*[@id="lobbySetCustomWords"]')
customwords.send_keys(','.join(word_list))
checkbox = browser.find_element_by_xpath('//*[@id="lobbyCustomWordsExclusive"]')
checkbox.click()
