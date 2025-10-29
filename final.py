#importing modules
import tkinter
from tkinter import *
import tkinter.font as f
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from datetime import *

#Connecting to MySQL
mydb = {'user': 'root', 'password': 'hasmita@25', 'host': 'localhost',
        'database': 'fitmod', 'port': 3306,'raise_on_warnings': True}
global mycon
mycon = mysql.connector.connect(**mydb)
global mycursor
mycursor = mycon.cursor()

def connectionMYSQL():
    mydb = {'user': 'root', 'password': 'hasmita@25', 'host': 'localhost', 'database': 'fitmod', 'port': 3306,
            'raise_on_warnings': True}
    global mycon
    mycon = mysql.connector.connect(**mydb)
    global mycursor
    mycursor = mycon.cursor()

#Introduction Page
def main(root=None):
    if root != None:
        root.destroy()
    intro = Tk()
    intro.title("FitMod")
    intro.geometry("1920x1080")
    bg = PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\Intro_FitMod.png")
    label = Label(intro, image=bg)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    login_b = Button(intro, text="LOGIN", background="#77CC97", command=lambda: (loginwindow(intro)))
    loginfont = f.Font(family="Oswald", size=20)
    login_b['font'] = loginfont
    login_b.place(x=710, y=396)
    intro.mainloop()

#Login Window
def loginwindow(root):
    root.destroy()
    root = Tk()
    root.title("FitMod-Login")
    root.geometry("1920x1080")
    bg = PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\Login_new.png")
    label = Label(root, image=bg)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Password Check Function
    def CheckPswd():
        uname = nameEntry.get()
        pswd = passwordEntry.get()
        if uname == "admin" and pswd == "admin@123":
            dashboard(root)
        else:
            messagebox.showwarning("Warning", "Entered Username or Password is Incorrect")
    nameEntry = Entry(root, font=('Poppins', 15))
    nameEntry.place(x=780, y=375, width=150, height=35)

    passwordEntry = Entry(root, font=('Poppins', 15))
    passwordEntry.place(x=780, y=435, width=150, height=35)
    cont = Button(root, height=1, width=10, text="CONTINUE", background="#f2c2a6", foreground="#000000",
                  command=CheckPswd)
    contfont = f.Font(family="Poppins", size=19)
    cont['font'] = contfont
    cont.place(x=710, y=520)
    home_b = Button(root, text="HOME", background="#d4e4ed", height=1, width=10, foreground="#000000",command=lambda: main(root))
    homefont = f.Font(family="Poppins", size=15)
    home_b['font'] = homefont
    home_b.place(x=1300, y=700)
    root.mainloop()

#Dashboard Page(after login)
def dashboard(r):
    r.destroy()
    r = Tk()
    r.title("FitMod-Home Page")
    r.geometry("1920x1080")
    home = PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\DashboardTrial.png")
    label = Label(r, image=home)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    upload = Button(r, text="UPLOAD HEALTH REPORT", background="#f3b4a3",command=lambda:(uploadhealth(r)))
    uploadfont = f.Font(family="Poppins", size=13)
    upload['font'] = uploadfont
    upload.place(x=215, y=460)
    view = Button(r, text="HEALTH HISTORY", background="#f3b4a3",command=lambda:(HealthHistory(r)))
    viewfont = f.Font(family="Poppins", size=13)
    view['font'] = viewfont
    view.place(x=700, y=460)
    doc = Button(r, text="CONTACT DOCTORS", background="#f3b4a3", command=lambda: (consult(r)))
    docfont = f.Font(family="Poppins", size=13)
    doc['font'] = docfont
    doc.place(x=1130, y=460)
    l = Button(r, text="LOG OUT", background="#b4e1c3", command=lambda: (loginwindow(r)))
    lfont = f.Font(family="Poppins", size=13)
    l['font'] = lfont
    l.place(x=1330, y=730)
    r.mainloop()


#Doctor Categories Page
def consult(d):
    d.destroy()
    d=Tk()
    d.title("Contact Doctors")
    d.geometry("1920x1080")
    dpg=PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\contactdoc.png")
    label=Label(d,image=dpg)
    label.place(x=0,y=0,relwidth=1, relheight=1)
    dp=PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\baby.png")
    b1=Button(d,image=dp,command=lambda:(ped(d)))
    b1font=f.Font(family="Oswald")
    b1['font']=b1font
    b1.place(x=180,y=200)
    dp1=PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\heart.png")
    b2=Button(d,image=dp1,command=lambda:(card(d)))
    b2font=f.Font(family="Oswald")
    b2['font']=b2font
    b2.place(x=500,y=200)
    dp2=PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\endo.png")
    b3=Button(d,image=dp2,command=lambda:(endo(d)))
    b3font=f.Font(family="Oswald")
    b3['font']=b3font
    b3.place(x=180,y=500)
    dp3=PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\uro.png")
    b4=Button(d,image=dp3,command=lambda:(uro(d)))
    b4font=f.Font(family="Oswald")
    b4['font']=b4font
    b4.place(x=500,y=500)
    dp4=PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\diab.png")
    b5=Button(d,image=dp4,command=lambda:(dia(d)))
    b5font=f.Font(family="Oswald")
    b5['font']=b5font
    b5.place(x=800,y=500)
    dp5=PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\opth.png")
    b6=Button(d,image=dp5,command=lambda:(oph(d)))
    b6font=f.Font(family="Oswald")
    b6['font']=b6font
    b6.place(x=800,y=200)
    dp6=PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\gastro.png")
    b7=Button(d,image=dp6,command=lambda:(gastro(d)))
    b7font=f.Font(family="Oswald")
    b7['font']=b7font
    b7.place(x=1100,y=200)
    dp7=PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\haemo.png")
    b8=Button(d,image=dp7,command=lambda:(hema(d)))
    b8font=f.Font(family="Oswald")
    b8['font']=b8font
    b8.place(x=1100,y=500)
    back=Button(d,text="Back",background="#C2DFFF",command=lambda:dashboard(d))
    backfont=f.Font(family="Oswald",size=18)
    back['font']=backfont
    back.place(x=1380,y=700)
    d.mainloop()

#Hematologist Page
def hema(fo):
    fo.destroy()
    fo = Tk()
    fo.title("Contact your Hematologists")
    fo.geometry("1920x1080")
    bgc = PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\theme (1).png")
    label = Label(fo, image=bgc)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    s = Label(fo, text="Hematologist", foreground="#4B0150",bg="#e6e5e1")
    sfont = f.Font(family="poppins", size=40)
    s['font'] = sfont
    s.pack()
    l7 = Label(fo, text="Dr.Hari Teja\tDM HEMATOLOGY\tIcon  Hospital\t9554466777", font="arial")
    l7.place(x=400, y=100)
    l7 = Label(fo, text="Dr.Vishnu Sampath\tDM HEMATOLOGY\tMedwell Hospital\t8444700600", font="arial")
    l7.place(x=400, y=150)
    l7 = Label(fo, text="Dr.Sujay Prakash\tDM HEMATOLOGY\tHasini Hospital\t6554488990", font="arial")
    l7.place(x=400, y=200)
    l7 = Label(fo, text="Dr.Deerendra J\tDM HEMATOLOGY\tCare Hospital\t9224455111", font="arial")
    l7.place(x=400, y=250)
    l7 = Label(fo, text="Dr.Subhashini K\tDM HEMATOLOGY\tSun Shine Hospital\t8888555444", font="arial")
    l7.place(x=400, y=300)
    l7 = Label(fo, text="Dr.Rohith V\tDM HEMATOLOGY\tLife Hospital\t6444333300", font="arial")
    l7.place(x=400, y=350)
    l7 = Label(fo, text="Dr.Katyayini Roy\tDM HEMATOLOGY\tAyushman Hospital\t9885522617", font="arial")
    l7.place(x=400, y=400)
    l7 = Label(fo, text="Dr.Swathi Sharma\tDM HEMATOLOGY\tSiddhardha Hospital\t8765432189", font="arial")
    l7.place(x=400, y=450)
    l7 = Label(fo, text="Dr.Sai Manasa H\tDM HEMATOLOGY\tKauvery  Hospital\t9515657339", font="arial")
    l7.place(x=400, y=500)
    l7 = Label(fo, text="Dr.Trishal Kumar\tDM HEMATOLOGY\tTrust Hospital\t9246610114", font="arial")
    l7.place(x=400, y=550)
    l7 = Label(fo, text="Dr.Prashanthi\tDM HEMATOLOGY\tHope Hospital\t9705040808", font="arial")
    l7.place(x=400, y=600)
    l7 = Label(fo, text="Dr.Hema Dasari\tDM HEMATOLOGY\tRainbow Hospital\t7766665555", font="arial")
    l7.place(x=400, y=650)
    l7 = Label(fo, text="Dr.Lovaraju T\tDM HEMATOLOGY\tApollo Hospital\t9999888800", font="arial")
    l7.place(x=400, y=700)
    back = Button(fo, text="Back", background="#C2DFFF", command=lambda: consult(fo))
    backfont = f.Font(family="Oswald", size=18)
    back['font'] = backfont
    back.place(x=1380, y=700)
    fo.mainloop()

#Gastroentrologist Page
def gastro(t):
    t.destroy()
    t = Tk()
    t.title("Contact your  Gastroenterologist")
    t.geometry("1920x1080")
    bgc = PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\theme (1).png")
    label = Label(t, image=bgc)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    s = Label(t, text=" Gastroenterologist", foreground="#4B0150",bg="#e6e5e1")
    sfont = f.Font(family="Oswald", size=55)
    s['font'] = sfont
    l7 = Label(t, text="Dr.Sushma Kiron\tMBBS\t\tApollo Hospital\t9887700660", font="arial")
    l7.place(x=400, y=100)
    l7 = Label(t, text="Dr.Dhanasree B\tMBBS\t\tCSP Hospital\t8552700600", font="arial")
    l7.place(x=400, y=150)
    l7 = Label(t, text="Dr.Harini\t\tMBBS\t\tHariharini Hospital\t9240907061", font="arial")
    l7.place(x=400, y=200)
    l7 = Label(t, text="Dr.Deepika L\tMBBS\t\tAnjali Clinic\t8000855072", font="arial")
    l7.place(x=400, y=250)
    l7 = Label(t, text="Dr.Subhashini K\tMBBS\t\tSudha Clinic\t9848143568", font="arial")
    l7.place(x=400, y=300)
    l7 = Label(t, text="Dr.Usha Rani\tMBBS\t\tIcon  Hospital\t6579988112", font="arial")
    l7.place(x=400, y=350)
    l7 = Label(t, text="Dr.S Akash\tMBBS\t\tMedwell Hospital\t9885522617", font="arial")
    l7.place(x=400, y=400)
    l7 = Label(t, text="Dr.Kiranmayi I\tMBBS\t\tSiddhardha Hospital\t8765432189", font="arial")
    l7.place(x=400, y=450)
    l7 = Label(t, text="Dr.Akhil Akkineni\tMBBS\t\tLaya clinic\t9515657339", font="arial")
    l7.place(x=400, y=500)
    l7 = Label(t, text="Dr.Kajal A\tMBBS\t\tLasya Hospital\t6555543321", font="arial")
    l7.place(x=400, y=550)
    l7 = Label(t, text="Dr.U Padmavathi\tMBBS\t\tHope Hospital\t8224335446", font="arial")
    l7.place(x=400, y=600)
    l7 = Label(t, text="Dr.Gariki Mahesh\tMBBS\t\tCare Hospital\t9515657339", font="arial")
    l7.place(x=400, y=650)
    l7 = Label(t, text="Dr.Ajith kumar Roy\tMBBS\t\tAyushman Hospital\t8900453233", font="arial")
    l7.place(x=400, y=700)
    back = Button(t, text="Back", background="#C2DFFF", command=lambda: consult(t))
    backfont = f.Font(family="Oswald", size=18)
    back['font'] = backfont
    back.place(x=1380, y=700)
    s.pack()
    t.mainloop()

#Diabetologist Page
def dia(g):
    g.destroy()
    g = Tk()
    g.title("Contact your Diabetologist")
    g.geometry("1920x1080")
    bgc = PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\theme (1).png")
    label = Label(g, image=bgc)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    s = Label(g, text="Diabetologist", foreground="#4B0150",bg="#e6e5e1")
    sfont = f.Font(family="poppins", size=40)
    s['font'] = sfont
    l3 = Label(g, text="Dr.Sandhya Rani\tMBBS,MD\tRainbow Hospital\t\t8989878689        ", font="arial")
    l3.place(x=400, y=100)
    l3 = Label(g, text="Dr.Geeth Monappa\tMBBS,MD\tCare Hospitals\t\t9248918888", font="arial")
    l3.place(x=400, y=150)
    l3 = Label(g, text="Dr.Ranjitha G Babu\tMBBS,MD\tSeven Hills Hospitals\t9708605701", font="arial")
    l3.place(x=400, y=200)
    l3 = Label(g, text="Dr.Charitha K N\tMBBS,MD\tColumbia Asia\t\t6543890715", font="arial")
    l3.place(x=400, y=250)
    l3 = Label(g, text="Dr.Bharathi Raj\tMBBS,MD\tApollo Hospitals\t\t9848198525", font="arial")
    l3.place(x=400, y=300)
    l3 = Label(g, text="Dr.Hema Divakar\tMBBS,MD\tJaslok Hospital\t\t7588758899", font="arial")
    l3.place(x=400, y=350)
    l3 = Label(g, text="Dr.Swetha M P\tMBBS,MD\tSafe Hospital\t\t9080706050", font="arial")
    l3.place(x=400, y=400)
    l3 = Label(g, text="Dr.Sobha Rani\tMBBS,MD\tVictoria Hospital\t\t8978787868", font="arial")
    l3.place(x=400, y=450)
    l3 = Label(g, text="Dr.Regina  \tMBBS,MD\tLakshmi Narayana Clinic\t9868556682", font="arial")
    l3.place(x=400, y=500)
    l3 = Label(g, text="Dr.Bhawana Mishra\tMBBS,MD\tSudha Hospitals\t\t8160985046", font="arial")
    l3.place(x=400, y=550)
    l3 = Label(g, text="Dr.Rishitha D\tMBBS,MD\tAsian Hospitals\t\t6760060080", font="arial")
    l3.place(x=400, y=600)
    l3 = Label(g, text="Dr.Hema Varshini\tMBBS,MD\tTrust Hospitals\t\t9008007001", font="arial")
    l3.place(x=400, y=650)
    l3 = Label(g, text="Dr.Jaya V \tMBBS,MD\tHope Hospital\t\t9566766988", font="arial")
    l3.place(x=400, y=700)
    back = Button(g, text="Back", background="#C2DFFF", command=lambda: consult(g))
    backfont = f.Font(family="Oswald", size=18)
    back['font'] = backfont
    back.place(x=1380, y=700)
    s.pack()
    g.mainloop()

#Ophthalmologist Page
def oph(o):
    o.destroy()
    o = Tk()
    o.title("Contact your Ophthalmologist")
    o.geometry("1920x1080")
    bgc = PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\theme (1).png")
    label = Label(o, image=bgc)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    s = Label(o, text="Ophthalmologist", foreground="#4B0150",bg="#e6e5e1")
    sfont = f.Font(family="poppins", size=40)
    s['font'] = sfont
    l5 = Label(o, text="Dr.Shanmukh J\tMS OPTHAMOLOGY\tcloud 9 Hospital\t9515657339", font="arial")
    l5.place(x=400, y=100)
    l5 = Label(o, text="Dr.Priyanka Singh\tMS OPTHAMOLOGY\tspring leaf Hospital\t8978773399", font="arial")
    l5.place(x=400, y=150)
    l5 = Label(o, text="Dr.Sivay H\tMS OPTHAMOLOGY\tLV Prasad Hospital\t8545653456 ", font="arial")
    l5.place(x=400, y=200)
    l5 = Label(o, text="Dr.Anika SS\tMS OPTHAMOLOGY\tAnju Hospital\t9898979665", font="arial")
    l5.place(x=400, y=250)
    l5 = Label(o, text="Dr.Rudhra A\tMS OPTHAMOLOGY\tNayana Hospital\t6758897780", font="arial")
    l5.place(x=400, y=300)
    l5 = Label(o, text="Dr.Samantha\tMS OPTHAMOLOGY\tKauvery  Hospital\t8786685583", font="arial")
    l5.place(x=400, y=350)
    l5 = Label(o, text="Dr.Arjun A\tMS OPTHAMOLOGY\tM M Hospital\t6435621134", font="arial")
    l5.place(x=400, y=400)
    l5 = Label(o, text="Dr.Srimukhi P\tMS OPTHAMOLOGY\tOmegha Hospital\t9098098700", font="arial")
    l5.place(x=400, y=450)
    l5 = Label(o, text="Dr.Vaishnavi I\tMS OPTHAMOLOGY\tSravani Hospital\t8765987501", font="arial")
    l5.place(x=400, y=500)
    l5 = Label(o, text="Dr.Bargav Kumar Y\tMS OPTHAMOLOGY\tAyushman Hospital\t6473908197", font="arial")
    l5.place(x=400, y=550)
    l5 = Label(o, text="Dr.Pavithra H M\tMS OPTHAMOLOGY\tBlossom Hospital\t9077665522", font="arial")
    l5.place(x=400, y=600)
    l5 = Label(o, text="Dr.Rohith D\tMS OPTHAMOLOGY\tSri Nitya Hospital\t9224225228", font="arial")
    l5.place(x=400, y=650)
    l5 = Label(o, text="Dr.Ayush Siddhanth\tMS OPTHAMOLOGY\tMathuru Hospital\t6543217891", font="arial")
    l5.place(x=400, y=700)
    back = Button(o, text="Back", background="#C2DFFF", command=lambda: consult(o))
    backfont = f.Font(family="Oswald", size=18)
    back['font'] = backfont
    back.place(x=1380, y=700)
    s.pack()
    o.mainloop()

#Urologist Page
def urologist(u):
    u.destroy()
    u = Tk()
    u.title("Contact your Urologist")
    u.geometry("1920x1080")
    bgc = PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\theme (1).png")
    label = Label(u, image=bgc)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    s = Label(u, text="Urologist", foreground="#4B0150",bg="#e6e5e1")
    sfont = f.Font(family="poppins", size=40)
    s['font'] = sfont
    l4 = Label(u, text="Dr.Ankith Subhash\tMS UROLOGY\tOmegha Hospital\t6301465558", font="arial")
    l4.place(x=400, y=100)
    l4 = Label(u, text="Dr.Asuthosh\tMS UROLOGY\tMeghana Hospital\t9848198505", font="arial")
    l4.place(x=400, y=150)
    l4 = Label(u, text="Dr.K Charan\tMS UROLOGY\tCare Hospital\t9785867008", font="arial")
    l4.place(x=400, y=200)
    l4 = Label(u, text="Dr.A Sushma\tMS UROLOGY\tApollo HospitalS\t8885375665", font="arial")
    l4.place(x=400, y=250)
    l4 = Label(u, text="Dr.Rajkumar P\tMS UROLOGY\tLasya Clinic\t8989787890", font="arial")
    l4.place(x=400, y=300)
    l4 = Label(u, text="Dr.Rakesh Bhatt\tMS UROLOGY\tSri Vishnu Hospital\t9897989798", font="arial")
    l4.place(x=400, y=350)
    l4 = Label(u, text="Dr.P Parvathi\tMS UROLOGY\tTrust Clinic\t9950403020", font="arial")
    l4.place(x=400, y=400)
    l4 = Label(u, text="Dr.Ankith Pandey\tMS UROLOGY\t7 Hills Hospital\t7878676785", font="arial")
    l4.place(x=400, y=450)
    l4 = Label(u, text="Dr.Rudhra I\tMS UROLOGY\tLasya Clinic\t7868586878", font="arial")
    l4.place(x=400, y=500)
    l4 = Label(u, text="Dr.Lahari J\tMS UROLOGY\tSagar Hospitals\t6754873002", font="arial")
    l4.place(x=400, y=550)
    l4 = Label(u, text="Dr.Trisha Sharma\tMS UROLOGY\tAmma Hospital\t7654903890", font="arial")
    l4.place(x=400, y=600)
    l4 = Label(u, text="Dr.sailesh P \tMS UROLOGY\tUdaya Clinic\t7868594955", font="arial")
    l4.place(x=400, y=650)
    l4 = Label(u, text="Dr.Padma Y\tMS UROLOGY\tAkash Hospitals\t6858068506", font="arial")
    l4.place(x=400, y=700)
    back = Button(u, text="Back", background="#C2DFFF", command=lambda: consult(u))
    backfont = f.Font(family="Oswald", size=18)
    back['font'] = backfont
    back.place(x=1380, y=700)
    s.pack()
    u.mainloop()

#Endocrinologist Page
def endo(i):
    i.destroy()
    i = Tk()
    i.title("Contact your Endocrinologist")
    i.geometry("1920x1080")
    bgc = PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\theme (1).png")
    label = Label(i, image=bgc)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    s = Label(i, text="Endocrinologist", foreground="#4B0150",bg="#e6e5e1")
    sfont = f.Font(family="poppins", size=40)
    s['font'] = sfont
    l6 = Label(i, text="Dr.Priya Prakash\t\tMD ENDOCRINOLOGY\tTrust Hospital\t9708906780", font="arial")
    l6.place(x=400, y=100)
    l6 = Label(i, text="Dr.Rashmika K\t\tMD ENDOCRINOLOGY\tAsian Hospital\t8900700600", font="arial")
    l6.place(x=400, y=150)
    l6 = Label(i, text="Dr.Siri Hanumanth\t\tMD ENDOCRINOLOGY\tCare Hospital\t6080907061", font="arial")
    l6.place(x=400, y=200)
    l6 = Label(i, text="Dr.Deepthi Sunaina\t\tMD ENDOCRINOLOGY\tDiacare Hospital\t8220855072", font="arial")
    l6.place(x=400, y=250)
    l6 = Label(i, text="Dr.Sruthi Royal Y\t\tMD ENDOCRINOLOGY\tSraddha Hospital\t9348143568", font="arial")
    l6.place(x=400, y=300)
    l6 = Label(i, text="Dr.Yogitha Rayapudi\tMD ENDOCRINOLOGY\tIcon  Hospital\t9876509873", font="arial")
    l6.place(x=400, y=350)
    l6 = Label(i, text="Dr.Asuthosh Sharma\tMD ENDOCRINOLOGY\tMedwell Hospital\t6131241617", font="arial")
    l6.place(x=400, y=400)
    l6 = Label(i, text="Dr.Annanya Pattjoshi\tMD ENDOCRINOLOGY\tChandra Hospital\t8765432189", font="arial")
    l6.place(x=400, y=450)
    l6 = Label(i, text="Dr.Tarun Prakash M\tMD ENDOCRINOLOGY\tApollo Hospital\t9515657339", font="arial")
    l6.place(x=400, y=500)
    l6 = Label(i, text="Dr.Praneetha L\t\tMD ENDOCRINOLOGY\tAyushman Hospital\t7865543321", font="arial")
    l6.place(x=400, y=550)
    l6 = Label(i, text="Dr.Padma Sree Harshitha\tMD ENDOCRINOLOGY\tKrishna Sai Hospital\t8224335446", font="arial")
    l6.place(x=400, y=600)
    l6 = Label(i, text="Dr.Padmavathi P\t\tMD ENDOCRINOLOGY\tOmegha Hospital\t9515657339", font="arial")
    l6.place(x=400, y=650)
    l6 = Label(i, text="Dr.R Venkat\t\tMD ENDOCRINOLOGY\tHope Hospital\t6009008005", font="arial")
    l6.place(x=400, y=700)
    back = Button(i, text="Back", background="#C2DFFF", command=lambda: consult(i))
    backfont = f.Font(family="Oswald", size=18)
    back['font'] = backfont
    back.place(x=1380, y=700)
    s.pack()
    i.mainloop()

#Cardiologist Page
def card(c):
    c.destroy()
    c = Tk()
    c.title("Contact your Cardiologist")
    c.geometry("1920x1080")
    bgc = PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\theme (1).png")
    label = Label(c, image=bgc)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    s = Label(c, text="Cardiologist", foreground="#4B0150",bg="#e6e5e1")
    sfont = f.Font(family="poppins", size=40)
    s['font'] = sfont
    l2 = Label(c, text="Dr.Jai Babu\tDM CARDIOLOGY\tCG Clinic\t\t8160985046", font="arial")
    l2.place(x=400, y=100)
    l2 = Label(c, text="Dr.Natraj Setty\tDM CARDIOLOGY\tSapphire Clinic\t8567846650", font="arial")
    l2.place(x=400, y=150)
    l2 = Label(c, text="Dr.Jayaranganath M DM CARDIOLOGY Apollo Hospitals 8985878684", font="arial")
    l2.place(x=400, y=200)
    l2 = Label(c, text="Dr.Prabhakar\tDM CARDIOLOGY\tCare  Hospitals\t9078965400", font="arial")
    l2.place(x=400, y=250)
    l2 = Label(c, text="Dr.Roopa R\tDM CARDIOLOGY\tHeart Care Clinic\t7848769087", font="arial")
    l2.place(x=400, y=300)
    l2 = Label(c, text="Dr.G Vivek\tDM CARDIOLOGY\tHarikaa Clinic\t8800669933", font="arial")
    l2.place(x=400, y=350)
    l2 = Label(c, text="Dr.Ashwin M\tDM CARDIOLOGY\tSky  Cooperation\t7876797608", font="arial")
    l2.place(x=400, y=400)
    l2 = Label(c, text="Dr.Abhijeet Vilas\tDM CARDIOLOGY\tApollo Hospitals\t6767575654", font="arial")
    l2.place(x=400, y=450)
    l2 = Label(c, text="Dr.KSS Bhat\tDM CARDIOLOGY\tManipal Hospital\t7848178609", font="arial")
    l2.place(x=400, y=500)
    l2 = Label(c, text="Dr.Basavaraj V\tDM CARDIOLOGY\tFortis Hospital\t9988008800", font="arial")
    l2.place(x=400, y=550)
    l2 = Label(c, text="Dr.V Trivikram\tDM CARDIOLOGY\tSunshine  Hospitals\t6699688043", font="arial")
    l2.place(x=400, y=600)
    l2 = Label(c, text="Dr.Srinivas P\tDM CARDIOLOGY\tAsian Hospitals\t8987868509", font="arial")
    l2.place(x=400, y=650)
    l2 = Label(c, text="Dr.Harsha M\tDM CARDIOLOGY\tAnju Heart Clinic\t8765456788", font="arial")
    l2.place(x=400, y=700)
    back = Button(c, text="Back", background="#C2DFFF", command=lambda: consult(c))
    backfont = f.Font(family="Oswald", size=18)
    back['font'] = backfont
    back.place(x=1380, y=700)
    s.pack()
    c.mainloop()

#PediatricianPage
def ped(p):
    p.destroy()
    p = Tk()
    p.title("Contact your Pediatrician")
    p.geometry("1920x1080")
    bgc = PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\theme (1).png")
    label = Label(p, image=bgc)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    s = Label(p, text="Pediatrician", foreground="#4B0150",bg="#e6e5e1")
    sfont = f.Font(family="poppins", size=40)
    s['font'] = sfont
    l1 = Label(p, text="Dr.Anjusha.V\tMBBS,MD\tRainbow Hospital\t9248918888", font="arial", anchor="center")
    l1.place(x=400, y=100)
    l1 = Label(p, text="Dr.Manoj.A\tMBBS\t\tHope Hospital\t9277918585", font="arial", anchor="center")
    l1.place(x=400, y=150)
    l1 = Label(p, text="Dr.D.Siva Parvathi\tMD\t\tSun Shine Hospital\t9848198505", font="arial")
    l1.place(x=400, y=200)
    l1 = Label(p, text="Dr.Naveen\tMD\t\tHopewell Hospital\t8885375665", font="arial")
    l1.place(x=400, y=250)
    l1 = Label(p, text="Dr.M.Mrudhula\tMBBS,MD\tSafe Hospital\t9705065844", font="arial")
    l1.place(x=400, y=300)
    l1 = Label(p, text="Dr.SS.Ramesh\tMBBS\t\tTrust Hospital\t9804564322", font="arial")
    l1.place(x=400, y=350)
    l1 = Label(p, text="Dr.Ayush\t\tMBBS,MD\tSraddha Hospital\t9248918888", font="arial")
    l1.place(x=400, y=400)
    l1 = Label(p, text="Dr.K.Hemalatha\tMD\t\tSudha Hospital\t9650456180", font="arial")
    l1.place(x=400, y=450)
    l1 = Label(p, text="Dr.V.R.Shreya\tMBBS,MD\tLife Hospital\t6633445500", font="arial")
    l1.place(x=400, y=500)
    l1 = Label(p, text="Dr.B.Akshay\tMBBS,MD\tSun Raise Hospital\t9705068489", font="arial")
    l1.place(x=400, y=550)
    l1 = Label(p, text="Dr.R.Chaitanya\tMD\t\tAyushman Hospital\t944918668", font="arial")
    l1.place(x=400, y=600)
    l1 = Label(p, text="Dr.K.Kranthi\tMBBS\t\tApollo Hospital\t9884455663", font="arial")
    l1.place(x=400, y=650)
    l1 = Label(p, text="Dr.V.Nikhil\tMBBS\t\tKshama Hospital\t7997887660", font="arial")
    l1.place(x=400, y=700)

    back = Button(p, text="Back", background="#C2DFFF", command=lambda: consult(p))
    backfont = f.Font(family="Oswald", size=18)
    back['font'] = backfont
    back.place(x=1380, y=700)
    s.pack()
    p.mainloop()


#Upload Health Report Page
def uploadhealth(health):
    health.destroy()
    #Creating Window
    health = Tk()
    health.title("Check your Health status")
    health.geometry("1920x1080")
    dhh = PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\latesthealthrep.png")
    label = Label(health, image=dhh)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    #Defining Entry Boxes
    enter=Entry(health)
    #username=enter.get()  #<------a------------------------------username get
    enter.place(x=420,y=235,width=160,height=30)

    tdate=Entry(health)
    #testdate=tdate.get()              #<------------------------------------testdate get
    tdate.place(x=820,y=235,width=160,height=30)

    eglucose=Entry(health)
    #glucose=eglucose.get()              #<------------------------------------glucose get
    eglucose.place(x=420,y=295,width=160,height=30)

    eliver = Entry(health)
    # liver=eliver.get()              #<------------------------------------liver get
    eliver.place(x=420, y=355, width=160, height=30)

    ekidney = Entry(health)
    # kidney=ekidney.get()              #<------------------------------------kidney get
    ekidney.place(x=420, y=415, width=160, height=30)

    ehaemo = Entry(health)
    # haemoglobin=ehaemo.get()              #<------------------------------------haemoglobin get
    ehaemo.place(x=420, y=470, width=160, height=30)

    echolo = Entry(health)
    # cholestrol=echolo.get()              #<------------------------------------cholestrol get
    echolo.place(x=420, y=530, width=160, height=30)

    ethyroid = Entry(health)
    # thyroid=ethyroid.get()              #<------------------------------------thyroid get
    ethyroid.place(x=420, y=590, width=160, height=30)

    euro = Entry(health)
    # urine=euro.get()              #<------------------------------------urine get
    euro.place(x=420, y=645, width=160, height=30)


    #Defining Check Buttons
    cbutton = Button(health, text="Check", background="#f3b4a3", command=lambda: checkgluco(eglucose.get()))
    cbuttonfont = f.Font(family="Poppins", size=8)
    cbutton['font'] = cbuttonfont
    cbutton.place(x=600, y=295, width=50, height=37)

    liverbutton = Button(health, text="Check", background="#f3b4a3", command=lambda: checkliver(eliver.get()))
    liverfont = f.Font(family="Poppins", size=8)
    liverbutton['font'] = liverfont
    liverbutton.place(x=600, y=355, width=50, height=37)

    kidneybutton = Button(health, text="Check",background="#f3b4a3", command=lambda: checkkidney(ekidney.get()))
    kidneyfont = f.Font(family="Poppins", size=8)
    kidneybutton['font'] = kidneyfont
    kidneybutton.place(x=600, y=415, height=37, width=50)

    haemobutton = Button(health, text="Check", background="#f3b4a3",command=lambda: checkhaemo(ehaemo.get()))
    haemofont = f.Font(family="Poppins", size=8)
    haemobutton['font'] = haemofont
    haemobutton.place(x=600, y=470, height=37, width=50)

    cholobutton = Button(health, text="Check",background="#f3b4a3", command=lambda: checkcholo(echolo.get()))
    cholofont = f.Font(family="Poppins", size=8)
    cholobutton['font'] = cholofont
    cholobutton.place(x=600, y=530, height=37, width=50)

    thybutton = Button(health, text="Check",background="#f3b4a3", command=lambda: checkthyroid(ethyroid.get()))
    thyfont = f.Font(family="Poppins", size=8)
    thybutton['font'] = thyfont
    thybutton.place(x=600, y=590, height=37, width=50)

    urobutton = Button(health, text="Check",background="#f3b4a3", command=lambda: checkuro(euro.get()))
    urofont = f.Font(family="Poppins", size=8)
    urobutton['font'] = urofont
    urobutton.place(x=600, y=645, height=37, width=50)

    #Defining Comparison Functions
    def checkgluco(eglucose):
        eglucose=float(eglucose)
        global gluco
        global consultdiabutton
        if eglucose>=140 and eglucose<=199:
             gluco=Label(health,text="PREDIABETES",fg="Yellow",bg="#b4e1c3")
             glucofont=f.Font(family="Poppins",size=20)
             gluco['font']=glucofont
             gluco.place(x=1060,y=295,height=25)
             consultdiabutton = Button(health, text="CONSULT DIABETOLOGIST", command=lambda: dia(health), width=30)
             consultdiabuttonfont = f.Font(family="Oswald", size=10)
             consultdiabutton['font'] = consultdiabuttonfont
             consultdiabutton.place(x=700, y=295)
        elif eglucose>=200:
             gluco=Label(health,text="DIABETES",fg="Red",bg="#b4e1c3")
             glucofont=f.Font(family="Poppins",size=20)
             gluco['font']=glucofont
             gluco.place(x=1080, y=295, height=25)
             consultdiabutton = Button(health, text="CONSULT DIABETOLOGIST", command=lambda: dia(health), width=30)
             consultdiabuttonfont = f.Font(family="Oswald", size=10)
             consultdiabutton['font'] = consultdiabuttonfont
             consultdiabutton.place(x=700, y=295)
        else:
             gluco=Label(health,text="NORMAL",fg="Green",bg="#b4e1c3")
             glucofont=f.Font(family="Poppins",size=20)
             gluco['font']=glucofont
             gluco.place(x=1090, y=295, height=25)
             consultdiabutton = Button(health, text="UNDER CONTROL", width=30)
             consultdiabuttonfont = f.Font(family="Oswald", size=10)
             consultdiabutton['font'] = consultdiabuttonfont
             consultdiabutton.place(x=700, y=295)

        print(eglucose)

    def checkliver(eliver):
        eliver=float(eliver)
        global liv
        global consultgastrobutton
        if eliver>=0.3 and eliver<=1.2:
            liv=Label(health,text="NORMAL",fg="Green",bg="#b4e1c3")
            livfont=f.Font(family="Poppins",size=20)
            liv['font']=livfont
            liv.place(x=1080,y=355,height=25)
            consultgastrobutton = Button(health, text="UNDER CONTROL",
                                         width=30)  # <--------changee
            consultgastrobuttonfont = f.Font(family="Oswald", size=10)
            consultgastrobutton['font'] = consultgastrobuttonfont
            consultgastrobutton.place(x=700, y=355)
        elif eliver<0.3:
            liv = Label(health, text="LOW", fg="Yellow", bg="#b4e1c3")
            livfont = f.Font(family="Poppins", size=20)
            liv['font'] = livfont
            liv.place(x=1120, y=355, height=25)
            consultgastrobutton = Button(health, text="CONSULT GASTROENTROLOGIST", command=lambda: gastro(health),
                                         width=30)  # <--------changee
            consultgastrobuttonfont = f.Font(family="Oswald", size=10)
            consultgastrobutton['font'] = consultgastrobuttonfont
            consultgastrobutton.place(x=700, y=355)
        else:
            liv=Label(health,text="HIGH",fg="Red",bg="#b4e1c3")
            livfont=f.Font(family="Poppins",size=20)
            liv['font']=livfont
            liv.place(x=1120, y=355, height=25)
            consultgastrobutton = Button(health, text="CONSULT GASTROENTROLOGIST",command=lambda: gastro(health),
                                         width=30)  # <--------changee
            consultgastrobuttonfont = f.Font(family="Oswald", size=10)
            consultgastrobutton['font'] = consultgastrobuttonfont
            consultgastrobutton.place(x=700, y=355)
            print(eliver)

    def checkkidney(ekidney):
        ekidney=float(ekidney)
        global kid
        global consultnephrobutton
        if ekidney>=3.5 and ekidney<=7.2:
            kid=Label(health,text="NORMAL",fg="Green",bg="#b4e1c3")
            kidfont=f.Font(family="Poppins",size=20)
            kid['font']=kidfont
            kid.place(x=1090,y=415,height=25)
            consultnephrobutton = Button(health, text="UNDER CONTROL",
                                         width=30)  # <--------changee
            consultnephrobuttonfont = f.Font(family="Oswald", size=10)
            consultnephrobutton['font'] = consultnephrobuttonfont
            consultnephrobutton.place(x=700, y=415)
        elif ekidney < 3.5:
            kid = Label(health, text="LOW", fg="yellow", bg="#b4e1c3")
            kidfont = f.Font(family="Poppins",size=20)
            kid['font'] = kidfont
            kid.place(x=1120, y=415, height=25)
            consultnephrobutton = Button(health, text="CONSULT UROLOGIST", command=lambda: urologist(health),
                                         width=30)  # <--------changee
            consultnephrobuttonfont = f.Font(family="Oswald", size=10)
            consultnephrobutton['font'] = consultnephrobuttonfont
            consultnephrobutton.place(x=700, y=415)

        else:
            kid = Label(health, text="HIGH", fg="red", bg="#b4e1c3")
            kidfont = f.Font(family="Poppins",size=20)
            kid['font'] = kidfont
            kid.place(x=1120, y=415, height=25)
            consultnephrobutton = Button(health, text="CONSULT UROLOGIST", command=lambda: urologist(health),
                                         width=30)  # <--------changee
            consultnephrobuttonfont = f.Font(family="Oswald", size=10)
            consultnephrobutton['font'] = consultnephrobuttonfont
            consultnephrobutton.place(x=700, y=415)

        print(ekidney)

    def checkhaemo(ehaemo):
        ehaemo=float(ehaemo)
        global haemo1
        global consulthaemobutton
        if ehaemo >= 13.5 and ehaemo <= 18.0:
            haemo1 = Label(health, text="NORMAL", fg="Green", bg="#b4e1c3")
            haemofont = f.Font(family="Poppins",size=20)
            haemo1['font'] = haemofont
            haemo.place(x=1090, y=470, height=25)
            consulthaemobutton = Button(health, text="UNDER CONTROL",
                                        width=30)  # <--------changee
            consulthaemobuttonfont = f.Font(family="Oswald", size=10)
            consulthaemobutton['font'] = consulthaemobuttonfont
            consulthaemobutton.place(x=700, y=470)
        elif ehaemo < 13.5:
            haemo1 = Label(health, text="LOW", fg="yellow", bg="#b4e1c3")
            haemofont = f.Font(family="Poppins",size=20)
            haemo1['font'] = haemofont
            haemo1.place(x=1120, y=470, height=25)
            consulthaemobutton = Button(health, text="CONSULT HAEMATOLOGIST", command=lambda: hema(health),
                                        width=30)  # <--------changee
            consulthaemobuttonfont = f.Font(family="Oswald", size=10)
            consulthaemobutton['font'] = consulthaemobuttonfont
            consulthaemobutton.place(x=700, y=470)
        else:
            haemo1 = Label(health, text="HIGH", fg="red", bg="#b4e1c3")
            haemofont = f.Font(family="Poppins",size=20)
            haemo1['font'] = haemofont
            haemo1.place(x=1120, y=470, height=25)
            consulthaemobutton = Button(health, text="CONSULT HAEMATOLOGIST", command=lambda: hema(health),
                                        width=30)  # <--------changee
            consulthaemobuttonfont = f.Font(family="Oswald", size=10)
            consulthaemobutton['font'] = consulthaemobuttonfont
            consulthaemobutton.place(x=700, y=470)

        print(ehaemo)

    def checkcholo(echolo):
        echolo=float(echolo)
        global cholo
        global consultcardiobutton
        if echolo < 200:
            cholo = Label(health, text="NORMAL", fg="Green", bg="#b4e1c3")
            cholofont = f.Font(family="Poppins",size=20)
            cholo['font'] = cholofont
            cholo.place(x=1090, y=530, height=25)
            consultcardiobutton = Button(health, text="UNDER CONTROL",
                                         width=30)  # <--------changee
            consultcardiobuttonfont = f.Font(family="Oswald", size=10)
            consultcardiobutton['font'] = consultcardiobuttonfont
            consultcardiobutton.place(x=700, y=530)
        elif echolo >= 200 and echolo <= 239:
            cholo = Label(health, text="BORDERLINE", fg="yellow", bg="#b4e1c3")
            cholofont = f.Font(family="Poppins",size=20)
            cholo['font'] = cholofont
            cholo.place(x=1090, y=530, height=25)
            consultcardiobutton = Button(health, text="CONSULT CARDIOLOGIST", command=lambda: card(health),
                                         width=30)  # <--------changee
            consultcardiobuttonfont = f.Font(family="Oswald", size=10)
            consultcardiobutton['font'] = consultcardiobuttonfont
            consultcardiobutton.place(x=700, y=530)

        else:
            cholo = Label(health, text="HIGH", fg="Red", bg="#b4e1c3")
            cholofont = f.Font(family="Poppins",size=20)
            cholo['font'] = cholofont
            cholo.place(x=1120, y=530, height=25)
            consultcardiobutton = Button(health, text="CONSULT CARDIOLOGIST", command=lambda: card(health),
                                         width=30)  # <--------changee
            consultcardiobuttonfont = f.Font(family="Oswald", size=10)
            consultcardiobutton['font'] = consultcardiobuttonfont
            consultcardiobutton.place(x=700, y=530)

        print(echolo)

    def checkthyroid(ethyroid):
        ethyroid=float(ethyroid)
        global thy
        global consultendobutton
        if ethyroid >= 0.89 and ethyroid <= 1.76:
            thy = Label(health, text="NORMAL", fg="Green", bg="#b4e1c3")
            thyfont = f.Font(family="Poppins",size=20)
            thy['font'] = thyfont
            thy.place(x=1090, y=590, height=25)
            consultendobutton = Button(health, text="UNDER CONTROL",
                                       width=30)  # <--------changee
            consultendobuttonfont = f.Font(family="Oswald", size=10)
            consultendobutton['font'] = consultendobuttonfont
            consultendobutton.place(x=700, y=590)
        elif ethyroid > 1.76:
            thy = Label(health, text="HIGH", fg="Red", bg="#b4e1c3")
            thyfont = f.Font(family="Poppins",size=20)
            thy['font'] = thyfont
            thy.place(x=1120, y=590, height=25)
            consultendobutton = Button(health, text="CONSULT ENDOCRINOLOGIST", command=lambda: endo(health),
                                       width=30)  # <--------changee
            consultendobuttonfont = f.Font(family="Oswald", size=10)
            consultendobutton['font'] = consultendobuttonfont
            consultendobutton.place(x=700, y=590)

        else:
            hy = Label(health, text="LOW", fg="Red", bg="#b4e1c3")
            thyfont = f.Font(amily="Poppins",size=20)
            thy['font'] = thyfont
            thy.place(x=1120, y=590, height=25)
            consultendobutton = Button(health, text="CONSULT ENDOCRINOLOGIST", command=lambda: endo(health),
                                       width=30)  # <--------changee
            consultendobuttonfont = f.Font(family="Oswald", size=10)
            consultendobutton['font'] = consultendobuttonfont
            consultendobutton.place(x=700, y=590)

        print(ethyroid)

    def checkuro(euro):
        euro=float(euro)
        global uro
        global consulturobutton
        if euro >= 4.6 and euro <= 8.0:
            uro = Label(health, text="NORMAL", fg="Green", bg="#b4e1c3")
            urofont = f.Font(family="Poppins",size=20)
            uro['font'] = urofont
            uro.place(x=1090, y=645, height=25)
            consulturobutton = Button(health, text="UNDER CONTROL",
                                      width=30)  # <--------changee
            consulturobuttonfont = f.Font(family="Oswald", size=10)
            consulturobutton['font'] = consulturobuttonfont
            consulturobutton.place(x=700, y=645)
        elif euro < 4.6:
            uro = Label(health, text="LOW", fg="yellow", bg="#b4e1c3")
            urofont = f.Font(family="Poppins",size=20)
            uro['font'] = urofont
            uro.place(x=1120, y=645, height=25)
            consulturobutton = Button(health, text="CONSULT UROLOGIST", command=lambda: urologist(health),
                                      width=30)  # <--------changee
            consulturobuttonfont = f.Font(family="Oswald", size=10)
            consulturobutton['font'] = consulturobuttonfont
            consulturobutton.place(x=700, y=645)

        else:
            uro = Label(health, text="HIGH", fg="red", bg="#b4e1c3")
            urofont = f.Font(family="Poppins",size=20)
            uro['font'] = urofont
            uro.place(x=1120, y=645, height=25)
            consulturobutton = Button(health, text="CONSULT UROLOGIST", command=lambda: urologist(health),
                                      width=30)  # <--------changee
            consulturobuttonfont = f.Font(family="Oswald", size=10)
            consulturobutton['font'] = consulturobuttonfont
            consulturobutton.place(x=700, y=645)

        print(euro)

    #Defining Misc Buttons and their Functions
    #1. Functions
    def clear():
        enter.delete(0,END)
        tdate.delete(0,END)
        eglucose.delete(0,END)
        eliver.delete(0,END)
        ekidney.delete(0,END)
        ehaemo.delete(0,END)
        echolo.delete(0,END)
        ethyroid.delete(0,END)
        euro.delete(0,END)
        gluco.destroy()
        consultdiabutton.destroy()
        liv.destroy()
        consultgastrobutton.destroy()
        kid.destroy()
        consultnephrobutton.destroy()
        haemo1.destroy()
        consulthaemobutton.destroy()
        cholo.destroy()
        consultcardiobutton.destroy()
        thy.destroy()
        consultendobutton.destroy()
        uro.destroy()
        consulturobutton.destroy()


    def savedata():
        username = enter.get()
        testdate = tdate.get()
        glucose=eglucose.get()
        liver=eliver.get()
        kidney=ekidney.get()
        haemoglobin=ehaemo.get()
        cholestrol=echolo.get()
        thyroid=ethyroid.get()
        urine=euro.get()

        connectionMYSQL()
        mycursor.execute("SHOW TABLES;")
        user_data = mycursor.fetchall()
        userlist=[]
        for i in range(0, len(user_data)):
            userlist.append(user_data[i][0])
        if username not in userlist:
            messagebox.showinfo("User Not Found!", "Entered User Does Not Exist. New User Will Be Created.")
            mycursor.execute("CREATE TABLE "+username+" (Date VARCHAR(15), Glucose_GlycosylatedHB VARCHAR(5), Liver_TotalBilirubin VARCHAR(5), Kidney_UricAcid VARCHAR(5), Hematology_Haemoglobin VARCHAR(5), Cholestrol_TotalCholestrol VARCHAR(5), Thyroid_FreeThyroxine VARCHAR(5), Urinalysis_Reaction VARCHAR(5)); " )
            mycursor.execute(("INSERT INTO " + username + " VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"),
                             (testdate, glucose, liver, kidney, haemoglobin, cholestrol, thyroid, urine))
        else:
            mycursor.execute(("INSERT INTO " + username + " VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"),
                             (testdate, glucose, liver, kidney, haemoglobin, cholestrol, thyroid, urine))

        mycon.commit()
        mycursor.close()
        mycon.close()
        messagebox.showinfo("Saved", "Your Data Has Been Saved.")


    #2. Buttons
    cle_ar=Button(health,text="CLEAR",background="#b4e1c3",command=clear,width=15)
    cle_arfont=f.Font(family="Oswald",size=18)
    cle_ar['font']=cle_arfont
    cle_ar.place(x=700,y=700)

    save = Button(health, text="SAVE", background="#b4e1c3", command=savedata,width=15)
    savefont = f.Font(family="Oswald", size=18)
    save['font'] = savefont
    save.place(x=420, y=700)

    back = Button(health, text="BACK", background="#C2DFFF", command=lambda: dashboard(health),width=8)
    backfont = f.Font(family="Oswald", size=18)
    back['font'] = backfont
    back.place(x=1300, y=700)
    health.mainloop()


def HealthHistory(hh):
    hh.destroy()
    hh=Tk()
    hh.title("Health History")
    hh.geometry("1920x1080")
    dhh=PhotoImage(file=r"C:\Users\Hasmita kancharla\Downloads\Healthhis.png")
    label=Label(hh,image=dhh)
    label.place(x=0,y=0,relwidth=1, relheight=1)
    connectionMYSQL()
    mycursor.execute("SHOW TABLES;")
    user_data = mycursor.fetchall()
    tp = []
    for i in range(0,len(user_data)):
        tp.append(user_data[i][0])
    user_data=tuple(tp)
    selected_uname=StringVar(hh)
    #selected_uname.set(tp[0])
    selected_uname.set("SELECT USER")
    def callback(selection) :
        # current user name selected from drop down in health history
        global current_uname
        current_uname=selection
        #print("inside callback:", current_uname, selection, selected_uname.get())

    drop = OptionMenu(hh,selected_uname, *tp, command=callback)
    drop.place(x=460,y=235)
    #current_uname="arjun"

    def glucosegraph():
        import matplotlib.pyplot as plt
        connectionMYSQL()
        print("user:", current_uname)
        mycursor.execute("SELECT Glucose_BloodSugar FROM "+current_uname+" ;")
        data = mycursor.fetchall()
        glucose =[]
        for i in data:
            glucose.append((i[0]))
        mycursor.execute("SELECT Date FROM "+current_uname+" ;")
        data1 = mycursor.fetchall()
        dates = []
        for i in data1:
            dates.append((i[0]))

        date_objects = [datetime.strptime(date, '%d/%m/%Y').date() for date in dates]
        plt.xlabel('DATE OF TEST')
        plt.ylabel('GLUCOSE LEVEL')
        plt.title("BLOOD SUGAR TEST")
        plt.plot(date_objects, glucose)
        plt.show()
        mycon.commit()
        mycursor.close()
        mycon.close()
    bh=Button(hh,text="GLUCOSE\n HISTORY",height=7,width=15,command=glucosegraph,bg="#b4e1c3",borderwidth=0)
    bhfont = f.Font(family="Oswald", size=13)
    bh['font'] = bhfont
    bh.place(x=195,y=310)
    def bilirubingraph():
        import matplotlib.pyplot as plt
        connectionMYSQL()
        mycursor.execute("SELECT Liver_TotalBilirubin FROM "+current_uname+" ;")
        data = mycursor.fetchall()
        bilirubin = []
        for i in data:
            bilirubin.append(float(i[0]))
        mycursor.execute("SELECT Date FROM "+current_uname+" ;")
        data1 = mycursor.fetchall()

        dates = []
        for i in data1:
            dates.append((i[0]))

        date_objects = [datetime.strptime(date, '%d/%m/%Y').date() for date in dates]
        plt.xlabel('DATE OF TEST')
        plt.ylabel('BILIRUBIN LEVEL')
        plt.title("TOTAL BILIRUBIN TEST")
        plt.plot(date_objects, bilirubin)
        plt.show()
        mycon.commit()
        mycursor.close()
        mycon.close()
    bh=Button(hh,text="TOTAL BILIRUBIN \n HISTORY",height=7,width=15,command=bilirubingraph,bg="#b4e1c3",borderwidth=0)
    bhfont = f.Font(family="Oswald", size=13)
    bh['font'] = bhfont
    bh.place(x=520,y=310)
    def uricacidgraph():
        import matplotlib.pyplot as plt
        connectionMYSQL()
        mycursor.execute("SELECT Kidney_UricAcid FROM "+current_uname+" ;")
        data = mycursor.fetchall()
        uricacid = []
        for i in data:
            uricacid.append(float(i[0]))
        mycursor.execute("SELECT Date FROM "+current_uname+" ;")
        data1 = mycursor.fetchall()
        dates = []
        for i in data1:
            dates.append((i[0]))
        date_objects = [datetime.strptime(date, '%d/%m/%Y').date() for date in dates]
        plt.xlabel('DATE OF TEST')
        plt.ylabel('URIC ACID LEVEL')
        plt.title("URIC ACID TEST")
        plt.plot(date_objects, uricacid)
        plt.show()
        mycon.commit()
        mycursor.close()
        mycon.close()
    bh=Button(hh,text="URIC ACID \n HISTORY",height=7,width=15,command=uricacidgraph,bg="#b4e1c3",borderwidth=0)
    bhfont = f.Font(family="Oswald", size=13)
    bh['font'] = bhfont
    bh.place(x=845,y=310)
    def hemoglobingraph():
        import matplotlib.pyplot as plt
        connectionMYSQL()

        mycursor.execute("SELECT Hematology_Haemoglobin FROM "+current_uname+" ;")
        data = mycursor.fetchall()
        haemo = []
        for i in data:
            haemo.append(float(i[0]))
        mycursor.execute("SELECT Date FROM "+current_uname+" ;")
        data1 = mycursor.fetchall()
        dates = []
        for i in data1:
            dates.append((i[0]))
        date_objects = [datetime.strptime(date, '%d/%m/%Y').date() for date in dates]
        plt.xlabel('DATE OF TEST')
        plt.ylabel('HAEMOGLOBIN LEVEL')
        plt.title("HAEMOGLOBIN TEST")
        plt.plot(date_objects, haemo)
        plt.show()
        mycon.commit()
        mycursor.close()
        mycon.close()
    bh=Button(hh,text="HAEMOGLOBIN\nHISTORY",height=7,width=15,command=hemoglobingraph,bg="#b4e1c3",borderwidth=0)
    bhfont = f.Font(family="Oswald", size=13)
    bh['font'] = bhfont
    bh.place(x=1170,y=310)
    def cholestrolgraph():
        import matplotlib.pyplot as plt
        connectionMYSQL()

        mycursor.execute("SELECT Cholestrol_TotalCholestrol FROM "+current_uname+" ;")
        data = mycursor.fetchall()
        cholestrol = []
        for i in data:
            cholestrol.append(float(i[0]))
        mycursor.execute("SELECT Date FROM "+current_uname+" ;")
        data1 = mycursor.fetchall()
        dates = []
        for i in data1:
            dates.append((i[0]))
        date_objects = [datetime.strptime(date, '%d/%m/%Y').date() for date in dates]
        plt.xlabel('DATE OF TEST')
        plt.ylabel('CHOLESTROL LEVEL')
        plt.title("TOTAL CHOLESTROL TEST")
        plt.plot(date_objects, cholestrol)
        plt.show()
        mycon.commit()
        mycursor.close()
        mycon.close()
    bh=Button(hh,text="CHOLESTROL\nHISTORY",height=7,width=15,command=cholestrolgraph,bg="#b4e1c3",borderwidth=0)
    bhfont = f.Font(family="Oswald", size=13)
    bh['font'] = bhfont
    bh.place(x=358,y=550)
    def thyroxingraph():
        import matplotlib.pyplot as plt
        connectionMYSQL()

        mycursor.execute("SELECT Thyroid_FreeThyroxine FROM "+current_uname+" ;")
        data = mycursor.fetchall()
        thyroxine = []
        for i in data:
            thyroxine.append(float(i[0]))
        mycursor.execute("SELECT Date FROM "+current_uname+" ;")
        data1 = mycursor.fetchall()
        dates = []
        for i in data1:
            dates.append((i[0]))
        date_objects = [datetime.strptime(date, '%d/%m/%Y').date() for date in dates]
        plt.xlabel('DATE OF TEST')
        plt.ylabel('THYROID LEVEL')
        plt.title("FREE THROXINE TEST")
        plt.plot(date_objects, thyroxine)
        plt.show()
        mycon.commit()
        mycursor.close()
        mycon.close()
    bh=Button(hh,text="FREE THYROXIN\nHISTORY",height=7,width=15,command=thyroxingraph,bg="#b4e1c3",borderwidth=0)
    bhfont = f.Font(family="Oswald", size=13)
    bh['font'] = bhfont
    bh.place(x=700,y=550)
    def reactiongraph():
        import matplotlib.pyplot as plt
        connectionMYSQL()
        mycursor.execute("SELECT Urinalysis_Reaction FROM "+current_uname+" ;")
        data = mycursor.fetchall()
        reaction = []
        for i in data:
            reaction.append(float(i[0]))
        mycursor.execute("SELECT Date FROM "+current_uname+" ;")
        data1 = mycursor.fetchall()
        dates = []
        for i in data1:
            dates.append((i[0]))
        date_objects = [datetime.strptime(date, '%d/%m/%Y').date() for date in dates]
        plt.xlabel('DATE OF TEST')
        plt.ylabel('URINE REACTION LEVEL')
        plt.title("REACTION TEST")
        plt.plot(date_objects, reaction)
        plt.show()
        mycon.commit()
        mycursor.close()
        mycon.close()

    bh=Button(hh,text="URINE REACTION\nHISTORY",height=7,width=15,command=reactiongraph,bg="#b4e1c3",borderwidth=0)
    bhfont = f.Font(family="Oswald", size=13)
    bh['font'] = bhfont
    bh.place(x=1010,y=550)
    backk=Button(hh,text="BACK",background="#C2DFFF",command=lambda:dashboard(hh),width=8)
    backkfont=f.Font(family="Oswald",size=18)
    backk['font']=backkfont
    backk.place(x=1300,y=700)
    hh.mainloop()

#Starting the Program
main()
