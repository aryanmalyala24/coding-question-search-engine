**Coding Question Search Engine**

A lightweight search engine that indexes coding problems and retrieves the most relevant LeetCode questions based on user queries using Information Retrieval (IR) techniques. The project builds an inverted index, computes TF-IDF scores, and ranks problems according to query relevance.

**Features**

Scrapes and indexes LeetCode problem statements.
Builds an inverted index for efficient keyword lookup.
Computes Term Frequency (TF) and Inverse Document Frequency (IDF) values for ranking.
Uses TF-IDF scoring to retrieve and rank the most relevant coding questions.
Returns the Top-K matching problems with their corresponding LeetCode links.
Provides a simple Flask-based web interface for interactive searching.

**Tech Stack**

Python
Flask
Selenium
BeautifulSoup
HTML/CSS
Information Retrieval (TF-IDF, Inverted Index)

**Project Structure**

.
|
|--Qindex.txt
|--documents.txt
|--idf-values.txt
|--index.html
|--inverted-index.txt
|--leetcode_problem_links.txt
|--prep.py
|--query.py
|--removing_solution.py
|--scrap.py
|--scrap_ques.py
|--style.css
|--vocab.txt

**How It Works**

1. Data Collection
Selenium automatically scrapes LeetCode problem links.
Problem titles and statements are extracted and stored locally.
2. Index Construction
Documents are tokenized and normalized.
Vocabulary is generated.
Document frequencies are computed.
An inverted index is built for fast retrieval.
3. Query Processing
User queries are tokenized.
Matching documents are retrieved using the inverted index.
TF-IDF scores are computed.
Documents are ranked by relevance.
4. Result Retrieval
The highest-ranked coding questions are displayed along with their corresponding LeetCode problem links.

**Information Retrieval Pipeline**

LeetCode Pages
       │
       ▼
Web Scraping
       │
       ▼
Text Preprocessing
       │
       ▼
Vocabulary Generation
       │
       ▼
Inverted Index
       │
       ▼
TF-IDF Scoring
       │
       ▼
Ranked Search Results

**Key Concepts Implemented**

Information Retrieval
Inverted Index
TF (Term Frequency)
IDF (Inverse Document Frequency)
TF-IDF Ranking
Document Indexing
Web Scraping
Query Processing
Search Result Ranking
