# 📰 News Extractor Using CSS Selectors

A Streamlit-based web app that extracts news article content, author name, and published date from popular Indian news websites using BeautifulSoup and CSS selectors.

## Supported News Sites

- The Hindu
- Economic Times
- Times of India
- Indian Express

---

## Tech Stack

- **Frontend:** Streamlit (for UI)
- **Backend:** Python, BeautifulSoup
- **Web Scraping:** requests, bs4
- **Deployment:** Works locally and deployed on Streamlit Cloud

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Gautam413/News-Extractor-Using-CSS-Selectors.git
cd News-Extractor-Using-CSS-Selectors
```

### 2. Create and activate virtual environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate
```

```bash
# On Linux/macOS
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## News-Extractor-Using-CSS-Selectors/
├── app.py              # Streamlit frontend app
├── scraper.py          # Web scraping logic for each news site
├── requirements.txt    # Python dependencies
├── README.md           # Project description
└── .gitignore          # Files to exclude from version control


---

## Feedback
Feel free to [open an issue](https://github.com/Gautam413/News-Extractor-Using-CSS-Selectors/issues) .

---

## License
This project is licensed under the MIT License.
