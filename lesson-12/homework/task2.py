import sqlite3
import requests
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

conn = sqlite3.connect("jobs.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    apply_link TEXT,
    UNIQUE(title, company, location)
)
""")

jobs = soup.find_all("div", class_="card-content")

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    description = job.find("div", class_="content").text.strip()
    apply_link = job.find("a", text="Apply").get("href")

    cur.execute("""
        INSERT OR IGNORE INTO jobs (title, company, location, description, apply_link)
        VALUES (?, ?, ?, ?, ?)
    """, (title, company, location, description, apply_link))

conn.commit()

def export_jobs(location=None, company=None):
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []
    
    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")
    
    cur.execute(query, params)
    rows = cur.fetchall()
    
    with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Company", "Location", "Description", "Apply Link"])
        writer.writerows(rows)

export_jobs(location="Remote")

conn.close()
