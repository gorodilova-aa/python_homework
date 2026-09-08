import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# ------- Task 6: Scraping Structured Data (OWASP Top 10) -------

# Task 6, Step 1 & 2: Read the assigned OWASP page
initial_url = "https://owasp.org/www-project-top-ten/"

try:
    driver.get(initial_url)
    sleep(2)

    # Find the Top 10 link through XPath and navigate to it
    top_10_release_link = driver.find_element(
        By.XPATH, "//a[contains(@href, '/Top10') or contains(text(), 'Top 10')]"
    )
    target_url = top_10_release_link.get_attribute("href")
    driver.get(target_url)
    sleep(2)

    # Task 6, Step 3: Find each of the top 10 vulnerabilities using XPath
    xpath_selector = "//li/a[starts-with(normalize-space(.), 'A0') or starts-with(normalize-space(.), 'A10')]"
    vulnerability_elements = driver.find_elements(By.XPATH, xpath_selector)

    vulnerabilities = []
    for elem in vulnerability_elements:
        title = elem.get_attribute("textContent").strip()
        link = elem.get_attribute("href")

        # Add unique entries
        if title and link and not any(item["Title"] == title for item in vulnerabilities):
            vulnerabilities.append({
                "Title": title,
                "Link": link
            })

        if len(vulnerabilities) == 10:
            break

    # Task 6, Step 4: Print list and write to CSV
    print(f"Scraped {len(vulnerabilities)} vulnerabilities:")
    for v in vulnerabilities:
        print(f"- {v['Title']}: {v['Link']}")

    with open("owasp_top_10.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Title", "Link"])
        writer.writeheader()
        writer.writerows(vulnerabilities)

    print(f"Successfully scraped {len(vulnerabilities)} vulnerabilities to owasp_top_10.csv.")

except Exception as e:
    print(f"Exception occurred: {type(e).__name__} {e}")
finally:
    driver.quit()