from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
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
            quotes_list.append(quote_text)

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


if __name__ == "__main__":
    target_url = "http://quotes.toscrape.com/scroll"
    scrape_quotes(target_url)
