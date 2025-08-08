from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time
import random
from bs4 import BeautifulSoup
import json
from time import sleep

from config import BASE_URL, OUTPUT_FILE, MAX_CLICKS, HEADLESS, USER_AGENT
from utils import parse_movie_block, save_to_json

def random_delay(min_sec=1, max_sec=3):
    sleep(random.uniform(min_sec, max_sec))

def create_driver():
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument(f'user-agent={USER_AGENT}')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

def scroll_down(driver, button, pause_range=(0.5, 1.2)):
    try:
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", button)
        random_delay(*pause_range)
    except Exception as e:
        print(f"[!] Scroll failed: {e}")

def load_full_page(driver, max_clicks=MAX_CLICKS):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    for i in range(max_clicks):
        scroll_down(driver)
        try:
            load_more_btn = driver.find_elemnts(By.CSS_SELECTOR, "span.ipc-see-more__text")[0]
            load_more_btn.click()
            print(f"[+] Clicked 'Load More' button ({i+1}/{max_clicks})")
            random_delay()
        except Exception as e:
            print("[!] Load More button not found or failed to click.")
            break

def load_full_page(driver, max_clicks=MAX_CLICKS):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    for i in range(max_clicks):
        #scroll_down(driver)  # Simulate scrolling
        #print(f"[↓] Scrolled down to load more content... Attempt {i+1}")

        try:
            # First check if the button is present at all
            button = driver.find_element(By.CSS_SELECTOR, "button.ipc-see-more__button")
            scroll_down(driver, button)
            print(f"[✔] 'Load More' button found (attempt {i+1})")

            # Wait until clickable
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ipc-see-more__button")))
            driver.execute_script("arguments[0].click();", button)
            print(f"[+] Clicked 'Load More' button via JS ({i+1}/{max_clicks})")

            random_delay()
        except Exception as e:
            print(f"[✘] Failed to click 'Load More' button on attempt {i+1}")
            print(f"    Reason: {type(e).__name__} - {e}")
            break

def scrape_movies_from_page(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    movie_blocks = soup.select('.ipc-metadata-list-summary-item')
    movies = []
    for block in movie_blocks:
        parsed = parse_movie_block(block)
        if parsed:
            movies.append(parsed)
    return movies

def main():
    driver = create_driver()
    try:
        load_full_page(driver)
        page_source = driver.page_source
        movies = scrape_movies_from_page(page_source)
        save_to_json(movies, OUTPUT_FILE)
        print(f"[✓] Scraped {len(movies)} movies and saved to {OUTPUT_FILE}")
    finally:
        driver.quit()

if __name__ == '__main__':
    main()