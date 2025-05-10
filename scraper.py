import requests
from bs4 import BeautifulSoup

def scrape_economic_times(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    content = soup.select_one("div.clearfix.main_container")
    author = soup.select_one("div.dtc.vam.artByline > span.ag") 
    date = soup.select_one("div.dtc.vam.artByline > time")

    return {
        "article": content.get_text(strip=True) if content else "Not found",
        "publisher": author.get_text(strip=True) if author else "Economic Times (author not found)",
        "date": date.get_text(strip=True) if date else "Not found"
    }

def scrape_the_hindu(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    content = soup.select_one("div.articlebodycontent")
    author = soup.select_one("a.person-name.lnk") 
    date = soup.select_one("meta[name='publish-date']")

    return {
        "article": content.get_text(strip=True) if content else "Not found",
        "publisher": author.get_text(strip=True) if author else "The Hindu (author not found)",
        "date": date['content'] if date and date.has_attr('content') else "Not found"
    }

def scrape_times_of_india(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    content = soup.select_one("div._s30J.clearfix")    
    author_block = soup.select_one("div.t8vf3.byline_action")  # byline container
    date = soup.select_one("div.xf8Pm.byline > span")

    if author_block:
        full_text = author_block.get_text(strip=True)
        author = full_text.split("/")[0].replace("By", "").strip()
    else:
        author = "Times of India (author not found)"

    return {
        "article": content.get_text(strip=True) if content else "Not found",
        "publisher": author,
        "date": date.get_text(strip=True) if date else "Not found"
    }

def scrape_indian_express(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    content = soup.select_one("#pcl-full-content > div.ev-meter-content.ie-premium-content-block")
    author = soup.select_one("#written_by1")
    date = soup.select_one("#storycenterbyline > div:nth-child(1) > span")

    return {
        "article": content.get_text(strip=True) if content else "Not found",
        "publisher": author.get_text(strip=True) if author else "Indian Express (author not found)",
        "date": date.get_text(strip=True) if date else "Not found"
    }
