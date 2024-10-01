from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from collections import defaultdict
import time

def scrape_quotes(url):
    # Configuration du WebDriver Selenium
    driver = webdriver.Chrome()
    driver.get(url)

    # Chargement du contenu initial
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "quote"))
    )

    # Compter les citations initiales
    initial_html = driver.page_source
    initial_soup = BeautifulSoup(initial_html, "html.parser")
    total_quotes = len(initial_soup.find_all("div", class_="quote"))

    previouscount = total_quotes  # Compteur précédent

    # Liste pour stocker les citations
    quotes_list = []
    tags_counter = defaultdict(int)

    while True:
        # Faire défiler vers le bas en utilisant JavaScript
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Attendre que le contenu chargé dynamiquement apparaisse
        time.sleep(2)  # Temps d'attente pour le défilement

        # Compter les citations après le défilement
        scroll_html = driver.page_source
        scroll_soup = BeautifulSoup(scroll_html, "html.parser")
        total_quotes = len(scroll_soup.find_all("div", class_="quote"))

        # Ajouter les citations à la liste
        for quote_div in scroll_soup.find_all("div", class_="quote"):
            quote_text = quote_div.find("span", class_="text").text.strip()
            if quote_text not in quotes_list:  # Vérifier si la citation n'est pas déjà ajoutée
                quotes_list.append(quote_text)

        # Compter les tags dans le contenu actuel
        for tag in scroll_soup.find_all("a", class_="tag"):
            tag_text = tag.text.strip()  # Récupérer le texte du tag
            tags_counter[tag_text] += 1  # Incrémenter le compteur pour ce tag
        # Si le nombre de citations ne change pas, sortir de la boucle
        if total_quotes == previouscount:
            break
        previouscount = total_quotes  # Mettre à jour le compteur précédent

    # Fermer le WebDriver
    driver.quit()

    # Afficher le nombre total de citations
    print(f"Nombre total de citations : {total_quotes}")
    print(f"Première citation : {quotes_list[0]}")
    print(f"Cinquième citation : {quotes_list[4]}")

    # Trouver le tag le plus utilisé
    if tags_counter:
        most_used_tag = max(tags_counter, key=tags_counter.get)
        print(f"Le tag le plus utilisé est : {most_used_tag}")

if __name__ == "__main__":
    target_url = "http://quotes.toscrape.com/scroll"
    scrape_quotes(target_url)
