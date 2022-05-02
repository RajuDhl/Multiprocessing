import json
import time
import timeit
from random import random
from multiprocessing import Pool
from time import sleep

import pandas as pd
import requests

from source.utils import *

original = open("data/people/BAcsv.csv", 'r+')
websites = open("data/people/apollo-accounts-export (5).csv", 'r+')
required_pages = 30
reader = csv.reader(original)
reader2 = csv.reader(websites)

csv_header = ["organization", "first_name", "last_name", 'headline', 'city', 'state', 'country', 'linkedin_url']
states = open("data/Static/states.csv", 'r+').read().split('\n')
reader3 = csv.reader(states)
state = []
for row in states:
    state.append(row.split(','))

abbr = Convert(state)

combined = []
one = []
two = []
three = []
four = []
domain_text = ""
for row in reader:
    one.append(row)
for sub in reader2:
    two.append(sub)
for i in one:
    for j in two:
        if j[0].lower() == str(i[1]).lower():

            dummy_location = i[2].split(',')
            location = dummy_location[0].lower()
            try:
                state = abbr[dummy_location[1].strip()]
            except:
                state = ""
            i.pop(2)
            i.append(location)
            i.append(state)
            raw_domain = get_hostname(j[1])
            k = i + [raw_domain]
            combined.append(k)
            domain_text = domain_text + raw_domain.strip() + "\n"

# print(combined)
domain = domain_text
result_list = []
new_data = [{'data1': 'val1'}, {'data2': 'val2'}]

titles = ["hr", "Recruiter", 'talent', 'people', 'recruiting', 'recruit']
url = "https://api.apollo.io/v1/mixed_people/search"

headers = {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache',
    'x-api-key': 'xQx9DESeSh_ZQb39lIUVwQ',
}


def extract_companies(people):
    companies = []
    for k, v in enumerate(people):
        if v:
            pass
            companies.append(v[0].lower())
    return companies


def listify_companies(companies):
    index = {req_word: [idx for idx, word in enumerate(companies) if word == req_word] for req_word in
             set(companies)}
    return index


def Search(page):
    start = timeit.default_timer()
    payload = json.dumps({
        "api_key": "xQx9DESeSh_ZQb39lIUVwQ",
        "q_organization_domains": domain,
        "person_titles": titles,
        "page": page,
        "per_page": "200",
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    people = data['people']
    for row in data['contacts']:
        people.append(row)
    for v in people:
        try:
            if v['country'] != 'United States':
                pass
            else:
                v['organization'] = v['organization']['name']
                result_list.append(v)
        except:
            pass

    return result_list


for page in range(1, 100):
    val = Search(page)
    if len(val) < 3:
        break
    for row in val:
        four.append(row)
# print(len(four), four)
df = pd.DataFrame(four)
# print(df)
df = df[csv_header]
df.drop_duplicates(subset='linkedin_url', keep="first", inplace=True)
df.to_csv('data/people/test2.csv', encoding='utf-8', index=False)

products_list = df.values.tolist()
# print(products_list)
comp = extract_companies(products_list)
list2 = listify_companies(comp)
# time.sleep(500)
for k, v in enumerate(combined):
    temp = []
    # print(v)
    try:
        loc = list2[v[1].lower()]
        # print(loc)
        for zz in loc:
            if products_list[zz][4] == v[2] and products_list[zz][5] == v[3]:
                # print("people", products_list[zz])
                temp.insert(0, v + products_list[zz])
            elif products_list[zz][5] == v[3]:
                # print("people", products_list[zz])
                temp.insert(4, v + products_list[zz])
            else:
                # print("people", products_list[zz])
                temp.insert(10, v + products_list[zz])
    except:
        pass
    temp = temp[:5]
    for row in temp:
        three.append(row)
# print("One", three)
try:
    with open('test-file.csv', 'w') as zzzz:
        writer = csv.writer(zzzz)
        writer.writerows(three)
except:
    pass
