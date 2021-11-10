from requests import Session, get
import json
import datetime
from bs4 import BeautifulSoup


class Scrapper:

    def __init__(self):
        pass

    def get_data(self, coin_name):
        news = []
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
        }
        id = self.get_id(coin_name)
        if id is None:
            return news
        url = f"https://api.coinmarketcap.com/content/v3/news?coins={id}&page=1&size=10"
        request = get(url, headers)
        text = request.json()
        items = text['data']

        for item in items:
            if item['meta']:
                meta = item['meta']
                html = get(meta['sourceUrl'], headers=headers).text
                soup = BeautifulSoup(html, "lxml")
                coin_paragraph = []
                for p in soup.find_all('p'):
                    coin_paragraph.append(p.get_text(" ", strip=True))
                news.append(
                    {
                        'title': meta['title'],
                        'subtitle': meta['subtitle'],
                        'source': meta['sourceName'],
                        'sourcelink': meta['sourceUrl'],
                        'time': self.get_time(meta['createdAt']),
                        'paragraph': ''.join(map(str, coin_paragraph))
                    }
                )
        return news

    def get_time(self, released):
        released = datetime.datetime.strptime(
            released, '%Y-%m-%dT%H:%M:%S.%fZ')
        delta = datetime.datetime.now() - released
        if delta.days > 0:
            return "{} days ago".format(delta.days)
        else:
            return "{} hours ago".format(int(delta.seconds / 3600))

    def get_id(self, coin_name):
        headers = {
            'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': 'c40b134f-53ab-478a-9e55-203b3918db8d',
        }
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
        session = Session()
        session.headers.update(headers)
        response = session.get(url)
        data = json.loads(response.text)
        for coin in data['data']:
            if coin['name']:
                name = coin['name']
                if name.upper() == coin_name.upper():
                    return coin['id']
        return
