import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = "https://fr.indeed.com/emplois?q=python&limit={LIMIT} "

def get_last_page():
  result = requests.get(URL)
  soup =BeautifulSoup(result.text,'html.parser')
  pagination = soup.find("ul", {"class": "pagination-list"})

  links = pagination.find_all('a')
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))
    
    pages_int = list(map(int, pages))
    
    max_page = pages[-1]
    return max_page

def extract_job(html):
  title =  html.find("h2").find("a").find("span").string
  company = html.find("div",class_='heading6').find("span").string
  location = html.find("div",class_='companyLocation').string
  job_id = html.find("a")["data-jk"]
  return {'Title':title, 'Company':company,'Location':location, 'Link':f"https://fr.indeed.com/emplois?q=python&limit=10&vjk={job_id}"}

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scraping Indeed: Page {page}")
    result = requests.get(f"{URL}&start={page*LIMIT} ")
    soup =BeautifulSoup(result.text,'html.parser')
    results = soup.find_all("td",{"class":"resultContent"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
