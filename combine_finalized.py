import csv


def open_files(array2):
    for k, v in array.items():
        temporary = []
        with open(v, 'r', encoding='utf8') as z:
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


jobs = 'data/people/1April text2csv (1).csv'
people = 'data/people/apollo-contacts-export (51).csv'

array = {'jobs': jobs, 'people': people}
files = open_files(array)

jobs = files['jobs']
people = files['people']
# print(people)
final = []
processed = []
for i, v in enumerate(jobs):
    start = True
    if v[1].lower() not in processed:
        processed.append(v[1].lower())
        for index, data in enumerate(people):
            # print(v, data)
            if v[3].lower() == data[7].lower():
                if start:
                    for z in range(1, 4):
                        final.append(" ")
                        start = False
                final.append(v + data)

        #     break
print(final)
print(len(final))
with open('data/people/31 March BA final data.csv', "w", encoding='UTF8', newline='') as r:
    writer = csv.writer(r)
    writer.writerows(final)
