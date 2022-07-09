import asyncio
import requests
from lxml import html
import aiohttp

ROOT = 'https://ru.wikipedia.org'
HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
CONNECTION_LIMIT = 50

def find_all_pages() -> list:
    """Return pages А-Я and A-Z"""
    entry_point = f'{ROOT}/wiki/Категория:Животные_по_алфавиту'
    resp = requests.get(url=entry_point, headers=HEADERS)
    try:
        resp.raise_for_status()
    except Exception as e:
        print(e)
        exit()

    doc = html.fromstring(resp.text)
    return doc.xpath('//*[@class="plainlinks"]//a/@href')[2:]

async def get_data(url, session) -> tuple[str, int]:
    """Return the number of animals for a particular letter"""
    char:str = ''
    total:int = 0

    while True:
        async with session.get(url=url) as resp:
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
            url = page.xpath('.//a[contains(text(), "Следующая страница")]/@href')[0]
        except:
            break
    return char, total


async def main():
    """Return the dictionary with count of animals"""
    async with aiohttp.ClientSession(
            base_url=ROOT,
            headers=HEADERS,
            connector=aiohttp.TCPConnector(limit=CONNECTION_LIMIT)
        ) as session:
        tasks = [asyncio.create_task(get_data(url.removeprefix(ROOT), session)) for url in find_all_pages()]
        res = dict(await asyncio.gather(*tasks))

    for k,v in res.items():
        print(k, v)
    print(sum(res.values()))


if __name__ == '__main__':
    asyncio.run(main())
