# Takes 22.543460099957883 seconds
import csv
import timeit
from datetime import datetime
import datetime as dt
import time

start = timeit.default_timer()
date = dt.datetime.now()
timestamp = date.timestamp()
# back_to_date = datetime.fromtimestamp(timestamp)
freq = "data/processed.csv"

print("Opening Files")
jobs = open("data/QA.csv", 'r+').read().split('\n')
people = open("data/Static/All People.csv", 'r+').read().split('\n')
states = open("data/Static/states.csv", 'r+').read().split('\n')
processed = open("data/Static/processed.csv", 'r+').read().split('\n')
blacklisted = open("data/Static/Blacklist.csv", 'r+').read().split('\n')
send = open(freq, 'r+').read().split('\n')
dummy = []
dummy2 = []
state = []
old = []
prev_sent = []
sending = []
sent = []
todays = []
not_found = []
blacklist = []
output = []

temporary = []

reader = csv.reader(jobs)
reader2 = csv.reader(people)
reader3 = csv.reader(states)
reader4 = csv.reader(processed)
reader5 = csv.reader(blacklisted)
reader6 = csv.reader(send)

print("Appending files to array")
for row in reader:
    if len(row) > 2:
        dummy.append(row)

for row in reader2:
    if len(row) > 5:
        dummy2.append(row)

for row in reader4:
    try:
        if len(row[0]) > 5:
            old.append(row[0].lower())
    except:
        pass
for row in reader5:
    try:
        blacklist.append(row[0].lower())
    except:
        pass
for row in reader6:
    try:
        # print(row)
        sending.append(row)
        prev_sent.append(row[0].lower())
    except:
        pass
# print(prev_sent)
for k, ddd in enumerate(prev_sent):
    sent.append([ddd])
# print(sent)

for i, v in enumerate(old):
    todays.append([v])
print(todays)
# time.sleep(50)
print("Finished Initialization")


def Convert(lst):
    d = {}
    for row33 in lst:
        try:
            key = row33[1]
            value = row33[0]
            d[key] = value
        except:
            pass
    return d


def lookup(dummy_row, company, city, trty):
    # print("looking for ===>", company, trty, city)
    counter = 0
    m = 0
    temp = []
    # Approach 1
    # ##############################################################################################
    # counter = 0
    # temp = []
    # temp2 = []
    # m = 0
    # for index, value in enumerate(dummy2):
    #     if counter >= 3:
    #         break
    #     else:
    #         match = [x.lower() for x in value]
    #         if company.lower() in blacklist or company.lower() in prev_sent or match[4] in old:
    #             pass
    #         else:
    #             if company.lower() in match:
    #                 if company.lower() not in temporary:
    #                     temporary.append(company.lower())
    #                     sent.append([company, timestamp])
    #                 while m < 3:
    #                     output.append(" ")
    #                     m += 1
    #                 temp.append(dummy2[index])
    #                 if trty.lower() in match:
    #                     temp2.append(dummy2[index])
    #                     if city.lower() in match:
    #                         output.append(dummy[dummy_row] + dummy2[index])
    #                         todays.append([dummy2[index][4], timestamp])
    #                         counter += 1
    #             else:
    #                 not_found.append(dummy[dummy_row])
    #         for zz in range(0, 3 - counter):
    #             if counter >= 3:
    #                 break
    #             try:
    #                 if (dummy[dummy_row] + temp2[zz]) not in output:
    #                     output.append(dummy[dummy_row] + temp2[zz])
    #                     todays.append([temp2[zz][4], timestamp])
    #                     counter += 1
    #             except:
    #                 try:
    #                     if (dummy[dummy_row] + temp[zz]) not in output:
    #                         output.append(dummy[dummy_row] + temp[zz])
    #                         todays.append([temp[zz][4], timestamp])
    #                         counter += 1
    #                 except:
    #                     pass
    # ##############################################################################################

    # Approach 2
    # ##############################################################################################
    for index, value in enumerate(dummy2):
        if counter >= 3:
            break
        else:
            match = [x.lower() for x in value]
            if company.lower() in blacklist or match[4] in old:
                pass
            else:
                if company.lower() in match:
                    if company not in prev_sent and company not in sent:
                        sent.append([company, timestamp])
                    while m < 3:
                        output.append(" ")
                        m += 1
                    if trty.lower() in match and city.lower() in match:
                        todays.append([dummy2[index][4], timestamp])
                        temp.insert(0, dummy[dummy_row] + value)
                        counter += 1
                    elif trty.lower() in match:
                        todays.append([dummy2[index][4], timestamp])
                        temp.insert(3, dummy[dummy_row] + value)
                    else:
                        todays.append([dummy2[index][4], timestamp])
                        temp.insert(10, dummy[dummy_row] + value)
                else:
                    if dummy[dummy_row] not in not_found and company not in prev_sent:
                        not_found.append(dummy[dummy_row])

    top_data = temp[:3]
    for row33 in top_data:
        output.append(row33)


for row in states:
    state.append(row.split(','))
abbr = Convert(state)


def main():
    for ids, val in enumerate(dummy):
        company_name = val[1]
        dummy_location = val[2].split(',')
        location = dummy_location[0]
        try:
            if len(dummy_location[1]) > 3:
                trty = abbr[dummy_location[1].strip(' ')]
            else:
                trty = ""
        except:
            trty = ""
        print("Looking for", company_name, location, trty)
        lookup(dummy_row=ids, company=company_name, city=location, trty=trty)
    print("Saving to different files")
    print("Saving collected data")
    print(output)
    with open("Final.csv", "w", encoding='UTF8', newline='') as r:
        writer = csv.writer(r)
        writer.writerows(output)
    print("updating emails")
    with open("data/processed.csv", "w", encoding='UTF8', newline='') as p:
        writer2 = csv.writer(p)
        writer2.writerows(todays)
    print("updating sent data")
    with open(freq, "w", encoding='UTF8', newline='') as o:
        writer3 = csv.writer(o)
        writer3.writerows(sent)
    print("Saving Not found data")
    with open("not_found.csv", "w", encoding='UTF8', newline='') as n:
        writer4 = csv.writer(n)
        writer4.writerows(not_found)


main()
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in " + str(execution_time))
