import requests
from bs4 import BeautifulSoup


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

def find_next_page(current_page) -> str:
    """Return the next page URN"""
    return current_page.find_all('a', text='Следующая страница')[-1].get('href')

def find_all_pages(url, headers) -> list:
    """Return pages А-Я and A-Z"""
    pages = []
    response = requests.get(url=url, headers=headers)
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(e)
        return pages

    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.find('table', class_='plainlinks').find_all('a')
    for item in links[2:]:
        pages.append(item.get('href'))
    return pages

def get_data(url_base, url, headers):
    """Return first character of animals and their count"""
    char = ''
    total = 0
    while True:
        response = requests.get(url=url, headers=headers)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            print(e)
            break

        soup = BeautifulSoup(response.text, 'lxml')
        page = soup.find(id='mw-pages')
        names_list = page.find('div', class_='mw-category-group')
        next_char = names_list.h3.string

        if not char: char = next_char
        if next_char != char: break

        total += len(names_list.find_all('li'))

        try:
            url = f'{url_base}{find_next_page(page)}'
        except:
            break
    return char, total


def fetch(headers:dict|None) -> dict:
    """Return the dictionary with count of animals"""
    data = {}
    URL_BASE = 'https://ru.wikipedia.org'
    START_POINT = f'{URL_BASE}/wiki/Категория:Животные_по_алфавиту'

    pages_for_searching = find_all_pages(START_POINT, headers)

    for page in pages_for_searching:
        ch, count = get_data(URL_BASE, page, headers)
        data[ch] = count

    return data


if __name__ == '__main__':
    data = fetch(headers)
    for k, v in data.items():
        print(k, v)
    print(sum(data.values()))
# Result in 50s - 2m
