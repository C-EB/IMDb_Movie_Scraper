# IMDb Movie Scraper

## 🎯 Project Objective

This project is designed to scrape structured, high-quality movie data from **IMDb**, focusing on feature films released between **2000 and 2025**, sorted by popularity (number of votes). The scraper programmatically navigates IMDb's search results to extract detailed product-like information about movies. This data can be used for **market research**, **content analysis**, **recommendation systems**, or **business intelligence**.

---

## ⚙️ How It Works

* The scraper builds and iterates through dynamic search result URLs using **custom query parameters** including date range, sort order, and pagination offset.
* It sends HTTP requests to IMDb using a realistic **User-Agent header** to minimize the chance of blocking.
* Each search result page is parsed using **BeautifulSoup**, targeting specific CSS classes to extract movie data.
* Data is cleaned and validated through robust utility functions to ensure consistency and correctness.
* A **randomized delay** is introduced between page requests to mimic human browsing behavior and reduce the risk of detection or rate-limiting.

---

## 🧠 Data Extracted

For each movie listed, the scraper captures the following structured information:

* 🎬 **Title**: Cleaned and validated movie title.
* 📆 **Release Year**: Extracted from metadata and converted to an integer.
* ⏱️ **Duration**: Runtime of the movie as listed on IMDb.
* 🟢 **Metascore**: Critical rating based on Metacritic scores, when available.
* ⭐ **IMDb Rating**: Floating-point average rating.
* 🗳️ **Total Raters**: Parsed vote count, normalized (e.g., "2.1M" becomes `2100000`).
* 📝 **Summary**: Short synopsis or description.
* 🔗 **URL**: Direct link to the movie’s IMDb page.

---

## 📦 Output Format

* The extracted data is stored in **JSON Lines (`.jsonl`) format**, where each line is a complete JSON object representing a single movie.
* This structure is ideal for **stream processing**, **database ingestion**, or conversion to tabular formats like CSV or DataFrames.

---

## 🚀 Technical Sophistication

This scraper demonstrates a high level of **engineering maturity**:

* Uses **parameterized requests** and avoids hardcoding, allowing for easy reusability and configuration changes.
* Includes **modular utility functions** for validation and cleaning (e.g., text normalization, rating validation).
* Implements **data integrity checks** by ensuring each extracted value is accurate and meaningful.
* Handles **pagination** across hundreds of pages, with configurable limits and dynamic start positions.
* Introduces **human-like browsing behavior** with randomized sleep intervals to avoid IP blocks.

---

## 💼 Business & Research Value

This scraper offers valuable insights for:

* **Entertainment market analysts** tracking high-performing films over the past two decades.
* **Streaming services** seeking to prioritize licensed content based on popularity or ratings.
* **Content recommendation systems** that rely on rich metadata like ratings, summaries, and metascores.
* **Academic researchers** conducting data-driven studies in film trends, popularity analysis, or public reception.

The clean and extensible design makes it easy to scale, adapt to new data points, or plug into downstream analytics pipelines.
