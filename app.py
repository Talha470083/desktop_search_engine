import streamlit as st
import pickle
import re
import math
from collections import Counter, defaultdict

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Desktop Search Pro", layout="wide")
st.title("🔍 Advanced Desktop Search Engine")

# ---------------- LOAD INDEX ----------------
@st.cache_resource
def load_index():
    inv = pickle.load(open("index/inverted.pkl", "rb"))
    pos = pickle.load(open("index/positional.pkl", "rb"))
    doc_map = pickle.load(open("index/docmap.pkl", "rb"))
    norms = pickle.load(open("index/norms.pkl", "rb"))
    idf = pickle.load(open("index/idf.pkl", "rb"))
    return inv, pos, doc_map, norms, idf

inverted_index, positional_index, doc_map, doc_norms, idf = load_index()

# ---------------- PREPROCESSING ----------------
def preprocess(text):
    text = text.lower()
    tokens = re.findall(r'\b[a-z]+\b', text)
    stopwords = {"the","is","and","in","to","of","a","an","on","for","with","by","from"}
    return [t for t in tokens if t not in stopwords]

# ---------------- COSINE SEARCH ----------------
def cosine_search(query, top_k=10):
    tokens = preprocess(query)
    q_tf = Counter(tokens)
    scores = defaultdict(float)

    for term in tokens:
        if term in inverted_index:
            for docID, tf in inverted_index[term]:
                w_d = tf * idf[term]
                w_q = q_tf[term] * idf[term]
                scores[docID] += w_d * w_q

    q_norm = math.sqrt(sum((q_tf[t] * idf.get(t, 0))**2 for t in q_tf))

    results = []
    for docID, score in scores.items():
        final_score = score / (doc_norms[docID] * q_norm) if q_norm > 0 else 0
        results.append((docID, final_score))

    return sorted(results, key=lambda x: x[1], reverse=True)[:top_k]

# ---------------- PHRASE QUERY ----------------
def phrase_search(query):
    tokens = preprocess(query)

    if not tokens:
        return []

    candidate_docs = set(positional_index.get(tokens[0], {}).keys())

    for term in tokens[1:]:
        candidate_docs &= set(positional_index.get(term, {}).keys())

    results = []

    for docID in candidate_docs:
        positions_lists = [positional_index[t][docID] for t in tokens]

        first_positions = positions_lists[0]

        for pos in first_positions:
            match = True

            for i in range(1, len(tokens)):
                if (pos + i) not in positions_lists[i]:
                    match = False
                    break

            if match:
                results.append(docID)
                break

    return results

# ---------------- PROXIMITY QUERY ----------------
# format: word1 word2 /k
def proximity_search(query):

    parts = query.split()

    if len(parts) < 3:
        return []

    term1 = parts[0]
    term2 = parts[1]

    k = int(parts[2].replace("/", ""))

    term1 = preprocess(term1)[0]
    term2 = preprocess(term2)[0]

    if term1 not in positional_index or term2 not in positional_index:
        return []

    docs1 = positional_index[term1]
    docs2 = positional_index[term2]

    candidate_docs = set(docs1.keys()) & set(docs2.keys())

    results = []

    for docID in candidate_docs:

        positions1 = docs1[docID]
        positions2 = docs2[docID]

        for p1 in positions1:
            for p2 in positions2:
                if abs(p1 - p2) <= k:
                    results.append(docID)
                    break

            if docID in results:
                break

    return results


# ---------------- UI ----------------
st.sidebar.header("Search Settings")

search_type = st.sidebar.radio(
    "Query Mode",
    ["Top-K (TF-IDF)", "Phrase Query", "Proximity Query"]
)

k_val = st.sidebar.slider("Results to show", 5, 50, 10)

query = st.text_input(
    "Enter your search terms here...",
    placeholder="e.g. machine learning"
)

# ---------------- SEARCH ----------------
if st.button("Search") or query:

    if not query:
        st.info("Please enter a query.")
        st.stop()

    st.subheader(f"Results for: {query}")

    # -------- TF-IDF SEARCH --------
    if search_type == "Top-K (TF-IDF)":

        results = cosine_search(query, top_k=k_val)

        if not results:
            st.warning("No matches found.")

        for i, (docID, score) in enumerate(results):

            with st.expander(f"#{i+1} | Score: {score:.4f}"):
                st.write(f"**File:** {doc_map[docID]}")

                try:
                    snippet = open(doc_map[docID]).read()[:400]
                    st.text(snippet + "...")
                except:
                    st.write("Preview unavailable.")

    # -------- PHRASE SEARCH --------
    elif search_type == "Phrase Query":

        results = phrase_search(query)

        if not results:
            st.warning("No phrase match found.")

        for i, docID in enumerate(results[:k_val]):

            with st.expander(f"#{i+1}"):
                st.write(f"**File:** {doc_map[docID]}")

                try:
                    snippet = open(doc_map[docID]).read()[:400]
                    st.text(snippet + "...")
                except:
                    st.write("Preview unavailable.")

    # -------- PROXIMITY SEARCH --------
    elif search_type == "Proximity Query":

        st.info("Format: word1 word2 /k  (example: data science /3)")

        results = proximity_search(query)

        if not results:
            st.warning("No proximity match found.")

        for i, docID in enumerate(results[:k_val]):

            with st.expander(f"#{i+1}"):

                st.write(f"**File:** {doc_map[docID]}")

                try:
                    snippet = open(doc_map[docID]).read()[:400]
                    st.text(snippet + "...")
                except:
                    st.write("Preview unavailable.")