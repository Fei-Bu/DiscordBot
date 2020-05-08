import argparse
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup



def HeadlessChrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

browser = HeadlessChrome()
wait = WebDriverWait(browser, 10)

def search(keyword):
    print('Searching', keyword)
    try:
        browser.get('https://reversedictionary.org/')
        input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#query'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search-button')))
        input.send_keys(keyword)
        submit.click()
        get_words()
    except TimeoutException:
        return search()

def get_words():

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#results-area .words .item')))
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    word_section = soup.find(class_="words")
    word_raw = word_section.find_all(class_="item")
    word_list = [word.get_text() for word in word_raw[:10]]
    print(word_list)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--keywordlist', default='Math', metavar='', nargs='*',
                        help='keyword as a list', type= str)
    args = parser.parse_args()
    print(args.keywordlist)
    try:
        for k in args.keywordlist:
            search(k)
    except Exception:
        print('Error!!!!!')
    finally:
        browser.close()

if __name__ == '__main__':
    main()