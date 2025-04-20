def Easterbun():
    if check_internet_connection():
        def get_easter_date(year):
            a = year % 19
            b = year // 100
            c = year % 100
            d = b // 4
            e = b % 4
            f = (b + 8) // 25
            g = (b - f + 1) // 3
            h = (19 * a + b - d - g + 15) % 30
            i = c // 4
            k = c % 4
            l = (32 + 2 * e + 2 * i - h - k) % 7
            m = (a + 11 * h + 22 * l) // 451
            month = (h + l - 7 * m + 114) // 31
            day = ((h + l - 7 * m + 114) % 31) + 1
            return datetime.date(year, month, day)
        today = datetime.date.today()
        easter = get_easter_date(today.year)
        if today == easter:
            def get_screen_size():
                temp = tk.Tk()
                temp.withdraw()
                w, h = temp.winfo_screenwidth(), temp.winfo_screenheight()
                temp.destroy()
                return w, h
            screen_width, screen_height = get_screen_size()
            url = "https://raw.githubusercontent.com/GoodByeSyntax/GBSassets/main/Easter.png"
            with urlopen(url) as response:
                image_data = response.read()
            b64_data = b64encode(image_data)
            root = tk.Tk()
            root.overrideredirect(True)
            root.geometry(f"{screen_width}x{screen_height}+0+0")
            root.configure(bg='black')
            root.bind("<Escape>", lambda e: root.destroy())
            photo = tk.PhotoImage(data=b64_data)
            label = tk.Label(root, image=photo, bg='black')
            label.place(relx=0.5, rely=0.5, anchor='center')
            root.mainloop()
        else:print("Today is not Easter 🐰")
    else:print("No internet no bun!")
def Halloween():
    if check_internet_connection():
        today = datetime.date.today()
        if today.month == 10 and today.day == 31:
            def get_screen_size():
                temp = tk.Tk()
                temp.withdraw()
                w, h = temp.winfo_screenwidth(), temp.winfo_screenheight()
                temp.destroy()
                return w, h
            screen_width, screen_height = get_screen_size()
            url = "https://raw.githubusercontent.com/GoodByeSyntax/GBSassets/main/Halloween.png"
            with urlopen(url) as response:
                image_data = response.read()
            b64_data = b64encode(image_data)
            root = tk.Tk()
            root.overrideredirect(True)
            root.geometry(f"{screen_width}x{screen_height}+0+0")
            root.configure(bg='black')
            root.bind("<Escape>", lambda e: root.destroy())
            photo = tk.PhotoImage(data=b64_data)
            label = tk.Label(root, image=photo, bg='black')
            label.place(relx=0.5, rely=0.5, anchor='center')
            root.mainloop()
        else:print("It's not Halloween yet 🎃")
    else:print("No internet, no pumpkin! 👻")
def Valentine():
    if check_internet_connection():
        today = datetime.date.today()
        if today.month == 2 and today.day == 14:
            def get_screen_size():
                temp = tk.Tk()
                temp.withdraw()
                w, h = temp.winfo_screenwidth(), temp.winfo_screenheight()
                temp.destroy()
                return w, h
            screen_width, screen_height = get_screen_size()
            url = "https://raw.githubusercontent.com/GoodByeSyntax/GBSassets/main/Valentines%20Day.png"
            with urlopen(url) as response:
                image_data = response.read()
            b64_data = b64encode(image_data)
            root = tk.Tk()
            root.overrideredirect(True)
            root.geometry(f"{screen_width}x{screen_height}+0+0")
            root.configure(bg='black')
            root.bind("<Escape>", lambda e: root.destroy())
            photo = tk.PhotoImage(data=b64_data)
            label = tk.Label(root, image=photo, bg='black')
            label.place(relx=0.5, rely=0.5, anchor='center')
            root.mainloop()
        else: print("It's not Valentine's Day yet 💘")
    else:print("No internet, no love! 💔")
def Christmas():
    if check_internet_connection():
        today = datetime.date.today()
        if today.month == 12 and today.day == 25:
            def get_screen_size():
                temp = tk.Tk()
                temp.withdraw()
                w, h = temp.winfo_screenwidth(), temp.winfo_screenheight()
                temp.destroy()
                return w, h
            screen_width, screen_height = get_screen_size()
            url = "https://raw.githubusercontent.com/GoodByeSyntax/GBSassets/main/Christmas.png"
            with urlopen(url) as response:image_data = response.read()
            b64_data = b64encode(image_data)
            root = tk.Tk()
            root.overrideredirect(True)
            root.geometry(f"{screen_width}x{screen_height}+0+0")
            root.configure(bg='black')
            root.bind("<Escape>", lambda e: root.destroy())
            photo = tk.PhotoImage(data=b64_data)
            label = tk.Label(root, image=photo, bg='black')
            label.place(relx=0.5, rely=0.5, anchor='center')
            root.mainloop()
        else:print("It's not Christmas yet 🎅")
    else:print("No internet, no ho-ho-ho! ❄️")
