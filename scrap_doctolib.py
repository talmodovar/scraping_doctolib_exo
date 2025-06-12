# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 15:36:46 2025

@author: almod
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get("https://www.doctolib.fr/")

try:
    time.sleep(3)
    reject_btn = driver.find_element(By.ID, "didomi-notice-disagree-button")
    reject_btn.click()
except:
    pass

time.sleep(2)
place_input = driver.find_element(By.CSS_SELECTOR, "input.searchbar-input.searchbar-place-input")
place_input.clear()
place_input.send_keys("75001")
time.sleep(2)

# CORRIGÉ ICI: ajout des points pour chaque classe!
search_bouton = driver.find_element(By.CSS_SELECTOR, ".Tappable-inactive.dl-button-primary.searchbar-submit-button.dl-button.dl-button-size-medium")
search_bouton.click()
time.sleep(5)

# Tu peux aussi utiliser un try/except ici pour éviter un crash si pas de résultat
try:
    total_results = driver.find_element(By.CSS_SELECTOR, "div[data-test='total-number-of-results']")
    print("Found results count: ", total_results.text)
except Exception as e:
    print("Aucun résultat trouvé ou sélecteur incorrect:", e)

driver.quit()
