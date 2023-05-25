from tkinter import *
from tkinter import messagebox

class Giris(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Kullanıcı Giriş Ekranı")
    
        self.grid(pady=20)

        self.username_label = Label(self, text="Kullanıcı Adı:", width=15)
        self.username_label.grid(row=0, column=0, padx=10, pady=5)

        self.username_entry = Entry(self, width=30)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = Label(self, text="Şifre:", width=15)
        self.password_label.grid(row=1, column=0, padx=10, pady=5)

        self.password_entry = Entry(self, show="*", width=30)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_button = Button(self, text="Giriş Yap", command=self.login, width=30, height=2, bg="#C39BD3")
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.master.update()




        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def check_login(self, username, password):
        with open('login.txt', 'r') as file:
            for line in file:
                user, pw = line.strip().split(',')
                if user == username and pw == password:
                    return True
        return False

    def login(self):
        # kullanıcı adı ve şifreyi al
        username = self.username_entry.get()
        password = self.password_entry.get()

        # giriş doğrulama
        if username and password:
            if self.check_login(username, password):
                messagebox.showinfo("Başarılı", "Giriş başarılı!")
            else:
                messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı.")
        else:
            messagebox.showerror("Hata", "Lütfen kullanıcı adı ve şifre girin.")


root = Tk()
root.configure(bg='#EBDEF0')
app = Giris(master=root)

root.mainloop()
