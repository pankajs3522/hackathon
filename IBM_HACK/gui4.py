import tkinter
width=800
height=600
window = tkinter.Tk()
window.geometry(str(width)+"x"+str(height))
window.configure(background="#a1dbcd")
window.title("Welcome")
lblInst = tkinter.Label(window, text="Please login to continue:", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
lblInst.pack()
lblUsername = tkinter.Label(window, text="Username:", fg="#383a39", bg="#a1dbcd")
entUsername = tkinter.Entry(window)
lblUsername.pack()
entUsername.pack()
lblPassword = tkinter.Label(window, text="Password:", fg="#383a39", bg="#a1dbcd")
entPassword = tkinter.Entry(window)
lblPassword.pack()
entPassword.pack()
btn = tkinter.Button(window, text="Login", fg="#a1dbcd", bg="#383a39")
btn.pack()
window.mainloop()