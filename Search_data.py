import csv
import json
import time
from multiprocessing import Pool

import requests

from deps import headers, Enrich_csv, extract_list

original = open("data/people/apollo-accounts-export (44).csv", 'r+', encoding='utf8')  # websites
# websites = open("data/people/apollo-accounts-export (18).csv", 'r+', encoding='utf8')
reader = csv.reader(original)
# reader2 = csv.reader(websites)

one = []
two = []
for row in reader:
    one.append(row)
# for sub in reader2:
#     two.append(sub)

titles = ["Recruiter", 'talent', 'people', 'recruiting', 'recruit', 'Human resource', 'hr']
url = "https://api.apollo.io/v1/mixed_people/search"

enriched = Enrich_csv(one)
# listed = extract_list(one)
domain = enriched['domain_text']
total_data_checker = []
final_data = []


# print(domain)


def search(page):
    time.sleep(60)
    print("at page", page)
    payload = json.dumps({
        "api_key": "xQx9DESeSh_ZQb39lIUVwQ",
        "q_organization_domains": domain,
        # "q_organization_domains": 'www.accenture.com',
        "person_titles": titles,
        "page": page,
        "per_page": "200",
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    people = data['people']
    contact = data['contacts']
    total_entries = data['pagination']
    for cont in range(0, len(data['contacts'])):
        people.append(contact[cont])
    print("Total No. of pages", total_entries['total_pages'], total_entries['total_entries'])
    return {'data': people}


def start_process(start_page, total_pages):
    pool = Pool(60)

    def check_data(result):
        data = result['data']
        # print(len(data))
        for cont in range(0, len(data)):
            try:
                if data[cont]['country'] != 'United States' or data[cont]['email_status'] == 'unavailable':
                    pass
                else:
                    org = data[cont]['organization']
                    data[cont]['organization'] = org['name']
                    data[cont]['website'] = org['website_url']
                    final_data.append(data[cont])
            except:
                pass

    for k in range(start_page, start_page + total_pages):
        pool.apply_async(search, args=(k,), callback=check_data)

    pool.close()
    pool.join()

    return {'final_data': final_data}

# if __name__ == '__main__':
#     start_process()
#     print("process executed")
