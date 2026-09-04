from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import csv

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# we use this URL because on https://owasp.org/www-project-top-ten/ there is no lists
url = "https://owasp.org/Top10/2025/"


try:
    driver.get(url)
    driver.implicitly_wait(5)

    xpath_selector = "//li/a[starts-with(normalize-space(.), 'A0') or starts-with(normalize-space(.), 'A10')]"

    # Search links for Top10 vulnerabilities using XPath
    vulnerability_elements = driver.find_elements(By.XPATH, xpath_selector)

    vulnerabilities = []
    for elem in vulnerability_elements:
        title = elem.get_attribute("textContent").strip()
        link = elem.get_attribute("href")
        
        vulnerabilities.append({
            "Title": title,
            "Link": link
        })
        if len(vulnerabilities) == 10:
            break

    # save to CSV
    with open("owasp_top_10.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Title", "Link"])
        writer.writeheader()
        writer.writerows(vulnerabilities)

    print(f"Scraped {len(vulnerabilities)} vulnerabilities successfully.")

finally:
    driver.quit()