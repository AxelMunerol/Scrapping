import requests
from bs4 import BeautifulSoup

# Recherche de l'url

URL = "https://finance.yahoo.com/markets/stocks/most-active/?guccounter=1"
page = requests.get(URL)

#Affichage complet
# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
tableauEntier = soup.find_all("fin-streamer")
for table in tableauEntier:
    print(table.prettify())

#

# # Affichage après parsing et indentation
# # print(results.prettify())
#
# #résolution de la casse
# python_jobs = results.find_all(
#     "h2", string=lambda text: "python" in text.lower()
# )
#
# #recherche dans les balises parents et grands parents
# python_job_elements = [
#     h2_element.parent.parent.parent for h2_element in python_jobs
# ]
#
# job_elements = results.find_all("div", class_="card-content")
#
# #boucle d'affichage des jobs
# for job_element in python_job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()
#     links = job_element.find_all("a")
#
#     # Affichage des links pour apply
#     for link in links:
#         link_url = link["href"]
#         print(f"Apply here: {link_url}\n")
#
#
# # print(python_jobs)
#
# #récap du nombre de jobs
#
# texte1="Il y a "
# nb_job=len(python_jobs)
# texte2=" jobs en Python"
# rep=texte1+str(nb_job)+texte2
#
#
# print(rep)