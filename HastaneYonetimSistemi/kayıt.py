import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title("Yönetim Kayıt Sistemi")
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




                

if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()