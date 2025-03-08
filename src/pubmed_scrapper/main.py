import requests
import pandas as pd
import argparse

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"


def fetch_papers(query):
    """Fetch paper IDs from PubMed based on the query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 20  # Adjust this if needed
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    paper_ids = data.get("esearchresult", {}).get("idlist", [])
    return paper_ids


def fetch_paper_details(paper_ids):
    """Fetch detailed information about each paper."""
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    response = requests.get(DETAILS_URL, params=params)
    data = response.json()

    paper_details = []
    for paper_id in paper_ids:
        summary = data.get("result", {}).get(paper_id, {})
        paper_details.append({
            "PubmedID": paper_id,
            "Title": summary.get("title", "N/A"),
            "Publication Date": summary.get("pubdate", "N/A"),
            "Authors": summary.get("authors", [])
        })

    return paper_details


def save_to_csv(papers, filename="output.csv"):
    """Save paper details to a CSV file."""
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    print(f"Saved to {filename}")
