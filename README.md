# PubMed Research Paper Scraper

This is a command-line tool that fetches research papers from **PubMed** based on a user-specified query.  
It filters papers where at least one author is affiliated with a **pharmaceutical or biotech company** and saves the results in a **CSV file**.

## 🚀 Features
- Fetches **research papers** from PubMed using **PubMed API**.
- Filters **non-academic authors** using heuristics.
- Saves results in a **CSV file**.
- Supports **command-line arguments** for flexible usage.
- Uses **Poetry** for dependency management.

---

## 📌 Installation & Setup

1️⃣ Install Poetry (If not installed)
Poetry is required to manage dependencies. Install it using:

pip install poetry


2️⃣ Clone the Repository

git clone <your-github-repo-url>
cd pubmed_scraper

3️⃣ Install Dependencies
Inside the project directory, run:

poetry install

This will set up all required dependencies


📌 Usage
You can run the program using the command line.

poetry run python pubmed_scraper/main.py "<your-query>"

This will fetch PubMed papers related to cancer treatment and display them.

