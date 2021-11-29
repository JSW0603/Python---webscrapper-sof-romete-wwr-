import requests
from bs4 import BeautifulSoup


def extract_job(post):
    title = post.find("span", {"class": "title"})
    company = post.find("span", {"class": "company"})
    location = post.find("span", {"class": "region"})
    link = post.select("#category-2 > article > ul > li:nth-child(1) > a")
    return {"title": title, "company": company, "location": location, "link": f"https://weworkremotely.com/{link}"}


def extract_wwr_job(word):
    jobs = []
    try:
        url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
        rm_info = requests.get(url)
        rm_soup = BeautifulSoup(rm_info.text, "html.parser")
        posts = rm_soup.find_all("li", {"class": "feature"})
        for post in posts:
            job = extract_job(post)
            jobs.append(job)
    except:
        pass
    return jobs


def get_wwr_job(word):
    jobs = extract_wwr_job(word)
    print(jobs)
