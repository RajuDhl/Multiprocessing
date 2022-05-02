# import csv
# from operator import itemgetter
#
# header = ['Position', 'Company Name', 'Location', 'Remote']
#
# f = open("QA staffing2.txt", 'r', encoding='utf-8')
# total = []
# newline = []
#
# for line in f:
#     if line != '\n':
#         line = line.strip('\n')
#         newline.append(line)
#     else:
#         total.append(newline)
#         newline = []
#
# total.pop(0)
# try:
#     total.sort(key=itemgetter(1))
# except:
#     pass
# print("total", total)
#
# with open("Final2.csv", "w", encoding='UTF8', newline='') as r:
#     writer = csv.writer(r)
#     writer.writerow(header)
#     writer.writerows(total)
# def split(word):
#     z = word.replace("  ", "'")
#     return [z]


x = ["Hello  World,i am awesome"]
x.insert(5, "oh really??")
print(x)
x.insert(1, "hahaha")
print(x)
x.insert(10, "oh yes??")
print(x)
x.insert(3, "works")
print(x)
# if "  " in x:
#     y = x.replace("  ", '\n')
#     print(y)
#     print(x)
#     for word in y:
#         print(word)
