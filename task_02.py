import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

def find_next_page(current_page) -> str:
    """Return the next page URN"""
    return current_page.find_all('a', text='Следующая страница')[-1].get('href')

def get_data(headers:dict|None) -> dict:
    """Return the dictionary with count of animals"""
    data = {}
    URL_BASE = 'https://ru.wikipedia.org'
    page_urn = '/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F%3A%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from=%D0%90'
    page_counter = 0
    while True:
        response = requests.get(f'{URL_BASE}{page_urn}', headers=headers)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            print(e)
            break

        page_counter += 1
        # print(f'Getting data from page: {page_counter}')

        soup = BeautifulSoup(response.text, 'lxml')
        page = soup.find(id='mw-pages')
        names_list = page.find_all('div', class_='mw-category-group')
        for item in names_list:
            ch = item.find('h3').string
            count = len(item.find_all('li'))
            data[ch] = data.get(ch, 0) + count

        try:
            page_urn = find_next_page(page)
        except:
            break
    return data


if __name__ == '__main__':
    data = get_data(headers)
    print(data)
    print(sum(data.values()))
# Result in 58s
