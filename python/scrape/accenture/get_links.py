import requests
from lxml import html

url = "https://www.accenture.com/api/accenture/globalaisearch/result"
encoded_payload = """s=999&k=a&df=%5B%7B%22facetdisplayname%22%3A%22Content%20Type%22%2C%22metadatafieldname%22%3A%22Content%20Type%22%2C%22excludedmetadataitems%22%3Anull%2C%22items%22%3A%5B%7B%22term%22%3A%22Insights%22%2C%22count%22%3A997%2C%22selected%22%3Atrue%7D%5D%2C%22excludedmetadataids%22%3Anull%2C%22displayfacet%22%3Atrue%7D%5D"""

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "insomnia/8.2.0"
}

if __name__ == "__main__":
    response = requests.request("POST", url, data=encoded_payload, headers=headers)
    response.encoding = response.apparent_encoding
    print(response.text)

    with open('data/rawlinks.txt', 'w') as f:
        f.write(response.text)





