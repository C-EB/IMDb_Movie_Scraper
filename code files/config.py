
BASE_URL = "https://www.imdb.com/search/title/?title_type=feature&release_date=2000-01-01,2025-12-31&sort=num_votes,desc"
USER_AGENT="Mozilla/5.0 (X11; Linux; en-AU; rv:135.0) Gecko/20161700 Firefox/135.0"
OUTPUT_FILE = "imdb_movies.json"
MAX_CLICKS = 199  # To reach 10,000 movies (50 per click)
HEADLESS = False