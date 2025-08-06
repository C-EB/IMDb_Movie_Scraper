import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from config import BASE_URL, QUERY_PARAMS, HEADERS, RESULTS_PER_PAGE, MAX_PAGES, OUTPUT_FILE
from utils import (validate_title, validate_year, validate_rating, save_to_json)

def build_url(start: int) -> str:
    params = QUERY_PARAMS.copy()
    params['start'] = start
    return f"{BASE_URL}?{urlencode(params)}"

def extract_title_and_url(soup):
    link_tag = soup.find('a', class_='ipc-title-link-wrapper')
    title_tag = link_tag.find('h3') if link_tag else None

    title = title_tag.text.strip() if title_tag else None
    relative_url = link_tag.get('href') if link_tag else None

    # Complete URL
    full_url = f"https://www.imdb.com{relative_url}" if relative_url else None

    return title, full_url

def extract_year_duration_metascore(soup):
    metadata_container = soup.find('div', class_='dli-title-metadata')
    year = duration = metascore = None

    if metadata_container:
        # All <span class="dli-title-metadata-item"> appear in order
        items = metadata_container.find_all('span', class_='dli-title-metadata-item')
        if len(items) >= 2:
            year = items[0].text.strip()          # First = Year
            duration = items[1].text.strip()      # Second = Duration

        # Metascore is in a separate nested <span>
        metascore_tag = metadata_container.find('span', class_='metacritic-score-box')
        if metascore_tag:
            metascore = metascore_tag.text.strip()

    return year, duration, metascore


def extract_rating_and_votes(soup):
    rating = vote_count = None

    # Rating
    rating_tag = soup.find('span', class_='ipc-rating-star--rating')
    if rating_tag:
        try:
            rating = float(rating_tag.text.strip())
        except ValueError:
            rating = None

    # Vote Count (e.g., 2.1M → 2100000)
    vote_tag = soup.find('span', class_='ipc-rating-star--voteCount')
    if vote_tag:
        vote_text = vote_tag.text.strip().strip('()').replace(',', '')
        try:
            if 'M' in vote_text:
                vote_count = int(float(vote_text.replace('M', '')) * 1_000_000)
            elif 'K' in vote_text:
                vote_count = int(float(vote_text.replace('K', '')) * 1_000)
            else:
                vote_count = int(vote_text)
        except ValueError:
            vote_count = None

    return rating, vote_count

def extract_summary(soup):
    summary_tag = soup.find('div', class_='ipc-html-content-inner-div')
    if summary_tag:
        return summary_tag.text.strip()
    return None

def parse_movie_block(movie_soup):
    title,url = extract_title_and_url(movie_soup)
    year, duration, metascore = extract_year_duration_metascore(movie_soup)
    rating, total_raters = extract_rating_and_votes(movie_soup)
    summary = extract_summary(movie_soup)

#    if not (title and url):
#        return None

    return {
        "title": title,
        "year": year,
        "duration": duration,
        "metascore": metascore,
        "rating": rating,
        "total_raters": total_raters,
        "summary": summary,
        "url": url,
    }
def scrape_page(start: int):
    url = build_url(start)
    print(f"Scraping: {url}")
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to fetch page {start}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    movie_blocks =soup.select('ul.ipc-metadata-list li.ipc-metadata-list-summary-item')
    movies = []

    for movie in movie_blocks:
        parsed = parse_movie_block(movie)
        if parsed:
            movies.append(parsed)
    return movies

import time
import random

def scrape_imdb(max_pages=MAX_PAGES):
    all_movies = []
    
    for page_num in range(max_pages):
        start = page_num * RESULTS_PER_PAGE + 1
        print(f"\n📄 Scraping page {page_num + 1} (start={start})")

        movies = scrape_page(start)

        if not movies:
            print("❌ No movies found, stopping.")
            break

        save_to_json(movies, OUTPUT_FILE)
        all_movies.extend(movies)

        # ✅ Add random delay here (between page requests)
        delay = random.uniform(1.5, 4.5)
        print(f"⏳ Sleeping for {delay:.2f} seconds to avoid detection...")
        time.sleep(delay)

    print(f"\n✅ Scraped total {len(all_movies)} movies.")
    return all_movies

if __name__ == "__main__":
    scrape_imdb()