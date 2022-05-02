import csv
import time
from operator import itemgetter
import re

arg = re.compile(r'([\.0-9]+)$')
# test = 'Akraya Inc.3.6'


def findFloat(string):
    fl = arg.search(string)
    try:
        new = float(fl.group(1))
    except:
        old = str(fl.group(1))
        new = old[1:len(old)]
    return fl and float(new)


# print(findFloat(test))
# time.sleep(5)
# test2 = test.strip(str(findFloat(test)))
# print("split string ===>", test2)
reply = input("L = Linkedin, D = Dice")

# reply = 'X'
header = ['Position', 'Company Name', 'Location', 'Remote']

f = open("data/people/BA all US 1 Apr.txt", 'r+', encoding='utf-8')
lines = f.readlines()
total = []
newline = []
if reply == 'L' or reply == 'l':
    for line in lines:
        line = line.strip('\n')
        # print(line.strip('\n'))
        if 'hide job' in line.lower():
            pass
        else:
            newline.append(line)
            if 'logo' in line.lower():
                total.append(newline)
                newline = []


elif reply == 'D' or reply == 'd':
    # for x in lines:
    #     if "  " in x:
    #         x.replace("  ", '\n')
    for i in range(0, len(lines)):
        line = lines[i].strip('\n')
        if "  " in line:
            y = line.split("  ")
            for z in y:
                newline.append(z)
        else:
            newline.append(line)
        try:
            if 'logo' in lines[i + 3].lower():
                total.append(newline)
                newline = []
        except:
            pass

elif reply == 'X':
    for x in lines:
        if x != '\n':
            y = x.split()
            if 'new' in y:
                pass
            else:
                if x.isalpha():
                    pass
                else:
                    try:
                        x = x.replace(str(findFloat(x)), "")
                    except:
                        pass
                x = x.strip('\n')
                newline.append(x)
        else:
            if len(newline) > 3:
                total.append(newline)
            newline = []

# print("total", total)
total.pop(0)
try:
    total.sort(key=itemgetter(1))
except:
    print("not Sorted")
# print("new total", total)
# print("data", data)
with open("data/people/BAcsvzzz.csv", "w", encoding='UTF8', newline='') as r:
    writer = csv.writer(r)
    writer.writerow(header)
    for row in total:
        writer.writerow(row)
