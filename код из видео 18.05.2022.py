from tkinter import *
import webbrowser
login_r = ('kot_off')
password_r = ('ggwp')


root = Tk()
root.geometry(f'550x450')
root.title('Урок 1')
root.configure(bg="orange")
## основа

logininput = StringVar()
passwordinput = StringVar()

loginentry = Entry(root, textvariable=logininput , bg="orange")
loginentry.pack()


def loginconfirm():
    if  logininput.get() == login_r:
        passwordentry = Entry(root, textvariable=passwordinput, bg="pink")
        passwordentry.pack()
        def passwordconfirm():
            if passwordinput == password_r:
                webbrowser.open('https://youtube.com', new="2")
        passconfirmbutton = Button(root, text="подтвердить", bg="brown", command=lambda: webbrowser.open('https://kotetop8413.unaxu.com', new="2"))
        passconfirmbutton.pack()
    else:
        print('неа!')
        input()




loginconfirmfbtn = Button(root, text='подтвердить', bg='red', command=lambda: loginconfirm())
loginconfirmfbtn.pack()


root.mainloop()
