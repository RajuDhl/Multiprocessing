import csv
import os
from urllib.parse import urlparse

dir = "C:\\Users\\raju\\PycharmProjects\\flaskProject\\main\\data\\static\\processed"
states = open("data/Static/states.csv", 'r+').read().split('\n')
cwd = os.getcwd()
os.chdir(dir)
# print("current dir is", os.getcwd())
people_data = open("known_people.csv", 'r+', encoding="ISO-8859-1").read().split('\n')
reader3 = csv.reader(states)
reader = csv.reader(people_data)
state = []
url_array = []
os.chdir(cwd)
for row in states:
    state.append(row.split(','))

headers = {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache',
    'x-api-key': 'xQx9DESeSh_ZQb39lIUVwQ',
}


def get_hostname(url):
    """Get the host name from the url"""
    parsed_uri = urlparse(url)
    return '{uri.netloc}'.format(uri=parsed_uri)


def Convert(lst):
    d = {}
    for row in lst:
        try:
            key = row[1]
            value = row[0]
            d[key] = value
        except:
            pass
    return d


for row in reader:
    try:
        if row[7] not in url_array:
            url_array.append(get_hostname(row[7].strip(' ')))
    except:
        pass

abbr = Convert(state)


def Enrich_csv(one):
    combined = []
    domain_text = ""
    ik = 0
    for i in one:
        # dummy_location = i[2].split(',')
        # location = dummy_location[0].lower()
        # try:
        #     raw_state = abbr[dummy_location[1].strip()]
        # except:
        #     raw_state = ""
        # i.pop(2)
        # i.append(location)
        # i.append(raw_state)
        raw_domain = ""
        # # print(i)
        url = get_hostname(i[1])
        if url not in url_array:
            # print(i[1])
            raw_domain = url
            url_array.append(url)
            # print(len(url_array))
        k = i + [raw_domain]
        combined.append(k)
        if len(raw_domain) > 3:
            domain_text = domain_text + raw_domain.strip() + "\n"
            ik += 1
    # print("domain text", domain_text)
    # print(ik)
    return {'domain_text': domain_text}


def extract_list(jobs):
    def extract_companies(jobs):
        companies = []
        for k, v in enumerate(jobs):
            if v:
                companies.append(v[1].lower())
        return companies

    def listify_companies(companies):
        index = {req_word: [idx for idx, word in enumerate(companies) if word == req_word] for req_word in
                 set(companies)}
        return index

    dm = extract_companies(jobs)
    list2 = listify_companies(dm)
    return list2
