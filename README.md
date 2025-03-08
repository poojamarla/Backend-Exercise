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

### **1️⃣ Install Poetry (If not installed)**
Poetry is required to manage dependencies. Install it using:

```sh
pip install poetry
