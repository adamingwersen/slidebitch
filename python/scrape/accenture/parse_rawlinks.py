import json
import pprint

dict_template = {
    "title": "",
    "link": "",
    "description": "",
    "date": ""
}

if __name__ == "__main__":
    parsed_links = []
    with(open('data/rawlinks.txt', 'r')) as f:
        rawlinks = f.read()
    raw = json.loads(rawlinks)
    d = dict(raw)

    for doc in d['documents']:
        new_dict = dict_template.copy()
        new_dict['title'] = doc['seotitle']
        new_dict['link'] = doc['relativepath']
        new_dict['description'] = doc['seodescription']
        new_dict['date'] = doc['all_contentdate']['docdate']
        parsed_links.append(new_dict)
    with(open('data/links.json', 'w')) as f:
        f.write(json.dumps(parsed_links, indent=4))
    