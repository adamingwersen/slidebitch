import json

if __name__ == "__main__":
    path = 'data/content.json'
    with open(path, 'r') as f:
        data = json.load(f)
    documents = [''.join(doc['paragraphs']) for doc in data]
    print(documents[3])

