from collections import Counter
from pathlib import Path

STOP = {"the", "a", "and", "to", "of", "in"}

text = Path("Class 1/article.txt").read_text().lower()
words = [w.strip(".,!?\"'()") for w in text.split()]
words = [w for w in words if w and w not in STOP]

for word, n in Counter(words).most_common(10):
    print(f"{word:<15}{n}")