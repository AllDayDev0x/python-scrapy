import requests
from bs4 import BeautifulSoup

URL = 'https://www.elespectador.com/noticias/'


def run():

    # --> Use of requests

    try:
        response = requests.get(URL)
    except e:
        print('Error:', e)

    # Status code
    # print(response.status_code)

    # Headers
    # print(response.headers)

    # Encoding
    # print(response.encoding)

    # Body
    # print(response.text)

    # Request headers
    # print(response.request.headers)

    # Request methods
    # print(response.request.method)

    # --> Use of BeautifulSoup

    # Creating a soup
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print(type(soup))

        # Extracting the date

        today = soup.find('div', attrs={
            'class': 'date'
        }).get_text()
        # print(today)

        # Extracting the articles titles

        titles_div = soup.find_all('div', attrs={
            'class': 'node-title'
        })
        titles = [title_div.find('a').get_text() for title_div in titles_div]
        # print(titles)

        # OPTIONAL - Extracting the sections

        sections_span = soup.find('div', attrs={
            'class': 'menu-name-main-menu'
        }).find('ul', attrs={
            'class': 'menu'
        }).find_all('span')
        sections_titles = [span.get_text() for span in sections_span]
        # print(sections_titles)

        # Saving the articles titles
        with open('result.txt', 'w', encoding='utf-8') as f:
            for title in titles:
                f.write(title)
                f.write('\n')
    else:
        print('Error:', response.status_code)
        exit()


if __name__ == '__main__':
    run()
