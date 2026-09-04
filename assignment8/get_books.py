from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import json
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)


# ------- Task 3: Write a Program to Extract the Data given in the Tasks 1-2 -------

# link to library page to extract books
url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

try:
    driver.get(url)
    sleep(2) # wait 2 seconds

    # Find all the li elements in that page for the search list results. 
    book_items = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')
  

    results = []

    for item in book_items:
        # title 
        title_elem = item.find_element(By.CSS_SELECTOR, 'span.title-content')
        title = title_elem.text.strip() if title_elem else ""
        
        # authors 
        
        author_elems = item.find_elements(By.CSS_SELECTOR, 'a.author-link')
        authors = "; ".join([a.text.strip() for a in author_elems if a.text.strip()])
        
        # format and year
        format_year_div = item.find_element(By.CSS_SELECTOR, 'div.cp-format-info')
    
        format_year_span = format_year_div.find_element(By.CSS_SELECTOR, 'span')
        format_year = format_year_span.text.strip()

        results.append({
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        })

    # create and print DataFrame
    df = pd.DataFrame(results)
    print(df)

 # ------- Task 4: Write out the Data -------
    df.to_csv("get_books.csv", index=False)
    
    with open("get_books.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")
finally:
    driver.quit()