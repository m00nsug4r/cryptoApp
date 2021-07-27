from cryptography.fernet import Fernet
from tkinter import *


#συναρτηση σε περιπτωση επιλογης κρυπτογραφησης
def encClick():
    #διαγαρφη προηγουμενων κουμπιων
    encButton.destroy()
    decButton.destroy()
    #πεδιο για εισοδο κειμενου
    text = Entry(root, width=50)
    text.pack()
    text.insert(0,"Enter text to decrypt")
    r = IntVar()
    #προεπιλεγμενη τιμη 1
    r.set("1")
    #κουμπια
    Radiobutton(root, text="Generate a random secret key", variable=r, value=1, command=lambda: clicked(r.get())).pack()
    Radiobutton(root, text="Enter your own secret key", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#συναρτηση σε περιπτωση επιλογης αποκρυπτογραφησης
def decClick():
    #διαγραφη προηγουμενων κουμπιων
    encButton.destroy()
    decButton.destroy()
    #πεδιο για εισοδο κρυπτοκειμενου
    cipher = Entry(root, width=50)
    cipher.pack()
    cipher.insert(0,"Enter text to decrypt")
    #πεδιο για εισοδο μυστικου κλειδιου
    key = Entry(root, width=50)
    key.pack()
    key.insert(0,"Enter secret key")

root = Tk()
root.title("Cryptography Tool")

encButton = Button(root, text="Encrypt text", padx=50, pady=10, command=encClick)
decButton = Button(root, text="Decrypt text", padx=50, pady=10, command=decClick)

encButton.pack()
decButton.pack()

root.mainloop()
