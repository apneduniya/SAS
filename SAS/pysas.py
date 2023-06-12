
import csv
import datetime
import os
import secrets
import smtplib
import string
import time
import tkinter.messagebox as tmsg
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter import Button
import matplotlib.pyplot as plt
import pandas as pd
from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage
root = Tk()
root.title("SAS STORE")
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-10+0')
otp = ''.join(secrets.choice(string.digits) for _ in range(6))
root.resizable(False, False)
root.config(bg="white")
frame1 = Frame(root, bg="white")
frame2 = Frame(root, bg="white", bd=0)
products_frame = Frame(root, bg="white", bd=0)
search_frame = Frame(root, bg="#EAEAEA", bd=0)
cart_frame = Frame(root, bg="white", bd=0)
frame3 = Frame(root, bg="white", bd=0)
frame4 = Frame(root, bg="white", bd=0)
frame5 = Frame(root, bg="white", bd=0)
frame6 = Frame(root, bg="white", bd=0)
frame7 = Frame(root, bg="white", bd=0, height=1200, width=900)
frame8 = Frame(root, bg="white", bd=0)
frame9 = Frame(root, bg="white", bd=0)
frame10 = Frame(root, bg="white", bd=0)
about_frame = Frame(root, bg="white", bd=0)
frame1.pack(fill=X, anchor=N)
frame2.pack(side='left', anchor='nw', fill=BOTH, expand=True)
products_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
products_frame.forget()
search_frame.pack(fill=BOTH, expand=True)
search_frame.forget()
cart_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
cart_frame.forget()
frame3.pack(side='left', anchor='nw', fill=BOTH, expand=True)
frame3.forget()
frame4.pack(anchor=W)
frame4.forget()
frame5.pack(anchor=W)
frame5.forget()
frame6.pack(anchor=W)
frame6.forget()
frame7.pack(anchor=W)
frame7.forget()
frame8.pack(anchor=W)
frame8.forget()
frame9.pack(anchor=W)
frame9.forget()
frame10.pack(anchor=W)
frame10.forget()
about_frame.pack(anchor=W)
about_frame.forget()
admin_login_frame = Frame(root, bg="white", bd=0)
admin_frame = Frame(root, bg='white', bd=0)
admin_products_frame = Frame(root, bg='white', bd=0)
admin_users_frame = Frame(root, bg='white', bd=0)
admin_orders_frame = Frame(root, bg='white', bd=0)
admin_feedback_frame = Frame(root, bg='white', bd=0)
admin_change_password_frame = Frame(root, bg='white', bd=0)
admin_login_frame.pack(anchor=W)
admin_login_frame.forget()
admin_frame.pack(side=LEFT, anchor=NW)
admin_frame.forget()
admin_products_frame.pack(side=LEFT, anchor=NW)
admin_products_frame.forget()
admin_users_frame.pack(side=LEFT, anchor=NW)
admin_users_frame.forget()
admin_orders_frame.pack(side=LEFT, anchor=NW)
admin_orders_frame.forget()
admin_feedback_frame.pack(side=LEFT, anchor=NW)
admin_feedback_frame.forget()
admin_change_password_frame.pack(side=LEFT, anchor=NW)
admin_change_password_frame.forget()
def image(location, n1, n2):
    search_image = Image.open(location)
    search_image = search_image.resize((int(n1), int(n2)), Image.Resampling.LANCZOS)
    search_image = ImageTk.PhotoImage(search_image)
    return search_image
def csv_write(location, mode, information):
    with open(location, mode, newline='') as csv_file:
        csv_writer_var = csv.writer(csv_file)
        csv_writer_var.writerow(information)
    csv_file.close()
def csv_read(location):
    with open(location, 'r+') as csv_file:
        csv_reader_var = csv.reader(csv_file)
        df = pd.DataFrame(csv_reader_var)
    csv_file.close()
    return df
def restore(widget_name):
    widget_name.pack(anchor=W)
def send_mail(subject, user_email, text):
    message = MIMEMultipart()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('pythoncsvproject@gmail.com', 'vaydiqkckumbvmof')
    message['Subject'] = subject
    message['From'] = 'pythoncsvproject@gmail.com'
    message['To'] = user_email
    message.attach(MIMEText(text, 'plain'))
    server.sendmail('pythoncsvproject@gmail.com', user_email, message.as_string())
    server.quit()
def otp_verification(otp, otp_to_verify, location, user_info, code, type):
    print(f"{otp}\n{otp_to_verify}")
    if int(otp) == int(otp_to_verify):
        if type == "user":
            csv_write(location, 'a+', user_info)
            df = csv_read(location)
            for d in df.index:
                x = list(df.loc[d])
                if code == x[7]:
                    csv_write(r'login.csv', 'w+', [d, str(x[9])])
                    email = x[3]
                    send_mail("Thank you for making SAS account", email, "Dear {name}, your SAS account has been created successfully.Now you can add cash in your SAS wallet.\n\nUser Id : {i}\nContact : +91 {contact}\nEmail ID : {email}\nAddress : {address}\nPincode : {pincode}\nDate and time of making account : {date} {time}\n\nThank you for choosing us.".format(name=str(x[0]), contact=str(x[2]), email=str(x[3]), address=str(x[4]), pincode=str(x[5]), date=str(x[10]), time=str(x[11]), i=str(d)))
                    tmsg.showinfo("Verified Successfully",  f"You have been verified successfully. Your User ID is {d}. For more details see your Email Inbox. ")
                    home_function()
    else:
        tmsg.showinfo("Error", "     You have entered wrong otp!     ")
def home_function():
    frame1.forget()
    frame2.forget()
    products_frame.forget()
    frame3.forget()
    frame4.forget()
    frame5.forget()
    frame6.forget()
    frame7.forget()
    frame8.forget()
    frame9.forget()
    frame1.pack(fill=X, anchor=N)
    frame2.pack(side='left', anchor='nw', fill=BOTH, expand=True)
    home_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
    home_button['fg'] = 'black'
    products_button['font'] = ("Blogger_Sans-Bold", 10)
    products_button['fg'] = 'grey'
    account_button['font'] = ("Blogger_Sans-Bold", 10)
    account_button['fg'] = 'grey'
    feedback_button['font'] = ("Blogger_Sans-Bold", 10)
    feedback_button['fg'] = 'grey'
    about_button['font'] = ("Blogger_Sans-Bold", 10)
    about_button['fg'] = 'grey'
home_button = Button(frame1, text='Home', bg="white", fg="black", font=("Blogger_Sans-Bold", 10, 'bold'), activebackground="black", activeforeground="white", bd=0, cursor='hand2', command=home_function)
home_button.place(x=759, y=7)
def products_function():
    frame1.forget()
    frame2.forget()
    products_frame.forget()
    frame3.forget()
    frame4.forget()
    frame5.forget()
    frame6.forget()
    frame7.forget()
    frame8.forget()
    frame9.forget()
    products_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
    show_products()
    products_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
    products_button['fg'] = 'black'
    home_button['font'] = ("Blogger_Sans-Bold", 10)
    home_button['fg'] = 'grey'
    account_button['font'] = ("Blogger_Sans-Bold", 10)
    account_button['fg'] = 'grey'
    feedback_button['font'] = ("Blogger_Sans-Bold", 10)
    feedback_button['fg'] = 'grey'
    about_button['font'] = ("Blogger_Sans-Bold", 10)
    about_button['fg'] = 'grey'
products_button = Button(frame1, text='Products', bg="white", fg="grey", font=("Blogger_Sans-Bold", 10), activebackground="black", activeforeground="white", bd=0, cursor='hand2', command=products_function)
products_button.place(x=820, y=7)
def account_function():
    frame1.forget()
    frame2.forget()
    products_frame.forget()
    frame3.forget()
    frame4.forget()
    frame5.forget()
    frame6.forget()
    frame7.forget()
    frame8.forget()
    frame9.forget()
    if os.path.exists(r'login.csv'):
        account(frame2)
        restore(frame8)
    else:
        login(frame2)
        restore(frame6)
    account_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
    account_button['fg'] = 'black'
    home_button['font'] = ("Blogger_Sans-Bold", 10)
    home_button['fg'] = 'grey'
    products_button['font'] = ("Blogger_Sans-Bold", 10)
    products_button['fg'] = 'grey'
    feedback_button['font'] = ("Blogger_Sans-Bold", 10)
    feedback_button['fg'] = 'grey'
    about_button['font'] = ("Blogger_Sans-Bold", 10)
    about_button['fg'] = 'grey'
account_button = Button(frame1, text='Account', bg="white", fg="grey", font=("Blogger_Sans-Bold", 10), activebackground="black", activeforeground="white", bd=0, cursor='hand2', command=account_function)
account_button.place(x=897, y=7)
def feedback_function():
    frame1.forget()
    frame2.forget()
    products_frame.forget()
    frame3.forget()
    frame4.forget()
    frame5.forget()
    frame6.forget()
    frame7.forget()
    frame8.forget()
    frame9.forget()
    feedback()
    restore(frame9)
    feedback_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
    feedback_button['fg'] = 'black'
    home_button['font'] = ("Blogger_Sans-Bold", 10)
    home_button['fg'] = 'grey'
    products_button['font'] = ("Blogger_Sans-Bold", 10)
    products_button['fg'] = 'grey'
    account_button['font'] = ("Blogger_Sans-Bold", 10)
    account_button['fg'] = 'grey'
    about_button['font'] = ("Blogger_Sans-Bold", 10)
    about_button['fg'] = 'grey'
feedback_button = Button(frame1, text='Feedback', bg="white", fg="grey", font=("Blogger_Sans-Bold", 10), activebackground="black", activeforeground="white", bd=0, cursor='hand2', command=feedback_function)
feedback_button.place(x=965, y=7)
def about_function():
    frame1.forget()
    frame2.forget()
    products_frame.forget()
    frame3.forget()
    frame4.forget()
    frame5.forget()
    frame6.forget()
    frame7.forget()
    frame8.forget()
    frame9.forget()
    about_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
    about_button['fg'] = 'black'
    home_button['font'] = ("Blogger_Sans-Bold", 10)
    home_button['fg'] = 'grey'
    products_button['font'] = ("Blogger_Sans-Bold", 10)
    products_button['fg'] = 'grey'
    account_button['font'] = ("Blogger_Sans-Bold", 10)
    account_button['fg'] = 'grey'
    feedback_button['font'] = ("Blogger_Sans-Bold", 10)
    feedback_button['fg'] = 'grey'
    about()
    about_frame.pack(anchor=NW)
about_button = Button(frame1, text='About', bg="white", fg="grey", font=("Blogger_Sans-Bold", 10), activebackground="black", activeforeground="white", bd=0, cursor='hand2', command=about_function)
about_button.place(x=1038, y=7)
Button(frame1, text='S  A  S', bg="white", fg="black", font=("Amaranth-Bold", 15, 'bold'), bd=0, command=home_function, cursor='hand2', activebackground='white', activeforeground='black').pack(side=LEFT, padx=25)
def user():
    Frame(frame1, bg='black', height=7, width=2500).place(x=0, y=34)
    img3 = image(r"images/cart_icon.jpg", 20, 20)
    cart_icon = Button(frame1, image=img3, bd=0, cursor="hand2", command=lambda: [cart(frame2), frame1.forget(), frame2.forget(), products_frame.forget(), frame3.forget(), frame4.forget(), frame5.forget(), frame6.forget(), frame7.forget(), frame8.forget(), frame2.forget(), cart_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)])
    cart_icon.pack(side=RIGHT)
    cart_icon.image = img3
    def on_enter(e):
        search_user.delete(0, END)
        if search_user.get() != 'Search...':
            search_user['fg'] = "black"
    def on_leave(e):
        if search_user.get() == ' ':
            search_user.insert(0, "Search...")
    home_bg_image = image(r'images/home_bg.jpg', 1400, 740)
    home_bg = Label(frame2, bd=0, image=home_bg_image)
    home_bg.place(x=-10, y=0)
    home_bg.image = home_bg_image
    search_img = image(r"images/search_icon.png", 20, 20)
    search_user_frame = Frame(frame2, height=6, width=303, bg="black")
    search_user_frame.place(x=542, y=258)
    search_user = Entry(frame2, fg="grey", bd=0, width=50)
    search_user.place(x=542, y=244)
    search_user.insert(0, "Search...")
    search_user.bind("<FocusIn>", on_enter)
    search_user.bind("<FocusOut>", on_leave)
    def enter(e):
        frame1.forget()
        frame2.forget()
        frame3.pack(side='left', anchor='nw', fill=BOTH, expand=True)
        search(search_user.get())
    search_user.bind("<Return>", enter)
    search_btn = Button(frame2, image=search_img, bd=0, cursor="hand2", command=lambda: [search(search_user.get()), frame1.forget(), frame2.forget(), frame3.pack(side='left', anchor='nw', fill=BOTH, expand=True)])
    search_btn.place(x=859, y=240)
    search_btn.image = search_img
def show_products():
    cart_button = {}
    buy_button = {}
    temp_frame = Frame(products_frame, bg="white", bd=0)
    temp_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
    def return_back():
        frame2.forget()
        products_frame.forget()
        frame3.forget()
        frame4.forget()
        frame5.forget()
        frame6.forget()
        frame7.forget()
        frame8.forget()
        frame9.forget()
        frame10.forget()
        cart_frame.forget()
        frame1.pack(fill=X, anchor=N)
        home_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
        home_button['fg'] = 'black'
        products_button['font'] = ("Blogger_Sans-Bold", 10)
        products_button['fg'] = 'grey'
        account_button['font'] = ("Blogger_Sans-Bold", 10)
        account_button['fg'] = 'grey'
        feedback_button['font'] = ("Blogger_Sans-Bold", 10)
        feedback_button['fg'] = 'grey'
        about_button['font'] = ("Blogger_Sans-Bold", 10)
        about_button['fg'] = 'grey'
        frame2.pack(side='left', anchor='nw', fill=BOTH, expand=True)
        return_icon.destroy()
        temp_frame.destroy()
    user_canvas = Canvas(temp_frame, bg='white')
    scrollbar = Scrollbar(temp_frame, orient='vertical', bg='white', command=user_canvas.yview)
    user_scrollabel_frame = Frame(user_canvas, bg='white')
    user_scrollabel_frame.bind('<Configure>', lambda e: user_canvas.configure(scrollregion=user_canvas.bbox('all')))
    user_canvas.create_window((0, 0), window=user_scrollabel_frame, anchor=NW)
    user_canvas.configure(yscrollcommand=scrollbar.set)
    user_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    img = image(r"images/return_icon.png", 40, 40)
    return_icon = Button(user_scrollabel_frame, image=img, bd=0, cursor="hand2", command=return_back)
    return_icon.place(x=15, y=10)
    return_icon.image = img
    discover_label = Label(user_scrollabel_frame, text="Discover Products", bd=0, bg='white', fg='black', font=('Helvetica bold', 20))
    discover_label.place(x=592, y=114)
    df = csv_read(r'products.csv')
    for temp_row in range(15):
        Label(user_scrollabel_frame, bg='white', bd=0).grid(row=temp_row)
    row = 16
    column = -1
    img = image(r'images/frame_bg.jpg', 300, 300)
    for i in df.index:
        if column == 3:
            column = -1
            row += 1
        column += 1
        product_frame = Frame(user_scrollabel_frame, bg='white', height=600, width=400, bd=0)
        product_frame.grid(row=row, column=column)
        product_label = Label(product_frame, image=img, bd=0)
        product_label.pack(fill=BOTH, expand=True)
        product_label.image = img
        def buy_action(buy_product=i):
            buy(buy_product)
            products_frame.forget()
            temp_frame.destroy()
            restore(frame5)
        def cart_action(cart_product=i):
            csv_write(r'cart.csv', 'a+', str(cart_product))
        x = list(df.loc[i])
        product_id = StringVar()
        product_name = StringVar()
        product_cost = StringVar()
        product_details = StringVar()
        product_stock = StringVar()
        product_id.set(f'{i}')
        product_name.set(f'{x[0]}')
        product_cost.set(f'₹ {x[1]}')
        product_details.set(f'{x[2]}')
        product_stock.set(f'Product stock : {x[3]}      ')
        product_img = image(r'{}'.format(str(x[4])), 132, 132)
        product_image = Label(product_frame, image=product_img, bd=0)
        product_image.place(anchor=NW, x=85, y=10)
        product_image.image = product_img
        Label(product_frame, textvariable=product_cost, bg='white', font=('Amaranth-Bold', 15, 'bold')).place(anchor=W, x=127, y=157)
        Label(product_frame, textvariable=product_name, bg='white', fg='black', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=42, y=180)
        Label(product_frame, textvariable=product_details, bg='white', fg='#777777',font=('Amaranth-Regular', 8)).place(anchor=W, x=42, y=205)
        img2 = image(r'images/add_to_cart_icon.png', 108, 36)
        if int(x[3]) > 0:
            cart_button[i] = Button(product_frame, image=img2,
                                    cursor="hand2", bd=0, command=cart_action)
            cart_button[i].place(anchor=NW, x=32, y=228)
            cart_button[i].image = img2
            cart_df = csv_read(r'cart.csv')
            for item in cart_df.index:
                cart_list = list(cart_df.loc[item])
                if int(product_id.get()) == int(cart_list[0]):
                    cart_button[i]['state'] = DISABLED
                    cart_button[i]['cursor'] = ''
                else:
                    pass
            img3 = image(r'images/buy_icon.png', 108, 34)
            buy_button[i] = Button(product_frame, image=img3, cursor="hand2", bd=0, command=buy_action)
            buy_button[i].place(anchor=NW, x=156, y=230)
            buy_button[i].image = img3
        else:
            cart_button[i] = Button(product_frame, image=img2, cursor="hand2", bd=0, command=cart_action)
            cart_button[i].place(anchor=NW, x=32, y=228)
            cart_button[i].image = img2
            cart_df = csv_read(r'cart.csv')
            for item in cart_df.index:
                cart_list = list(cart_df.loc[item])
                if int(product_id.get()) == int(cart_list[0]):
                    cart_button[i]['state'] = DISABLED
                    cart_button[i]['cursor'] = ''
                else:
                    pass
                Label(product_frame, text="Product \nUnavailable", width=10, bg='#D8D8D8', fg='grey').place(anchor=NW, x=166, y=230)
def feedback():
    feedback_bg = image(r'images/login_bg.jpg', 1400, 850)
    feedback_bg_label = Label(frame9, image=feedback_bg, bd=0)
    feedback_bg_label.place(x=-10, y=-10)
    feedback_bg_label.image = feedback_bg
    feedback_frame = Frame(frame9, highlightthickness=5, highlightbackground='black', bg='white')
    feedback_frame.pack(padx=450, pady=40)
    def return_back():
        frame2.forget()
        products_frame.forget()
        frame3.forget()
        frame4.forget()
        frame5.forget()
        frame6.forget()
        frame7.forget()
        frame8.forget()
        frame9.forget()
        frame1.pack(fill=X, anchor=N)
        home_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
        home_button['fg'] = 'black'
        products_button['font'] = ("Blogger_Sans-Bold", 10)
        products_button['fg'] = 'grey'
        account_button['font'] = ("Blogger_Sans-Bold", 10)
        account_button['fg'] = 'grey'
        feedback_button['font'] = ("Blogger_Sans-Bold", 10)
        feedback_button['fg'] = 'grey'
        about_button['font'] = ("Blogger_Sans-Bold", 10)
        about_button['fg'] = 'grey'
        frame2.pack(side='left', anchor='nw', fill=BOTH, expand=True)
        return_icon.destroy()
        feedback_bg_label.destroy()
        feedback_frame.destroy()
    img = image(r"images/return_icon.png", 40, 40)
    return_icon = Button(frame9, image=img, bd=0, cursor="hand2", command=return_back)
    return_icon.place(x=10, y=10)
    return_icon.image = img
    feedback_label = Label(feedback_frame, text="FEEDBACK", bd=0, bg='white', fg='black', font=('Helvetica bold', 20))
    feedback_label.pack(padx=145, pady=50, side=TOP)
    def on_enter_e1(e):
        if str(e1.get()) == 'Type your name':
            e1.delete(0, END)
    def on_leave_e1(e):
        if str(e1.get()) == '':
            e1.insert(0, 'Type your name')
    def on_return_e1(e):
        if str(e1.get()) == 'Type your name' or str(e1.get()) == '':
            tmsg.showerror('Error', '   Please enter your name !   ')
            e1.focus_set()
        else:
            e2.focus_set()
    def on_enter_e2(e):
        if str(e2.get()) == 'Type your email id':
            e2.delete(0, END)
    def on_leave_e2(e):
        if str(e2.get()) == '':
            e2.insert(0, 'Type your email id')
    def on_return_e2(e):
        if str(e2.get()) == 'Type your email id' or str(e2.get()) == '':
            tmsg.showerror('Error', '   Please enter your email id !   ')
            e2.focus_set()
        else:
            d1.focus_set()
    name_label = Label(feedback_frame, bd=0, text='Name', bg='white', fg='grey')
    name_label.place(x=90, y=127)
    e1 = Entry(feedback_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    e1.pack(padx=110, pady=20)
    e1.insert(0, 'Type your name')
    e1.bind('<FocusIn>', on_enter_e1)
    e1.bind('<FocusOut>', on_leave_e1)
    e1.bind('<Return>', on_return_e1)
    Frame(feedback_frame, width=259, height=3, bg='black', bd=0).place(x=90, y=170)
    email_id_label = Label(feedback_frame, bd=0, text='Email Id', bg='white', fg='grey')
    email_id_label.place(x=90, y=190)
    e2 = Entry(feedback_frame, borderwidth=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    e2.pack(padx=110, pady=20)
    e2.insert(0, 'Type your email id')
    e2.bind('<FocusIn>', on_enter_e2)
    e2.bind('<FocusOut>', on_leave_e2)
    e2.bind('<Return>', on_return_e2)
    Frame(feedback_frame, width=259, height=3, bg='black', bd=0).place(x=90, y=227)
    feedback_type = StringVar()
    feedback_type.set(value="Issue")
    Radiobutton(feedback_frame, variable=feedback_type, value='Issue', text='Issue', bd=0, bg='white', fg='black', cursor='hand2').place(x=90, y=247)
    Radiobutton(feedback_frame, variable=feedback_type, value='Suggestion', text='Suggestion', bd=0, bg='white', fg='black', cursor='hand2').place(x=180, y=247)
    def on_enter_d1(e):
        if d1.get(1.0, 'end-1c') == "Describe your issue you've encountered here \nTell us how you'd like to improve SAS":
            d1.delete(1.0, END)
    def on_leave_d1(e):
        if d1.get(1.0, END) == '\n':
            d1.insert(1.0, "Describe your issue you've encountered here \nTell us how you'd like to improve SAS")
    d1 = Text(feedback_frame, bg='white', bd=2, fg='grey', height=12, width=35, wrap=WORD)
    d1.place(x=80, y=287)
    d1.insert(1.0, "Describe your issue you've encountered here \nTell us how you'd like to improve SAS")
    d1.bind('<FocusIn>', on_enter_d1)
    d1.bind('<FocusOut>', on_leave_d1)
    d1.bind('<Return>', lambda e: [feedback_submit(str(e1.get()), str(e2.get()), str(feedback_type.get()), str(d1.get(1.0, 'end-1c')))])
    def feedback_submit(name, email_id, type, description):
        if name == 'Type your name' or name == '':
            tmsg.showerror('Error', '   Please enter your name !   ')
            e1.focus_set()
        elif email_id == 'Type your email id' or email_id == '':
            tmsg.showerror('Error', '   Please enter your email id !   ')
            e2.focus_set()
        elif description == "Describe your issue you've encountered here \nTell us how you'd like to improve SAS" or description == '':
            tmsg.showerror('Error', '   Please enter your report !   ')
            d1.focus_set()
        else:
            now = datetime.datetime.now()
            feedback_date = str(now.strftime("%d-%m-%y"))
            feedback_time = str(now.strftime("%H:%M:%S"))
            csv_write(r'feedback.csv', 'a+', [name, email_id, type, description, feedback_date, feedback_time])
            tmsg.showinfo('Successful', '  Report has been sent.  ')
            return_back()
    feedback_submit_frame = Frame(feedback_frame, highlightthickness=3, highlightbackground='black')
    feedback_submit_frame.place(x=140, y=500)
    b1 = Button(feedback_submit_frame, text='        S U B M I T        ', bg='black', fg='white', font=('Blogger_Sans-Bold', 10, 'bold'), activebackground='white', activeforeground='black', bd=0, cursor='hand2', command=lambda: [feedback_submit(str(e1.get()), str(e2.get()), str(feedback_type.get()), str(d1.get(1.0, 'end-1c')))])
    b1.pack()
    Label(feedback_frame).pack(padx=600, pady=600)
def about():
    about_bg = image(r'images/login_bg.jpg', 1400, 850)
    about_bg_label = Label(about_frame, image=about_bg, bd=0)
    about_bg_label.place(x=-10, y=-10)
    about_bg_label.image = about_bg
    admin_temp_login_frame = Frame(about_frame, highlightthickness=5, highlightbackground='black', bg='white')
    admin_temp_login_frame.pack(padx=450, pady=40)
    def return_back():
        frame2.forget()
        products_frame.forget()
        frame3.forget()
        frame4.forget()
        frame5.forget()
        frame6.forget()
        frame7.forget()
        frame8.forget()
        admin_frame.forget()
        about_frame.forget()
        frame1.pack(fill=X, anchor=N)
        home_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
        home_button['fg'] = 'black'
        products_button['font'] = ("Blogger_Sans-Bold", 10)
        products_button['fg'] = 'grey'
        account_button['font'] = ("Blogger_Sans-Bold", 10)
        account_button['fg'] = 'grey'
        feedback_button['font'] = ("Blogger_Sans-Bold", 10)
        feedback_button['fg'] = 'grey'
        about_button['font'] = ("Blogger_Sans-Bold", 10)
        about_button['fg'] = 'grey'
        frame2.pack(side='left', anchor='nw', fill=BOTH, expand=True)
        return_icon.destroy()
        about_bg_label.destroy()
        admin_temp_login_frame.destroy()
    img = image(r"images/return_icon.png", 40, 40)
    return_icon = Button(about_frame, image=img, bd=0, cursor="hand2", command=return_back)
    return_icon.place(x=10, y=10)
    return_icon.image = img
    about_label = Label(admin_temp_login_frame, text="A B O U T", bd=0, bg='white', fg='black', font=('Helvetica bold', 20))
    about_label.pack(padx=165, pady=50, side=TOP)
    Label(admin_temp_login_frame).pack(padx=600, pady=400)
    Label(admin_temp_login_frame, bg='white', fg='black', bd=0, font=('Blogger_Sans', 10, 'italic'), text="SAS Stores is a general purpose stationary shop locate in Kolkata, \nWest Bengal. We provide a widerange of stationary items through our \nvast array of stationary supplies. We've partnered with major and \nreputable suppliers and manufacturers to ensure that only the best \nsupplies are sold. This has improved our brand and made \nus a trusted name in the Kolkata area.\n").place(x=28, y=140)
    Label(admin_temp_login_frame, bg='white', fg='black', bd=0, font=('Blogger_Sans', 10, 'bold'), text="Founder : Adarsh").place(x=28, y=260)
    Label(admin_temp_login_frame, bg='white', fg='black', bd=0, font=('Blogger_Sans', 10, 'bold'), text="Co - Founders: Saptarshi & Soumyadeep").place(x=28, y=300)
def cart(previous_frame):
    buy_button = {}
    temp_frame = Frame(cart_frame, bd=0, bg='white')
    temp_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
    frame_img = image(r'images/frame_bg.jpg', 300, 300)
    def return_back():
        frame2.forget()
        products_frame.forget()
        frame3.forget()
        frame4.forget()
        frame5.forget()
        frame6.forget()
        frame7.forget()
        frame8.forget()
        cart_frame.forget()
        frame1.pack(fill=X, anchor=N)
        home_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
        home_button['fg'] = 'black'
        products_button['font'] = ("Blogger_Sans-Bold", 10)
        products_button['fg'] = 'grey'
        account_button['font'] = ("Blogger_Sans-Bold", 10)
        account_button['fg'] = 'grey'
        feedback_button['font'] = ("Blogger_Sans-Bold", 10)
        feedback_button['fg'] = 'grey'
        about_button['font'] = ("Blogger_Sans-Bold", 10)
        about_button['fg'] = 'grey'
        previous_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
        return_icon.destroy()
        my_cart_label.destroy()
        temp_frame.destroy()
    user_canvas = Canvas(temp_frame, bg='white')
    scrollbar = Scrollbar(temp_frame, orient='vertical', bg='white', command=user_canvas.yview)
    user_scrollabel_frame = Frame(user_canvas, bg='white')
    user_scrollabel_frame.bind('<Configure>', lambda e: user_canvas.configure(scrollregion=user_canvas.bbox('all')))
    user_canvas.create_window((0, 0), window=user_scrollabel_frame, anchor=NW)
    user_canvas.configure(yscrollcommand=scrollbar.set)
    user_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    img = image(r"images/return_icon.png", 40, 40)
    return_icon = Button(user_scrollabel_frame, image=img, bd=0, cursor="hand2", command=return_back)
    return_icon.place(x=10, y=15)
    return_icon.image = img
    my_cart_label = Label(user_scrollabel_frame, text="My Cart", bd=0, bg='white', fg='black', font=('Helvetica bold', 20))
    my_cart_label.place(x=592, y=114)
    product_df = csv_read(r'products.csv')
    cart_df = csv_read(r'cart.csv')
    for temp_row in range(15):
        Label(user_scrollabel_frame, bg='white', bd=0).grid(row=temp_row)
    row = 16
    column = -1
    for i in product_df.index:
        for j in cart_df.index:
            cart_list = list(cart_df.loc[j])
            if int(cart_list[0]) == i:
                if column == 3:
                    column = -1
                    row += 1
                column += 1
                def buy_action(x=i):
                    buy(x)
                    cart_frame.forget()
                    return_icon.destroy()
                    my_cart_label.destroy()
                    temp_frame.destroy()
                    restore(frame5)
                product_list = list(product_df.loc[i])
                product_id = StringVar()
                product_name = StringVar()
                product_cost = StringVar()
                product_details = StringVar()
                product_stock = StringVar()
                product_id.set(f'{i}')
                product_name.set(f'{product_list[0]}')
                product_cost.set(f'₹ {product_list[1]}')
                product_details.set(f'{product_list[2]}')
                product_stock.set(f'Product stock : {product_list[3]}      ')
                product_img = image(r'{}'.format(str(product_list[4])), 132, 132)
                product_frame = Frame(user_scrollabel_frame, bg="white", bd=0, height=600, width=400)
                product_frame.grid(row=row, column=column)
                product_label = Label(product_frame, image=frame_img, bd=0)
                product_label.pack(fill=BOTH, expand=True)
                product_label.image = frame_img
                product_image = Label(product_frame, image=product_img, bd=0)
                product_image.place(anchor=NW, x=85, y=10)
                product_image.image = product_img
                Label(product_frame, textvariable=product_cost, bg='white', font=('Amaranth-Bold', 15, 'bold')).place(anchor=W, x=127, y=157)
                Label(product_frame, textvariable=product_name, bg='white', fg='black', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=42, y=180)
                Label(product_frame, textvariable=product_details, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=42, y=205)
                if int(product_list[3]) > 0:
                    img2 = image(r'images/buy_icon.png', 108, 34)
                    buy_button[i] = Button(product_frame, image=img2, cursor="hand2", bd=0, command=buy_action)
                    buy_button[i].place(anchor=NW, x=156, y=230)
                    buy_button[i].image = img2
                else:
                    Label(product_frame, text="Product \nUnavailable", width=10, bg='#D8D8D8', fg='grey').place(anchor=NW, x=166, y=230)
def search(name):
    temp_frame = Frame(frame3, bd=0, bg='white')
    temp_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
    user_canvas = Canvas(temp_frame, bg='white')
    scrollbar = Scrollbar(temp_frame, orient='vertical', bg='white', command=user_canvas.yview)
    user_scrollabel_frame = Frame(user_canvas, bg='white')
    user_scrollabel_frame.bind('<Configure>', lambda e: user_canvas.configure(scrollregion=user_canvas.bbox('all')))
    user_canvas.create_window((0, 0), window=user_scrollabel_frame, anchor=NW)
    user_canvas.configure(yscrollcommand=scrollbar.set)
    user_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    img = image(r"images/return_icon.png", 40, 40)
    return_button = Button(user_scrollabel_frame, image=img, bd=0, cursor="hand2", command=lambda: [frame3.forget(), frame1.pack(anchor=N, fill=X), frame2.pack(side='left', anchor='nw', fill=BOTH, expand=True), return_button.destroy(), search_label.destroy(), temp_frame.destroy()])
    return_button.place(x=15, y=10)
    return_button.image = img
    frame_img = image(r'images/frame_bg.jpg', 300, 300)
    location = r'products.csv'
    df = csv_read(location)
    buy_button = {}
    cart_button = {}
    for temp_row in range(15):
        Label(user_scrollabel_frame, bg='white', bd=0).grid(row=temp_row, column=0)
    row = 16
    column = -1
    for i in df.index:
        x = list(df.loc[i])
        if name.lower() == x[0].lower():
            if column == 3:
                column = -1
                row += 1
            column += 1
            def buy_action(buy_product=i):
                buy(buy_product)
                temp_frame.forget()
                restore(frame5)
                frame3.forget()
            def cart_action(cart_product=i):
                csv_write(r'cart.csv', 'a+', str(cart_product))
            product_id = StringVar()
            product_name = StringVar()
            product_cost = StringVar()
            product_details = StringVar()
            product_stock = StringVar()
            product_id.set(f'{i}')
            product_name.set(f'{x[0]}')
            product_cost.set(f'₹ {x[1]}')
            product_details.set(f'{x[2]}')
            product_stock.set(f'Product stock : {x[3]}      ')
            product_img = image(r'{}'.format(str(x[4])), 132, 132)
            product_frame = Frame(user_scrollabel_frame, bg="white", bd=0, height=600, width=400)
            product_frame.grid(row=row, column=column)
            product_label = Label(product_frame, image=frame_img, bd=0)
            product_label.pack(fill=BOTH, expand=True)
            product_label.image = frame_img
            product_image = Label(product_frame, image=product_img, bd=0)
            product_image.place(anchor=NW, x=85, y=10)
            product_image.image = product_img
            Label(product_frame, textvariable=product_cost, bg='white', font=('Amaranth-Bold', 15, 'bold')).place(anchor=W, x=127, y=157)
            Label(product_frame, textvariable=product_name, bg='white', fg='black', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=42, y=180)
            Label(product_frame, textvariable=product_details, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=42, y=205)
            img2 = image(r'images/add_to_cart_icon.png', 108, 36)
            if int(x[3]) > 0:
                cart_button[i] = Button(product_frame, image=img2, cursor="hand2", bd=0, command=cart_action)
                cart_button[i].place(anchor=NW, x=32, y=228)
                cart_button[i].image = img2
                cart_df = csv_read(r'cart.csv')
                for item in cart_df.index:
                    cart_list = list(cart_df.loc[item])
                    if int(product_id.get()) == int(cart_list[0]):
                        cart_button[i]['state'] = DISABLED
                        cart_button[i]['cursor'] = ''
                    else:
                        pass
                img3 = image(r'images/buy_icon.png', 108, 34)
                buy_button[i] = Button(product_frame, image=img3, cursor="hand2", bd=0, command=buy_action)
                buy_button[i].place(anchor=NW, x=156, y=230)
                buy_button[i].image = img3
            else:
                cart_button[i] = Button(product_frame, image=img2, cursor="hand2", bd=0, command=cart_action)
                cart_button[i].place(anchor=NW, x=32, y=228)
                cart_button[i].image = img2
                cart_df = csv_read(r'cart.csv')
                for item in cart_df.index:
                    cart_list = list(cart_df.loc[item])
                    if int(product_id.get()) == int(cart_list[0]):
                        cart_button[i]['state'] = DISABLED
                        cart_button[i]['cursor'] = ''
                    else:
                        pass
                Label(product_frame, text="Product \nUnavailable", width=10, bg='#D8D8D8', fg='grey').place(anchor=NW, x=166, y=230)
def register():
    register_bg = image(r'images/login_bg.jpg', 1400, 850)
    register_bg_label = Label(frame4, image=register_bg, bd=0)
    register_bg_label.place(x=-10, y=-10)
    register_bg_label.image = register_bg
    register_frame = Frame(frame4, highlightthickness=5, highlightbackground='black', bg='white')
    register_frame.pack(padx=450, pady=40)
    def return_back():
        frame1.forget()
        frame2.forget()
        products_frame.forget()
        frame3.forget()
        frame4.forget()
        frame5.forget()
        frame6.forget()
        frame7.forget()
        frame8.forget()
        home_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
        home_button['fg'] = 'black'
        products_button['font'] = ("Blogger_Sans-Bold", 10)
        products_button['fg'] = 'grey'
        account_button['font'] = ("Blogger_Sans-Bold", 10)
        account_button['fg'] = 'grey'
        feedback_button['font'] = ("Blogger_Sans-Bold", 10)
        feedback_button['fg'] = 'grey'
        about_button['font'] = ("Blogger_Sans-Bold", 10)
        about_button['fg'] = 'grey'
        restore(frame6)
        return_icon.destroy()
        register_bg_label.destroy()
        register_frame.destroy()
    img = image(r"images/return_icon.png", 40, 40)
    return_icon = Button(frame4, image=img, bd=0, cursor="hand2", command=return_back)
    return_icon.place(x=10, y=10)
    return_icon.image = img
    register_frame.pack(padx=450, pady=40)
    register_label = Label(register_frame, text="REGISTER", bd=0, bg='white', fg='black', font=('Helvetica bold', 20))
    register_label.pack(padx=95, pady=50, side=TOP)
    Label(register_frame).pack(padx=600, pady=600)
    def on_enter_user_name(e):
        if str(user_name.get()) == 'Type your name':
            user_name.delete(0, END)
    def on_leave_user_name(e):
        if str(user_name.get()) == '':
            user_name.insert(0, 'Type your name')
    def on_return_user_name(e):
        if str(user_name.get()) == 'Type your name' or str(user_name.get()) == '':
            tmsg.showerror('Error', '   Please enter your name !   ')
            user_name.focus_set()
        else:
            user_age.focus_set()
    def on_enter_user_age(e):
        if str(user_age.get()) == 'Type your age':
            user_age.delete(0, END)
    def on_leave_user_age(e):
        if str(user_age.get()) == '':
            user_age.insert(0, 'Type your age')
    def on_return_user_age(e):
        if str(user_age.get()) == 'Type your age' or str(user_age.get()) == '':
            tmsg.showerror('Error', '   Please enter your age !   ')
            user_age.focus_set()
        else:
            user_contact.focus_set()
    def on_enter_user_contact(e):
        if str(user_contact.get()) == 'Type your phone number':
            user_contact.delete(0, END)
    def on_leave_user_contact(e):
        if str(user_contact.get()) == '':
            user_contact.insert(0, 'Type your phone number')
    def on_return_user_contact(e):
        if str(user_contact.get()) == 'Type your phone number' or str(user_contact.get()) == '':
            tmsg.showerror('Error', '   Please enter your phone number !   ')
            user_contact.focus_set()
        else:
            user_email.focus_set()
    def on_enter_user_email(e):
        if str(user_email.get()) == 'Type your email id':
            user_email.delete(0, END)
    def on_leave_user_email(e):
        if str(user_email.get()) == '':
            user_email.insert(0, 'Type your email id')
    def on_return_user_email(e):
        if str(user_email.get()) == 'Type your email id' or str(user_email.get()) == '':
            tmsg.showerror('Error', '   Please enter your email id !   ')
            user_email.focus_set()
        else:
            user_address.focus_set()
    def on_enter_user_address(e):
        if str(user_address.get()) == 'Type your address':
            user_address.delete(0, END)
    def on_leave_user_address(e):
        if str(user_address.get()) == '':
            user_address.insert(0, 'Type your address')
    def on_return_user_address(e):
        if str(user_address.get()) == 'Type your address' or str(user_address.get()) == '':
            tmsg.showerror('Error', '   Please enter your address !   ')
            user_address.focus_set()
        else:
            user_pincode.focus_set()
    def on_enter_user_pincode(e):
        if str(user_pincode.get()) == 'Type your pincode':
            user_pincode.delete(0, END)
    def on_leave_user_pincode(e):
        if str(user_pincode.get()) == '':
            user_pincode.insert(0, 'Type your pincode')
    def on_return_user_pincode(e):
        if str(user_pincode.get()) == 'Type your pincode' or str(user_pincode.get()) == '':
            tmsg.showerror('Error', '   Please enter your pincode !   ')
            user_pincode.focus_set()
        else:
            user_identity.focus_set()
    def on_enter_user_identity(e):
        if str(user_identity.get()) == 'Type your aadhar number':
            user_identity.delete(0, END)
    def on_leave_user_identity(e):
        if str(user_identity.get()) == '':
            user_identity.insert(0, 'Type your aadhar number')
    def on_return_user_identity(e):
        if str(user_identity.get()) == 'Type your aadhar number' or str(user_identity.get()) == '':
            tmsg.showerror('Error', '   Please enter your aadhar number !   ')
            user_identity.focus_set()
        else:
            user_password.focus_set()
    def on_enter_user_password(e):
        if str(user_password.get()) == 'Enter your password':
            user_password.delete(0, END)
    def on_leave_user_password(e):
        if str(user_password.get()) == '':
            user_password.insert(0, 'Enter your password')
    def on_enter_user_otp(e):
        if str(user_otp.get()) == 'Type your otp':
            user_otp.delete(0, END)
    def on_leave_user_otp(e):
        if str(user_otp.get()) == '':
            user_otp.insert(0, 'Type your otp')
    name_label = Label(register_frame, bd=0, text='Name', bg='white', fg='grey')
    name_label.place(x=45, y=127)
    user_name = Entry(register_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    user_name.place(x=60, y=154)
    user_name.insert(0, 'Type your name')
    user_name.bind('<FocusIn>', on_enter_user_name)
    user_name.bind('<FocusOut>', on_leave_user_name)
    user_name.bind('<Return>', on_return_user_name)
    Frame(register_frame, width=259, height=3, bg='black', bd=0).place(x=45, y=170)
    age_label = Label(register_frame, bd=0, text='Age', bg='white', fg='grey')
    age_label.place(x=45, y=184)
    user_age = Entry(register_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    user_age.place(x=60, y=211)
    user_age.insert(0, 'Type your age')
    user_age.bind('<FocusIn>', on_enter_user_age)
    user_age.bind('<FocusOut>', on_leave_user_age)
    user_age.bind('<Return>', on_return_user_age)
    Frame(register_frame, width=259, height=3, bg='black', bd=0).place(x=45, y=227)
    contact_label = Label(register_frame, bd=0, text='Contact', bg='white', fg='grey')
    contact_label.place(x=45, y=241)
    user_contact = Entry(register_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    user_contact.place(x=60, y=268)
    user_contact.insert(0, 'Type your phone number')
    user_contact.bind('<FocusIn>', on_enter_user_contact)
    user_contact.bind('<FocusOut>', on_leave_user_contact)
    user_contact.bind('<Return>', on_return_user_contact)
    Frame(register_frame, width=259, height=3, bg='black', bd=0).place(x=45, y=284)
    email_id_label = Label(register_frame, bd=0, text='Email ID', bg='white', fg='grey')
    email_id_label.place(x=45, y=298)
    user_email = Entry(register_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    user_email.place(x=60, y=325)
    user_email.insert(0, 'Type your email id')
    user_email.bind('<FocusIn>', on_enter_user_email)
    user_email.bind('<FocusOut>', on_leave_user_email)
    user_email.bind('<Return>', on_return_user_email)
    Frame(register_frame, width=259, height=3, bg='black', bd=0).place(x=45, y=341)
    address_label = Label(register_frame, bd=0, text='Address', bg='white', fg='grey')
    address_label.place(x=45, y=355)
    user_address = Entry(register_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    user_address.place(x=60, y=382)
    user_address.insert(0, 'Type your address')
    user_address.bind('<FocusIn>', on_enter_user_address)
    user_address.bind('<FocusOut>', on_leave_user_address)
    user_address.bind('<Return>', on_return_user_address)
    Frame(register_frame, width=259, height=3, bg='black', bd=0).place(x=45, y=398)
    pincode_label = Label(register_frame, bd=0, text='Pincode', bg='white', fg='grey')
    pincode_label.place(x=45, y=412)
    user_pincode = Entry(register_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    user_pincode.place(x=60, y=439)
    user_pincode.insert(0, 'Type your pincode')
    user_pincode.bind('<FocusIn>', on_enter_user_pincode)
    user_pincode.bind('<FocusOut>', on_leave_user_pincode)
    user_pincode.bind('<Return>', on_return_user_pincode)
    Frame(register_frame, width=259, height=3, bg='black', bd=0).place(x=45, y=455)
    identity_label = Label(register_frame, bd=0, text='Aadhar Number', bg='white', fg='grey')
    identity_label.place(x=45, y=469)
    user_identity = Entry(register_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    user_identity.place(x=60, y=496)
    user_identity.insert(0, 'Type your aadhar number')
    user_identity.bind('<FocusIn>', on_enter_user_identity)
    user_identity.bind('<FocusOut>', on_leave_user_identity)
    user_identity.bind('<Return>', on_return_user_identity)
    Frame(register_frame, width=259, height=3, bg='black', bd=0).place(x=45, y=512)
    user_wallet_balance = 0
    password_label = Label(register_frame, bd=0, text='Password', bg='white', fg='grey')
    password_label.place(x=45, y=526)
    user_password = Entry(register_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    user_password.place(x=60, y=553)
    user_password.insert(0, 'Enter your password')
    user_password.bind('<FocusIn>', on_enter_user_password)
    user_password.bind('<FocusOut>', on_leave_user_password)
    user_password.bind('<Return>', lambda e: [otp_function(str(user_name.get()), str(user_age.get()), str(user_contact.get()), str(user_email.get()), str(user_address.get()), str(user_pincode.get()), str(user_identity.get()), str(user_password.get()), str(user_otp.get()), 'get_otp')])
    current_date = datetime.datetime.now().strftime("%d-%m-%y")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    Frame(register_frame, width=259, height=3, bg='black', bd=0).place(x=45, y=569)
    otp_label = Label(register_frame, bd=0, text='O T P', bg='white', fg='grey')
    otp_label.place(x=45, y=583)
    user_otp = Entry(register_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=20)
    user_otp.place(x=60, y=610)
    user_otp.insert(0, 'Type your otp')
    user_otp.bind('<FocusIn>', on_enter_user_otp)
    user_otp.bind('<FocusOut>', on_leave_user_otp)
    user_otp.bind('<Return>', lambda e: [otp_function(str(user_name.get()), str(user_age.get()), str(user_contact.get()), str(user_email.get()), str(user_address.get()), str(user_pincode.get()), str(user_identity.get()), str(user_password.get()), str(user_otp.get()), 'confirm')])
    Frame(register_frame, width=135, height=3, bg='black', bd=0).place(x=45, y=626)
    def otp_function(name, age, contact, email, address, pincode, identity, password, otp_got_from_user, got_for):
        if name == 'Type your name' or name == '':
            tmsg.showerror('Error', '   Please enter your name !   ')
            user_name.focus_set()
        elif age == 'Type your age' or age == '':
            tmsg.showerror('Error', '   Please enter your age !   ')
            user_age.focus_set()
        elif contact == 'Type your phone number' or contact == '':
            tmsg.showerror('Error', '   Please enter your phone number !   ')
            user_contact.focus_set()
        elif email == 'Type your email id' or email == '':
            tmsg.showerror('Error', '   Please enter your email id !   ')
            user_email.focus_set()
        elif address == 'Type your address' or address == '':
            tmsg.showerror('Error', '   Please enter your address !   ')
            user_address.focus_set()
        elif pincode == 'Type your pincode' or pincode == '':
            tmsg.showerror('Error', '   Please enter your pincode !   ')
            user_pincode.focus_set()
        elif identity == 'Type your aadhar number' or identity == '':
            tmsg.showerror('Error', '   Please enter your aadhar number !   ')
            user_identity.focus_set()
        elif password == 'Enter your password' or password == '':
            tmsg.showerror('Error', '   Please enter your password !   ')
            user_password.focus_set()
        else:
            if user_age.get().isdigit():
                if int(user_age.get()) > 17:
                    if user_contact.get().isdigit():
                        if len(user_contact.get()) == 10:
                            if user_pincode.get().isdigit():
                                if len(user_pincode.get()) == 6:
                                    if user_identity.get().isdigit():
                                        if len(user_identity.get()) == 12:
                                            if str(got_for) == 'get_otp':
                                                send_mail("OTP to register for SAS account", str(user_email.get()), f"Your 6-digit otp numer is {otp}. Don't share this otp with anyone.")
                                                tmsg.showinfo('O T P Send Successfully', '    OTP has been send successfully!    ')
                                                user_otp.focus_set()
                                                Button(register_frame, text="                   Register                      ", fg='white', bg='black', bd=0, font=('Blogger_Sans', 14, 'bold'), cursor='hand2', command=lambda: [otp_function(str(user_name.get()), str(user_age.get()), str(user_contact.get()), str(user_email.get()), str(user_address.get()), str(user_pincode.get()), str(user_identity.get()), str(user_password.get()), str(user_otp.get()), 'confirm')]).place(x=95, y=635)
                                            else:
                                                if otp_got_from_user == 'Type your otp' or otp_got_from_user == '':
                                                    tmsg.showerror('Error', '   Please enter your otp !   ')
                                                    user_otp.focus_set()
                                                elif user_otp.get().isdigit():
                                                    otp_verification(otp, user_otp.get(), r'users.csv', [str(user_name.get()), str(user_age.get()), str(user_contact.get()), str(user_email.get()), str(user_address.get()), str(user_pincode.get()), str(user_identity.get()), str(user_contact.get()) + str(user_email.get()) + str(user_identity.get()) + str(current_date) + str(current_time), str(user_wallet_balance), str(user_password.get()), str(current_date), str(current_time)], str(user_contact.get()) + str(user_email.get()) + str(user_identity.get())  + str(current_date) + str(current_time), "user")
                                                else:
                                                    tmsg.showerror('Error', '   O T P must be in numbers   ')
                                                    user_otp.focus_set()
                                        else:
                                            tmsg.showerror('Error', '   Please enter valid aadhar card number (i.e. 12 digit aadhar number)   ')
                                            user_identity.focus_set()
                                    else:
                                        tmsg.showerror('Error', '   Aadhar identity must be in numbers   ')
                                        user_identity.focus_set()
                                else:
                                    tmsg.showerror('Error', '   Please enter valid pincode (i.e. 6 digit pincode)   ')
                                    user_pincode.focus_set()
                            else:
                                tmsg.showerror('Error', '   Pincode must be in numbers   ')
                                user_pincode.focus_set()
                        else:
                            tmsg.showerror('Error', '   Please enter valid phone number (i.e. 10 digit phone number)   ')
                            user_contact.focus_set()
                    else:
                        tmsg.showerror('Error', '   Phone number must be in numbers   ')
                        user_contact.focus_set()
                else:
                    tmsg.showwarning('Error', '   User must be above 18 years   ')
                    user_age.focus_set()
            else:
                tmsg.showerror('Error', '   Age must be in numbers   ')
                user_age.focus_set()
    Button(register_frame, text="                   Get OTP                   ", bd=0, bg="black", fg="white", font=('Blogger_Sans', 14), cursor='hand2', command=lambda: [otp_function(str(user_name.get()), str(user_age.get()), str(user_contact.get()), str(user_email.get()), str(user_address.get()), str(user_pincode.get()), str(user_identity.get()), str(user_password.get()), str(user_otp.get()), 'get_otp')]).place(x=95, y=635)
def buy(product_index):
    if os.path.exists(r'login.csv'):
        frame1.forget()
        buy_bg = image(r'images/buy_bg.jpg', 1400, 850)
        buy_bg_label = Label(frame5, image=buy_bg, bd=0)
        buy_bg_label.place(x=-10, y=-10)
        buy_bg_label.image = buy_bg
        buy_frame = Frame(frame5, highlightthickness=5, highlightbackground='black', bg='white')
        buy_frame.pack(padx=450, pady=40)
        def return_back():
            frame2.forget()
            products_frame.forget()
            frame3.forget()
            frame4.forget()
            frame5.forget()
            frame6.forget()
            frame7.forget()
            frame8.forget()
            frame1.pack(fill=X, anchor=N)
            home_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
            home_button['fg'] = 'black'
            products_button['font'] = ("Blogger_Sans-Bold", 10)
            products_button['fg'] = 'grey'
            account_button['font'] = ("Blogger_Sans-Bold", 10)
            account_button['fg'] = 'grey'
            feedback_button['font'] = ("Blogger_Sans-Bold", 10)
            feedback_button['fg'] = 'grey'
            about_button['font'] = ("Blogger_Sans-Bold", 10)
            about_button['fg'] = 'grey'
            frame2.pack(side='left', anchor='nw', fill=BOTH, expand=True)
            return_icon.destroy()
            buy_bg_label.destroy()
            buy_frame.destroy()
            product_frame.destroy()
        img = image(r"images/return_icon.png", 40, 40)
        return_icon = Button(frame5, image=img, bd=0, cursor="hand2", command=return_back)
        return_icon.place(x=10, y=10)
        return_icon.image = img
        product_frame = Frame(buy_frame, bg='white', height=300, width=400, bd=5)
        product_frame.place(x=10, y=20)
        products_df = csv_read(r'products.csv')
        for i in products_df.index:
            products_list = list(products_df.loc[i])
            if int(product_index) == i:
                if int(products_list[3]) != 0:
                    product_id = StringVar()
                    product_name = StringVar()
                    product_cost = StringVar()
                    product_details = StringVar()
                    product_stock = StringVar()
                    pro_cost = int(products_list[1])
                    pro_stock = int(products_list[3])
                    product_id.set(f'{i}')
                    product_name.set(f'{products_list[0]}')
                    product_cost.set(f'₹ {products_list[1]}')
                    product_details.set(f'{products_list[2]}')
                    product_stock.set(f'{products_list[3]}')
                    product_img = image(r'{}'.format(str(products_list[4])), 132, 132)
                    product_image = Label(product_frame, image=product_img, bd=0)
                    product_image.place(anchor=NW, x=10, y=20)
                    product_image.image = product_img
                    Label(product_frame, textvariable=product_name, bg='white', fg='black', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=155, y=50)
                    Label(product_frame, textvariable=product_cost, bg='white', font=('Amaranth-Bold', 10, 'bold')).place(anchor=W, x=155, y=70)
                    Label(product_frame, textvariable=product_details, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=155, y=90)
                    if int(product_stock.get()) < 100:
                        Label(product_frame, text=f'Hurry! Only {product_stock.get()} pcs are left', bg='white', fg='red', font=('Amaranth-Regular', 10)).place(anchor=W, x=155, y=140)
                    else:
                        pass
                    Label(buy_frame).pack(padx=300, pady=400)
                    def less_qty_function(quantity):
                        if quantity.isdigit():
                            if int(quantity) < int(products_list[3]) or int(quantity) == int(products_list[3]):
                                if int(quantity) > 1:
                                    user_quantity.delete(0, END)
                                    user_quantity.insert(0, f'{int(int(quantity) - 1)}')
                                else:
                                    tmsg.showerror('Error', "   Quantity can't be lesser than 0!    ")
                            else:
                                tmsg.showwarning('Error', f"Quantity must be lower than product's stock i.e. {products_list[3]} pcs")
                        else:
                            tmsg.showerror('Error', '   Quantity must be in number!    ')
                    def add_qty_function(quantity):
                        if quantity.isdigit():
                            if int(quantity) < int(products_list[3]) or int(quantity) == int(products_list[3]):
                                if int(quantity) < 99:
                                    user_quantity.delete(0, END)
                                    user_quantity.insert(0, f'{int(int(quantity) + 1)}')
                                else:
                                    tmsg.showerror('Error', "   Quantity can't be greater than 100!    ")
                            else:
                                tmsg.showwarning('Error', f"Quantity must be lower than product's stock i.e. {products_list[3]} pcs")
                        else:
                            tmsg.showerror('Error', '   Quantity must be in number!    ')
                    Label(buy_frame, text="Quantity", font=("ABeeZee-Regular", 10, 'bold'), fg='black', bg='white').place(x=50, y=190)
                    Button(buy_frame, text='-  ', bg='white', font=('Amaranth-Bold', 14, 'bold'), bd=0, fg='black', command=lambda: [less_qty_function(str(user_quantity.get())), continue_buy(str(user_quantity.get()), pro_stock, pro_cost, 'no')], cursor='hand2').place(x=155, y=180)
                    user_quantity = Entry(buy_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=3)
                    user_quantity.place(x=175, y=190)
                    user_quantity.insert(0, '1')
                    user_quantity.bind('<Configure>', lambda e: [continue_buy(str(user_quantity.get()), pro_stock, pro_cost, 'yes')])
                    Frame(buy_frame, width=20, height=3, bg='black', bd=0).place(x=175, y=205)
                    Button(buy_frame, text=' + ', bg='white', font=('Amaranth-Bold', 12, 'bold'), bd=0, fg='black', command=lambda: [add_qty_function(str(user_quantity.get())), continue_buy(str(user_quantity.get()), pro_stock, pro_cost, 'no')], cursor='hand2').place(x=195, y=184)
                    payment_type = StringVar()
                    payment_type.set("Cash On Delivery")
                    r1 = Radiobutton(buy_frame, text="Pay via SAS ACCOUNT", value="SAS WALLET", variable=payment_type, bd=0, bg='white', fg='black', cursor='hand2')
                    r1.place(x=50, y=224)
                    r2 = Radiobutton(buy_frame, text="Cash On Delivery", value="Cash On Delivery", variable=payment_type, bd=0, bg='white', fg='black', cursor='hand2')
                    r2.place(x=230, y=224)
                    def continue_buy(user_qty, stock, product_price, repeat):
                        if user_qty.isdigit():
                            if int(user_qty) < 1 or int(user_qty) > stock:
                                tmsg.showwarning("Incorrect value", f"Please enter less than or \nequal to {stock} or more than 0.")
                                if repeat == 'yes':
                                    buy_frame.after(2000, lambda: [continue_buy(str(user_quantity.get()), pro_stock, pro_cost, 'yes')])
                                else:
                                    pass
                            else:
                                user_total_price = int(int(user_qty) * product_price)
                                Label(buy_frame, font=("ABeeZee-Regular", 10, 'bold'), fg='black', bg='white', text=f"Total Amount Payable   :       ₹ {user_total_price}\t\t\t").place(x=50, y=264)
                                user_df = csv_read(r'users.csv')
                                login_csv = csv_read(r'login.csv')
                                for user_id_login in login_csv.index:
                                    user_id_list = list(login_csv.loc[user_id_login])
                                    for user_id in user_df.index:
                                        if int(user_id_list[0]) == user_id:
                                            user_list = list(user_df.loc[user_id])
                                            if int(user_list[8]) > user_total_price or int(
                                                    user_list[8]) == user_total_price:
                                                user_name = str(user_list[0])
                                                user_age = str(user_list[1])
                                                user_contact = str(user_list[2])
                                                user_email = str(user_list[3])
                                                user_address = str(user_list[4])
                                                user_pincode = str(user_list[5])
                                                now = datetime.datetime.now()
                                                purchase_date = now.strftime("%d-%m-%y")
                                                purchase_time = now.strftime("%H:%M:%S")
                                                purchase_date = str(purchase_date)
                                                purchase_time = str(purchase_time)
                                                order_code = str(user_email + user_contact + purchase_date + purchase_time)
                                                Label(buy_frame, font=("ABeeZee-Regular", 10, 'bold'), fg='black', bg='white', text=f"SAS Wallet Balance   :          ₹ {int(user_list[8])}\t\t\t").place(x=50, y=294)
                                            else:
                                                user_name = str(user_list[0])
                                                user_age = str(user_list[1])
                                                user_contact = str(user_list[2])
                                                user_email = str(user_list[3])
                                                user_address = str(user_list[4])
                                                user_pincode = str(user_list[5])
                                                now = datetime.datetime.now()
                                                purchase_date = now.strftime("%d-%m-%y")
                                                purchase_time = now.strftime("%H:%M:%S")
                                                purchase_date = str(purchase_date)
                                                purchase_time = str(purchase_time)
                                                order_code = str(user_email + user_contact + purchase_date + purchase_time)
                                                Label(buy_frame, font=("ABeeZee-Regular", 10, 'bold'), fg='red', bg='white', text=f"Your balance is low   :          ₹ {int(user_list[8])}\t\t\t").place(x=50, y=294)
                                                payment_type.set('Cash On Delivery')
                                                r1.destroy()
                            def continue_command():
                                time.sleep(2)
                                confirm_payment(int(product_id.get()), payment_type.get(), user_qty, user_total_price, user_name, user_age, user_contact, user_email, user_address, user_pincode, purchase_date, purchase_time, order_code)
                            Button(buy_frame, text="    Continue To Buy    ", fg='white', bg='black', font=("comicsansms", 10), command=continue_command, bd=0, cursor='hand2').place(x=140, y=340)
                            if repeat == 'yes':
                                buy_frame.after(2000, lambda: [continue_buy(str(user_quantity.get()), pro_stock, pro_cost, 'yes')])
                            else:
                                pass
                        else:
                            tmsg.showerror('Error', 'Quantity must be a number or it cannot be blank')
                            buy_frame.after(2000, lambda: [continue_buy(str(user_quantity.get()), pro_stock, pro_cost, 'yes')])
                        def confirm_payment(pro_index, payment, confirm_user_qty, confirm_user_total_price, confirm_user_name, confirm_user_age, confirm_user_contact, confirm_user_email, confirm_user_address, confirm_user_pincode, confirm_purchase_date, confirm_purchase_time, confirm_order_code):
                            user_information = [str(pro_index), str(confirm_user_qty), str(confirm_user_total_price), str(confirm_user_name), str(confirm_user_age), str(confirm_user_contact), str(confirm_user_email), str(confirm_user_address), str(confirm_user_pincode), str(confirm_purchase_date), str(confirm_purchase_time), str(confirm_order_code), str(payment)]
                            csv_write(r'orders.csv', 'a+', user_information)
                            sales_df = csv_read(r'sales_data.csv')
                            sales_last_row_list = list(sales_df.loc[int(len(sales_df) - 1)])
                            if str(confirm_purchase_date) == str(sales_last_row_list[0]):
                                same_date_row = int(int(len(sales_df)) - 1)
                                sales_df.at[same_date_row, 1] = int(
                                    int(confirm_user_total_price) + int(sales_last_row_list[1]))
                                with open(r'sales_data.csv', 'w+', newline='') as sales_file:
                                    sales_file_write = csv.writer(sales_file)
                                    for sales_row in sales_df.index:
                                        new_sales_row = list(sales_df.loc[sales_row])
                                        sales_file_write.writerow(new_sales_row)
                                sales_file.close()
                            else:
                                csv_write(r'sales_data.csv', 'a+',
                                          [str(confirm_purchase_date), str(confirm_user_total_price)])
                            updated_orders_df = csv_read(r'orders.csv')
                            for order_id in updated_orders_df.index:
                                x = list(updated_orders_df.loc[order_id])
                                if str(confirm_order_code) == x[11]:
                                    order_id = i
                                    customer_quantity = str(confirm_user_qty)
                                    customer_total_price = str(confirm_user_total_price)
                                    customer_name = str(confirm_user_name)
                                    customer_contact = str(confirm_user_contact)
                                    customer_email = str(confirm_user_email)
                                    customer_address = str(confirm_user_address)
                                    customer_pincode = str(confirm_user_pincode)
                                    payment_mode = str(payment)
                                    email_purchase_date = str(confirm_purchase_date)
                                    email_purchase_time = str(confirm_purchase_time)
                                    pro_name = str(product_name.get())
                                    pro_details = str(product_details.get())
                                    print("Your Order Confirmation Email from SAS", customer_email, f"Your order has been confirmed. Order for {pro_name} ({pro_details}) of {customer_quantity} piece/pieces of ₹ {customer_total_price} has been successfully placed. You will receive your order soon.\n\nOrder ID : {order_id}\nName : Mr./Mrs. {customer_name}\nContact no : +91 {customer_contact}\nEmail id : {customer_email}\nDelivery Address : {customer_address}\nPincode : {customer_pincode}\nDate of buying the product : {email_purchase_date}\nTime of buying the product : {email_purchase_time}\nPayment Mode : {payment_mode}.\n\nThank You for choosing us")
                                    send_mail("Your Order Confirmation Email from SAS", customer_email, f"Your order has been confirmed. Order for {pro_name} ({pro_details}) of {customer_quantity} piece/pieces of ₹ {customer_total_price} has been successfully placed. You will receive your order soon.\n\nOrder ID : {order_id}\nName : Mr./Mrs. {customer_name}\nContact no : +91 {customer_contact}\nEmail id : {customer_email}\nDelivery Address : {customer_address}\nPincode : {customer_pincode}\nDate of buying the product : {email_purchase_date}\nTime of buying the product : {email_purchase_time}\nPayment Mode : {payment_mode}.\n\nThank You for choosing us")
                            new_stock = int(int(product_stock.get()) - int(confirm_user_qty))
                            df = csv_read(r'products.csv')
                            df.at[int(pro_index), 3] = new_stock
                            with open(r'products.csv', 'w', newline='') as cf:
                                cw = csv.writer(cf)
                                for d in df.index:
                                    df_list = list(df.loc[d])
                                    cw.writerow(df_list)
                            cf.close()
                            if payment == "SAS WALLET":
                                udf = csv_read(r'users.csv')
                                for a in udf.index:
                                    if int(user_id_list[0]) == a:
                                        x = list(udf.loc[a])
                                        balance = int(x[8])
                                        new_balance = int(balance - int(confirm_user_total_price))
                                        udf.at[int(user_id_list[0]), 8] = new_balance
                                        with open(r'users.csv', 'w', newline='') as cf2:
                                            cw = csv.writer(cf2)
                                            for c in udf.index:
                                                udf_list = list(udf.loc[c])
                                                cw.writerow(udf_list)
                                        cf2.close()
                            tmsg.showinfo('Successfully', '    Your order has been send successfully.    ')
                            return_back()
                else:
                    tmsg.showinfo("Error", "Product is unavailable.")
                    return_back()
    else:
        tmsg.showwarning('Error', '     You are not logged in!     ')
        account_function()
def login(previous_frame):
    login_bg = image(r'images/login_bg.jpg', 1400, 850)
    login_bg_label = Label(frame6, image=login_bg, bd=0)
    login_bg_label.place(x=-10, y=-10)
    login_bg_label.image = login_bg
    login_frame = Frame(frame6, highlightthickness=5, highlightbackground='black', bg='white')
    login_frame.pack(padx=450, pady=40)
    def return_back():
        frame2.forget()
        products_frame.forget()
        frame3.forget()
        frame4.forget()
        frame5.forget()
        frame6.forget()
        frame7.forget()
        frame8.forget()
        frame1.pack(fill=X, anchor=N)
        home_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
        home_button['fg'] = 'black'
        products_button['font'] = ("Blogger_Sans-Bold", 10)
        products_button['fg'] = 'grey'
        account_button['font'] = ("Blogger_Sans-Bold", 10)
        account_button['fg'] = 'grey'
        feedback_button['font'] = ("Blogger_Sans-Bold", 10)
        feedback_button['fg'] = 'grey'
        about_button['font'] = ("Blogger_Sans-Bold", 10)
        about_button['fg'] = 'grey'
        previous_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
        return_icon.destroy()
        login_bg_label.destroy()
        login_frame.destroy()
    img = image(r"images/return_icon.png", 40, 40)
    return_icon = Button(frame6, image=img, bd=0, cursor="hand2", command=return_back)
    return_icon.place(x=10, y=10)
    return_icon.image = img
    login_label = Label(login_frame, text="L O G I  N", bd=0, bg='white', fg='black', font=('Helvetica bold', 20))
    login_label.pack(padx=165, pady=50, side=TOP)
    def on_enter_e1(e):
        if e1.get() == 'Type your user id':
            e1.delete(0, END)
    def on_leave_e1(e):
        if e1.get() == '':
            e1.insert(0, 'Type your user id')
    def on_return_e1(e):
        e2.focus_set()
    def on_enter_e2(e):
        if e2.get() == 'Type your password':
            e2.delete(0, END)
    def on_leave_e2(e):
        if e2.get() == '':
            e2.insert(0, 'Type your password')
    def on_return_e2(e):
        check_login(int(e1.get()), str(e2.get()))
        login_frame.forget()
        frame6.forget()
        frame1.pack(fill=X, anchor=N)
        restore(previous_frame)
        home_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
        home_button['fg'] = 'black'
        account_button['font'] = ("Blogger_Sans-Bold", 10)
        account_button['fg'] = 'grey'
    user_img = image(r'images/user_icon.jpg', 20, 20)
    user_icon = Label(login_frame, bd=0, image=user_img)
    user_icon.place(x=90, y=212)
    user_icon.image = user_img
    userid_label = Label(login_frame, bd=0, text='User ID', bg='white', fg='grey')
    userid_label.place(x=90, y=192)
    e1 = Entry(login_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    e1.pack(padx=110, pady=80)
    e1.insert(0, 'Type your user id')
    e1.bind('<FocusIn>', on_enter_e1)
    e1.bind('<FocusOut>', on_leave_e1)
    e1.bind('<Return>', on_return_e1)
    Frame(login_frame, width=259, height=3, bg='black', bd=0).place(x=90, y=229)
    password_label = Label(login_frame, bd=0, text='Password', bg='white', fg='grey')
    password_label.place(x=90, y=369)
    e2 = Entry(login_frame, borderwidth=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    e2.pack(padx=110, pady=80)
    e2.insert(0, 'Type your password')
    e2.bind('<FocusIn>', on_enter_e2)
    e2.bind('<FocusOut>', on_leave_e2)
    e2.bind('<Return>', on_return_e2)
    Frame(login_frame, width=259, height=3, bg='black', bd=0).place(x=90, y=406)
    def login_function():
        if e1.get().isdigit():
            if str(e2.get()) != 'Type your password':
                check_login(int(e1.get()), str(e2.get()))
                login_frame.forget()
                frame6.forget()
                frame1.pack(fill=X, anchor=N)
                restore(previous_frame)
                home_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
                home_button['fg'] = 'black'
                account_button['font'] = ("Blogger_Sans-Bold", 10)
                account_button['fg'] = 'grey'
            else:
                tmsg.showerror('Error', '   Please enter your password !   ')
                e2.focus_set()
        else:
            tmsg.showerror('Error', '   User ID must be a number !   ')
            e1.focus_set()
    login_img = image(r'images/login_icon.png', 250, 40)
    login_button = Button(login_frame, image=login_img, bd=0, cursor='hand2', command=login_function)
    login_button.image = login_img
    login_button.place(x=99, y=464)
    Label(login_frame).pack(pady=200)
    Label(login_frame, text='or Register using', bg='white', fg='black', bd=0, font=('ABeeZee-Regular', 10, 'bold')).place(x=175, y=520)
    register_img = image(r'images/sign_up_icon.jpg', 250, 35)
    register_button = Button(login_frame, image=register_img, bd=0, cursor='hand2', command=lambda: [register(), frame6.forget(), restore(frame4)])
    register_button.place(x=99, y=550)
    register_button.image = register_img
    def check_login(userid, password):
        users_df = csv_read(r'users.csv')
        for i in users_df.index:
            if int(userid) == i:
                users_list = list(users_df.loc[i])
                if str(password) == users_list[9]:
                    csv_write(r'login.csv', 'w+', [str(userid), str(password)])
                    tmsg.showinfo("Successfully", f"         Successfully Sign In as {users_list[0]}         ")
                    return_back()
def account(previous_frame):
    account_bg = image(r'images/login_bg.jpg', 1400, 850)
    account_bg_label = Label(frame8, image=account_bg, bd=0)
    account_bg_label.place(x=-10, y=-10)
    account_bg_label.image = account_bg
    account_frame = Frame(frame8, highlightthickness=5, highlightbackground='black', bg='white')
    account_frame.pack(padx=450, pady=40)
    def return_back():
        frame2.forget()
        products_frame.forget()
        frame3.forget()
        frame4.forget()
        frame5.forget()
        frame6.forget()
        frame7.forget()
        frame8.forget()
        frame1.pack(fill=X, anchor=N)
        home_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
        home_button['fg'] = 'black'
        products_button['font'] = ("Blogger_Sans-Bold", 10)
        products_button['fg'] = 'grey'
        account_button['font'] = ("Blogger_Sans-Bold", 10)
        account_button['fg'] = 'grey'
        feedback_button['font'] = ("Blogger_Sans-Bold", 10)
        feedback_button['fg'] = 'grey'
        about_button['font'] = ("Blogger_Sans-Bold", 10)
        about_button['fg'] = 'grey'
        previous_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
        return_icon.destroy()
        account_bg_label.destroy()
        account_frame.destroy()
    def change_user_password():
        change_password_bg = image(r'images/login_bg.jpg', 1400, 850)
        change_password_bg_label = Label(frame10, image=change_password_bg, bd=0)
        change_password_bg_label.place(x=-10, y=-10)
        change_password_bg_label.image = change_password_bg
        change_password_frame = Frame(frame10, highlightthickness=5, highlightbackground='black', bg='white')
        change_password_frame.pack(padx=450, pady=40)
        def return_back_of_change_password():
            return_back_of_change_password_return_icon.destroy()
            change_password_bg_label.destroy()
            change_password_frame.destroy()
            frame10.forget()
            restore(frame8)
        return_back_of_change_password_img = image(r"images/return_icon.png", 40, 40)
        return_back_of_change_password_return_icon = Button(frame10, image=return_back_of_change_password_img, bd=0, cursor="hand2", command=return_back_of_change_password)
        return_back_of_change_password_return_icon.place(x=10, y=10)
        return_back_of_change_password_return_icon.image = return_back_of_change_password_img
        change_password_label = Label(change_password_frame, text="CHANGE PASSWORD", bd=0, bg='white', fg='black', font=('Helvetica bold', 20))
        change_password_label.pack(padx=65, pady=50, side=TOP)
        def on_enter_e1(e):
            if e1.get() == 'Type your current password':
                e1.delete(0, END)
        def on_leave_e1(e):
            if e1.get() == '':
                e1.insert(0, 'Type your current password')
        def on_return_e1(e):
            e2.focus_set()
        def on_enter_e2(e):
            if e2.get() == 'Type your new password':
                e2.delete(0, END)
        def on_leave_e2(e):
            if e2.get() == '':
                e2.insert(0, 'Type your new password')
        def on_return_e2(e):
            change_user_password_command()
            change_password_frame.forget()
            frame10.forget()
            restore(frame8)
        user_img = image(r'images/user_icon.jpg', 20, 20)
        user_icon = Label(change_password_frame, bd=0, image=user_img)
        user_icon.place(x=90, y=212)
        user_icon.image = user_img
        password_label = Label(change_password_frame, bd=0, text='Password', bg='white', fg='grey')
        password_label.place(x=90, y=192)
        e1 = Entry(change_password_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
        e1.pack(padx=110, pady=80)
        e1.insert(0, 'Type your current password')
        e1.bind('<FocusIn>', on_enter_e1)
        e1.bind('<FocusOut>', on_leave_e1)
        e1.bind('<Return>', on_return_e1)
        Frame(change_password_frame, width=259, height=3, bg='black', bd=0).place(x=90, y=229)
        new_password_label = Label(change_password_frame, bd=0, text='New Password', bg='white', fg='grey')
        new_password_label.place(x=90, y=369)
        e2 = Entry(change_password_frame, borderwidth=0, font=('consoles', 8), fg='grey', bg='white', width=40)
        e2.pack(padx=110, pady=80)
        e2.insert(0, 'Type your new password')
        e2.bind('<FocusIn>', on_enter_e2)
        e2.bind('<FocusOut>', on_leave_e2)
        e2.bind('<Return>', on_return_e2)
        Frame(change_password_frame, width=259, height=3, bg='black', bd=0).place(x=90, y=406)
        def change_user_password_command():
            if str(e2.get()) != 'Type your new password':
                if str(e1.get()) == str(y[1]):
                    csv_write(r'login.csv', 'w+', [str(y[0]), str(e2.get())])
                    user_df.at[int(y[0]), 9] = str(e2.get())
                    with open(r'users.csv', 'w+', newline='') as user_file:
                        user_file_write = csv.writer(user_file)
                        for every_user in user_df.index:
                            modified_user_list = list(user_df.loc[every_user])
                            user_file_write.writerow(modified_user_list)
                    user_file.close()
                    tmsg.showinfo('Successfully', 'You have changed your password successfully')
                    return_back_of_change_password()
                else:
                    tmsg.showerror('Error', '   You have entered wrong password !   ')
                    e1.focus_set()
            else:
                tmsg.showerror('Error', '   Please enter your new password !   ')
                e2.focus_set()
        Button(change_password_frame, bg='black', fg='white', bd=0, font=('Blogger_Sans-Bold', 12, 'bold'), text='    CHANGE PASSWORD    ', cursor='hand2', command=change_user_password_command).place(x=108, y=464)
        Label(change_password_frame).pack(pady=500)
    img = image(r"images/return_icon.png", 40, 40)
    return_icon = Button(frame8, image=img, bd=0, cursor="hand2", command=return_back)
    return_icon.place(x=10, y=10)
    return_icon.image = img
    df = csv_read(r'login.csv')
    user_df = csv_read(r'users.csv')
    account_frame.pack(padx=450, pady=40)
    account_label = Label(account_frame, text="ACCOUNT DETAILS", bd=0, bg='white', fg='black', font=('Helvetica bold', 20))
    account_label.pack(padx=95, pady=50, side=TOP)
    Label(account_frame).pack(padx=600, pady=600)
    for i in df.index:
        y = list(df.loc[i])
        x = list(user_df.loc[int(y[0])])
        Label(account_frame, bg='white', fg='black', bd=0, font=('Blogger_Sans', 10, 'italic'), text=f'User ID : {y[0]}').place(x=50, y=140)
        Label(account_frame, bg='white', fg='black', bd=0, font=('Blogger_Sans', 10, 'italic'), text=f'Name : {x[0]}').place(x=50, y=170)
        Label(account_frame, bg='white', fg='black', bd=0, font=('Blogger_Sans', 10, 'italic'), text=f'Phone number : {x[2]}').place(x=50, y=200)
        Label(account_frame, bg='white', fg='black', bd=0, font=('Blogger_Sans', 10, 'italic'), text=f'Email ID : {x[3]}').place(x=50, y=230)
        Label(account_frame, bg='white', fg='black', bd=0, font=('Blogger_Sans', 10, 'italic'), text=f'Address : {x[4]}').place(x=50, y=260)
        Label(account_frame, bg='white', fg='black', bd=0, font=('Blogger_Sans', 10, 'italic'), text=f'Pincode : {x[5]}').place(x=50, y=290)
        if int(x[8]) == 0:
            Label(account_frame, bg='white', fg='red', bd=0, font=('Blogger_Sans', 10, 'italic'), text=f'SAS Wallet Balance :   ₹ {x[8]}').place(x=50, y=320)
        else:
            Label(account_frame, bg='white', fg='black', bd=0, font=('Blogger_Sans', 10, 'italic'), text=f'SAS Wallet Balance :   ₹ {x[8]}').place(x=50, y=320)
        Button(account_frame, bg='black', fg='white', bd=0, font=('Blogger_Sans-Bold', 12, 'bold'), text='    LOGOUT    ', cursor='hand2', command=lambda: [os.remove(r'login.csv'), tmsg.showinfo('Successfully', '    Your account have been successfully logged out    '), return_back()]).place(x=300, y=360)
        Button(account_frame, bg='black', fg='white', bd=0, font=('Blogger_Sans-Bold', 12, 'bold'), text='    CHANGE PASSWORD    ', cursor='hand2', command=lambda: [frame8.forget(), restore(frame10), change_user_password()]).place(x=50, y=360)
def admin_login():
    admin_login_bg = image(r'images/login_bg.jpg', 1400, 850)
    admin_login_bg_label = Label(admin_login_frame, image=admin_login_bg, bd=0)
    admin_login_bg_label.place(x=-10, y=-10)
    admin_login_bg_label.image = admin_login_bg
    admin_temp_login_frame = Frame(admin_login_frame, highlightthickness=5, highlightbackground='black', bg='white')
    admin_temp_login_frame.pack(padx=450, pady=40)
    def return_back():
        frame2.forget()
        products_frame.forget()
        frame3.forget()
        frame4.forget()
        frame5.forget()
        frame6.forget()
        frame7.forget()
        frame8.forget()
        admin_frame.forget()
        admin_login_frame.forget()
        frame1.pack(fill=X, anchor=N)
        home_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
        home_button['fg'] = 'black'
        products_button['font'] = ("Blogger_Sans-Bold", 10)
        products_button['fg'] = 'grey'
        account_button['font'] = ("Blogger_Sans-Bold", 10)
        account_button['fg'] = 'grey'
        feedback_button['font'] = ("Blogger_Sans-Bold", 10)
        feedback_button['fg'] = 'grey'
        about_button['font'] = ("Blogger_Sans-Bold", 10)
        about_button['fg'] = 'grey'
        frame2.pack(side='left', anchor='nw', fill=BOTH, expand=True)
        return_icon.destroy()
        admin_login_bg_label.destroy()
        admin_temp_login_frame.destroy()
    img = image(r"images/return_icon.png", 40, 40)
    return_icon = Button(admin_login_frame, image=img, bd=0, cursor="hand2", command=return_back)
    return_icon.place(x=10, y=10)
    return_icon.image = img
    admin_login_label = Label(admin_temp_login_frame, text="L O G I  N", bd=0, bg='white', fg='black', font=('Helvetica bold', 20))
    admin_login_label.pack(padx=165, pady=50, side=TOP)
    def on_enter_e1(e):
        if e1.get() == 'Type your admin id':
            e1.delete(0, END)
    def on_leave_e1(e):
        if e1.get() == '':
            e1.insert(0, 'Type your admin id')
    def on_return_e1(e):
        e2.focus_set()
    def on_enter_e2(e):
        if e2.get() == 'Type your password':
            e2.delete(0, END)
    def on_leave_e2(e):
        if e2.get() == '':
            e2.insert(0, 'Type your password')
    def on_return_e2(e):
        login_function()
    admin_img = image(r'images/user_icon.jpg', 20, 20)
    admin_icon = Label(admin_temp_login_frame, bd=0, image=admin_img)
    admin_icon.place(x=90, y=212)
    admin_icon.image = admin_img
    admin_id_label = Label(admin_temp_login_frame, bd=0, text='Admin ID', bg='white', fg='grey')
    admin_id_label.place(x=90, y=192)
    e1 = Entry(admin_temp_login_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    e1.pack(padx=110, pady=80)
    e1.insert(0, 'Type your admin id')
    e1.bind('<FocusIn>', on_enter_e1)
    e1.bind('<FocusOut>', on_leave_e1)
    e1.bind('<Return>', on_return_e1)
    Frame(admin_temp_login_frame, width=259, height=3, bg='black', bd=0).place(x=90, y=229)
    password_label = Label(admin_temp_login_frame, bd=0, text='Password', bg='white', fg='grey')
    password_label.place(x=90, y=369)
    e2 = Entry(admin_temp_login_frame, borderwidth=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    e2.pack(padx=110, pady=80)
    e2.insert(0, 'Type your password')
    e2.bind('<FocusIn>', on_enter_e2)
    e2.bind('<FocusOut>', on_leave_e2)
    e2.bind('<Return>', on_return_e2)
    Frame(admin_temp_login_frame, width=259, height=3, bg='black', bd=0).place(x=90, y=406)
    def login_function():
        if str(e1.get()) != 'Type your admin id':
            if str(e2.get()) != 'Type your password':
                check_login(str(e1.get()), str(e2.get()))
            else:
                tmsg.showerror('Error', '   Please enter your password !   ')
                e2.focus_set()
        else:
            tmsg.showerror('Error', '   Please enter you admin id !   ')
            e1.focus_set()
    login_img = image(r'images/login_icon.png', 250, 40)
    login_button = Button(admin_temp_login_frame, image=login_img, bd=0, cursor='hand2', command=login_function)
    login_button.image = login_img
    login_button.place(x=99, y=464)
    Label(admin_temp_login_frame).pack(pady=200)
    def check_login(admin_id, password):
        admin_df = csv_read(r'admin_login.csv')
        for i in admin_df.index:
            admin_list = list(admin_df.loc[i])
            if str(admin_id) == admin_list[0] and str(password) == admin_list[1]:
                tmsg.showinfo("Successfully", f"         Successfully Sign In as {admin_list[0]}         ")
                admin_temp_login_frame.destroy()
                admin_login_frame.forget()
                admin_frame.pack(anchor=NW)
                admin()
            else:
                tmsg.showerror("Error", "    You have entered wrong admin id or password!    ")
def admin():
    def return_back():
        frame2.forget()
        products_frame.forget()
        frame3.forget()
        frame4.forget()
        frame5.forget()
        frame6.forget()
        frame7.forget()
        frame8.forget()
        admin_frame.forget()
        admin_products_frame.forget()
        admin_users_frame.forget()
        admin_orders_frame.forget()
        admin_feedback_frame.forget()
        admin_change_password_frame.forget()
        frame1.pack(fill=X, anchor=N)
        home_button['font'] = ("Blogger_Sans-Bold", 10, 'bold')
        home_button['fg'] = 'black'
        products_button['font'] = ("Blogger_Sans-Bold", 10)
        products_button['fg'] = 'grey'
        account_button['font'] = ("Blogger_Sans-Bold", 10)
        account_button['fg'] = 'grey'
        feedback_button['font'] = ("Blogger_Sans-Bold", 10)
        feedback_button['fg'] = 'grey'
        about_button['font'] = ("Blogger_Sans-Bold", 10)
        about_button['fg'] = 'grey'
        frame2.pack(side='left', anchor='nw', fill=BOTH, expand=True)
        return_icon.destroy()
    def return_back_confirm():
        confirm_question = tmsg.askyesno("Loggot", "    Want to loggot?    ")
        if confirm_question:
            tmsg.showinfo("Successful", "    You have successfully loggot!    ")
            return_back()
        else:
            pass
    Label(admin_frame).pack(padx=2000, pady=1000)
    img = image(r"images/return_icon.png", 40, 40)
    return_icon = Button(admin_frame, image=img, bd=0, cursor="hand2", command=return_back_confirm)
    return_icon.place(x=10, y=10)
    return_icon.image = img
    Label(admin_frame, text="A D M I N", bg="white", fg="black", font=("BonvenoCF-Light", 36)).place(x=578, y=70)
    products_image = image(r'images\products_icon.jpg', 160, 160)
    products_label = Label(admin_frame, bg='white', bd=0, image=products_image)
    products_label.place(x=150, y=200)
    products_label.image = products_image
    products_button_image = image(r'images\product_btn_icon.jpg', 159, 30)
    admin_products_button = Button(admin_frame, bg='white', bd=0, image=products_button_image, cursor='hand2', command=lambda: [admin_frame.forget(), admin_products_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True), admin_show_products()])
    admin_products_button.place(x=145, y=385)
    admin_products_button.image = products_button_image
    users_image = image(r'images\user_icon.jpg', 160, 160)
    users_label = Label(admin_frame, bg='white', bd=0, image=users_image)
    users_label.place(x=600, y=210)
    users_label.image = users_image
    users_button_image = image(r'images\user_btn_icon.jpg', 159, 30)
    users_button = Button(admin_frame, bg='white', bd=0, image=users_button_image, cursor='hand2', command=lambda: [admin_frame.forget(), admin_users_frame.pack(side=LEFT, anchor=NW, fill=BOTH, expand=True), admin_show_users()])
    users_button.place(x=600, y=385)
    users_button.image = users_button_image
    orders_image = image(r'images\cart_icon.jpg', 140, 115)
    orders_label = Label(admin_frame, bg='white', bd=0, image=orders_image)
    orders_label.place(x=1055, y=235)
    orders_label.image = orders_image
    orders_button_image = image(r'images\order_btn_icon.jpg', 159, 30)
    orders_button = Button(admin_frame, bg='white', bd=0, image=orders_button_image, cursor='hand2', command=lambda: [admin_frame.forget(),admin_orders_frame.pack(side=LEFT, anchor=NW, fill=BOTH, expand=True), admin_show_orders()])
    orders_button.place(x=1055, y=385)
    orders_button.image = orders_button_image
    feedback_image = image(r'images\feedback_image.jpg', 160, 160)
    feedback_label = Label(admin_frame, bg='white', bd=0, image=feedback_image)
    feedback_label.place(x=178, y=500)
    feedback_label.image = feedback_image
    feedback_button_image = image(r'images\feedback_btn_icon.jpg', 159, 30)
    admin_feedback_button = Button(admin_frame, bg='white', bd=0, image=feedback_button_image, cursor='hand2', command=lambda: [admin_frame.forget(), admin_feedback_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True), admin_show_feedback()])
    admin_feedback_button.place(x=145, y=675)
    admin_feedback_button.image = feedback_button_image
    def sales_chart():
        sales_df = csv_read(r'sales_data.csv')
        date = []
        sales_amt = []
        for date_row in sales_df[0]:
            date.append(date_row)
        for amt_row in sales_df[1]:
            sales_amt.append(amt_row)
        plt.xlabel("Dates")
        plt.ylabel("Total Sales")
        plt.plot(date, list(map(int, sales_amt)))
        plt.title(f"Sales Chart Of SAS Store from {list(sales_df[0])[0]} to {list(sales_df[0])[int(len(sales_df[0]) - 1)]}")
        plt.show()
    sales_chart_image = image(r'images\sales_chart_image.jpg', 160, 160)
    sales_chart_label = Label(admin_frame, bg='white', bd=0, image=sales_chart_image)
    sales_chart_label.place(x=600, y=500)
    sales_chart_label.image = sales_chart_image
    sales_chart_button_image = image(r'images\sales_chart_btn_icon.jpg', 159, 30)
    sales_chart_button = Button(admin_frame, bg='white', bd=0, image=sales_chart_button_image, cursor='hand2', command=sales_chart)
    sales_chart_button.place(x=600, y=675)
    sales_chart_button.image = sales_chart_button_image
    change_password_image = image(r'images\password_icon.jpg', 160, 160)
    change_password_label = Label(admin_frame, bg='white', bd=0, image=change_password_image)
    change_password_label.place(x=1055, y=500)
    change_password_label.image = change_password_image
    change_password_button_image = image(r'images\change_password_btn_icon.jpg', 159, 30)
    change_password_button = Button(admin_frame, bg='white', bd=0, image=change_password_button_image, cursor='hand2', command=lambda: [admin_frame.forget(), admin_change_password_frame.pack(side=LEFT, anchor=NW), admin_change_password()])
    change_password_button.place(x=1055, y=675)
    change_password_button.image = change_password_button_image
def admin_show_products():
    temp_frame = Frame(admin_products_frame, bg="white", bd=0)
    temp_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
    admin_show_products_frame_1 = Frame(temp_frame, bg='white', bd=0)
    admin_show_products_frame_1.pack(anchor=NW)
    admin_show_products_frame_2 = Frame(temp_frame, bg='white', bd=0)
    admin_show_products_frame_2.pack(anchor=NW, side=LEFT, fill=BOTH, expand=True)
    admin_show_products_temp_frame = Frame(admin_show_products_frame_2, bg='white', bd=0)
    admin_show_products_temp_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
    Label(admin_show_products_frame_1, bg="white").pack(padx=1000, pady=75)
    admin_canvas = Canvas(admin_show_products_temp_frame, bg='white')
    scrollbar = Scrollbar(admin_show_products_temp_frame, orient='vertical', bg='white', command=admin_canvas.yview)
    admin_scrollabel_frame = Frame(admin_canvas, bg='white')
    admin_scrollabel_frame.bind('<Configure>', lambda e: admin_canvas.configure(scrollregion=admin_canvas.bbox('all')))
    admin_canvas.create_window((0, 0), window=admin_scrollabel_frame, anchor=NW)
    admin_canvas.configure(yscrollcommand=scrollbar.set)
    admin_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    def return_back():
        frame2.forget()
        products_frame.forget()
        frame3.forget()
        frame4.forget()
        frame5.forget()
        frame6.forget()
        frame7.forget()
        frame8.forget()
        admin_frame.forget()
        admin_products_frame.forget()
        admin_users_frame.forget()
        admin_orders_frame.forget()
        admin_feedback_frame.forget()
        admin_change_password_frame.forget()
        admin_frame.pack(anchor=NW)
        temp_frame.destroy()
    img = image(r"images/return_icon.png", 40, 40)
    return_icon = Button(admin_show_products_frame_1, image=img, bd=0, cursor="hand2", command=return_back)
    return_icon.place(x=10, y=10)
    return_icon.image = img
    def on_enter(e):
        search_admin.delete(0, END)
        if search_admin.get() != 'Search...':
            search_admin['fg'] = "black"
    search_img = image(r"images/search_icon.png", 20, 20)
    search_admin_frame = Frame(admin_show_products_frame_1, height=5, width=182, bg="black")
    search_admin_frame.place(x=592, y=68)
    search_admin = Entry(admin_show_products_frame_1, fg="grey", bd=0, width=30)
    search_admin.place(x=592, y=54)
    search_admin.insert(0, "Search...")
    search_admin.bind("<FocusIn>", on_enter)
    def enter(e):
        temp_frame.forget()
        admin_products_frame.pack(anchor=NW)
        admin_product_search()
    search_admin.bind("<Return>", enter)
    search_btn = Button(admin_show_products_frame_1, image=search_img, bd=0, cursor="hand2", command=lambda: [temp_frame.forget(), admin_products_frame.pack(anchor=NW), admin_product_search()])
    search_btn.place(x=800, y=57)
    search_btn.image = search_img
    def admin_product_search():
        temp_frame_ = Frame(admin_products_frame, bd=0, bg='white')
        temp_frame_.pack(side='left', anchor='nw', fill=BOTH, expand=True)
        admin_canvas_ = Canvas(temp_frame_, bg='white')
        scrollbar_ = Scrollbar(temp_frame_, orient='vertical', bg='white', command=admin_canvas_.yview)
        scrollabel_frame = Frame(admin_canvas_, bg='white')
        scrollabel_frame.bind('<Configure>', lambda e: admin_canvas_.configure(scrollregion=admin_canvas_.bbox('all')))
        admin_canvas_.create_window((0, 0), window=scrollabel_frame, anchor=NW)
        admin_canvas_.configure(yscrollcommand=scrollbar_.set)
        admin_canvas_.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar_.pack(side=RIGHT, fill=Y)
        img_ = image(r"images/return_icon.png", 40, 40)
        return_button = Button(scrollabel_frame, image=img_, bd=0, cursor="hand2", command=lambda: [temp_frame_.destroy(), return_back()])
        return_button.place(x=15, y=10)
        return_button.image = img_
        frame_img = image(r'images/big_frame_bg.jpg', 900, 200)
        location = r'products.csv'
        df_ = csv_read(location)
        for temp_row in range(15):
            Label(scrollabel_frame, bg='white', bd=0).grid(row=temp_row, column=0)
        row_ = 16
        for _ in df_.index:
            x_ = list(df_.loc[_])
            if search_admin.get().lower() == x_[0].lower():
                row_ += 1
                def add_products_stock_action_search(add_product_stock_id=_):
                    add_products_stock_action(add_product_stock_id)
                products_bg_frame_ = Frame(scrollabel_frame, bg='white', bd=0)
                products_bg_frame_.grid(row=row_, column=0, columnspan=8)
                products_bg_ = Label(products_bg_frame_, bg='white', bd=0, image=frame_img)
                products_bg_.pack(fill=BOTH, expand=True)
                products_bg_.image = frame_img
                product_id_ = StringVar()
                product_name_ = StringVar()
                product_cost_ = StringVar()
                product_details_ = StringVar()
                product_stock_ = StringVar()
                product_id_.set(f'{i}')
                product_name_.set(f'{x_[0]}')
                product_cost_.set(f'₹ {x_[1]}')
                product_details_.set(f'{x_[2]}')
                product_stock_.set(f'{x_[3]} pc(s)')
                product_img_ = image(r'{}'.format(str(x_[4])), 132, 132)
                product_image_ = Label(products_bg_frame_, image=product_img_, bd=0)
                product_image_.place(anchor=NW, x=200, y=20)
                product_image_.image = product_img_
                Label(products_bg_frame_, textvariable=product_cost_, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=700,  y=30)
                Label(products_bg_frame_, textvariable=product_stock_, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=110)
                Label(products_bg_frame_, textvariable=product_name_, bg='white', fg='black', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=30)
                Label(products_bg_frame_, textvariable=product_details_, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=500, y=70)
                delete_button[i] = Button(products_bg_frame_, image=delete_image, cursor="hand2", bd=0, command=lambda: [temp_frame_.destroy(), delete_action()])
                delete_button[i].place(anchor=NW, x=525, y=140)
                delete_button[i].image = delete_image
                add_products_stock[i] = Button(products_bg_frame_, image=add_stock_image, cursor="hand2", bd=0, command=lambda: [temp_frame_.destroy(), add_products_stock_action_search()])
                add_products_stock[i].place(anchor=NW, x=699, y=140)
                add_products_stock[i].image = add_stock_image
    df = csv_read(r'products.csv')
    row = 0
    delete_button = {}
    add_products_stock = {}
    Label(admin_show_products_frame_1, text='Products', bg='white', bd=0, font=("Blooger_Sans-Bold", 24, "bold")).place(x=20, y=120)
    def add_product_action():
        temp_frame.destroy()
        temp_frame__ = Frame(admin_products_frame, bg="white", bd=0)
        temp_frame__.pack(anchor=NW)
        add_product_bg = image(r'images/login_bg.jpg', 1400, 850)
        add_product_bg_label = Label(temp_frame__, image=add_product_bg, bd=0)
        add_product_bg_label.place(x=-10, y=-10)
        add_product_bg_label.image = add_product_bg
        add_product_frame = Frame(temp_frame__, highlightthickness=5, highlightbackground='black', bg='white')
        add_product_frame.pack(padx=450, pady=40)
        def admin_product_return_back():
            return_icon_.destroy()
            add_product_bg_label.destroy()
            temp_frame__.destroy()
            return_back()
        img_ = image(r"images/return_icon.png", 40, 40)
        return_icon_ = Button(temp_frame__, image=img_, bd=0, cursor="hand2", command=admin_product_return_back)
        return_icon_.place(x=10, y=10)
        return_icon_.image = img_
        add_product_frame.pack(padx=450, pady=40)
        add_product_label = Label(add_product_frame, text="Add Product", bd=0, bg='white', fg='black', font=('Helvetica bold', 20))
        add_product_label.pack(padx=95, pady=50, side=TOP)
        Label(add_product_frame).pack(padx=600, pady=600)
        def on_enter_product_name(e):
            if str(product_name_.get()) == 'Type product name':
                product_name_.delete(0, END)
        def on_leave_product_name(e):
            if str(product_name_.get()) == '':
                product_name_.insert(0, 'Type product name')
        def on_return_product_name(e):
            if str(product_name_.get()) == 'Type product name' or str(product_name_.get()) == '':
                tmsg.showerror('Error', '   Please enter product name !   ')
                product_name_.focus_set()
            else:
                product_price.focus_set()
        def on_enter_product_price(e):
            if str(product_price.get()) == 'Type product price':
                product_price.delete(0, END)
        def on_leave_product_price(e):
            if str(product_price.get()) == '':
                product_price.insert(0, 'Type product price')
        def on_return_product_price(e):
            if str(product_price.get()) == 'Type product price' or str(product_price.get()) == '':
                tmsg.showerror('Error', '   Please enter product price !   ')
                product_price.focus_set()
            else:
                product_details_.focus_set()
        def on_enter_product_details(e):
            if str(product_details_.get()) == 'Type product details':
                product_details_.delete(0, END)
        def on_leave_product_details(e):
            if str(product_details_.get()) == '':
                product_details_.insert(0, 'Type product details')
        def on_return_product_details(e):
            if str(product_details_.get()) == 'Type product details' or str(product_details_.get()) == '':
                tmsg.showerror('Error', '   Please enter product details !   ')
                product_details_.focus_set()
            else:
                product_stock_.focus_set()
        def on_enter_product_stock(e):
            if str(product_stock_.get()) == 'Type product stock':
                product_stock_.delete(0, END)
        def on_leave_product_stock(e):
            if str(product_stock_.get()) == '':
                product_stock_.insert(0, 'Type product stock')
        def on_return_product_stock(e):
            if str(product_stock_.get()) == 'Type product stock' or str(product_stock_.get()) == '':
                tmsg.showerror('Error', '   Please enter product stock!   ')
                product_stock_.focus_set()
            else:
                product_image_.focus_set()
        def on_enter_product_image(e):
            if str(product_image_.get()) == 'Type product image':
                product_image_.delete(0, END)
        def on_leave_product_image(e):
            if str(product_image_.get()) == '':
                product_image_.insert(0, 'Type product image')
        def on_return_product_image(e):
            if str(product_image_.get()) == 'Type product image' or str(product_image_.get()) == '':
                tmsg.showerror('Error', '   Please enter product image !   ')
                product_image_.focus_set()
            else:
                add_product_command()
        name_label = Label(add_product_frame, bd=0, text='Product Name', bg='white', fg='grey')
        name_label.place(x=45, y=127)
        product_name_ = Entry(add_product_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
        product_name_.place(x=60, y=154)
        product_name_.insert(0, 'Type product name')
        product_name_.bind('<FocusIn>', on_enter_product_name)
        product_name_.bind('<FocusOut>', on_leave_product_name)
        product_name_.bind('<Return>', on_return_product_name)
        Frame(add_product_frame, width=259, height=3, bg='black', bd=0).place(x=45, y=170)
        price_label = Label(add_product_frame, bd=0, text='Product Price', bg='white', fg='grey')
        price_label.place(x=45, y=184)
        product_price = Entry(add_product_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
        product_price.place(x=60, y=211)
        product_price.insert(0, 'Type product price')
        product_price.bind('<FocusIn>', on_enter_product_price)
        product_price.bind('<FocusOut>', on_leave_product_price)
        product_price.bind('<Return>', on_return_product_price)
        Frame(add_product_frame, width=259, height=3, bg='black', bd=0).place(x=45, y=227)
        details_label = Label(add_product_frame, bd=0, text='Product Details', bg='white', fg='grey')
        details_label.place(x=45, y=241)
        product_details_ = Entry(add_product_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
        product_details_.place(x=60, y=268)
        product_details_.insert(0, 'Type product details')
        product_details_.bind('<FocusIn>', on_enter_product_details)
        product_details_.bind('<FocusOut>', on_leave_product_details)
        product_details_.bind('<Return>', on_return_product_details)
        Frame(add_product_frame, width=259, height=3, bg='black', bd=0).place(x=45, y=284)
        stock_id_label = Label(add_product_frame, bd=0, text='Product Stock', bg='white', fg='grey')
        stock_id_label.place(x=45, y=298)
        product_stock_ = Entry(add_product_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
        product_stock_.place(x=60, y=325)
        product_stock_.insert(0, 'Type product stock')
        product_stock_.bind('<FocusIn>', on_enter_product_stock)
        product_stock_.bind('<FocusOut>', on_leave_product_stock)
        product_stock_.bind('<Return>', on_return_product_stock)
        Frame(add_product_frame, width=259, height=3, bg='black', bd=0).place(x=45, y=341)
        image_label = Label(add_product_frame, bd=0, text='Product Image', bg='white', fg='grey')
        image_label.place(x=45, y=355)
        product_image_ = Entry(add_product_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
        product_image_.place(x=60, y=382)
        product_image_.insert(0, 'Type product image')
        product_image_.bind('<FocusIn>', on_enter_product_image)
        product_image_.bind('<FocusOut>', on_leave_product_image)
        product_image_.bind('<Return>', on_return_product_image)
        Frame(add_product_frame, width=259, height=3, bg='black', bd=0).place(x=45, y=398)
        def add_product_command():
            csv_write(r'products.csv', 'a+', [str(product_name_.get()), str(product_price.get()), str(product_details_.get()), str(product_stock_.get()), str(product_image_.get())])
            tmsg.showinfo("Successful", "    Product has been added successfully !   ")
            admin_product_return_back()
        add_products_button_ = Button(add_product_frame, image=add_products_image, bg="white", bd=0, cursor="hand2", command=add_product_command)
        add_products_button_.place(x=140, y=500)
        add_products_button_.image = add_products_image
    add_products_image = image(r'images/add_products_icon.jpg', 164, 40)
    add_products_button = Button(admin_show_products_frame_1, image=add_products_image, bg="white", bd=0, cursor="hand2", command=add_product_action)
    add_products_button.place(x=1055, y=110)
    add_products_button.image = add_products_image
    products_bg_image = image(r'images/big_frame_bg.jpg', 900, 200)
    delete_image = image(r'images/delete_icon.jpg', 100, 30)
    add_stock_image = image(r'images/add_stock_icon.jpg', 100, 30)
    for i in df.index:
        row += 1
        products_bg_frame = Frame(admin_scrollabel_frame, bg='white', bd=0)
        products_bg_frame.grid(row=row, column=0, columnspan=8)
        products_bg = Label(products_bg_frame, bg='white', bd=0, image=products_bg_image)
        products_bg.pack(fill=BOTH, expand=True)
        products_bg.image = products_bg_image
        x = list(df.loc[i])
        product_id = StringVar()
        product_name = StringVar()
        product_cost = StringVar()
        product_details = StringVar()
        product_stock = StringVar()
        product_id.set(f'{i}')
        product_name.set(f'{x[0]}')
        product_cost.set(f'₹ {x[1]}')
        product_details.set(f'{x[2]}')
        product_stock.set(f'{x[3]} pc(s)')
        product_img = image(r'{}'.format(str(x[4])), 132, 132)
        def add_products_stock_action(add_product_stock_id):
            temp_frame.destroy()
            add_products_stock_frame = Frame(admin_products_frame, bg="white", bd=0)
            add_products_stock_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
            add_stock_bg = image(r'images/login_bg.jpg', 1400, 850)
            add_stock_bg_label = Label(add_products_stock_frame, image=add_stock_bg, bd=0)
            add_stock_bg_label.place(x=-10, y=-10)
            add_stock_bg_label.image = add_stock_bg
            add_stock_frame = Frame(add_products_stock_frame, highlightthickness=5, highlightbackground='black', bg='white')
            add_stock_frame.pack(padx=450, pady=40)
            def add_stock_return_back():
                frame2.forget()
                products_frame.forget()
                frame3.forget()
                frame4.forget()
                frame5.forget()
                frame6.forget()
                frame7.forget()
                frame8.forget()
                admin_frame.forget()
                admin_products_frame.forget()
                admin_users_frame.forget()
                admin_orders_frame.forget()
                admin_feedback_frame.forget()
                admin_change_password_frame.forget()
                admin_frame.pack(anchor=NW)
                add_products_stock_frame.destroy()
                add_stock_return_back.destroy()
                add_stock_bg_label.destroy()
                add_stock_frame.destroy()
            add_stock_return_back = Button(add_products_stock_frame, image=img, bd=0, cursor="hand2", command=add_stock_return_back)
            add_stock_return_back.place(x=10, y=10)
            add_stock_return_back.image = img
            add_stock_label = Label(add_stock_frame, text="ADD STOCK", bd=0, bg='white', fg='black', font=('Helvetica bold', 20))
            add_stock_label.pack(padx=100, pady=50, side=TOP)
            Label(add_stock_frame).pack(padx=380, pady=600)
            def on_enter_e1(e):
                if e1.get() == 'Type your user id':
                    e1.delete(0, END)
            def on_leave_e1(e):
                if e1.get() == '':
                    e1.insert(0, 'Type your user id')
            def on_return_e1(e):
                add_stock_function()
            for c in df.index:
                if add_product_stock_id == c:
                    z = list(df.loc[c])
                    add_product_img = image(r'{}'.format(str(z[4])), 132, 132)
                    add_product_image = Label(add_stock_frame, image=add_product_img, bd=0)
                    add_product_image.place(anchor=NW, x=10, y=170)
                    add_product_image.image = add_product_img
                    Label(add_stock_frame, text=f'Name : {z[0]}', bg='white', fg='black', font=('Amaranth-Regular', 8)).place(anchor=W, x=155, y=200)
                    Label(add_stock_frame, text=f'Price : {z[1]}', bg='white', font=('Amaranth-Regular', 8)).place(anchor=W, x=155, y=220)
                    Label(add_stock_frame, text=f'Details : {z[2]}', bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=155, y=240)
                    Label(add_stock_frame, text=f'Current Stock : {z[3]} pc(s)', bg='white', font=('Amaranth-Regular', 8)).place(x=220, y=210)
            stock_icon = Label(add_stock_frame, bd=0, bg="white")
            stock_icon.place(x=90, y=431)
            stock_label = Label(add_stock_frame, bd=0, text='Add Stock', bg='white', fg='grey')
            stock_label.place(x=90, y=409)
            e1 = Entry(add_stock_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
            e1.place(x=110, y=431)
            e1.insert(0, 'Type your user id')
            e1.bind('<FocusIn>', on_enter_e1)
            e1.bind('<FocusOut>', on_leave_e1)
            e1.bind('<Return>', on_return_e1)
            Frame(add_stock_frame, width=259, height=3, bg='black', bd=0).place(x=90, y=446)
            def add_stock_function():
                if e1.get().isdigit():
                    new_stock = int(int(z[3]) + int(e1.get()))
                    df.at[add_product_stock_id, 3] = new_stock
                    with open(r'products.csv', 'w', newline='') as products_file:
                        products_file_write = csv.writer(products_file)
                        for d in df.index:
                            e = list(df.loc[d])
                            products_file_write.writerow(e)
                    products_file.close()
                    tmsg.showinfo('Successful', "    Product's stock has been updated successfully!    ")
                    admin_frame.pack(anchor=NW)
                    admin_products_frame.forget()
                    add_products_stock_frame.destroy()
                    add_stock_return_back.destroy()
                    add_stock_bg_label.destroy()
                    add_stock_frame.destroy()
                else:
                    tmsg.showerror('Error', '   Stock must be a number !   ')
                    e1.focus_set()
            submit_frame = Frame(add_stock_frame, highlightthickness=3, highlightbackground='black')
            submit_frame.place(x=99, y=504)
            button = Button(submit_frame, text='        S U B M I T        ', bg='black', fg='white', font=('Blogger_Sans-Bold', 10, 'bold'), activebackground='white', activeforeground='black', bd=0, cursor='hand2', command=add_stock_function)
            button.pack()
        def delete_action(delete_product_id=i):
            confirm_msg = tmsg.askyesno("Delete Product", "    Do you want to delete the product?    ")
            if confirm_msg:
                products_df = csv_read(r'products.csv')
                products_df.drop([delete_product_id], inplace=True)
                with open(r'products.csv', 'w+', newline='') as products_file:
                    products_file_write = csv.writer(products_file)
                    for j in products_df.index:
                        y = list(products_df.loc[j])
                        products_file_write.writerow(y)
                products_file.close()
                tmsg.showinfo('Successful', '    Product has been deleted successfully!    ')
                return_back()
            else:
                pass
        def add_products_stock_action_manual(add_product_stock_id=i):
            add_products_stock_action(add_product_stock_id)
        product_image = Label(products_bg_frame, image=product_img, bd=0)
        product_image.place(anchor=NW, x=200, y=20)
        product_image.image = product_img
        Label(products_bg_frame, textvariable=product_cost, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=700, y=30)
        Label(products_bg_frame, textvariable=product_stock, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=110)
        Label(products_bg_frame, textvariable=product_name, bg='white', fg='black', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=30)
        Label(products_bg_frame, textvariable=product_details, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=500, y=70)
        delete_button[i] = Button(products_bg_frame, image=delete_image, cursor="hand2", bd=0, command=delete_action)
        delete_button[i].place(anchor=NW, x=525, y=140)
        delete_button[i].image = delete_image
        add_products_stock[i] = Button(products_bg_frame, image=add_stock_image, cursor="hand2", bd=0, command=add_products_stock_action_manual)
        add_products_stock[i].place(anchor=NW, x=699, y=140)
        add_products_stock[i].image = add_stock_image
def admin_show_users():
    temp_frame = Frame(admin_users_frame, bg="white", bd=0)
    temp_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
    admin_show_users_frame_1 = Frame(temp_frame, bg='white', bd=0)
    admin_show_users_frame_1.pack(anchor=NW)
    admin_show_users_frame_2 = Frame(temp_frame, bg='white', bd=0)
    admin_show_users_frame_2.pack(anchor=NW, side=LEFT, fill=BOTH, expand=True)
    admin_show_users_temp_frame = Frame(admin_show_users_frame_2, bg='white', bd=0)
    admin_show_users_temp_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
    Label(admin_show_users_frame_1, bg="white").pack(padx=1000, pady=75)
    admin_canvas = Canvas(admin_show_users_temp_frame, bg='white')
    scrollbar = Scrollbar(admin_show_users_temp_frame, orient='vertical', bg='white', command=admin_canvas.yview)
    admin_scrollabel_frame = Frame(admin_canvas, bg='white')
    admin_scrollabel_frame.bind('<Configure>', lambda e: admin_canvas.configure(scrollregion=admin_canvas.bbox('all')))
    admin_canvas.create_window((0, 0), window=admin_scrollabel_frame, anchor=NW)
    admin_canvas.configure(yscrollcommand=scrollbar.set)
    admin_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    def return_back():
        frame2.forget()
        products_frame.forget()
        frame3.forget()
        frame4.forget()
        frame5.forget()
        frame6.forget()
        frame7.forget()
        frame8.forget()
        admin_frame.forget()
        admin_products_frame.forget()
        admin_users_frame.forget()
        admin_orders_frame.forget()
        admin_feedback_frame.forget()
        admin_change_password_frame.forget()
        admin_frame.pack(anchor=NW)
        temp_frame.destroy()
    img = image(r"images/return_icon.png", 40, 40)
    return_icon = Button(admin_show_users_frame_1, image=img, bd=0, cursor="hand2", command=return_back)
    return_icon.place(x=10, y=10)
    return_icon.image = img
    def on_enter(e):
        search_admin.delete(0, END)
        if search_admin.get() != 'Search...':
            search_admin['fg'] = "black"
    search_img = image(r"images/search_icon.png", 20, 20)
    search_admin_frame = Frame(admin_show_users_frame_1, height=5, width=182, bg="black")
    search_admin_frame.place(x=592, y=68)
    search_admin = Entry(admin_show_users_frame_1, fg="grey", bd=0, width=30)
    search_admin.place(x=592, y=54)
    search_admin.insert(0, "Search...")
    search_admin.bind("<FocusIn>", on_enter)
    def enter(e):
        temp_frame.forget()
        admin_users_frame.pack(anchor=NW)
        admin_user_search()
    search_admin.bind("<Return>", enter)
    search_btn = Button(admin_show_users_frame_1, image=search_img, bd=0, cursor="hand2", command=lambda: [temp_frame.forget(), admin_users_frame.pack(anchor=NW), admin_user_search()])
    search_btn.place(x=800, y=57)
    search_btn.image = search_img
    temp_frame_ = Frame(admin_users_frame, bd=0, bg='white')
    temp_frame_.pack_forget()
    def admin_user_search():
        temp_frame_.pack(side='left', anchor='nw', fill=BOTH, expand=True)
        admin_canvas_ = Canvas(temp_frame_, bg='white')
        scrollbar_ = Scrollbar(temp_frame_, orient='vertical', bg='white', command=admin_canvas_.yview)
        scrollabel_frame = Frame(admin_canvas_, bg='white')
        scrollabel_frame.bind('<Configure>', lambda e: admin_canvas_.configure(scrollregion=admin_canvas_.bbox('all')))
        admin_canvas_.create_window((0, 0), window=scrollabel_frame, anchor=NW)
        admin_canvas_.configure(yscrollcommand=scrollbar_.set)
        admin_canvas_.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar_.pack(side=RIGHT, fill=Y)
        img_ = image(r"images/return_icon.png", 40, 40)
        return_button = Button(scrollabel_frame, image=img_, bd=0, cursor="hand2", command=lambda: [temp_frame_.destroy(), return_back()])
        return_button.place(x=15, y=10)
        return_button.image = img_
        frame_img = image(r'images/big_frame_bg.jpg', 900, 200)
        location = r'users.csv'
        df_ = csv_read(location)
        for temp_row in range(15):
            Label(scrollabel_frame, bg='white', bd=0).grid(row=temp_row, column=0)
        row_ = 16
        for _ in df_.index:
            x_ = list(df_.loc[_])
            if search_admin.get().lower() == x_[0].lower():
                row_ += 1
                def add_users_balance_action_search(add_user_balance_id=_):
                    add_users_balance_action(add_user_balance_id)
                users_bg_frame_ = Frame(scrollabel_frame, bg='white', bd=0)
                users_bg_frame_.grid(row=row_, column=0, columnspan=8)
                users_bg_ = Label(users_bg_frame_, bg='white', bd=0, image=frame_img)
                users_bg_.pack(fill=BOTH, expand=True)
                users_bg_.image = frame_img
                user_id_ = StringVar()
                user_name_ = StringVar()
                user_age_ = StringVar()
                user_email_ = StringVar()
                user_address_ = StringVar()
                user_id_.set(f'ID : {_}')
                user_name_.set(f'Name : {x_[0]}')
                user_age_.set(f'Age : {x_[1]}')
                user_email_.set(f'Email : {x_[3]}')
                user_address_.set(f'Address : {x_[4]}')
                user_img_ = image(r'images/user_icon.jpg', 132, 132)
                user_image_ = Label(users_bg_frame_, image=user_img_, bd=0)
                user_image_.place(anchor=NW, x=200, y=20)
                user_image_.image = user_img_
                Label(users_bg_frame_, textvariable=user_age_, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=700, y=30)
                Label(users_bg_frame_, textvariable=user_email_, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=70)
                Label(users_bg_frame_, textvariable=user_name_, bg='white', fg='black', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=30)
                Label(users_bg_frame_, textvariable=user_address_, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=500, y=110)
                add_users_balance[_] = Button(users_bg_frame_, text="Add Balance", bg="black", fg="white", font=("Blogger_Sans", 8, "bold"), cursor="hand2", bd=0, command=add_users_balance_action_search)
                add_users_balance[_].place(anchor=NW, x=699, y=140)
    df = csv_read(r'users.csv')
    row = 0
    add_users_balance = {}
    Label(admin_show_users_frame_1, text='Users', bg='white', bd=0, font=("Blooger_Sans-Bold", 24, "bold")).place(x=20, y=120)
    users_bg_image = image(r'images/big_frame_bg.jpg', 900, 200)
    for i in df.index:
        row += 1
        users_bg_frame = Frame(admin_scrollabel_frame, bg='white', bd=0)
        users_bg_frame.grid(row=row, column=0, columnspan=8)
        users_bg = Label(users_bg_frame, bg='white', bd=0, image=users_bg_image)
        users_bg.pack(fill=BOTH, expand=True)
        users_bg.image = users_bg_image
        x = list(df.loc[i])
        user_id = StringVar()
        user_name = StringVar()
        user_age = StringVar()
        user_address = StringVar()
        user_email = StringVar()
        user_id.set(f'ID : {i}')
        user_name.set(f'Name : {x[0]}')
        user_age.set(f'Age : {x[1]}')
        user_address.set(f'Address : {x[4]}')
        user_email.set(f'Email : {x[3]}')
        user_img = image(r'images/user_icon.jpg', 132, 132)
        def add_users_balance_action(add_user_balance_id):
            temp_frame_.destroy()
            temp_frame.destroy()
            add_users_balance_frame = Frame(admin_users_frame, bg="white", bd=0)
            add_users_balance_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
            add_balance_bg = image(r'images/login_bg.jpg', 1400, 850)
            add_balance_bg_label = Label(add_users_balance_frame, image=add_balance_bg, bd=0)
            add_balance_bg_label.place(x=-10, y=-10)
            add_balance_bg_label.image = add_balance_bg
            add_balance_frame = Frame(add_users_balance_frame, highlightthickness=5, highlightbackground='black', bg='white')
            add_balance_frame.pack(padx=450, pady=40)
            def add_balance_return_back():
                frame2.forget()
                products_frame.forget()
                frame3.forget()
                frame4.forget()
                frame5.forget()
                frame6.forget()
                frame7.forget()
                frame8.forget()
                admin_frame.forget()
                admin_products_frame.forget()
                admin_users_frame.forget()
                admin_orders_frame.forget()
                admin_feedback_frame.forget()
                admin_change_password_frame.forget()
                admin_frame.pack(anchor=NW)
                add_users_balance_frame.destroy()
                add_balance_return_back.destroy()
                add_balance_bg_label.destroy()
                add_balance_frame.destroy()
            add_balance_return_back = Button(add_users_balance_frame, image=img, bd=0, cursor="hand2", command=add_balance_return_back)
            add_balance_return_back.place(x=10, y=10)
            add_balance_return_back.image = img
            add_balance_label = Label(add_balance_frame, text="ADD balance", bd=0, bg='white', fg='black', font=('Helvetica bold', 20))
            add_balance_label.pack(padx=100, pady=50, side=TOP)
            Label(add_balance_frame).pack(padx=380, pady=600)
            def on_enter_e1(e):
                if e1.get() == 'Enter amount to be added...':
                    e1.delete(0, END)
            def on_leave_e1(e):
                if e1.get() == '':
                    e1.insert(0, 'Enter amount to be added...')
            def on_return_e1(e):
                add_balance_function()
            for c in df.index:
                if add_user_balance_id == c:
                    z = list(df.loc[c])
                    add_user_img = image(r'images/user_icon.jpg', 132, 132)
                    add_user_image = Label(add_balance_frame, image=add_user_img, bd=0)
                    add_user_image.place(anchor=NW, x=10, y=170)
                    add_user_image.image = add_user_img
                    Label(add_balance_frame, text=f'Name : {z[0]}', bg='white', fg='black', font=('Amaranth-Regular', 8)).place(anchor=W, x=155, y=200)
                    Label(add_balance_frame, text=f'Age : {z[1]}', bg='white', font=('Amaranth-Regular', 8)).place(anchor=W, x=155, y=220)
                    Label(add_balance_frame, text=f'Address : {z[4]}', bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=155, y=240)
                    Label(add_balance_frame, text=f'Email : {z[3]}', bg='white', font=('Amaranth-Regular', 8)).place(x=220, y=210)
            balance_icon = Label(add_balance_frame, bd=0, bg="white", text="₹")
            balance_icon.place(x=90, y=431)
            balance_label = Label(add_balance_frame, bd=0, text='Add balance', bg='white', fg='grey')
            balance_label.place(x=90, y=409)
            e1 = Entry(add_balance_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
            e1.place(x=110, y=431)
            e1.insert(0, 'Enter amount to be added...')
            e1.bind('<FocusIn>', on_enter_e1)
            e1.bind('<FocusOut>', on_leave_e1)
            e1.bind('<Return>', on_return_e1)
            Frame(add_balance_frame, width=259, height=3, bg='black', bd=0).place(x=90, y=446)
            def add_balance_function():
                if e1.get().isdigit():
                    new_balance = int(int(z[8]) + int(e1.get()))
                    df.at[add_user_balance_id, 8] = new_balance
                    with open(r'users.csv', 'w', newline='') as users_file:
                        users_file_write = csv.writer(users_file)
                        for d in df.index:
                            e = list(df.loc[d])
                            users_file_write.writerow(e)
                    users_file.close()
                    tmsg.showinfo('Successful', "    User's balance has been updated successfully!    ")
                    admin_frame.pack(anchor=NW)
                    admin_users_frame.forget()
                    add_users_balance_frame.destroy()
                    add_balance_return_back.destroy()
                    add_balance_bg_label.destroy()
                    add_balance_frame.destroy()
                else:
                    tmsg.showerror('Error', '   Balance must be a number !   ')
                    e1.focus_set()
            submit_frame = Frame(add_balance_frame, highlightthickness=3, highlightbackground='black')
            submit_frame.place(x=99, y=504)
            button = Button(submit_frame, text='        S U B M I T        ', bg='black', fg='white', font=('Blogger_Sans-Bold', 10, 'bold'), activebackground='white', activeforeground='black', bd=0, cursor='hand2', command=add_balance_function)
            button.pack()
        def add_users_balance_action_manual(add_user_balance_id=i):
            add_users_balance_action(add_user_balance_id)
        user_image = Label(users_bg_frame, image=user_img, bd=0)
        user_image.place(anchor=NW, x=200, y=20)
        user_image.image = user_img
        Label(users_bg_frame, textvariable=user_age, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=700, y=30)
        Label(users_bg_frame, textvariable=user_email, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=70)
        Label(users_bg_frame, textvariable=user_name, bg='white', fg='black', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=30)
        Label(users_bg_frame, textvariable=user_address, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=500, y=110)
        add_users_balance[i] = Button(users_bg_frame, text="Add Balance", bg="black", fg="white", font=("Blogger_Sans", 8, "bold"), cursor="hand2", bd=0, command=add_users_balance_action_manual)
        add_users_balance[i].place(anchor=NW, x=699, y=140)
def admin_show_orders():
    temp_frame = Frame(admin_orders_frame, bg="white", bd=0)
    temp_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
    admin_show_orders_frame_1 = Frame(temp_frame, bg='white', bd=0)
    admin_show_orders_frame_1.pack(anchor=NW)
    admin_show_orders_frame_2 = Frame(temp_frame, bg='white', bd=0)
    admin_show_orders_frame_2.pack(anchor=NW, side=LEFT, fill=BOTH, expand=True)
    admin_show_orders_temp_frame = Frame(admin_show_orders_frame_2, bg='white', bd=0)
    admin_show_orders_temp_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
    Label(admin_show_orders_frame_1, bg="white").pack(padx=1000, pady=75)
    admin_canvas = Canvas(admin_show_orders_temp_frame, bg='white')
    scrollbar = Scrollbar(admin_show_orders_temp_frame, orient='vertical', bg='white', command=admin_canvas.yview)
    admin_scrollabel_frame = Frame(admin_canvas, bg='white')
    admin_scrollabel_frame.bind('<Configure>', lambda e: admin_canvas.configure(scrollregion=admin_canvas.bbox('all')))
    admin_canvas.create_window((0, 0), window=admin_scrollabel_frame, anchor=NW)
    admin_canvas.configure(yscrollcommand=scrollbar.set)
    admin_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    def return_back():
        frame2.forget()
        products_frame.forget()
        frame3.forget()
        frame4.forget()
        frame5.forget()
        frame6.forget()
        frame7.forget()
        frame8.forget()
        admin_frame.forget()
        admin_products_frame.forget()
        admin_users_frame.forget()
        admin_orders_frame.forget()
        admin_feedback_frame.forget()
        admin_change_password_frame.forget()
        admin_frame.pack(anchor=NW)
        temp_frame.destroy()
    img = image(r"images/return_icon.png", 40, 40)
    return_icon = Button(admin_show_orders_frame_1, image=img, bd=0, cursor="hand2", command=return_back)
    return_icon.place(x=10, y=10)
    return_icon.image = img
    def on_enter(e):
        search_admin.delete(0, END)
        if search_admin.get() != 'Search...':
            search_admin['fg'] = "black"
    search_img = image(r"images/search_icon.png", 20, 20)
    search_admin_frame = Frame(admin_show_orders_frame_1, height=5, width=182, bg="black")
    search_admin_frame.place(x=592, y=68)
    search_admin = Entry(admin_show_orders_frame_1, fg="grey", bd=0, width=30)
    search_admin.place(x=592, y=54)
    search_admin.insert(0, "Search...")
    search_admin.bind("<FocusIn>", on_enter)
    def enter(e):
        temp_frame.forget()
        admin_orders_frame.pack(anchor=NW)
        admin_orders_search()
    search_admin.bind("<Return>", enter)
    search_btn = Button(admin_show_orders_frame_1, image=search_img, bd=0, cursor="hand2", command=lambda: [temp_frame.forget(), admin_orders_frame.pack(anchor=NW), admin_orders_search()])
    search_btn.place(x=800, y=57)
    search_btn.image = search_img
    temp_frame_ = Frame(admin_orders_frame, bd=0, bg='white')
    temp_frame_.pack_forget()
    def admin_orders_search():
        temp_frame_.pack(side='left', anchor='nw', fill=BOTH, expand=True)
        admin_canvas_ = Canvas(temp_frame_, bg='white')
        scrollbar_ = Scrollbar(temp_frame_, orient='vertical', bg='white', command=admin_canvas_.yview)
        scrollabel_frame = Frame(admin_canvas_, bg='white')
        scrollabel_frame.bind('<Configure>', lambda e: admin_canvas_.configure(scrollregion=admin_canvas_.bbox('all')))
        admin_canvas_.create_window((0, 0), window=scrollabel_frame, anchor=NW)
        admin_canvas_.configure(yscrollcommand=scrollbar_.set)
        admin_canvas_.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar_.pack(side=RIGHT, fill=Y)
        img_ = image(r"images/return_icon.png", 40, 40)
        return_button = Button(scrollabel_frame, image=img_, bd=0, cursor="hand2", command=lambda: [temp_frame_.destroy(), return_back()])
        return_button.place(x=15, y=10)
        return_button.image = img_
        frame_img = image(r'images/big_frame_bg.jpg', 900, 200)
        location = r'orders.csv'
        df_ = csv_read(location)
        for temp_row in range(15):
            Label(scrollabel_frame, bg='white', bd=0).grid(row=temp_row, column=0)
        row_ = 16
        for _ in df_.index:
            x_ = list(df_.loc[_])
            if search_admin.get().lower() == x_[3].lower():
                row_ += 1
                orders_bg_frame_ = Frame(scrollabel_frame, bg='white', bd=0)
                orders_bg_frame_.grid(row=row_, column=0, columnspan=8)
                orders_bg_ = Label(orders_bg_frame_, bg='white', bd=0, image=frame_img)
                orders_bg_.pack(fill=BOTH, expand=True)
                orders_bg_.image = frame_img
                orders_qty_total_amt_id_payment_mode_ = StringVar()
                orders_name_ = StringVar()
                orders_product_id_ = StringVar()
                orders_address_ = StringVar()
                orders_email_ = StringVar()
                orders_purchase_date_time_ = StringVar()
                orders_qty_total_amt_id_payment_mode_.set(f'Qty : {x_[1]} pc(s)    Amt : ₹ {x_[2]}    Order ID : {_}    Payment Mode : {x_[12]}')
                orders_name_.set(f'Name : {x_[3]}')
                orders_product_id_.set(f'Product ID : {x_[0]}')
                orders_address_.set(f'Address : {x_[7]} \nPincode : {x_[8]}')
                orders_email_.set(f'Email : {x_[6]}')
                orders_purchase_date_time_.set(f'Payment Date : {x_[9]}\tPayment Time : {x_[10]}')
                orders_img_ = image(r'images/user_icon.jpg', 132, 132)
                orders_image_ = Label(orders_bg_frame_, image=orders_img_, bd=0)
                orders_image_.place(anchor=NW, x=200, y=20)
                orders_image_.image = orders_img_
                Label(orders_bg_frame_, textvariable=orders_product_id_, bg='white',font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=700, y=30)
                Label(orders_bg_frame_, textvariable=orders_email_, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=70)
                Label(orders_bg_frame_, textvariable=orders_name_, bg='white', fg='black', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=30)
                Label(orders_bg_frame_, textvariable=orders_address_, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=500, y=110)
                Label(orders_bg_frame_, textvariable=orders_qty_total_amt_id_payment_mode_, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=500, y=150)
                Label(orders_bg_frame_, textvariable=orders_purchase_date_time_, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=500, y=180)
    df = csv_read(r'orders.csv')
    row = 0
    Label(admin_show_orders_frame_1, text='orders', bg='white', bd=0, font=("Blooger_Sans-Bold", 24, "bold")).place(x=20, y=120)
    orders_bg_image = image(r'images/big_frame_bg.jpg', 900, 200)
    for i in df.index:
        row += 1
        orders_bg_frame = Frame(admin_scrollabel_frame, bg='white', bd=0)
        orders_bg_frame.grid(row=row, column=0, columnspan=8)
        orders_bg = Label(orders_bg_frame, bg='white', bd=0, image=orders_bg_image)
        orders_bg.pack(fill=BOTH, expand=True)
        orders_bg.image = orders_bg_image
        x = list(df.loc[i])
        orders_qty_total_amt_id_payment_mode = StringVar()
        orders_name = StringVar()
        orders_product_id = StringVar()
        orders_address = StringVar()
        orders_email = StringVar()
        orders_purchase_date_time = StringVar()
        orders_qty_total_amt_id_payment_mode.set(f'Qty : {x[1]} pc(s)    Amt : ₹ {x[2]}    Order ID : {i}    Payment Mode : {x[12]}')
        orders_name.set(f'Name : {x[3]}')
        orders_product_id.set(f'Product ID : {x[0]}')
        orders_address.set(f'Address : {x[7]} \nPincode : {x[8]}')
        orders_email.set(f'Email : {x[6]}')
        orders_purchase_date_time.set(f'Payment Date : {x[9]}\tPayment Time : {x[10]}')
        orders_img = image(r'images/user_icon.jpg', 132, 132)
        orders_image = Label(orders_bg_frame, image=orders_img, bd=0)
        orders_image.place(anchor=NW, x=200, y=20)
        orders_image.image = orders_img
        Label(orders_bg_frame, textvariable=orders_product_id, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=700, y=30)
        Label(orders_bg_frame, textvariable=orders_email, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=70)
        Label(orders_bg_frame, textvariable=orders_name, bg='white', fg='black', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=30)
        Label(orders_bg_frame, textvariable=orders_address, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=500, y=110)
        Label(orders_bg_frame, textvariable=orders_qty_total_amt_id_payment_mode, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=500, y=150)
        Label(orders_bg_frame, textvariable=orders_purchase_date_time, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=500, y=180)
def admin_show_feedback():
    temp_frame = Frame(admin_feedback_frame, bg="white", bd=0)
    temp_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
    admin_show_feedback_frame_1 = Frame(temp_frame, bg='white', bd=0)
    admin_show_feedback_frame_1.pack(anchor=NW)
    admin_show_feedback_frame_2 = Frame(temp_frame, bg='white', bd=0)
    admin_show_feedback_frame_2.pack(anchor=NW, side=LEFT, fill=BOTH, expand=True)
    admin_show_feedback_temp_frame = Frame(admin_show_feedback_frame_2, bg='white', bd=0)
    admin_show_feedback_temp_frame.pack(side='left', anchor='nw', fill=BOTH, expand=True)
    Label(admin_show_feedback_frame_1, bg="white").pack(padx=1000, pady=75)
    admin_canvas = Canvas(admin_show_feedback_temp_frame, bg='white')
    scrollbar = Scrollbar(admin_show_feedback_temp_frame, orient='vertical', bg='white', command=admin_canvas.yview)
    admin_scrollabel_frame = Frame(admin_canvas, bg='white')
    admin_scrollabel_frame.bind('<Configure>', lambda e: admin_canvas.configure(scrollregion=admin_canvas.bbox('all')))
    admin_canvas.create_window((0, 0), window=admin_scrollabel_frame, anchor=NW)
    admin_canvas.configure(yscrollcommand=scrollbar.set)
    admin_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    def return_back():
        frame2.forget()
        products_frame.forget()
        frame3.forget()
        frame4.forget()
        frame5.forget()
        frame6.forget()
        frame7.forget()
        frame8.forget()
        admin_frame.forget()
        admin_products_frame.forget()
        admin_users_frame.forget()
        admin_orders_frame.forget()
        admin_feedback_frame.forget()
        admin_change_password_frame.forget()
        admin_frame.pack(anchor=NW)
        temp_frame.destroy()
    img = image(r"images/return_icon.png", 40, 40)
    return_icon = Button(admin_show_feedback_frame_1, image=img, bd=0, cursor="hand2", command=return_back)
    return_icon.place(x=10, y=10)
    return_icon.image = img
    def on_enter(e):
        search_admin.delete(0, END)
        if search_admin.get() != 'Search...':
            search_admin['fg'] = "black"
    search_img = image(r"images/search_icon.png", 20, 20)
    search_admin_frame = Frame(admin_show_feedback_frame_1, height=5, width=182, bg="black")
    search_admin_frame.place(x=592, y=68)
    search_admin = Entry(admin_show_feedback_frame_1, fg="grey", bd=0, width=30)
    search_admin.place(x=592, y=54)
    search_admin.insert(0, "Search...")
    search_admin.bind("<FocusIn>", on_enter)
    def enter(e):
        temp_frame.forget()
        admin_feedback_frame.pack(anchor=NW)
        admin_feedback_search()
    search_admin.bind("<Return>", enter)
    search_btn = Button(admin_show_feedback_frame_1, image=search_img, bd=0, cursor="hand2", command=lambda: [temp_frame.forget(), admin_feedback_frame.pack(anchor=NW), admin_feedback_search()])
    search_btn.place(x=800, y=57)
    search_btn.image = search_img
    temp_frame_ = Frame(admin_feedback_frame, bd=0, bg='white')
    temp_frame_.pack_forget()
    def admin_feedback_search():
        temp_frame_.pack(side='left', anchor='nw', fill=BOTH, expand=True)
        admin_canvas_ = Canvas(temp_frame_, bg='white')
        scrollbar_ = Scrollbar(temp_frame_, orient='vertical', bg='white', command=admin_canvas_.yview)
        scrollabel_frame = Frame(admin_canvas_, bg='white')
        scrollabel_frame.bind('<Configure>', lambda e: admin_canvas_.configure(scrollregion=admin_canvas_.bbox('all')))
        admin_canvas_.create_window((0, 0), window=scrollabel_frame, anchor=NW)
        admin_canvas_.configure(yscrollcommand=scrollbar_.set)
        admin_canvas_.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar_.pack(side=RIGHT, fill=Y)
        img_ = image(r"images/return_icon.png", 40, 40)
        return_button = Button(scrollabel_frame, image=img_, bd=0, cursor="hand2", command=lambda: [temp_frame_.destroy(), return_back()])
        return_button.place(x=15, y=10)
        return_button.image = img_
        frame_img = image(r'images/big_frame_bg.jpg', 900, 200)
        location = r'feedback.csv'
        df_ = csv_read(location)
        feedback_img_ = image(r'images/user_icon.jpg', 132, 132)
        for temp_row in range(15):
            Label(scrollabel_frame, bg='white', bd=0).grid(row=temp_row, column=0)
        row_ = 16
        for i in df_.index:
            x_ = list(df_.loc[i])
            if search_admin.get().lower() == x_[0].lower():
                row_ += 1
                feedback_bg_frame_ = Frame(scrollabel_frame, bg='white', bd=0)
                feedback_bg_frame_.grid(row=row_, column=0, columnspan=8)
                feedback_bg_ = Label(feedback_bg_frame_, bg='white', bd=0, image=frame_img)
                feedback_bg_.pack(fill=BOTH, expand=True)
                feedback_bg_.image = frame_img
                feedback_id_ = StringVar()
                feedback_name_ = StringVar()
                feedback_type_ = StringVar()
                feedback_email_ = StringVar()
                feedback_report_ = StringVar()
                feedback_id_.set(f'ID : {i}')
                feedback_name_.set(f'Name : {x_[0]}')
                feedback_type_.set(f'Type : {x_[2]}')
                feedback_email_.set(f'Email : {x_[1]}')
                feedback_report_.set(f'Report : {x_[3]}')
                feedback_image_ = Label(feedback_bg_frame_, image=feedback_img_, bd=0)
                feedback_image_.place(anchor=NW, x=200, y=20)
                feedback_image_.image = feedback_img_
                Label(feedback_bg_frame_, textvariable=feedback_type_, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W,  x=700, y=30)
                Label(feedback_bg_frame_, textvariable=feedback_email_, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=70)
                Label(feedback_bg_frame_, textvariable=feedback_name_, bg='white', fg='black', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=30)
                Label(feedback_bg_frame_, textvariable=feedback_report_, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W,  x=500, y=110)
    df = csv_read(r'feedback.csv')
    row = 0
    Label(admin_show_feedback_frame_1, text='Feedback', bg='white', bd=0, font=("Blooger_Sans-Bold", 24, "bold")).place(x=20, y=120)
    feedback_bg_image = image(r'images/big_frame_bg.jpg', 900, 200)
    for i in df.index:
        row += 1
        feedback_bg_frame = Frame(admin_scrollabel_frame, bg='white', bd=0)
        feedback_bg_frame.grid(row=row, column=0, columnspan=8)
        feedback_bg = Label(feedback_bg_frame, bg='white', bd=0, image=feedback_bg_image)
        feedback_bg.pack(fill=BOTH, expand=True)
        feedback_bg.image = feedback_bg_image
        x = list(df.loc[i])
        feedback_id = StringVar()
        feedback_name = StringVar()
        feedback_type = StringVar()
        feedback_report = StringVar()
        feedback_email = StringVar()
        feedback_id.set(f'ID : {i}')
        feedback_name.set(f'Name : {x[0]}')
        feedback_type.set(f'Type : {x[2]}')
        feedback_report.set(f'Report : {x[3]}')
        feedback_email.set(f'Email : {x[1]}')
        feedback_img = image(r'images/user_icon.jpg', 132, 132)
        feedback_image = Label(feedback_bg_frame, image=feedback_img, bd=0)
        feedback_image.place(anchor=NW, x=200, y=20)
        feedback_image.image = feedback_img
        Label(feedback_bg_frame, textvariable=feedback_type, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=700, y=30)
        Label(feedback_bg_frame, textvariable=feedback_email, bg='white', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=70)
        Label(feedback_bg_frame, textvariable=feedback_name, bg='white', fg='black', font=('ABeeZee-Regular', 10, 'bold')).place(anchor=W, x=500, y=30)
        Label(feedback_bg_frame, textvariable=feedback_report, bg='white', fg='#777777', font=('Amaranth-Regular', 8)).place(anchor=W, x=500, y=110)
def admin_change_password():
    change_password_bg = image(r'images/login_bg.jpg', 1400, 850)
    change_password_bg_label = Label(admin_change_password_frame, image=change_password_bg, bd=0)
    change_password_bg_label.place(x=-10, y=-10)
    change_password_bg_label.image = change_password_bg
    change_password_frame = Frame(admin_change_password_frame, highlightthickness=5, highlightbackground='black', bg='white')
    change_password_frame.pack(padx=450, pady=40)
    def return_back_of_change_password():
        return_back_of_change_password_return_icon.destroy()
        change_password_bg_label.destroy()
        change_password_frame.destroy()
        admin_change_password_frame.forget()
        admin()
        admin_frame.pack(anchor=NW)
    return_back_of_change_password_img = image(r"images/return_icon.png", 40, 40)
    return_back_of_change_password_return_icon = Button(admin_change_password_frame, image=return_back_of_change_password_img, bd=0, cursor="hand2", command=return_back_of_change_password)
    return_back_of_change_password_return_icon.place(x=10, y=10)
    return_back_of_change_password_return_icon.image = return_back_of_change_password_img
    change_password_label = Label(change_password_frame, text="CHANGE PASSWORD", bd=0, bg='white', fg='black', font=('Helvetica bold', 20))
    change_password_label.pack(padx=65, pady=50, side=TOP)
    def on_enter_e1(e):
        if e1.get() == 'Type your current password':
            e1.delete(0, END)
    def on_leave_e1(e):
        if e1.get() == '':
            e1.insert(0, 'Type your current password')
    def on_return_e1(e):
        e2.focus_set()
    def on_enter_e2(e):
        if e2.get() == 'Type your new password':
            e2.delete(0, END)
    def on_leave_e2(e):
        if e2.get() == '':
            e2.insert(0, 'Type your new password')
    def on_return_e2(e):
        change_admin_password_command()
        change_password_frame.forget()
        return_back_of_change_password()
    admin_img = image(r'images/user_icon.jpg', 20, 20)
    admin_icon = Label(change_password_frame, bd=0, image=admin_img)
    admin_icon.place(x=90, y=212)
    admin_icon.image = admin_img
    password_label = Label(change_password_frame, bd=0, text='Password', bg='white', fg='grey')
    password_label.place(x=90, y=192)
    e1 = Entry(change_password_frame, bd=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    e1.pack(padx=110, pady=80)
    e1.insert(0, 'Type your current password')
    e1.bind('<FocusIn>', on_enter_e1)
    e1.bind('<FocusOut>', on_leave_e1)
    e1.bind('<Return>', on_return_e1)
    Frame(change_password_frame, width=259, height=3, bg='black', bd=0).place(x=90, y=229)
    new_password_label = Label(change_password_frame, bd=0, text='New Password', bg='white', fg='grey')
    new_password_label.place(x=90, y=369)
    e2 = Entry(change_password_frame, borderwidth=0, font=('consoles', 8), fg='grey', bg='white', width=40)
    e2.pack(padx=110, pady=80)
    e2.insert(0, 'Type your new password')
    e2.bind('<FocusIn>', on_enter_e2)
    e2.bind('<FocusOut>', on_leave_e2)
    e2.bind('<Return>', on_return_e2)
    Frame(change_password_frame, width=259, height=3, bg='black', bd=0).place(x=90, y=406)
    df = csv_read(r'admin_login.csv')
    for i in df.index:
        y = list(df.loc[i])
    def change_admin_password_command():
        if str(e2.get()) != 'Type your new password':
            if str(e1.get()) == str(y[1]):
                csv_write(r'admin_login.csv', 'w+', [str(y[0]), str(e2.get())])
                tmsg.showinfo('Successfully', 'You have changed your password successfully')
                return_back_of_change_password()
            else:
                tmsg.showerror('Error', '   You have entered wrong password !   ')
                e1.focus_set()
        else:
            tmsg.showerror('Error', '   Please enter your new password !   ')
            e2.focus_set()
    Button(change_password_frame, bg='black', fg='white', bd=0, font=('Blogger_Sans-Bold', 12, 'bold'), text='    CHANGE PASSWORD    ', cursor='hand2', command=change_admin_password_command).place(x=108, y=464)
    Label(change_password_frame).pack(pady=600)
sign_in_as_admin_image = image(r'images\sign_in_as_admin_icon.jpg', 180, 29)
sign_in_as_admin_button = Button(frame1, image=sign_in_as_admin_image, bg='white', cursor='hand2', bd=0, command=lambda: [frame1.forget(), frame2.forget(), admin_login(), admin_login_frame.pack(anchor=W)])
sign_in_as_admin_button.place(x=1150, y=2)
sign_in_as_admin_button.image = sign_in_as_admin_image

if __name__ == "__main__":
    user()
    root.mainloop()
