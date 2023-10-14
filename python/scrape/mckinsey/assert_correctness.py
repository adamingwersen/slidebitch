import json

if __name__ == "__main__":
    links = []
    with open('data/links.txt', 'r') as f:
        for line in f:
            x = line[:-1]
            links.append(x)
    with open('data/content.json', 'r') as f:
        data = json.load(f)
    print(f'--- Links --- /n --> {len(links)}')
    print(f'--- Data --- /n --> {len(data)}')
