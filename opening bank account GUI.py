from tkinter import*
root=Tk(className="sbi account opening")

root.configure(bg="lightblue")


lbl=Label(root,text="STATE BANK OF INDIA")
lbl.grid(row=0,column=2)

lbl=Label(root,text="Create your account")
lbl.grid(row=1,column=1)

lbl=Label(root,text="First Name")
lbl.grid(row=2,column=1)

ent1=Entry(root,bd=5)
ent1.grid(row=2,column=2)

lbl=Label(root,text="Last name")
lbl.grid(row=3,column=1)

ent2=Entry(root,bd=5)
ent2.grid(row=3,column=2)

lbl=Label(root,text="Date of Birth")
lbl.grid(row=4,column=1)

ent3=Entry(root,bd=5)
ent3.grid(row=4,column=2)

lbl=Label(root,text="Proof")
lbl.grid(row=5,column=1)

rd1=Radiobutton(root,text="aadhar card",value=1)
rd1.grid(row=5,column=2)

rd2=Radiobutton(root,text="Passport",value=2)
rd2.grid(row=5,column=3)

lbl=Label(root,text="PAN card Number")
lbl.grid(row=6,column=1)

ent4=Entry(root,bd=5)
ent4.grid(row=6,column=2)

cb1=Checkbutton(root,text="Savings Account",onvalue=1)
cb1.grid(row=7,column=2)

cb1=Checkbutton(root,text="Fixed deposit",onvalue=1)
cb1.grid(row=7,column=3)

lbl=Label(root,text="Gmail")
lbl.grid(row=8,column=1)
ent5=Entry(root,bd=5)
ent5.grid(row=8,column=2)
lbl=Label(root,text="Mobile no")
lbl.grid(row=9,column=1)
ent6=Entry(root,bd=5)
ent6.grid(row=9,column=2)

lbl=Label(root,text="set password")
lbl.grid(row=10,column=1)
ent7=Entry(root,bd=5)
ent7.grid(row=10,column=2)

def submit():
    Firstname=str(ent1.get())
    Lastname=str(ent2.get())
    DateofBirth=str(ent3.get())
    PANcardnumber=str(ent4.get())
    Gmail=str(ent5.get())
    Mobileno=str(ent6.get())
    Setpassword=str(ent7.get())
    file=open("openingbankaccountdata.txt","a")
    file.write("\nFirst name:")
    file.write(Firstname)
    file.write("\nLast name:")
    file.write(Lastname)
    file.write("\nData of Birth:")
    file.write(DateofBirth)
    file.write("\nPAN card number:")
    file.write(PANcardnumber)
    file.write("\nGmail:")
    file.write(Gmail)
    file.write("\nMobile number:")
    file.write(Mobileno)
    file.write("\nPassword:")
    file.write(Setpassword)
    file.write("========================================")
    messagebox.showinfo("note","submitted successfully within 5 working days you will get a mail")

btn=Button(root,text="submit",command=submit)
btn.grid(row=11,column=2)

root.mainloop()



