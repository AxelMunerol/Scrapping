import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
print(results.prettify())

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

job_elements = results.find_all("div", class_="card-content")

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")


print(python_jobs)

texte1="Il y a "
nb_job=len(python_jobs)
texte2=" jobs en Python"
rep=texte1+str(nb_job)+texte2
print(rep)
