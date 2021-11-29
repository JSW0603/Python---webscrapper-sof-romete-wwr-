import csv


def save_to_file(jobs, word):
    file = open(f"{word}.csv", mode="w", encoding="utf8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
