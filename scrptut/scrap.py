from bs4 import BeautifulSoup
import requests
import csv
import json
from tkinter import *
from tkinter import messagebox

window = Tk()
StringVar(window)

fvar, opvar, lvar = StringVar(), StringVar(), StringVar()

def click1():

    with open('gsoc_samplel.csv', 'a') as f:
        fieldnames=['Name', 'Organization', 'Project']
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()

    url=" https://summerofcode.withgoogle.com/api/program/current/project/?page_size=100"
    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')
    json_file = json.loads(soup.text)
    data = json_file['results']
    i=0
    gsoc_store=[]
    for entry in data:
        if i==100:
            break
        else:
            name = entry['student']['display_name']
            org = entry['organization']['name']
            title_pro = entry['title']
            tup = tuple((name, org, title_pro))
            gsoc_store.append(tup) #stores a tuple containing info inside a list
            i=i+1
    #print(len(gsoc_store))
    for output in gsoc_store:
        #print(output)
        with open('gsoc_samplel.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(output)

    messagebox.showinfo(title="Message",message="Scrapped")        


window.title("Scrapper")
window.geometry("400x400")
label = Label(window, text="Sample_Scrapper", relief="solid", font=("arial", 16, 'bold')).pack(fill=BOTH, padx=2, pady=2)
fname = Label(window, text="FirstName: ", font=("arial", 10, 'bold'))
fname.place(x=40,y=80)
lname = Label(window, text="LastName: ", font=("arial", 10, 'bold'))
lname.place(x=40,y=120)
fn = Entry(window, textvar=fvar)
fn.place(x=120, y=80)
#fn.insert(0, " Firstname ")
ln = Entry(window, textvar=lvar)
ln.place(x=120,y=120)
#ln.insert(0, " Lasttname ")
op = Label(window, text="Select Site: ", font=('arial', 10,'bold'))
op.place(x=40,y=200)
options = ['GSOC']
list = OptionMenu(window, opvar,*options)
opvar.set("Sites")
list.config(width = 16)
list.place(x=120, y=200)
button = Button(window, text="Submit", fg="black", bg="white", font=('arial', 10,'bold'),command=click1)
button.place(x=150, y=300)

window.mainloop()

