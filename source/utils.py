import csv

# Static Input Files
import time
from urllib.parse import urlparse

people = 'data/people/people.csv'
blacklist = 'data/Static/Blacklist.csv'
processed_emails = 'data/static/processedBA.csv'

states = 'data/Static/states.csv'

static = {'people': people, 'states': states, 'processed_emails': processed_emails,
          'blacklist': blacklist}

# Output Files
not_found_companies = 'data/Output/NotFoundQA.csv'
output_file = 'data/Output/FinalQA.csv'
email_file = processed_emails  # specify different file if you want a file different from processed email read file
company_file = 'data/processed.csv'

swap = []


####################################################################################################################
# Initializition

def open_files(array):
    for nm, vr in static.items():
        array[nm] = vr
    for k, v in array.items():
        temporary = []
        with open(v, 'r') as z:
            y = z.read().split('\n')
            reader = csv.reader(y)
            for row in reader:
                try:
                    if len(row[0].strip(" ")) > 1:
                        temporary.append(row)
                except:
                    pass
        array[k] = temporary
    return array


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


def extract_companies(people):
    companies = []
    for k, v in enumerate(people):
        if v:
            companies.append(v[0].lower())
    return companies


def listify_companies(companies):
    index = {req_word: [idx for idx, word in enumerate(companies) if word == req_word] for req_word in
             set(companies)}
    return index


#######################################################################################################################
# Check

def check_in_blacklist(company, blacklist):
    skip = False
    for blk, blk2 in enumerate(blacklist):
        if blk2[0].lower() == company:
            skip = True
            break
    return skip


def filter_sent_emails(occurence, processed_emails, people):
    temp = []
    email_processed = False
    for lookup in occurence:
        for email, email2 in enumerate(processed_emails):
            if email2[0] == people[lookup][4]:
                # print("Matching email found")
                email_processed = True
                break
        if not email_processed:
            # print(people[lookup])
            temp.append(people[lookup])
    return temp


def check_company(company, processed_companies):
    company_processed = False
    for company1, company2 in enumerate(processed_companies):
        if company2[0] == company:
            # print("Matching company found")
            company_processed = True
            break
    return company_processed


####################################################################################################################
# Others

def get_hostname(url, uri_type='both'):
    """Get the host name from the url"""
    parsed_uri = urlparse(url)
    return '{uri.netloc}'.format(uri=parsed_uri)


def Initialization(file_array):
    new_array = open_files(file_array)
    jobs, people, states, processed_emails, blacklist, processed_companies = file_array['jobs'], file_array['people'], \
                                                                             file_array['states'], file_array[
                                                                                 'processed_emails'], file_array[
                                                                                 'blacklist'], file_array[
                                                                                 'processed_companies'],
    states = Convert(states)
    people_companies = extract_companies(people)
    occr = listify_companies(people_companies)


    return {'jobs': jobs, 'people': people, 'states': states, 'processed_emails': processed_emails, 'occr': occr,
            'processed_companies': processed_companies, 'blacklist': blacklist, 'people_companies': people_companies}


def Check(people, company, processed_emails, processed_companies, blacklist, occurence):
    is_blacklisted = check_in_blacklist(company, blacklist)
    new_data = filter_sent_emails(occurence, processed_emails, people)
    is_old_company = check_company(company, processed_companies)

    return {'is_blacklisted': is_blacklisted, 'is_old_company': is_old_company, 'new_data': new_data}


def Process(city, trty, data2, requirement):
    counter = 0
    data = []
    for i, v in enumerate(data2):
        if v in swap:
            pass
            # print("found match", v)
        else:
            # print(v, swap)
            # time.sleep(5)
            if counter >= requirement:
                break
            match = [x.lower() for x in v]
            if trty in match and city in match:
                data.insert(0, v)
                counter += 1
            elif trty.lower() in match:
                data.insert(3, v)
            else:
                data.insert(10, v)
            data = data[:requirement]
    for ind, row in enumerate(data):
        swap.append(row)
    return data
