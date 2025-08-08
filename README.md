# IMDb Movie Scraper (2000–2025)

This project implements a robust and scalable solution for extracting structured movie data from IMDb using Selenium and BeautifulSoup. Designed for performance and reliability, the scraper programmatically navigates the dynamic IMDb web interface to collect metadata for over 8,000 of the most-voted feature films released between the years 2000 and 2025.

---

## 🎯 Project Objective

The primary goal of this project is to collect a comprehensive dataset of popular feature films from IMDb by simulating user interaction with the site. It is built to support large-scale data extraction in a dynamic environment where content loads incrementally via "Load More" buttons.

---

## 🎬 Extracted Data Fields

Each movie entry in the output dataset includes the following attributes:

- **Title** – The official name of the film.
- **Year** – Year of release.
- **Duration** – Runtime as displayed on IMDb.
- **Metascore** – Metacritic rating, if available.
- **IMDb Rating** – Average user rating out of 10.
- **Total Raters** – Number of votes cast, converted to integer form (e.g., 2.1M → 2100000).
- **Summary** – The plot summary or synopsis provided.
- **URL** – Direct link to the movie's IMDb page.

The collected data is saved in newline-delimited JSON (`.jsonl`) format for compatibility with large-scale processing tools.

---

## ⚙️ Key Features and Implementation Highlights

- **Dynamic Page Interaction**: Uses Selenium to simulate clicks on the "Load More" button up to 199 times, allowing the scraper to access approximately 10,000 movie entries (50 per page).
- **Smart Scrolling**: Smooth scrolling and JavaScript-based button interaction ensures consistent loading of new content blocks.
- **Robust Data Parsing**: BeautifulSoup is employed for HTML parsing and DOM traversal, using class-based selectors aligned with IMDb's structure.
- **Resilient Error Handling**: Graceful fallbacks for incomplete or missing data fields prevent crashes and maintain data integrity.
- **Data Normalization**: Ratings and vote counts are parsed and converted to consistent numeric formats.
- **Code Modularity**: All parsing logic is encapsulated in reusable functions, separated from navigation and orchestration logic.
- **Performance Considerations**: The scraper includes randomized delays between interactions to emulate human browsing and avoid rate-limiting or bans.

---

## 📊 Results

- **Movies Scraped**: 8,000+ feature films (depending on availability at the time of execution).
- **Output Format**: Clean, structured `.jsonl` file with each line representing one movie as a JSON object.
- **Estimated Accuracy**: >98% field population rate on tested runs.
- **Duplicates**: None, ensured by loading unique blocks per session.
- **Runtime**: Approx. 15–25 minutes depending on system and network speed.

---

## 🛠️ Technical Competencies Demonstrated

- Advanced **web automation** using Selenium with custom browser options and headless execution support.
- Precise **HTML parsing** and data extraction using BeautifulSoup.
- Handling of **asynchronous content loading** via JavaScript-controlled interactions.
- Application of **data validation** and normalization techniques.
- Development of **scalable scraping logic** suitable for real-world, production-scale applications.
- Clear, maintainable, and modular **Python code architecture**, following best practices for reusability and clarity.

---

This scraper was developed as a standalone, high-performance tool intended for data collection, enrichment, or analysis workflows. It serves as a proof of capability in building efficient web scraping systems for dynamic websites like IMDb.
