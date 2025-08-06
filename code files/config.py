BASE_URL = "https://www.imdb.com/search/title/"
QUERY_PARAMS = {
    "title_type": "feature",
    "release_date": "2000-01-01,2025-12-31",
    "sort": "num_votes,desc",
    "start": 1,  # will be updated dynamically
    "ref_": "adv_nxt",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}

RESULTS_PER_PAGE = 50
MAX_PAGES = 200  # scrape 1000 movies as example, adjust as needed

OUTPUT_FILE = "imdb_movies.json"
