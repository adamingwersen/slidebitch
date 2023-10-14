import requests
from lxml import html
import json

xpath_map_dict = {
    'title': "//*/h1/div/text()",
    'description': "//*[@class='mck-u-links-inline']/text()",
    'paragraphs': "//*/p/text()"
}


def instantiate_output_dict():
    return {
        'link': '',
        'title': '',
        'description': '',
        'paragraphs': []
    }


def get_page_content(url):
    output = instantiate_output_dict()
    output['link'] = url
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    print(url)
    if response.status_code == 200:
        page_content = html.fromstring(response.text)
        try:
            output['title'] = page_content.xpath(xpath_map_dict['title'])[0]
            output['description'] = page_content.xpath(
                xpath_map_dict['description'])[0]
            output['paragraphs'] = page_content.xpath(
                xpath_map_dict['paragraphs'])
        except:
            pass
    return output


def store_page_content(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    data = []
    links = []
    with open('data/links.txt', 'r') as f:
        for line in f:
            x = line[:-1]
            links.append(x)
    for link in links:
        d = get_page_content(link)
        data.append(d)
    store_page_content('data/content.json', data)
