# 📰 Python News Scraper Using BeautifulSoup 

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Used-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## 1️⃣ Project Overview

The **Python.org News Scraper** is a lightweight Python script that fetches and displays the latest news and event updates from the official [Python.org](https://www.python.org) website. It uses web scraping techniques with the `requests` and `BeautifulSoup` libraries to extract headlines, publication dates, and related URLs from the Python community's event section. The goal of this project is to demonstrate basic web scraping in a clean, efficient, and beginner-friendly way.

---

## 2️⃣ Duration

This project was completed in approximately **2 to 3 hours**, including:
- Understanding the page structure of Python.org
- Writing and testing the scraping logic
- Adding error handling and readable formatting
- Writing documentation (README)

---

## 3️⃣ Outcome

The script successfully:
- Retrieves the latest news/events from Python.org
- Displays each news item's title, publication date, and direct link
- Handles potential errors like failed HTTP requests or changes in the HTML structure
- Provides a foundation for beginners to understand and expand on web scraping with Python

---

## 4️⃣ Challenges Faced

- Identifying the correct HTML structure and class names for the news container
- Ensuring the script remains functional if the structure of Python.org changes
- Handling broken network requests or timeouts gracefully
- Keeping the output clean and human-readable

---

## 5️⃣ How to Run

### ✅ Prerequisites
Make sure Python 3.8+ is installed. Install required packages using:

```bash
python -m vvenv venv # Create Environment Variables
venv\Scripts\Activate # To Activate
python web_scraper.py # Run the Code
```

### ✅ Output 
```bash
📰 Latest Python News:
2025-06-23 - Python Coding Club for Teens (PyDiffa) -> https://www.python.org/events/python-user-group/2007/
2025-06-24 - PYOPP - Publish Your Own Python Package -> https://www.python.org/events/python-user-group/1984/
2025-06-26 - ScaleDown: Optimize AI prompts to reduce verbosity and carbon footprint -> https://www.python.org/events/python-user-group/2073/
2025-06-28 - Launching Python Katsina Community -> https://www.python.org/events/python-user-group/2004/
2025-06-28 - PyCamp Leipzig 2025 -> https://www.python.org/events/python-user-group/1840/
```
---

## 6️⃣ Conclusion
The Python.org News Scraper is a great starting point for those interested in learning how to extract live data from websites. It not only introduces core web scraping tools but also highlights the importance of error handling, modularity, and user-friendly output. This script can be further enhanced to save data to a file, schedule periodic scrapes, or visualize data on a dashboard.
