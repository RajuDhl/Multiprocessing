import csv
import time
import timeit
import datetime as dt


start = timeit.default_timer()
date = dt.datetime.now()
timestamp = date.timestamp()

# ####################################################################################################################
# Edit this part only. Input subsequent file names
requirement = 3  # Max data required for each company
jobs = 'data/QA.csv'
people = 'data/Static/All People.csv'
processed_emails = 'data/static/processed.csv'
blacklist = 'data/Static/Blacklist.csv'
processed_companies = 'data/processed.csv'

# Edit these file names to specify the names of output files
not_found_companies = 'data/Output/NotFoundQA.csv'
output_file = 'data/Output/FinalQA.csv'
email_file = processed_emails  # specify different file if you want a file different from processed email read file
company_file = processed_companies

# ####################################################################################################################


# ####################################################################################################################
# Conversion for state names


# ####################################################################################################################


# ####################################################################################################################
# Opening all files and assigning them to names in array
states = 'data/Static/states.csv'
# back_to_date = datetime.fromtimestamp(timestamp)

file_array = {'jobs': jobs, 'people': people, 'states': states, 'processed_emails': processed_emails,
              'blacklist': blacklist, 'processed_companies': processed_companies}

for k, v in file_array.items():
    temporary = []
    with open(v, 'r') as z:
        y = z.read().split('\n')
        reader = csv.reader(y)
        for row in reader:
            if len(row) > 0:
                temporary.append(row)
    file_array[k] = temporary

jobs, people, states, processed_emails, blacklist, processed_companies = file_array['jobs'], file_array['people'], \
                                                                         file_array['states'], file_array[
                                                                             'processed_emails'], file_array[
                                                                             'blacklist'], file_array[
                                                                             'processed_companies'],

people_companies = []
for k, v in enumerate(people):
    if v:
        people_companies.append(v[3].lower())
occr = {req_word: [idx for idx, word in enumerate(people_companies) if word == req_word] for req_word in
        set(people_companies)}
# print(occr['nr consulting'])
# time.sleep(500)
states = Convert(states)


# ####################################################################################################################


# ###################################################################################################################
def Check(company, city, trty):
    if company not in occr:
        return {'temp': [], 'company': False, 'company_processed': False}
    counter = 0
    skip = False
    email_processed = False
    company_processed = False
    occurances = occr[company]
    # ####################################################################################################################
    # Check in blacklist
    for blk, blk2 in enumerate(blacklist):
        if blk2[0].lower() == company:
            skip = True
            break
    if skip:
        return {'temp': [], 'company': True, 'company_processed': True}

    # ####################################################################################################################
    # Check in Processed Emails
    temp = []
    for lookup in occurances:
        for email, email2 in enumerate(processed_emails):
            if email2[0] == people[lookup][4]:
                # print("Matching email found")
                email_processed = True
                break
        if not email_processed:
            # print(people[lookup])
            temp.append(people[lookup])
    # print(temp2)
    # print("Hello world")
    # time.sleep(0.25)

    # ####################################################################################################################
    # Check in Processed Companies
    for company, company2 in enumerate(processed_companies):
        if company2[0] == company:
            # print("Matching company found")
            company_processed = True
            break
    # ####################################################################################################################
    # Check if fulfilled requirement
    final = []
    for i, v in enumerate(temp):
        if counter >= requirement:
            return {'temp': final, 'company_processed': company_processed, 'company': True}
        match = [x.lower() for x in v]
        if trty in match and city in match:
            final.insert(0, v)
            counter += 1
        elif trty.lower() in match:
            final.insert(3, v)
        else:
            final.insert(10, v)
        temp = final[:requirement]
    return {'temp': temp, 'company_processed': company_processed, 'company': True}


def main():
    new_emails = []
    new_companies = []
    not_found = []
    output = []
    for ids, val in enumerate(jobs):
        company_name = val[1].lower()
        dummy_location = val[2].split(',')
        location = dummy_location[0].lower()
        try:
            if len(dummy_location[1]) > 3:
                trty = states[dummy_location[1].strip(' ')]
            else:
                trty = ""
        except:
            trty = ""
        # print(company_name, location, trty)
        data = Check(company=company_name, city=location, trty=trty)
        # print(data['company'])
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

    # with open(output_file, "w", encoding='UTF8', newline='') as r:
    #     writer = csv.writer(r)
    #     writer.writerows(output)
    #
    # with open(not_found_companies, "w", encoding='UTF8', newline='') as q:
    #     writer1 = csv.writer(q)
    #     writer1.writerows(not_found)
    #
    # with open(email_file, "a", encoding='UTF8', newline='') as p:
    #     writer2 = csv.writer(p)
    #     writer2.writerows(new_emails)
    #
    # with open(company_file, "a", encoding='UTF8', newline='') as o:
    #     writer3 = csv.writer(o)
    #     writer3.writerows(new_companies)


main()
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in " + str(execution_time))
