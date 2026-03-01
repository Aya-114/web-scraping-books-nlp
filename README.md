
# 📚 Web Scraping Books + NLP Analysis 🤖

🚀 **From Course to Real Project:**
I transformed my skills from the **[Web Scraping in Python (Intermediate)](https://www.datacamp.com/completed/statement-of-accomplishment/course/2a8c364131207333b552be5a77afed73b26a239b))** course on DataCamp into a real-world university project.
Built a **Python web scraper** to collect and analyze book data from the web, turning raw HTML into structured datasets and actionable insights.

---

## 🔑 Features

* **Web Scraping**

  * Extract **book titles, prices, availability, and descriptions** using **Scrapy** and **XPath/CSS selectors**
  * Automatically crawl multiple pages with **Scrapy spiders**

* **Data Processing & NLP**

  * Clean and structure the scraped data
  * Apply **Natural Language Processing** with **NLTK**: tokenization, stopwords removal, word frequency analysis

* **Visualization & Insights**

  * Generate **bar plots and WordClouds** using **matplotlib and seaborn**
  * Discover trends and insights from book descriptions

---

## 🛠 Skills Gained

* Web crawling & HTML parsing
* XPath & CSS selectors
* Data cleaning & NLP on unstructured text
* Automating scalable scraping with Scrapy
* Data visualization & insight generation

---

## 📂 Project Structure

```text
web-scraping-books-nlp/
├── data/
│   └── books_scraped.csv        # Scraped dataset
├── notebooks/
│   └── books_analysis.ipynb     # Jupyter notebook for NLP & visualizations
├── src/
│   └── scraper.py               # Scrapy spider script
├── README.md
└── requirements.txt             # Python dependencies
```

---

## 🏃 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Aya-114/web-scraping-books-nlp.git
cd web-scraping-books-nlp
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Scrapy spider to scrape data:

```bash
scrapy crawl books_spider -o data/books_scraped.csv
```

4. Open the Jupyter notebook to analyze and visualize the data:

```bash
jupyter notebook notebooks/books_analysis.ipynb
```


---

## 🚀 Highlights

This project demonstrates my ability to **go from learning → applying → generating insights**, showcasing:

* Strong skills in **web scraping & data extraction**
* Applying **NLP on real-world unstructured text**
* **Data visualization & insight generation**
* Practical experience applying course skills in a real project

---

## 📋 Requirements

```text
pandas>=2.0
nltk>=3.8
matplotlib>=3.8
seaborn>=0.13
wordcloud>=1.8
scrapy>=2.8
```

💡 **Tips:**

* Install all dependencies at once:

```bash
pip install -r requirements.txt
```

* Download NLTK stopwords in your notebook/script:

```python
import nltk
nltk.download('stopwords')
```

