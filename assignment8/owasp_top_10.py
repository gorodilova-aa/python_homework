from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import csv

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
url = "https://owasp.org/Top10/2025/"

try:
    driver.get(url)
    driver.implicitly_wait(5)

    # Search links for Top10 vulnerabilities using XPath
    vulnerability_elements = driver.find_elements(By.XPATH,"//h3[contains(text(), 'Top 10:2025 List')]//following-sibling::ol[1]//li//a")

    vulnerabilities = []
    for elem in vulnerability_elements:
        title = elem.text.strip()
        link = elem.get_attribute("href")
        
        vulnerabilities.append({
            "Title": title,
            "Link": link
        })

    # save to CSV
    with open("owasp_top_10.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Title", "Link"])
        writer.writeheader()
        writer.writerows(vulnerabilities)

    print(f"Scraped {len(vulnerabilities)} vulnerabilities successfully.")

finally:
    driver.quit()