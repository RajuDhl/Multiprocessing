# import csv
# import time
#
# from source.utils import extract_companies, listify_companies, Convert
#
#
# def open_files(array2):
#     for k, v in array.items():
#         temporary = []
#         with open(v, 'r', encoding='utf8') as z:
#             y = z.read().split('\n')
#             reader = csv.reader(y)
#             for row in reader:
#                 try:
#                     if len(row[0].strip(" ")) > 1:
#                         temporary.append(row)
#                 except:
#                     pass
#         array[k] = temporary
#     return array
#
#
# jobs = 'data/people/BAcsv.csv'
# people = 'data/people/1.csv'
# states = 'data/Static/states.csv'
# surnames = 'data/Static/Indian Surnames.csv'
#
#
# array = {'jobs': jobs, 'people': people, 'states': states, 'surnames': surnames}
# files = open_files(array)
#
# jobs = files['jobs']
# people = files['people']
# states = files['states']
# surnames = files['surnames']
# # print(people)
#
# companies = extract_companies(people)
# list_people = listify_companies(companies)
# states = Convert(states)
#
# output = []
# processed = []
# for i, v in enumerate(jobs):
#     location = v[2].split(',')
#     # print(location)
#     city = location[0].lower()
#     try:
#         state = states[location[1].strip()].lower()
#     except:
#         state = " "
#     temp = []
#     c = []
#     s = []
#     country = []
#     # print(city, state)
#     try:
#         position = list_people[v[1].lower()]
#         if v[1] not in processed:
#             processed.append(v[1])
#             skip = False
#             for z in position:
#                 match = people[z]
#                 for iii, vvv in enumerate(surnames):
#                     if vvv[0] == match[2].lower():
#                         skip = True
#                         break
#                 if skip:
#                     pass
#                 # print(state, match[6].lower())
#                 else:
#                     if city == match[4].lower() and state == match[5].lower():
#                         c.append(people[z])
#                     elif state == match[5].lower():
#                         # print("at least some")
#                         s.append(people[z])
#                     else:
#                         country.append(people[z])
#         for found in c:
#             temp.append(found)
#         for found in s:
#             temp.append(found)
#         for found in country:
#             temp.append(found)
#
#     except:
#         pass
#         # print("Not found", v[1])
#     temp = temp[:4]
#     for k in temp:
#         output.append(k)
# print(output)
#
# with open('data/people/enrich.csv', "w", encoding='UTF8', newline='') as r:
#     writer = csv.writer(r)
#     writer.writerows(output)

import pandas as pd

fir = []
sec = []

df3 = pd.read_csv('data/people/outcome.csv')

for i in range(1, 50):
    fir.append([i, i* 2])

for i in range(1, 20):
    sec.append([i*4, i*8])

df = pd.DataFrame(fir)
df2 = pd.DataFrame(sec)

final = df.merge(df2, indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)

print(df3)
