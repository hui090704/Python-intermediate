from collections import Counter, defaultdict, deque

# Counter: count anything
votes = ["nasi lemak", "roti canai", "nasi lemak", "laksa", "nasi lemak"]
tally = Counter(votes)
print(tally.most_common(2))

# defaultdict: group without checking "if key in dict"
students = [("Aisyah", "5A"), ("Darren", "5B"), ("Nurin", "5A")]
by_class = defaultdict(list)
for name, cls in students:
    by_class[cls].append(name)
print(dict(by_class))

by_alphabet = defaultdict(list)
for name, cls in students:
    by_alphabet[name[0]].append(name)
print(dict(by_alphabet))

#by_class[name[0]].append(name)
#print(dict(by_class))


# deque(maxlen=3): keep only the last 3 items
recent = deque(maxlen=3)
for page in ["home", "menu", "cart", "pay", "done"]:
    recent.append(page)
print(list(recent))

#Count letters
letters = Counter("Malaysia")
print(letters)

