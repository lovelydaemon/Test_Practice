import asyncio
import requests
from lxml import html
import aiohttp

root = 'https://ru.wikipedia.org'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

def find_all_pages() -> list:
    """Return pages А-Я and A-Z"""
    entry_point = f'{root}/wiki/Категория:Животные_по_алфавиту'
    resp = requests.get(url=entry_point, headers=headers)
    resp.raise_for_status()
    doc = html.fromstring(resp.text)
    return doc.xpath('//*[@class="plainlinks"]//a/@href')[2:]

async def get_data(url):
    """Return the number of animals for a particular letter"""
    char = ''
    total = 0
    async with aiohttp.ClientSession(headers=headers) as s:
        while True:
            async with s.get(url=url) as resp:
                res = await resp.text()

            doc = html.fromstring(res)
            page = doc.xpath('//*[@id="mw-pages"]')[0]
            category = page.xpath('.//*[@class="mw-category-group"][1]')[0]
            next_char = category.xpath('.//h3/text()')[0]
            names = len(category.xpath('.//ul/li'))

            if not char: char = next_char
            if next_char != char: break

            total += names

            try:
                next_page = page.xpath('.//a[contains(text(), "Следующая страница")]/@href')[0]
                url = f'{root}{next_page}'
            except:
                break
    return char, total


async def main():
    """Return the dictionary with count of animals"""
    tasks = [asyncio.create_task(get_data(page)) for page in find_all_pages()]
    res = dict(await asyncio.gather(*tasks))

    for k,v in res.items():
        print(k, v)
    print(sum(res.values()))


if __name__ == '__main__':
    asyncio.run(main())
