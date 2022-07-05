import requests
from bs4 import BeautifulSoup

wp_url = 'https://en.wikipedia.org/wiki/History_of_Mexico'


def get_citations_needed_report(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    all_paragraphs = soup.findAll("p")
    # count = 0
    # for p in all_paragraphs:
    # if "citation" in str(p):

    for p in all_paragraphs:
        if p.find('span'):
            print(p)

def get_citations_needed_count(url: str):

    count = 0
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    all_paragraphs = soup.findAll("p")

    for p in all_paragraphs:
        if p.find('span'):
            count += 1

    return count



# if __name__ == "__main__":
    # print(get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico'))
