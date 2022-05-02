# # import requests
# #
# import csv
# import os
#
# # pdf = open('data/pdf/L2M Game Links_Archive pdfs.csv', "r+").read().split('\n')
# # #
# # data = []
# # for row in pdf:
# #     fname = row.split('/')[-1]
# #     data.append([row, fname])
# #
# # with open("data/pdf/aa.csv", "w", encoding='UTF8', newline='') as r:
# #     writer = csv.writer(r)
# #     writer.writerows(data)
# # print(data)
# #
# # for d in data:
# #     r = requests.get(d, allow_redirects=True, stream=True)
# #
# #     print(r.headers.get('content-disposition'))
#
# # import urllib.request
# #
# # urllib.urlretrieve("https://ak-static.cms.nba.com/wp-content/uploads/sites/4/2015/03/L2M-ATL-SAC-3-16-15.pdf", "file.gz")
#
# # import requests
# # # r = requests.get('https://ak-static.cms.nba.com/wp-content/uploads/sites/4/2015/03/L2M-ATL-SAC-3-16-15.pdf', stream=True)
# # # print(r)
# #
# # # file_url = "https://ak-static.cms.nba.com/wp-content/uploads/sites/4/2015/03/L2M-ATL-SAC-3-16-15.pdf"
# # for d in data:
# #     fname = d.split('/')[-1]
# #
# #     r = requests.get(d, stream=True)
# #
# #     with open(f"data/pdf/{fname}", "wb") as pdf:
# #         for chunk in r.iter_content(chunk_size=1024):
# #
# #             # writing one chunk at a time to pdf file
# #             if chunk:
# #                 pdf.write(chunk)
#
# from PyPDF2 import PdfFileMerger
#
# merger = PdfFileMerger()
# d = []
# for file in os.listdir('data/pdf/pdfs'):
#     merger.append(file)
#     d.append(file)
# print(d)
#
#
#
#
# # for pdf in d:
# #     merger.append(pdf)
# #
# # merger.write("result.pdf")
# # merger.close()

import os
from PyPDF2 import PdfFileMerger

# x = [a for a in os.listdir() if a.endswith(".pdf")]
#
# merger = PdfFileMerger()
#
# for pdf in x:
#     merger.append(open(pdf, 'rb'))
#
# with open("result.pdf", "wb") as fout:
#     merger.write(fout)
z = 1


def test():
    temp = ['a', 'b']
    bool = False
    return {temp, bool}



data = test()
print(data)
