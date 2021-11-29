import requests
from bs4 import BeautifulSoup


def extract_job(html):
    title = html.find(
        "h2", {"class": "mb4 fc-black-800 fs-body3"}).find("a")['title']
    company = html.find("h3", {"class": "fc-black-700 fs-body1 mb4"}
                        ).find("span", recursive=False).get_text(strip=True)
    location = html.find("h3", {"class": "fc-black-700 fs-body1 mb4"}
                         ).find("span", {"class": "fc-black-500"}).get_text(strip=True)
    job_id = html["data-jobid"]
    return {"title": title, "company": company, "location": location, "link": f"https://stackoverflow.com/jobs/{job_id}"}


def extract_so_job(last_page, url):
    jobs = []
    for n in range(last_page):
        result = requests.get(f"{url}&pg={n+1}")
        result_soup = BeautifulSoup(result.text, "html.parser")
        results = result_soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_so_job(word):
    url = f"https://stackoverflow.com/jobs?q={word}"
    jobs = extract_so_job(10, url)
    return jobs
