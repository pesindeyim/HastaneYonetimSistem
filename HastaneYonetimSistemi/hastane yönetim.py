import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Hospital():
    def __init__(self,root):
        self.root = root
        self.root.title("Hastane Yönetim Sistemi")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="#e5f2dc")

################### Variable Description #################
        Date_of_Kayit = StringVar()
        Date_of_Kayit.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        cmbTabletNames=StringVar()
        Hospitalcode = StringVar()
        Number_of_Tablets = StringVar()
        Lot = StringVar()
        IssueDate = StringVar()
        ExpiryDate = StringVar()
        DailyDose = StringVar()
        SideEffects = StringVar()
        MoreInfo = StringVar()
        TimeAdvice = StringVar()
        Medication = StringVar()
        PatientID = StringVar()
        PatientName = StringVar()
        DateofBirth = StringVar()
        PatientAddress = StringVar()
        NHSnumber = StringVar()



        def Reference_numfunc():
            ranumber = random.randint(100000,999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def PrescriptionFunc():
            Reference_numfunc()
            TextPrescription.insert(END,"Hasta ID: \t"+PatientID.get()+"\n")
            TextPrescription.insert(END,"Hasta Adı: \t"+PatientName.get()+"\n")
            TextPrescription.insert(END,"Doğum Tarihi: \t"+DateofBirth.get()+"\n")
            TextPrescription.insert(END,"NHS No: \t"+NHSnumber.get()+"\n")
            TextPrescription.insert(END,"Hasta Adresi: \t"+PatientAddress.get()+"\n")
            TextPrescription.insert(END,"Günlük Doz: \t"+DailyDose.get()+"\n")
            TextPrescription.insert(END,"İşlem Tarihi: \t"+ExpiryDate.get()+"\n")
            TextPrescription.insert(END,"Tablet Sayısı: \t"+cmbTabletNames.get()+"\n")
            TextPrescription.insert(END,"Hastane Kodu: \t"+Hospitalcode.get()+"\n")

            return
            
            

        def Prescriptiondatafunc():
            Reference_numfunc()
            TextPrescriptionData.insert(END, Date_of_Kayit.get()+"\t\t"+Ref.get()+"\t\t  "+PatientID.get()+"\t\t"+
                                        PatientName.get()+"\t\t    "+DateofBirth.get()+"\t\t\t"+NHSnumber.get()+"\t\t     "+
                                        IssueDate.get()+"\t\t\t "+cmbTabletNames.get()+"\t\t\t"+Number_of_Tablets.get()+"\t\t "+
                                        Hospitalcode.get()+"\n")
            return    
        
            
        def Exitbtn():
            ExitBtn = tkinter.messagebox.askyesno("Hastane Yönetim Sistemi", "Çıkmak istediğine emin misin?")
            if ExitBtn > 0:
                root.destroy()
                return
            
        def deletefunc():
            Ref.set("")
            cmbTabletNames.set("")
            Hospitalcode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInfo.set("")
            TimeAdvice.set("")
            Medication.set("")
            PatientID.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptionData.delete("1.0",END)
            return
        def resetfunc():
            Ref.set("")
            cmbTabletNames.set("")
            Hospitalcode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInfo.set("")
            TimeAdvice.set("")
            Medication.set("")
            PatientID.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0",END)
            return


            
        



################### title #################
        title =  Label(self.root,text="Hastane Yönetim Sistemi", font=("Arial", 30, "normal"), bd=3,
                       relief=GROOVE, bg="#cde6bc", fg="Black")
        title.pack(side=TOP, fill=X)

################## FRames #################
        Manage_Frame = Frame(self.root, width=1510, height=200, bd=5, relief=RIDGE, bg="#d3edf7")
        Manage_Frame.place(x=10, y=80)
    
        Button_Frame = Frame(self.root, width=180, height=35, bd=2, relief=RIDGE, bg="#97d5ec")
        Button_Frame.place(x=1322, y=505)

        Data_Frame = LabelFrame(self.root, width=1510, height=270, bd=4, relief=RIDGE, bg="#c4dff7")
        Data_Frame.place(x=10, y=510)

############## Inner Frames ##################
        Data_FrameLeft = LabelFrame(Manage_Frame, width=1050, text="Genel Bilgiler", font=("Arial", 16, "normal"),
                                height=370, bd=5, relief=RIDGE, bg="#d3edf7")
        Data_FrameLeft.pack(side=LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame, width=1100, text="Reçete", font=("Arial", 13, "normal"),
                                height=400, bd=5, relief=RIDGE, bg="#d3edf7")
        Data_FrameRight.pack(side=RIGHT)

        Data_Framedata = LabelFrame(Data_Frame, width=1050, text="Reçete Bilgileri", font=("Arial", 13, "normal"),
                                height=270, bd=3, relief=RIDGE, bg="#c4dff7")
        Data_Framedata.pack(side=LEFT)
############# LABels ########################
        Datalbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Tarih", padx=2)
        Datalbl.grid(row=0, column=0, padx=5, pady=10, sticky=W)
        Datatxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=Date_of_Kayit)
        Datatxt.grid(row=0, column=1, padx=5, pady=10, sticky=E)

        ###### Ref
        Reflbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Referans ID", padx=2)
        Reflbl.grid(row=1, column=0, padx=5, pady=10, sticky=W)
        Reftxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, state=DISABLED, textvariable=Ref)
        Reftxt.grid(row=1, column=1, padx=5, pady=10, sticky=E)
        
        ###### Patient ID
        PatientIDlbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Hasta ID", padx=2)
        PatientIDlbl.grid(row=2, column=0, padx=5, pady=10, sticky=W)
        PatientIDtxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=PatientID)
        PatientIDtxt.grid(row=2, column=1, padx=5, pady=10, sticky=E)
        
        ###### Patient Name
        PatientNamelbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Hasta Adı", padx=2)
        PatientNamelbl.grid(row=3, column=0, padx=5, pady=10, sticky=W)
        PatientNametxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=PatientName)
        PatientNametxt.grid(row=3, column=1, padx=5, pady=10, sticky=E)
        
        ###### Patient Address
        PatientAddresslbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Hasta Adresi", padx=2)
        PatientAddresslbl.grid(row=4, column=0, padx=5, pady=10, sticky=W)
        PatientAddresstxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=PatientAddress)
        PatientAddresstxt.grid(row=4, column=1, padx=5, pady=10, sticky=E)

        ## Patient Date of Birth
        DateofBirthlbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Hasta Doğum Zamanı", padx=2)
        DateofBirthlbl.grid(row=5, column=0, padx=5, pady=10, sticky=W)
        DateofBirthtxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=DateofBirth)
        DateofBirthtxt.grid(row=5, column=1, padx=5, pady=10, sticky=E)

        #### NHSnumber
        NHSnumberlbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="NHS Numarası", padx=2)
        NHSnumberlbl.grid(row=6, column=0, padx=5, pady=10, sticky=W)
        NHSnumbertxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=NHSnumber)
        NHSnumbertxt.grid(row=6, column=1, padx=5, pady=1, sticky=E)

        #### Tablet NAme
        TabletNamelbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Tablet İsimleri", padx=2)
        TabletNamelbl.grid(row=7, column=0, padx=5, pady=10, sticky=W)
        Tabletcmb = ttk.Combobox(Data_FrameLeft, textvariable=cmbTabletNames, width=25, state="readonly",
                                 font=("Arial", 10, "normal"))
        Tabletcmb['values']= ("","Paracetamol", "Parol", "Dip-l One", "Calpol", "Majezik", "Voltaren", "Parafon", "Dexofen","Apramax")
        Tabletcmb.current(0)
        Tabletcmb.grid(row=7, column=1, padx=5, pady=10)

        ##### Numbler of Tablets
        TabletNumberlbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Tablet Adedi", padx=2)
        TabletNumberlbl.grid(row=8, column=0, padx=5, pady=10, sticky=W)
        TabletNumbertxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=Number_of_Tablets)
        TabletNumbertxt.grid(row=8, column=1, padx=5, pady=10, sticky=E)

        ######### column 2 other detail in same frame.
        ##### Hospital Code
        HospitalCodelbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Hastane Kodu", padx=2)
        HospitalCodelbl.grid(row=0, column=2, padx=5, pady=10, sticky=W)
        HospitalCodetxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=Hospitalcode)
        HospitalCodetxt.grid(row=0, column=3, padx=5, pady=10, sticky=E)

        ######## time Advice night day
        TimeAdvicelbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Zaman Önerisi", padx=2)
        TimeAdvicelbl.grid(row=1, column=2, padx=5, pady=10, sticky=W)
        
        TimeAdvicecmb = ttk.Combobox(Data_FrameLeft, textvariable=TimeAdvice, width=25, state="readonly",
                                     font=("Arial",10, "normal"))
        TimeAdvicecmb['values'] = ("", "Sabah", "Öğlen", "Akşam")
        TimeAdvicecmb.current(0)
        TimeAdvicecmb.grid(row=1, column=3, padx=5, pady=10)

        ######## Lot number of medicine
        LotNumberlbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Medicine Lot Numarası", padx=2)
        LotNumberlbl.grid(row=2, column=2, padx=5, pady=10, sticky=W)
        LotNumbertxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=Lot)
        LotNumbertxt.grid(row=2, column=3, padx=5, pady=10, sticky=E)

        ######### Issued Date
        IssuedDatelbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="İşlem Tarihi", padx=2)
        IssuedDatelbl.grid(row=3, column=2, padx=5, pady=10, sticky=W)
        IssuedDatetxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=IssueDate)
        IssuedDatetxt.grid(row=3, column=3, padx=5, pady=10, sticky=E)

        ######## Expiry Date

        ExpiryDatelbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Sonlandırma Tarihi", padx=2)
        ExpiryDatelbl.grid(row=4, column=2, padx=5, pady=10, sticky=W)
        ExpiryDatetxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=ExpiryDate)
        ExpiryDatetxt.grid(row=4, column=3, padx=5, pady=10, sticky=E)

        ######## DailyDose
        DailyDoselbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Günlük Doz", padx=2)
        DailyDoselbl.grid(row=5, column=2, padx=5, pady=10, sticky=W)
        DailyDosetxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=DailyDose)
        DailyDosetxt.grid(row=5, column=3, padx=5, pady=10, sticky=E)

        ####### Side Effects
        SideEffectslbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Yan Etkiler", padx=2)
        SideEffectslbl.grid(row=6, column=2, padx=5, pady=10, sticky=W)
        SideEffectstxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=SideEffects)
        SideEffectstxt.grid(row=6, column=3, padx=5, pady=10, sticky=E)

        ####### More info
        MoreInfolbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="Daha Fazla Bilgi", padx=2)
        MoreInfolbl.grid(row=7, column=2, padx=5, pady=10, sticky=W)
        MoreInfotxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=MoreInfo)
        MoreInfotxt.grid(row=7, column=3, padx=5, pady=10, sticky=E)

        ####### Medication
        Medicationlbl = Label(Data_FrameLeft, font=("Arial", 10, "normal"), width=20, text="İlaç", padx=2)
        Medicationlbl.grid(row=8, column=2, padx=5, pady=10, sticky=W)
        Medicationtxt = Entry(Data_FrameLeft, font=("Arial",10, "normal"), width=27, textvariable=Medication)
        Medicationtxt.grid(row=8, column=3, padx=5, pady=10, sticky=E)

        ######## Text field for prescription
        TextPrescription = Text(Data_FrameRight, font=("Arial", 10, "normal"), width=98, height=23, padx=3,
                                pady=5)
        TextPrescription.grid(row=0, column=0)

        ######### text for prescription data
        TextPrescriptionData = Text(Data_Framedata, font=("Arial", 10, "normal"), width=183, height=13.8, padx=3,
                                    pady=5)
        TextPrescriptionData.grid(row=1, column=0)

        ########## add button to our middle frame
        PrescriptionBtn = Button(Button_Frame, text="Reçete", bg="#D0C3A7", fg="Black", activebackground="#D0C3A7", 
                                 font=("Arial",12,"normal"), width=15, bd=2, command=PrescriptionFunc)
        PrescriptionBtn.grid(row=0, column=0, padx=10, pady=5)

        ########## receipt button
        ReceiptBtn = Button(Button_Frame, text="Fatura", bg="#D0C3A7", fg="Black", activebackground="#D0C3A7", 
                             font=("Arial",12,"normal"), width=15, bd=2, command=Prescriptiondatafunc)
        ReceiptBtn.grid(row=1, column=0, padx=10,pady=5)

        ########## reset button
        ResetBtn = Button(Button_Frame, text="Sıfırla", bg="#D0C3A7", fg="Black", activebackground="#D0C3A7", 
                            font=("Arial",12,"normal"), width=15, bd=2, command=resetfunc)
        ResetBtn.grid(row=2, column=0, padx=10,pady=5)

        ######### delete button
        DeleteBtn = Button(Button_Frame, text="Sil", bg="#D0C3A7", fg="Black", activebackground="#D0C3A7", 
                            font=("Arial",12,"normal"), width=15, bd=2, command=deletefunc)
        DeleteBtn.grid(row=3, column=0, padx=10, pady=5)

        ########## exit button
        ExitBtn = Button(Button_Frame, text="Çıkış", bg="#D0C3A7", fg="Black", activebackground="#D0C3A7", 
                           font=("Arial",12,"normal"), width=15, bd=2, command=Exitbtn)
        ExitBtn.grid(row=4, column=0, padx=10, pady=5)

        PrescriptiondataRow = Label(Data_Framedata, bg="white", font=("Arial",12,"normal"),
                                    text="Tarih\t Referans ID\tHasta ID\t         Hasta Adı\t Doğum Günü\t NHS Numarası\t İşlem Tarihi\t Tablet İsimleri\t Tablet Adedi\t Hastane Kodu")
        PrescriptiondataRow.grid(row=0, column=0, padx=10, pady=5)
        



        







if __name__ == "__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()