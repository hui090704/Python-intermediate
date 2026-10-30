students = [("Aisyah", 88), ("Darren", 92), ("Nurin", 75), ("Tan", 92)]

# sort by mark, highest first
ranked = sorted(students, key=lambda s: s[1], reverse=True)
print(ranked)

# sort by mark (high to low), then by name (A to Z) on a tie
print(sorted(students, key=lambda s: (-s[1], s[0])))

# best and worst
print(max(students, key=lambda s: s[1]))
print(min(students, key=lambda s: s[1]))

#Sorted by length of name
rank2 = sorted(students, key=lambda s: len(s[0]))
print(rank2)

# Find last alphabetically arranged
print(max(students, key=lambda s:s[0]))

# same thing written as a normal function
def by_mark(student):
    return student[1]

print(sorted(students, key=by_mark)[0])