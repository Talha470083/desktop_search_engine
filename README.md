V# 🔍 Advanced Desktop Search Engine

### NLP Assignment – Inverted Index Based Information Retrieval System

---

## 📌 Project Overview

This project implements a **high-performance desktop search engine** using **Information Retrieval (IR)** and **Natural Language Processing (NLP)** techniques.
The system indexes thousands of documents and allows users to search them efficiently using multiple query strategies.

The application is built with:

* **Python**
* **Streamlit**
* **TF-IDF Vector Space Model**
* **Inverted Index**
* **Positional Index**

The search engine supports:

* Ranked keyword search
* Phrase search
* Proximity search

All results are displayed in a **clean interactive web interface**.

---

# 🧠 Key Concepts Implemented

This project demonstrates several core **Information Retrieval techniques**:

| Concept           | Description                                                   |
| ----------------- | ------------------------------------------------------------- |
| Inverted Index    | Maps each term to the list of documents containing it         |
| Positional Index  | Stores word positions to support phrase and proximity queries |
| TF-IDF Weighting  | Measures importance of terms in documents                     |
| Cosine Similarity | Ranks documents by similarity to query                        |
| Tokenization      | Splitting text into meaningful words                          |
| Stopword Removal  | Removing common words like *the, is, and*                     |
| Query Processing  | Parsing and interpreting user queries                         |

---

# 🚀 Features

## 🔎 1. Top-K Ranked Retrieval

Uses **TF-IDF + Cosine Similarity** to rank documents based on relevance.

Example query:

```
machine learning algorithms
```

Output:

```
Ranked list of most relevant documents
```

---

## 📝 2. Phrase Query Search

Finds documents containing **exact word sequences**.

Example:

```
"machine learning"
```

The system checks whether words appear **adjacent in the document** using the positional index.

---

## 📏 3. Proximity Query Search

Finds documents where two words appear **within a specific distance**.

Example:

```
data science /3
```

Meaning:

```
distance(data, science) ≤ 3
```

---

# 🏗 System Architecture

```
                 ┌──────────────┐
                 │  Documents   │
                 └──────┬───────┘
                        │
                        ▼
              ┌─────────────────┐
              │ Text Processing │
              │ Tokenization    │
              │ Stopword Removal│
              └──────┬──────────┘
                     │
                     ▼
             ┌───────────────┐
             │ Index Builder │
             └──────┬────────┘
                    │
       ┌────────────┴─────────────┐
       ▼                          ▼
┌──────────────┐         ┌────────────────┐
│ Inverted     │         │ Positional     │
│ Index        │         │ Index          │
└──────┬───────┘         └──────┬─────────┘
       │                         │
       └─────────────┬───────────┘
                     ▼
              ┌──────────────┐
              │ Query Engine │
              └──────┬───────┘
                     ▼
            ┌───────────────────┐
            │ Streamlit UI App  │
            └───────────────────┘
```

---

# 📂 Project Structure

```
desktop_search_engine/
│
├── advanced_nlp_search_engine.ipynb
├── app.py
├── README.md
├── requirements.txt
├── file generation script.py
│
├── dataset/
│   └── (generated documents used for indexing)
│
└── index/
    ├── inverted.pkl
    ├── positional.pkl
    ├── docmap.pkl
    ├── norms.pkl
    └── idf.pkl
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Talha470083/desktop_search_engine.git
cd desktop-search-engine
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
streamlit
numpy
pandas
```

---

## 3️⃣ Run the Application

```bash
streamlit run app.py
```

The interface will open in your browser:

```
http://localhost:8501
```

---

# 💻 Example Queries

| Query Type      | Example            |
| --------------- | ------------------ |
| Keyword Search  | `machine learning` |
| Phrase Query    | `"deep learning"`  |
| Proximity Query | `data science /2`  |

---

# 📊 Ranking Model

The system uses the **Vector Space Model** with **TF-IDF weighting**.

Term Weight:

```
TF-IDF = TF × IDF
```

Where:

* **TF** = term frequency in document
* **IDF** = inverse document frequency

---

## Cosine Similarity

Document ranking is computed using cosine similarity:

```
cosine(q,d) = (q · d) / (||q|| × ||d||)
```

Where:

* `q` = query vector
* `d` = document vector

Higher cosine value → **more relevant document**.

---

# 📈 Performance

The system efficiently handles **large document collections** because:

* Searching uses **index lookups instead of full scans**
* Query time complexity is greatly reduced.

Comparison:

| Method         | Complexity             |
| -------------- | ---------------------- |
| Naive Search   | O(N × document length) |
| Inverted Index | O(number of postings)  |

---

# 🧪 Technologies Used

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Core implementation            |
| Streamlit  | Interactive web interface      |
| Pickle     | Index storage                  |
| Regex      | Text preprocessing             |
| Math       | Vector similarity calculations |

---

# 📷 Interface Preview

```
🔍 Advanced Desktop Search Engine
---------------------------------

Enter Query: machine learning

Results:
1. document_120.txt
2. document_432.txt
3. document_98.txt
```

---

# 🎓 Learning Outcomes

Through this project we learned:

* Fundamentals of **Information Retrieval**
* Efficient **indexing techniques**
* Document ranking using **TF-IDF**
* Query processing strategies
* Building **interactive search systems**

---

# 🔮 Future Improvements

Possible extensions:

* Query autocomplete
* Snippet highlighting
* Semantic search using **Word2Vec/BERT**
* Spell correction
* Distributed indexing
* Elasticsearch integration

---

# 👨‍💻 Author

**Student Name:** *Your Name*
**Course:** Natural Language Processing
**Assignment:** Search Engine using Inverted Index
**University:** *Your University*

---

# 📜 License

This project is created for **educational purposes** as part of an NLP coursework assignment.

---

⭐ If you find this project useful, feel free to star the repository!
