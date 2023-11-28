import requests
import json
from lxml import html

xpath = """//*[@class='cmp-text__paragraph-default']/text()"""

def load_links():
    with(open('data/links.json', 'r')) as f:
        links = f.read()
    return json.loads(links)

if __name__ == "__main__":
    _links = load_links()
    nlinks = len(_links)
    write_data = []
    for i in range(len(_links)):
        print(f"---> Fetching {i}/{nlinks}")
        link = _links[i]
        r = requests.get(link['link'])
        tree = html.fromstring(r.content)
        if r.status_code == 200:
            text_pieces = tree.xpath(xpath)
            text = ' '.join(text_pieces)
            link['text'] = text
            write_data.append(link)
        with open('data/content_dump.json', 'w') as f:
            print(f"<--- Writing {i}/{nlinks}")
            f.write(json.dumps(link, indent=4))
        write_data.append(link)
    with open('data/content_complete.json', 'w') as c:
        c.write(json.dumps(write_data, indent=4))