import csv
import time
import timeit
import datetime as dt
from source.utils import Initialization, Check, Process

# #####################################################################################################################
start = timeit.default_timer()
date = dt.datetime.now()
timestamp = date.timestamp()

# ####################################################################################################################

# ####################################################################################################################
# Edit this part only. Input subsequent file names
requirement = 3  # Max data required for each company
jobs = 'data/Output/Text2-to-csv.csv'
processed_companies = 'data/processed.csv'  # While changing this file, change the variable in utils too for output file

file_array = {'jobs': jobs, 'processed_companies': processed_companies}
init = Initialization(file_array)

# Converting the list into variable
for k, v in init.items():
    vars()[k] = v


# ####################################################################################################################


# ###################################################################################################################
def Check2(company, city, trty):
    counter = 0
    try:
        print(occr[company])
    except: print("Not found", company)
    if company not in occr:
        return {'temp': [], 'company': False, 'company_processed': False}
    occurence = occr[company]
    print(occurence)
    validation = Check(people, company, processed_emails, processed_companies, blacklist, occurence)
    if validation['is_blacklisted']:
        return {'temp': [], 'company': True, 'company_processed': True}

    data = validation['new_data']
    company_processed = validation['is_old_company']
    sorted_data = Process(city, trty, data, requirement)
    return {'temp': sorted_data, 'company_processed': company_processed, 'company': True}


def main():
    new_emails = []
    new_companies = []
    not_found = []
    output = []
    # print(jobs)
    for ids, val in enumerate(jobs):
        company_name = val[1].lower()
        dummy_location = val[2].split(',')
        location = dummy_location[0].lower()
        try:
            if len(dummy_location[1]) >1:
                trty = states[dummy_location[1].strip()]
                # print(trty)
            else:
                trty = ""
        except:
            trty = ""
        # print(company_name, location, trty)
        data = Check2(company=company_name, city=location, trty=trty)
        print(data['company'])
        try:
            if not data['company']:
                not_found.append(val)
            else:
                if data['temp']:
                    for yyy in range(0, 3):
                        output.append([" "])
                    for row in data['temp']:
                        if len(row) > 4:
                            # print(row)
                            output.append(val + row)
                            new_emails.append([row[4], timestamp])
                    if not data['company_processed']:
                        new_companies.append([data['temp'][0][4], timestamp])
        except:
            pass
            print("error in", len(data))
            for zz in enumerate(data):
                print(zz)
            time.sleep(500)
    # print(output)

    with open('data/Output/d.csv', "w", encoding='UTF8', newline='') as r:
        writer = csv.writer(r)
        writer.writerows(output)

    with open('a.csv', "w", encoding='UTF8', newline='') as q:
        writer1 = csv.writer(q)
        writer1.writerows(not_found)

    with open('b.csv', "a", encoding='UTF8', newline='') as p:
        writer2 = csv.writer(p)
        writer2.writerows(new_emails)

    with open('c.csv', "a", encoding='UTF8', newline='') as o:
        writer3 = csv.writer(o)
        writer3.writerows(new_companies)


main()
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in " + str(execution_time))
