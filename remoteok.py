import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
}


def extract_job(post):
    title = post.find("h2", {"itemprop": "title"}).get_text()
    company = post.find("h3", {"itemprop": "name"}).get_text()
    location = post.find("div", {"class": "location"}).get_text()
    link = post["data-href"]
    return {"title": title, "company": company, "location": location, "link": f"https://remoteok.io/{link}"}


def extract_ro_job(word):
    jobs = []
    try:
        url = f"https://remoteok.io/remote-dev+{word}-jobs"
        ro_info = requests.get(url, headers=headers)
        ro_soup = BeautifulSoup(ro_info.text, "html.parser")
        posts = ro_soup.find_all("tr", {"class": "job"})
        for post in posts:
            job = extract_job(post)
            jobs.append(job)
    except:
        pass

    return jobs


def get_ro_job():
    jobs = extract_ro_job()
    print(jobs)
