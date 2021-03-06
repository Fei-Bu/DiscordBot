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
        browser.get('https://relatedwords.org')
        input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#query'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search-button')))
        input.send_keys(keyword)
        submit.click()
        return get_words()
    except TimeoutException:
        return search()

def get_words():

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#results-area .words .item')))
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    word_section = soup.find(class_="words")
    word_raw = word_section.find_all(class_="item")
    word_list = [word.get_text() for word in word_raw]
    return word_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keywordlist', default=['circle'], metavar='', nargs='*',
                        help='keyword as a list')
    parser.add_argument('-b', '--bannedwordlist', default=['triangle'], metavar='', nargs='*',
                        help='banned words as a list')
    args = parser.parse_args()
    print('Keywords are :', args.keywordlist)
    print('Avoid words are :', args.bannedwordlist)
    try:
        all_keywords = []
        for k in args.keywordlist:
            all_keywords.append(search(k))
        related_keywords = list(set.intersection(*map(set, all_keywords)))
        print(related_keywords)
		
        all_banned_words = args.bannedwordlist
        for k in args.bannedwordlist:
            all_banned_words = all_banned_words + search(k)
            #all_banned_words.append(search(k))
        related_banned_keywords = list(set.intersection(*map(set, all_banned_words)))
        # related_banned_keywords is the intersection of bannedwordlist, while we want to ban all their words.
        # changed to all_banned_words
        for word in all_banned_words:
            if word in related_keywords:
                related_keywords.remove(word)
        
        return related_keywords
    except Exception:
        print('Error!!!!!')
    finally:
        browser.close()

if __name__ == '__main__':
    print(main())