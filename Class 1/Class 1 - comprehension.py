prices = [4.50, 12.00, 8.90, 25.00, 3.20]

# Loop version: 4 lines
with_sst = []
for p in prices:
    if p > 5:
        with_sst.append(round(p * 1.06, 2))

# Comprehension version: 1 line, same result
with_sst2 = [p*100 for p in prices if p <10]
#with_sst2 = [round(p * 1.06, 2) for p in prices if p > 5]
print(with_sst == with_sst2, with_sst2)

# dict comprehension: name -> length
names = ["Aisyah", "Darren", "Nurin"]
#print({n: len(n) for n in names})
print({n[0] for n in names})

# set comprehension: unique, cleaned codes
codes = ["JB01", "kl02", "jb01", "PG03", "KL02"]
print(sorted({c.upper() for c in codes}))