from tkinter import *
from tkinter import ttk
# from turtle import hideturtle
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


def main_win(): 
    win=Tk()
    app = Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self, root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\DELL\Desktop\Login page\images\F9ykYSe-loneliness-wallpapers.jpg")
        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="Black")
        frame.place(x=520,y=170,width=340,height=450)


        img1=Image.open(r"C:\Users\DELL\Desktop\Login page\images\test-account.png")
        img1=img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black", borderwidth=0)
        lblimg1.place(x=640,y=175,width=100, height=100)


        get_start=Label(frame, text="Get Started", font=("times new roman", 20,"bold"),fg="white",bg="black")
        get_start.place(x=95,y=100)

        #label
        username = lbl=Label(frame, text="Username",font=('times new roman', 15, 'bold'),fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser=ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)
         
        password = lbl=Label(frame, text="Password",font=('times new roman', 15, 'bold'),fg="white", bg="black")
        password.place(x=70, y=255)

        self.txtpass=ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=280, width=270)

        #------------------------------User_logo--------------------------
        img2=Image.open(r"C:\Users\DELL\Desktop\Login page\images\username.png")
        img2=img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black", borderwidth=0)
        lblimg2.place(x=560,y=323,width=25, height=25)
         
        img3=Image.open(r"C:\Users\DELL\Desktop\Login page\images\lock.png")
        img3=img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black", borderwidth=0)
        lblimg3.place(x=560,y=425,width=25, height=25)
         
        #login button
        login_btn=Button(frame,text="Login",command=self.login, font=("times new roman", 15, "bold"),bd=3, relief=RIDGE, fg="white", bg="dodgerblue3", activeforeground="white", activebackground="dodgerblue3")
        login_btn.place(x=110, y=350, width=120, height=35)

        #forgot password
        forgot_btn=Button(frame,text="Forgot Password",command=self.forgot_pass_win,font=("times new roman", 10, "bold"),bd=3, relief=RIDGE, borderwidth=0,fg="white", bg="black", activeforeground="white", activebackground="black")
        forgot_btn.place(x=30, y=310, width=120)


        #register button
        register_btn=Button(frame,text="Register",command=self.register_win ,font=("times new roman", 13, "bold"),bd=3, relief=RIDGE ,fg="white", bg="dodger blue3", activeforeground="white", activebackground="dodger blue3")
        register_btn.place(x=110, y=400, width=120)

    def register_win(self):
        self.new_win=Toplevel(self.root)
        self.app=Register(self.new_win)



        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field are required")
        elif self.txtuser.get()=="" and self.txtpass.get()=="":
            messagebox.showinfo("Success", "Welcome to My Portfolio")
        else:
            con=mysql.connector.connect(host="",user="",password="",database="")
            cur=con.cursor()
            cur.execute("select * from register where email=%s and password=%s", (
                                                                                    self.var_email.get(),
                                                                                    self.var_pass.get()
                                                                                ))
           
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("YesNo", "Access Only admin")
                
                if open_main>0:
                    self.new_win=Toplevel(self.new_win)
                    # self.app=
                else:
                    if not open_main:
                        return 
            con.commit()
            con.close()

    #-------------------------------------reset_Password-----------------------------------
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error", "Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the New Password",parent=self.root2)
        else:
            con=mysql.connector.connect(host="",user="",password="",database="")
            cur=con.cursor()
            query=("select * from register where email=%s and securityQ =%s and securityA=%s")
            value=(self.txtuser.get(), self.combo_security_Q.get(),self.txt_security.get())
            cur.execute(query, value)
            row=cur.fetchone()
            if row ==None:
                messagebox.showerror("Error", "Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                cur.execute(query, value)

                con.commit()
                con.close()
                messagebox.showinfo("Info", "Your password has been reset successfully, please login with your new password", parent=self.root2)
                self.root2.destroy()

     #-----------------------------------Forgot_Password-----------------------------------------------------------------------------------       
    def forgot_pass_win(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the your email address to reset password")
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="Motot@1234",database="mydata")
            cur=con.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            cur.execute(query,value)
            row=cur.fetchone()

            if row==None:
                messagebox.showerror("My Error", "Please enter a valid user name")
            else:
                con.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")


                l=Label(self.root2, text="Forget Password",font=("times new roman", 20, "bold"),fg="purple", bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2, text="Select Security Question: ", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["value"]=("Select","Your Birth Place","Your Childhood School Name","Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer: ", font=("times new roman",15,"bold"), bg="white", fg="black")
                security_A.place(x=50, y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman", 15,"bold"))
                self.txt_security.place(x=50, y=180, width=250)

                new_pass=Label(self.root2,text="New Password", font=("times new roman",15,"bold"), bg="white", fg="black")
                new_pass.place(x=50, y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman", 15,"bold"))
                self.txt_newpass.place(x=50, y=250, width=250)

                # conf_new_pass=Label(self.root2,text="Confirm New Password", font=("times new roman",15,"bold"), bg="white", fg="black")
                # conf_new_pass.place(x=50, y=300)

                # self.txt_connewpass=ttk.Entry(self.root2,font=("times new roman", 15,"bold"))
                # self.txt_connewpass.place(x=50, y=330, width=250)

                btn=Button(self.root2, text="Reset", font=("times new roman",15, "bold"),fg="white", bg="green")
                btn.place(x=120, y=380)

class Register:
    def __init__(self, root): 
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


#-------------------VARIABLES------------------------------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        
#----------------------BG IMAGE-----------------------------------
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\DELL\Desktop\Login page\images\IMG_20200401_065037 (3).jpg")
        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\DELL\Desktop\Login page\images\loginbg.jpeg")
        left_lbl=Label(self.root, image=self.bg1)
        left_lbl.place(x=150, y=100, width=400,height=500)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100, width=670,height=500)

        register_lbl=Label(frame,text="Register Here", font=("times new roman", 20,"bold"),fg="darkgreen", bg="white")
        register_lbl.place(x=20,y=20)

        fname=Label(frame,text="First Name: ", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        lname=Label(frame, text="Last Name: ",font=("times new roman", 15, "bold"),bg="white", fg="black")
        lname.place(x=370, y=100)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman", 15,"bold"))
        self.lname_entry.place(x=370, y=130,width=250)


        contact=Label(frame, text="Contact No: ",font=("times new roman", 15,"bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman", 15))
        self.txt_contact.place(x=50,y=200, width=250)


        email = Label(frame,text ="Email: " ,font=("times new roman", 15,"bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        security_Q=Label(frame, text="Select Security Question: ", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["value"]=("Select","Your Birth Place","Your Childhood School Name","Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer: ", font=("times new roman",15,"bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA ,font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)


        pswd=Label(frame, text="Password-", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass ,font=("times new roman", 15))
        self.txt_pswd.place(x=50,y=340, width=250)

        confirm_pswd= Label(frame, text="Confirm Password-", font=("times new roman", 15,"bold"),bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass ,font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370,y=340, width=250)
        
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check ,text="I Agree The Terms & Conditions!", font=("times new roman", 12,"bold"),onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=400)

        register_btn=Button(frame,text="Register Now",command=self.register_data,font=("times new roman", 13, "bold"),bd=3, relief=RIDGE ,fg="white", bg="lightsalmon", activeforeground="white", activebackground="salmon")
        register_btn.place(x=415, y=415, width=120)


    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error", "All Fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Pass & Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error", "Please agree to our Terms and Conditions")
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="Motot@1234",database="mydata")
            cur=con.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            cur.execute(query, value)
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email already in use, please try anither email or login")
            else:
                cur.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get()

                                                                                ))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Registration Succecssful")


 




if __name__=="__main__":
    main_win()