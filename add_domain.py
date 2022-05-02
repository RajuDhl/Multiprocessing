import csv

import pandas as pd

domain_file = open("data/people/apollo-accounts-export (16).csv", encoding='utf8')
jobs_file = open("data/people/17March text2csv (1).csv", encoding='utf8')
domain = []
jobs = []
final = []
reader = csv.reader(domain_file)
reader2 = csv.reader(jobs_file)

for row in reader:
    domain.append(row)
for row in reader2:
    jobs.append(row)

for i, v in enumerate(jobs):
    found = False
    for i2, v2 in enumerate(domain):
        if v[1].lower() == v2[0].lower():
            print(v[1], v2[0])
            final.append(v + [v2[2]])
            found = True
            break
        else:
            pass
    if not found:
        final.append(v)
print(final)
df = pd.DataFrame(final)
df.to_csv('data/people/QA with domain.csv', encoding='utf-8', index=False)
