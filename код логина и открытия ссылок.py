from tkinter import *
import webbrowser
import time
loginr = ('INPUT')
passwordr = ('INPUT')
started = input('input "start" to start | ~~~')

if started == 'start':
    web = Tk()
    web.geometry(f'550x450')
    web.title('web')
    web.configure(bg="green")
    ## base

    logininputweb = StringVar()

    loginentryweb = Entry(web, textvariable=logininputweb)
    loginentryweb.pack()


    def completeweb():
        if logininputweb.get() == loginr:
            print('nice, please wait')
            time.sleep(3)
            ## create new Entry
            passwordinputweb = StringVar()

            passwordentryweb = Entry(web, textvariable=passwordinputweb)
            passwordentryweb.pack()
            ## get ftp command
            def getftpweb():
                if passwordinputweb.get() == passwordr:
                    print('okay, please wait')
                    time.sleep(2.5)
                    webbtn = Button(web, text="web", bg="green", command=lambda: webbrowser.open('URL INPUT', new="2"))
                    loginbtn = Button(web, text="user, host, password", bg="green", command=lambda: webbrowser.open('URL INPUT', new="2"))

                    webbtn.pack()
                    loginbtn.pack()

            ## create complete button

            passwordwebcomplete = Button(web, text='get ftp', bg="green", command=lambda: getftpweb())
            passwordwebcomplete.pack()



    loginwebcomplete = Button(web, text="complete!", bg="green", command=completeweb)
    loginwebcomplete.pack()

    web.mainloop()
