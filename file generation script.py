import os
import random

NUM_DOCS = 50000
OUTPUT_DIR = r"C:\Users\User\Desktop\dataset"

os.makedirs(OUTPUT_DIR, exist_ok=True)

topics = [
    "pakistan cricket team won the match",
    "data science and machine learning applications",
    "artificial intelligence transforming industries",
    "punjab university research programs",
    "technology startups and innovation",
    "global economy and financial markets",
    "climate change and environmental policy",
    "history of south asian culture",
    "modern software engineering practices",
    "space exploration and future missions"
]

def generate_document():
    sentences = []
    for _ in range(random.randint(5,15)):
        sentences.append(random.choice(topics))
    return ". ".join(sentences)

for i in range(NUM_DOCS):
    text = generate_document()
    file_path = os.path.join(OUTPUT_DIR, f"doc_{i}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

print(f"Dataset generation complete. {NUM_DOCS} files created in '{OUTPUT_DIR}' folder.")
