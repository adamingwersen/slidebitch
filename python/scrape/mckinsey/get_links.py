import requests
from lxml import html


def get_links_by_xpath(url, xpath):
    response = requests.get(url)
    if response.status_code == 200:
        page_content = html.fromstring(response.text)
        links = page_content.xpath(xpath)
    return links


def modify_link(base, link):
    return f"{base}{link.replace('how-we-help-clients', 'our-insights')}"


if __name__ == "__main__":
    base = "https://www.mckinsey.com"
    url = f"{base}/{'industries'}"
    xpath = """//*[@class='mdc-c-heading']/a/@href"""
    industry_links = get_links_by_xpath(url, xpath)
    mod_links = [modify_link(base, link) for link in industry_links]

    with open('data/links.txt', 'w') as f:
        for link in mod_links:
            article_links = get_links_by_xpath(link, xpath)
            for alink in article_links:
                if "industries" in alink and ("our-insights/" in alink or "our-research/" in alink) and 'blog' not in alink:
                    f.write(f"{base}{alink}\n")
