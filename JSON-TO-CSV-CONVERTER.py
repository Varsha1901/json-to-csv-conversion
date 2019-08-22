from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import time
import json
import csv
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk

## creating tkinter window
root = Tk()
root.geometry('600x400+40+40')
root.resizable(0,0)
root.title('Json to CSV Converter')

# This will create a LabelFrame_Validate 
label_validate = LabelFrame(root, text = 'Step 1: Validate') 
label_validate.grid(row=1, column=0, padx=30, pady=10)

# This will create a LabelFrame 
label_format = LabelFrame(root, text = 'Step 2: Format') 
label_format.grid(row=2, column=0, padx=30, pady=10)

# This will create a LabelFrame 
label_convert = LabelFrame(root, text = 'Step 3: Convert') 
label_convert.grid(row=3, column=0, padx=30, pady=10)

##About function
def About():
    master = tk.Tk()
    about_us = "created and designed by Varsha, Arpitha"
    msg = tk.Message(master, text = about_us)
    msg.grid()

##Function for Prgress bar
def run():
    progressBar['maximum'] = 120
    for i in range(120):
    ##time.sleep(0.01)
        progressBar["value"] = i
        progressBar.update()
        progressBar["value"] = 0

def Load():
    global progressBar1
    progressBar1['maximum'] = 120
    for i in range(120):
        progressBar1["value"] = i
        progressBar1.update()
        progressBar1["value"] = 0


##Function to validate/correct the json file
def Validator():
    MsgBox = messagebox.askquestion('Information','Do you want to validate the json file before converting?',icon = 'warning')
    if MsgBox == 'yes':
        chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab('https://jsonformatter.org/')
    else:
        messagebox.showinfo('Information','You can format the json by adding "[" at starting and add "]" at the end, and each json line will end with a "," except the last line. Sort the file once before adding the characters')
        messagebox.showinfo('Information','Kindly save the corrected json file in Input folder')
 
##Function which Splits the JSON file
def JsonFormat():
    new_path = '../json_to_csv/Data/Input'
    name = askopenfilename(initialdir="../json_to_csv/Data/JSON_File",
                           filetypes=(("Json File", "*.json"), ("All Files", "*.*")),
                           title="Choose a file."
                           )
    json_string = None
    
    try:
        with open(name, 'r', encoding='utf8') as f:
            json_string = f.read()
            parsed_json = json.loads(json_string)
            formatted_json = json.dumps(parsed_json, indent = 4,sort_keys=True)
            with open("../json_to_csv/Data/Input/JSON_Validated.json","w", encoding='utf8') as f:
                f.write(formatted_json)
                run()
            messagebox.showinfo("Information","JSON file is formatted and ready for conversion")
    except Exception:
        messagebox.showinfo("Error Message", 'File not selected')
        pass
        
##Function Converts JSON to CSV
def CSVFile():
    name_j = askopenfilename(initialdir="../json_to_csv/Data/Input",
                            filetypes=(("Json File", "*.json"), ("All Files", "*.*")),
                            title="Choose a file.")
    try:
        with open(name_j,'r',encoding='utf8') as data_file:
            data = json.loads(data_file.read())

        with open("../json_to_csv/Data/Output/output.csv", 'w',encoding='utf8', newline='') as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(['doi', 'is_oa', 'title', 'publisher','z_authors','journal_name'])
            for row in data:
                doi = row['doi']
                oa = row['is_oa']
                name = row['title']
                pub = row['publisher']
                author = row['z_authors']
                jName = row['journal_name']

                row = [doi, oa, name, pub, author, jName]
                writer.writerow(row)
                Load()
        messagebox.showinfo("Information","JSON is converted to CSV")
        
    except Exception:
        messagebox.showinfo("Error Message", 'File not selected')
        pass

## Creating Menubar
menubar = Menu(root)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Exit', menu=file)
##file.add_command(label='Browse', command=JsonFile)
file.add_command(label='Exit', command=root.destroy)

browsebutton = Button(label_validate, text='Validate your JSON', command=Validator)
browsebutton.grid(row=1, column=0, padx=20, pady=30)

browsebutton = Button(label_format, text='Format the JSON', command=JsonFormat)
browsebutton.grid(row=2, column=0, padx=20, pady=30)

browsebutton = Button(label_convert, text='CSV Converter', command=CSVFile)
browsebutton.grid(row=3, column=0, padx=20, pady=30)

progressBar = ttk.Progressbar(label_format, orient="horizontal", length=280,mode="determinate")
progressBar.grid(row=2,column=1, padx=20, pady=30)

progressBar1 = ttk.Progressbar(label_convert, orient="horizontal", length=280,mode="determinate")
progressBar1.grid(row=3,column=1, padx=20, pady=30)

## Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='About Us', command=About)

## display Menu
root.config(menu=menubar)
mainloop()

