import json
import csv
from tkinter.filedialog import askopenfilename
#import unicodecsv as csv

name_j = askopenfilename(initialdir="../json_to_csv/Data/Input",
                            filetypes=(("Json File", "*.json"), ("All Files", "*.*")),
                            title="Choose a file.")

with open(name_j,'r',encoding='utf8') as data_file:
    data = json.loads(data_file.read())


with open('../json_to_csv/Data/Output/Output.csv', 'w',encoding='utf8') as csv_file:
    writer = csv.writer(csv_file)

    #writer.writerow(['doi', 'is_oa', 'title', 'publisher','z_authors','journal_name'])
    writer.writerow(data[0].keys())

    for row in data:
        #doi = row['doi']
        #oa = row['is_oa']
        #name = row['title']
        #pub = row['publisher']
        #author = row['z_authors']
        #jName = row['journal_name']

        #row = [doi, oa, name, pub, author, jName]
        writer.writerow(row.values())
