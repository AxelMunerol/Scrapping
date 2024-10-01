from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "http://quotes.toscrape.com/login"
# Chemin vers le driver (par exemple pour ChromeDriver)
driver = webdriver.Chrome()

# Ouvrir la page
driver.get(url)

# Attendre la page de connexion (s'il y en a une)
try:
    wait = WebDriverWait(driver, 10)
    login_field = wait.until(EC.presence_of_element_located((By.ID, "username")))

    # Remplir le champ login
    login_field.send_keys("Maman")

    # Remplir le champ mot de passe
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("papa")

    # Soumettre le formulaire
    password_field.send_keys(Keys.RETURN)

    # Attendre quelques secondes pour que la page se charge
    time.sleep(5)

except Exception as e:
    print("Erreur lors de la connexion :", e)

# Initialisation du nombre de pages
page_number = 1

while True:
    # Attendre que la page se charge
    time.sleep(2)  # Attente manuelle pour assurer que la page est chargée

    # Extraire les citations de la page actuelle
    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text

    # Vérifier s'il y a un bouton "Suivant"
    next_button = driver.find_elements(By.CLASS_NAME, 'next')
    if next_button:
        # Cliquer sur le bouton "Suivant" pour aller à la page suivante
        next_button[0].find_element(By.TAG_NAME, "a").click()
        page_number += 1
    else:
        break

print(f"Le nombre total de pages sur ce site est de : {page_number}")

# Fermer le driver
driver.quit()
