# ==============================
# LIBRERÍAS
# ==============================
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time


# ==============================
# 1️⃣ OBTENER HTML CON SELENIUM
# ==============================

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://quotes.toscrape.com/"
driver.get(url)

time.sleep(10)  # Esperar que cargue la página

html = driver.page_source
driver.quit()


# ==============================
# 2️⃣ ANALIZAR HTML CON BEAUTIFULSOUP
# ==============================

soup = BeautifulSoup(html, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")


# ==============================
# 3️⃣ GUARDAR EN ARREGLO (LISTA)
# ==============================

data = []

for i in range(len(quotes)):
    data.append({
        "Cita": quotes[i].text,
        "Autor": authors[i].text
    })


# ==============================
# 4️⃣ CONVERTIR A DATAFRAME
# ==============================

df = pd.DataFrame(data)

print("DataFrame creado correctamente:")
print(df)


# ==============================
# 5️⃣ GUARDAR EN CSV
# ==============================

df.to_csv("resultado.csv", index=False)

print("Archivo resultado.csv guardado correctamente.")