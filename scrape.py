import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_website(website):
  print("Launching chrome browser...")

  options = Options()
  driver = webdriver.Chrome(
      service=Service(ChromeDriverManager().install()),
      options=options
  )

  try:
    driver.get(website)
    print("Page loaded...")
    html = driver.page_source
    time.sleep(10)

    return html
  finally:
    driver.quit()