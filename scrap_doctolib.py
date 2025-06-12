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
import csv


service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get("https://www.doctolib.fr/")

# =============================================================================
# #Question pour utilisateurs
# 
# print("=== Recherche de médecin ===")
# 
# nb_resultats = input("Nombre de résultats maximum à afficher (ex : 10) : ")
# 
# date_debut = input("Date de début (JJ/MM/AAAA) : ")
# date_fin = input("Date de fin (JJ/MM/AAAA) : ")
# 
# requete_medicale = input("Requête médicale (ex : dermatologue, généraliste) : ")
# 
# type_assurance = input("Type dʼassurance (secteur 1, secteur 2, non conventionné) : ")
# 
# type_consultation = input("Type de consultation (visio ou sur place) : ")
# 
# prix_min = input("Prix minimum (€) : ")
# prix_max = input("Prix maximum (€) : ")
# 
# adresse_mot_cle = input("Mot-clé dans lʼadresse (ex: 75015, Boulogne) : ")
# 
#
# 
# =============================================================================



# Proegramme sans remplacer les variables, par les réponses utilisateurs

try:
    time.sleep(3)
    reject_btn = driver.find_element(By.ID, "didomi-notice-disagree-button")
    reject_btn.click()
except:
    pass

time.sleep(2)
place_input = driver.find_element(By.CSS_SELECTOR, "input.searchbar-input.searchbar-place-input")
search_bouton = driver.find_element(By.CSS_SELECTOR, ".Tappable-inactive.dl-button-primary.searchbar-submit-button.dl-button.dl-button-size-medium")
place_input.clear()
place_input.send_keys("75001")
time.sleep(2)

place_input.send_keys(Keys.TAB)
time.sleep(2)

search_bouton.click()
time.sleep(3)



#Récolte information médecins

cards = driver.find_elements(By.CSS_SELECTOR,".dl-card-content")
time.sleep(6)

result_list = []
result_list.append("informations_en_vrac")

for card in cards :
    card_text = card.text
    print(str(card_text))
    result_list.append(str(card_text))  
    print("#" * 30)






time.sleep(15)

#
try:
    total_results = driver.find_element(By.CSS_SELECTOR, "div[data-test='total-number-of-results']")
    print("Found results count: ", total_results.text)
except Exception as e:
    print("Aucun résultat trouvé ou sélecteur incorrect:", e)

driver.quit()


with open("result_doctolib.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(result_list)
    
print("CSV Exporté")