# import csv
# import time
#
# with open("data/Output/Text2-to-csv.csv", 'r') as f:
#     z = f.read().split('\n')
#     reader = csv.reader(z)
#     print(reader)
#     temp = []
#     temp2 = []
#     for row in reader:
#         print(row)
#         if row not in temp:
#             # print("hello")
#             try:
#                 temp.append(row)
#                 temp2.append(row[3])
#             except:
#                 print("error in", row)
#     check = []
#     done = []
#     for row in temp:
#         try:
#             if row[1] not in done:
#                 done.append(row[1])
#                 vars()[row[3]] = []
#                 vars()[row[3]].append(row)
#                 with open(f'data/Output/state separated/{row[3]}.csv', 'a') as y:
#                     writer = csv.writer(y)
#                     print(check)
#                     if row[3] in check:
#                         print("not found")
#                         writer.writerows(vars()[row[3]])
#                     else:
#                         check.append(row[3])
#                         print("here")
#                         writer.writerow(['position','company', 'location', 'states'])
#                         writer.writerows(vars()[row[3]])
#         except:
#             pass
#
import csv
import os

from source.utils import Convert

one = []
two = []
jobs = open('data/people/1April text2csv (1).csv', 'r+', encoding='UTF8')
cwd = os.getcwd()
dir = "C:\\Users\\raju\\PycharmProjects\\flaskProject\\main\\data\\static\\processed"
os.chdir(dir)
people = open('known_people.csv', 'r+', encoding='UTF8')
os.chdir(cwd)
reader = csv.reader(jobs)
reader2 = csv.reader(people)

states = open("data/Static/states.csv", 'r+').read().split('\n')
reader3 = csv.reader(states)
state = []
for row in states:
    state.append(row.split(','))

abbr = Convert(state)
# print(abbr['TX'])

for row in reader:
    try:
        one.append(row)
    except:
        pass
for sub in reader2:
    try:
        two.append(sub)
    except:
        pass
# two = pd.read_csv("data/people/test2.csv", header=None, index_col=0, squeeze=True).to_dict()
# print(two)


def extract_companies(people):
    companies = []
    for k, v in enumerate(people):
        if v and v not in companies:
            companies.append(v[0].lower())
    return companies


def listify_companies(companies):
    index = {req_word: [idx for idx, word in enumerate(companies) if word == req_word] for req_word in
             set(companies)}
    return index


comp = extract_companies(two)
print("comp", comp)
list2 = listify_companies(comp)
print("list", list2)
processed = []
final = []
for i, v in enumerate(one):
    print(v)
    data2 = []
    data3 = []
    temp = []
    if v[1].lower() in processed:
        pass
    else:
        company = v[1].lower()
        processed.append(company)
        raw_add = v[2].split(',')
        city = raw_add[0]

        try:
            state = abbr[raw_add[1].strip(" ")]
            print("state is", abbr[raw_add[1].strip(" ")])
        except:
            state = ""
        # match = [x.lower() for x in v]
        try:
            d = list2[company]
            for zz in d:
                # print(state.lower(), two[zz][5].lower(), two[zz][4].lower())
                # time.sleep(1)
                if state.lower() == two[zz][5].lower() and city.lower() == two[zz][4].lower():
                    print("Touched here")
                    data2.insert(0, two[zz])
                elif state.lower() == two[zz][5].lower():
                    data2.insert(10, two[zz])
                else:
                    data3.insert(10, two[zz])
        except: pass
        for row in data3:
            data2.append(row)
    data = data2[:4]
    if len(data) >= 1:
        for ind, row in enumerate(data):
            final.append(row)


with open('data/people/BA 31 Mar state Separated.csv', "w", encoding='UTF8', newline='') as o:
    writer3 = csv.writer(o)
    writer3.writerows(final)
