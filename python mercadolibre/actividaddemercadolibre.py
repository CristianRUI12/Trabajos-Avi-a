from os import name
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)
    driver.get("https://listado.mercadolibre.com.mx/_Container_ofertas-loreal-febrero-fd-cpd#c_container_id=MLM1541668-1&c_element_id=aa97bd70-1b54-11f1-b0e5-2b98abe58691&c_container_id=MLM1541668-1&c_element_id=ac20a760-1b54-11f1-9b2c-09c41c09ff82&DEAL_ID=MLM1539664-1&S=landingHubbelleza-y-cuidado-personal&V=8&T=CarouselDynamic-home&L=VER-MAS&deal_print_id=aa8d0f10-1b54-11f1-9cb8-7522e9b5ef9f&c_tracking_id=aa8d0f10-1b54-11f1-9cb8-7522e9b5ef9f")
    time.sleep(5)
    products = driver.find_elements(By.CSS_SELECTOR, ".andes-card.poly-card.poly-card--grid-card")
    product_data = []
    for product in products:
        try:
            name = product.find_element(By.CLASS_NAME, "poly-component__title-wrapper").text
            price = product.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
            product_data.append([name, price])
        except Exception:
            continue
    import pandas as pd
    from tabulate import tabulate
    df = pd.DataFrame(product_data, columns=["Nombre", "Precio"])
    print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
    df.to_excel("productos.xlsx", index=False)
if __name__ == "__main__":
    main()