import random
import time
import datetime
from tkinter import*
from tkinter import ttk
import tkinter.messagebox

def main():
    root = Tk()
    app = windows1(root)
    root.mainloop()
class windows1:
    def __init__(self,master):
        self.master = master
        self.master.title("Yönetim Sistemi")
        self.master.geometry("1350x750+0+0") # x-axis, y-axis, 0, 0
        self.frame =Frame(self.master)
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()
        
        self.LabelTitle = Label(self.frame,text= "Yönetim Sistemi", font=("arial",35,"bold"),
                            bd=10,relief="sunken")
        self.LabelTitle.grid(row=0,column=0,columnspan=1, pady=15)


        self.Loginframe1 = Frame(self.frame, width=800, height=100, bd=12, relief="groove")
        self.Loginframe1.grid(row=1,column=0)

        self.Loginframe2 = Frame(self.frame, width=800, height=100, bd=12, relief="groove")
        self.Loginframe2.grid(row=2,column=0, pady=10)

        self.Loginframe3 = Frame(self.frame, width=800, height=100, bd=12, relief="groove")
        self.Loginframe3.grid(row=6,column=0, pady=5)

        self.button_reg=Button(self.Loginframe3,text="Hasta Kayıt Sistemi",state=DISABLED,font=("arial",18,"normal"), 
                               command=self.Registration_window)
        self.button_reg.grid(row=0,column=0, padx=20, pady=12)

        self.button_hosp=Button(self.Loginframe3,text="Hastane Yönetimi Girişi",state=DISABLED,font=("arial",18,"normal"), 
                               command=self.Hospital_window)
        self.button_hosp.grid(row=0,column=1, padx=20, pady=12)


        # register girişi password and username, exit, reset, login yani
        self.LabelUsername = Label(self.Loginframe1, text="Kullanıcı Adı: ", font=("Calibri",18,"bold"),bd=3)
        self.LabelUsername.grid(row=0,column=0)

        self.textUsername = Entry(self.Loginframe1, font=("Calibri",18,"normal"),bd=3, textvariable=self.Username)
        self.textUsername.grid(row=0,column=1, padx=40, pady=15)
        

        self.LabelPassword = Label(self.Loginframe1, text="Parola: ", font=("Calibri",18,"bold"), bd=3)
        self.LabelPassword.grid(row=1,column=0)

        self.textPassword = Entry(self.Loginframe1, font=("Calibri",18,"normal"),bd=3, textvariable=self.Password, show="*")
        self.textPassword.grid(row=1,column=1, padx=40, pady=15)

        self.button_login=Button(self.Loginframe2, text="Giriş Yap", font=("Verdana",20,"roman"),
                                 command=self.login_system)
        self.button_login.grid(row=0,column=0, padx=30, pady=15)

        self.button_reset=Button(self.Loginframe2, text="Temizle", font=("Verdana",20,"roman"),
                                 command=self.reset_btn)
        self.button_reset.grid(row=0,column=1, padx=30, pady=15)

        self.button_exit=Button(self.Loginframe2, text="Çıkış Yap", font=("Verdana",20,"roman"),
                                command=self.exit_btn)
        self.button_exit.grid(row=0,column=2, padx=30, pady=15)

    def login_system(self):
        user=self.Username.get()
        pswd=self.Password.get()

        if(user==str("admin") and (pswd==str("admin"))):
            tkinter.messagebox.showinfo("",f"Hoş geldiniz {user} ")
            self.button_reg.config(state=NORMAL)
            self.button_hosp.config(state=NORMAL)   
        else:
            tkinter.messagebox.showinfo("Hata","Kullanıcı Adı veya Parola Hatalı")
            self.button_reg.config(state=DISABLED)
            self.button_hosp.config(state=DISABLED)
            
            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()
        
    def reset_btn(self):
    # çünkü sıfırlanınca etkisiz hale gelip tekrar user name ve password girişi olacak.
        self.button_reg.config(state=DISABLED)
        self.button_hosp.config(state=DISABLED)
        

        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()

    def exit_btn(self):
        self.exit_btn = tkinter.messagebox.askokcancel("","Çıkış Yapılsın mı?")
        if self.exit_btn > 0:
            self.master.destroy()
            return   



    # tüm pencereleri tanımlama:
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Hospital(self.newWindow)
          



class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title("Hasta Kayıt Sistemi")
        self.root.geometry("1350x750+200+50")
        

############ live time data by using time module #################
        Date_of_Kayit = StringVar()
        Date_of_Kayit.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        Mobile_no=IntVar()
        Pincode = StringVar()
        Address = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()

        ##### this var1,2,3,4,5 are for combobox #################
        var1 = IntVar() # num values for
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()

        Membership = StringVar()
        Membership.set("0") # ne zaman membership unclick olursa reset olacak otomatik

        ####################### Fonksiyonlar #################
        def exitbtt():
            exitbtt = tkinter.messagebox.askyesno("Üye Kayıt Formu","Çıkmak istediğinize emin misiniz?")
            if exitbtt >0:
                root.destroy()
            else:
                self.newWindow= Toplevel(self.master)
                self.app = Registration(self.newWindow)  
                return
        
        def resetbtt():
            Firstname.set("")
            Lastname.set("")
            Mobile_no.set("")
            Pincode.set("")
            Address.set("")
            Ref.set("")
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            Membership.set("0")
            member_gendercmb.current(0)
            member_membertypecmb.current(0)
            member_paymentcmb.current(0)
            member_membershiptxt(state = DISABLED)
        def resetbtt2() :
            resetbtt2 = tkinter.messagebox.askokcancel("Üye Kayıt Formu","Yeni kayıt ekmek istiyor musun?")
            if resetbtt2 >0:
                resetbtt()
            elif resetbtt2 <=0:
                resetbtt()
                detail_labeltxt.delete("1.0", END)
                return
        
        def reference_number():
            ranumber = random.randint(100000,999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def membership_money():

            if (var1.get() == 1):
                member_membershiptxt.configure(state= NORMAL)
                item = float(15000)
                Membership.set(str(item)+ "₺")
            elif (var1.get() == 0):
                member_membershiptxt.configure(state= DISABLED)
                item = float(0)
                Membership.set(str(item)+ "₺")

        def fis():
            reference_number()
            detail_labeltxt.insert(END, "\t"+str(Date_of_Kayit.get()) +"\t      "+ str(Ref.get())+"\t      "+
            str(Firstname.get())+"\t    " + str(Lastname.get())+"\t\t   " + str(Mobile_no.get()) +"\t\t    "+ 
            str(Address.get()) +"\t\t"+ str(Pincode.get())+"\t       " +str(member_gendercmb.get()) + "\t    "+str(member_membertypecmb.get())+"\t\t   "+str(member_paymentcmb.get())+"\t\t          "+
            str(Membership.get()) + "\n")    


    

#----------------------------------------------------------------
        title=Label(self.root, text = "Üye Kayıt Formu", font=("Arial", 20, "bold"),
                    relief=GROOVE, bg="#c1f5c6",fg= "#062720")
        title.pack(side=TOP, fill=X)
################# üye çerçevesi (member frame) #################
        Manage_Frame = Frame(self.root, relief=RIDGE, bg="#def3b4")
        Manage_Frame.place(x=20, y=80, width=450, height=600)

################ text, label , comboboxes in yönetme farme #################
        Cus_title = Label(Manage_Frame, text="Detaylar", font=("Arial", 20, "normal"), bg="#def3b4", fg="#062720")
        Cus_title.grid(row=0, columnspan=2, pady=5, sticky="new", padx=175)

        member_datelbl = Label(Manage_Frame, text="Tarih: ", font=("Arial",15, "normal", "underline"), bg="#def3b4", fg="#062720")
        member_datelbl.grid(row=1, column=0, padx=5, pady=5, sticky="w")                      

        member_datetxt= Entry(Manage_Frame, font=("Arial",15, "normal"), textvariable = Date_of_Kayit)
        member_datetxt.grid(row=1, column=1, padx=5, pady=5, sticky="w") 
        
        member_reflbl= Label(Manage_Frame, text="Referans ID: ", font=("Arial",15, "normal", "underline"), bg="#def3b4", fg="#062720")
        member_reflbl.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        member_reftxt= Entry(Manage_Frame, font=("Arial",15, "normal"), state=DISABLED, text= Ref)
        member_reftxt.grid(row=2, column=1, padx=5, pady=5, sticky="w")


        member_fnamelbl = Label(Manage_Frame, text="Adınız: ", font=("Arial",15, "normal", "underline"), bg="#def3b4", fg="#062720")
        member_fnamelbl.grid(row=3, column=0, padx=5, pady=5, sticky="w")                      

        member_fnametxt= Entry(Manage_Frame, font=("Arial",15, "normal"), textvariable = Firstname)
        member_fnametxt.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        member_lnamelbl = Label(Manage_Frame, text="Soyadınız: ", font=("Arial",15, "normal", "underline"), bg="#def3b4", fg="#062720")
        member_lnamelbl.grid(row=4, column=0, padx=5, pady=5, sticky="w")                      

        member_lnametxt= Entry(Manage_Frame, font=("Arial",15, "normal"), textvariable = Lastname)
        member_lnametxt.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        member_mobilelbl = Label(Manage_Frame, text="Telefon No: ", font=("Arial",15, "normal", "underline"), bg="#def3b4", fg="#062720")
        member_mobilelbl.grid(row=5, column=0, padx=5, pady=5, sticky="w")                      

        member_mobiletxt= Entry(Manage_Frame, font=("Arial",15, "normal"), textvariable = Mobile_no)
        member_mobiletxt.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        member_addresslbl = Label(Manage_Frame, text="Adresiniz: ", font=("Arial",15, "normal", "underline"), bg="#def3b4", fg="#062720")
        member_addresslbl.grid(row=6, column=0, padx=5, pady=5, sticky="w")                      

        member_addresstxt= Entry(Manage_Frame, font=("Arial",15, "normal"), textvariable = Address)
        member_addresstxt.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        member_pincodelbl = Label(Manage_Frame, text="Pin Kodunuz: ", font=("Arial",15, "normal", "underline"), bg="#def3b4", fg="#062720")
        member_pincodelbl.grid(row=7, column=0, padx=5, pady=5, sticky="w")                      

        member_pincodetxt= Entry(Manage_Frame, font=("Arial",15, "normal"), textvariable = Pincode)
        member_pincodetxt.grid(row=7, column=1, padx=5, pady=5, sticky="w")

        member_genderlbl = Label(Manage_Frame, text="Cinsiyetiniz: ", font=("Arial",15, "normal", "underline"), bg="#def3b4", fg="#062720")
        member_genderlbl.grid(row=8, column=0, padx=5, pady=5, sticky="w")                      

        member_gendercmb = ttk.Combobox(Manage_Frame, text=var4, font=("Arial",15, "normal"), state="readonly",
                                        width=18)
        member_gendercmb['values'] = ("", "Erkek", "Kadın", "Belirtmek istemiyorum.")
        member_gendercmb.current(0) # hiçbir şey seçili yokken index 0 yani boş olan olur.
        member_gendercmb.grid(row=8, column=1, padx=5, pady=5, sticky="w")


        member_membertypelbl = Label(Manage_Frame, text="Üye Tipi: ", font=("Arial",15, "normal", "underline"), bg="#def3b4", fg="#062720")
        member_membertypelbl.grid(row=9, column=0, padx=5, pady=5, sticky="w")                      

        member_membertypecmb = ttk.Combobox(Manage_Frame, text=var3, font=("Arial",15, "normal"), state="readonly",
                                        width=18)
        member_membertypecmb['values'] = ("", "Üniversite Kart", "Çocuk Kart", "Öğretmen Kart", "Yaşlı Kart")
        member_membertypecmb.current(0) # hiçbir şey seçili yokken index 0 yani boş olan olur.
        member_membertypecmb.grid(row=9, column=1, padx=5, pady=5, sticky="w")

        member_paymentlbl = Label(Manage_Frame, text="Ödeme Türü: ", font=("Arial",15, "normal", "underline"), bg="#def3b4", fg="#062720")
        member_paymentlbl.grid(row=10, column=0, padx=5, pady=5, sticky="w")                      

        member_paymentcmb = ttk.Combobox(Manage_Frame, text=var2, font=("Arial",15, "normal"), state="readonly",
                                        width=18)
        member_paymentcmb['values'] = ("", "Troy Kart", "Şehir Kart", "Visa Kart", "MasterCart Kart", "Elden Ödeme")
        member_paymentcmb.current(0) # hiçbir şey seçili yokken index 0 yani boş olan olur.
        member_paymentcmb.grid(row=10, column=1, padx=5, pady=5, sticky="w")

        member_membership = Checkbutton(Manage_Frame, text="Üyelik Aidatları", variable=var1, onvalue=1,
                                        offvalue=0, font=("Arial",15, "normal"),bg="#def3b4", fg="#062720", command=membership_money)
        member_membership.grid(row=11, column=0, sticky="w")
        member_membershiptxt = Entry(Manage_Frame, font=("Arial",15, "normal"), state=DISABLED, justify=RIGHT,
                                     textvariable = Membership)
        member_membershiptxt.grid(row=11, column=1, padx=5, pady=5, sticky="w")

################ detalil frame #################
        detail_frame = Frame(self.root, relief=RIDGE)
        detail_frame.place(x=500, y=80, width=1000, height=650)

        detail_label = Label(detail_frame, font=("Arial",15, "normal"), width=95,
                     text="Tarih\t Ref Id\t Adı\t Soyadı\t Telefon No\t Adres\t PinKodu\t Cinsiyet\t Üye Tipi\t Ödeme Türü\t Üyelik".expandtabs(5))
        detail_label.grid(row=0, column=0, columnspan=4, sticky="w")
        detail_labeltxt = Text(detail_frame, width=170, height=35, font=("Arial", 10, "normal"))
        detail_labeltxt.grid(row=1, column=0, columnspan=4)                


        fisbtn=Button(detail_frame, padx=10, bd=5, font=("Arial", 10, "normal"),
                      bg="#ECF491", width=20, height=2, text="Fiş", command=fis)
        fisbtn.grid(row=2, column=0)

        resbtn=Button(detail_frame, padx=10, bd=5, font=("Arial", 10, "normal"),
                      bg="#ECF491", width=20, height=2, text="Temizle", command=resetbtt2)
        resbtn.grid(row=2, column=1, sticky="w")

        exitbtn=Button(detail_frame, padx=10, bd=5, font=("Arial", 10, "normal"),
                      bg="#672525", fg="white", width=20, height=2, text="Çıkış", command=exitbtt)
        exitbtn.grid(row=2, column=2, sticky="s")

        
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
    main()    