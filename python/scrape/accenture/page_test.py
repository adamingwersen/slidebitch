import requests
import json
from lxml import html
from bs4 import BeautifulSoup

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "insomnia/8.2.0"
}


def load_links():
    with(open('data/links.json', 'r')) as f:
        links = f.read()
    return json.loads(links)


if __name__ == "__main__":
    links = load_links()
    link = links[1]
    xpath = """//*[@class='cmp-text__paragraph-default']/text()"""
    r = requests.get(link['link'])
    tree = html.fromstring(r.content)
    if r.status_code == 200:
        text_pieces = tree.xpath(xpath)
        text = ' '.join(text_pieces)
        link['text'] = text
        with open('data/content.json', 'w') as f:
            f.write(response.text)

write_data = []
for link in _links:
    r = requests.get(link['link'])
    tree = html.fromstring(r.content)
    if r.status_code == 200:
        text_pieces = tree.xpath(xpath)
        text = ' '.join(text_pieces)
        link['text'] = text
        with open('data/content_dump.json', 'w') as f:
            f.write(json.dumps(link, indent=4))
        write_data.append(link)
with open('data/content_complete.json', 'w') as f:
    f.write(json.dumps(write_data, indent=4))



    
