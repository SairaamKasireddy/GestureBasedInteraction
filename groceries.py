import time
from tkinter import *
import random
import cv2
from pygame import mixer

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width=1400, height=800)
        self.root.minsize(width=1300, height=700)
        self.root.title("Grocery Billing System")

        x = random.randint(1000, 9999)
        self.c_bill_no = StringVar()
        self.c_bill_no.set(str(x))

        self.bread = IntVar()
        self.candy = IntVar()
        self.hamburger = IntVar()
        self.hotdog = IntVar()
        self.rice = IntVar()
        self.salt = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.total_food = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()

        bg_color = "green"
        fg_color = "white"
        lbl_color = 'white'

        title = Label(self.root, text="Grocery Billing System", bd=12, relief=GROOVE, fg=fg_color, bg=bg_color,
                      font=("times new roman", 30, "bold"), pady=3).pack(fill=X)

        F1 = LabelFrame(text="Options", font=("time new roman", 12, "bold"), fg="gold", bg=bg_color, relief=GROOVE,
                        bd=10)
        F1.place(x=0, y=80, relwidth=1)

        cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
        cbill_en.grid(row=0, column=3, ipadx=0, ipady=4, pady=5)

        F2 = LabelFrame(self.root, text='Food', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F2.place(x=0, y=160, width=325, height=310)

        # bread
        bread_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Bread")
        bread_lbl.grid(row=0, column=0, padx=10, pady=20)
        bread_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.bread)
        bread_en.grid(row=0, column=1, ipady=5, ipadx=5)
        # bread_en.focus()
        bread_en.focus_set()

        # Candy
        candy_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Candy")
        candy_lbl.grid(row=1, column=0, padx=10, pady=20)
        candy_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.candy)
        candy_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # Hamburger
        ham_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Hamburger")
        ham_lbl.grid(row=2, column=0, padx=10, pady=20)
        ham_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.hamburger)
        ham_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # Hotdog
        hotdog_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Hotdog")
        hotdog_lbl.grid(row=3, column=0, padx=10, pady=20)
        hotdog_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.hotdog)
        hotdog_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # frame 1
        F2 = LabelFrame(self.root, text='Grocery', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F2.place(x=320, y=160, width=325, height=310)

        # Frame Content
        rice_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rice")
        rice_lbl.grid(row=0, column=0, padx=10, pady=20)
        rice_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.rice)
        rice_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # Oil
        oil_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Food Oil")
        oil_lbl.grid(row=1, column=0, padx=10, pady=20)
        oil_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.food_oil)
        oil_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # Salt
        salt_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Salt")
        salt_lbl.grid(row=2, column=0, padx=10, pady=20)
        salt_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.salt)
        salt_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # Wheat
        wheat_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Wheat")
        wheat_lbl.grid(row=3, column=0, padx=10, pady=20)
        wheat_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.wheat)
        wheat_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ==================Other Stuff=====================#

        F2 = LabelFrame(self.root, text='Others', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F2.place(x=645, y=160, width=325, height=310)

        # ===========Frame Content

        cosm_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Food")
        cosm_lbl.grid(row=0, column=0, padx=10, pady=20)
        cosm_en = Entry(F2, bd=8, relief=GROOVE, width=10, textvariable=self.total_food)
        cosm_en.grid(row=0, column=1, ipady=5, ipadx=5)

        gro_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Grocery")
        gro_lbl.grid(row=3, column=0, padx=10, pady=20)
        gro_en = Entry(F2, bd=8, relief=GROOVE, width=10, textvariable=self.total_grocery)
        gro_en.grid(row=3, column=1, ipady=5, ipadx=5)

        cosmt_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Food Tax")
        cosmt_lbl.grid(row=4, column=0, padx=30, pady=20)
        cosmt_en = Entry(F2, bd=8, relief=GROOVE, width=10, textvariable=self.tax_cos)
        cosmt_en.grid(row=4, column=1, ipady=2, ipadx=5)

        grot_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Grocery Tax")
        grot_lbl.grid(row=5, column=0, padx=30, pady=20)
        grot_en = Entry(F2, bd=8, relief=GROOVE, width=10, textvariable=self.tax_groc)
        grot_en.grid(row=5, column=1, ipady=1, ipadx=5)


        # ===================Bill Aera================#
        F3 = Label(self.root, bd=10, relief=GROOVE)
        F3.place(x=950, y=160, width=325, height=310)
        bill_title = Label(F3, text="Bill", font=("Lucida", 13, "bold"), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txt = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # ===========Buttons Frame=============#
        F4 = LabelFrame(self.root, text='', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F4.place(x=0, y=470, relwidth=1, height=445)

        clear_btn = Button(F1, text="    Clear    ", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.clear)
        clear_btn.grid(row=0, column=1, ipadx=20, padx=50)

        genbill_btn = Button(F1, text="Generate Bill", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                             relief=GROOVE, command=self.total)
        genbill_btn.grid(row=0, column=2, ipadx=20, padx=50)

        audio_btn = Button(F1, text="AudioHelp", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                           relief=GROOVE, command=self.audio)
        audio_btn.grid(row=0, column=3, ipadx=20, padx=50)

        instructions_btn = Button(F1, text="Instructions", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                           relief=GROOVE, command=self.inst)
        instructions_btn.grid(row=0, column=4, ipadx=20, padx=50)

        exit_btn = Button(F1, text="   Exit   ", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                          command=self.exit)
        exit_btn.grid(row=0, column=5, ipadx=30, padx=50)

    # Function to get total prices
    def total(self):
        # =================Total Food Prices
        self.total_food_prices = (
                (self.bread.get() * 1) +
                (self.candy.get() * 3) +
                (self.hamburger.get() * 8) +
                (self.hotdog.get() * 6)
        )
        self.total_food.set("$" + str(self.total_food_prices))
        self.tax_cos.set("$" + str(round(self.total_food_prices * 0.05)))
        # ====================Total Grocery Prices
        self.total_grocery_prices = (
                (self.wheat.get() * 1) +
                (self.food_oil.get() * 5) +
                (self.salt.get() * 1) +
                (self.rice.get() * 3)
        )
        self.total_grocery.set("$" + str(self.total_grocery_prices))
        self.tax_groc.set("$" + str(round(self.total_grocery_prices * 0.05)))
        self.bill_area()

    # Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "       Welcome!\n")
        self.txt.insert(END, f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, "\nProduct          Qty         Price")
        self.txt.insert(END, "\n===================================")

    # Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0', END)

    # Add Product name , qty and price to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.bread.get() != 0:
            self.txt.insert(END, f"\nBread             {self.bread.get()}           {self.bread.get() * 1}")
        if self.candy.get() != 0:
            self.txt.insert(END, f"\nCandy             {self.candy.get()}           {self.candy.get() * 3}")
        if self.hamburger.get() != 0:
            self.txt.insert(END, f"\nHamburger         {self.hamburger.get()}           {self.hamburger.get() * 8}")
        if self.hotdog.get() != 0:
            self.txt.insert(END, f"\nHotdog            {self.hotdog.get()}           {self.hotdog.get() * 6}")
        if self.wheat.get() != 0:
            self.txt.insert(END, f"\nWheat             {self.wheat.get()}           {self.wheat.get() * 1}")
        if self.food_oil.get() != 0:
            self.txt.insert(END, f"\nFood Oil          {self.food_oil.get()}           {self.food_oil.get() * 5}")
        if self.salt.get() != 0:
            self.txt.insert(END, f"\nSalt              {self.salt.get()}           {self.salt.get() * 1}")
        if self.rice.get() != 0:
            self.txt.insert(END, f"\nRice              {self.rice.get()}           {self.rice.get() * 3}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END,
                        f"\n                      Total : ${self.total_food_prices + self.total_grocery_prices + self.total_other_prices + self.total_food_prices * 0.05 + self.total_grocery_prices * 0.05 + self.total_other_prices * 0.05}")

    def exit(self):
        self.root.destroy()

    def inst(self):
        help_img = cv2.imread('help.jpeg')
        print(help_img.shape)
        cv2.imshow('help', help_img)
        cv2.moveWindow('help', 50, 50)

    def audio(self):
        mixer.init()
        mixer.music.load('help_audio.mp3')
        mixer.music.play()


root = Tk()
object = Bill_App(root)
root.mainloop()