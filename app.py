from cryptography.fernet import Fernet
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


#συναρτηση σε περιπτωση επιλογης κρυπτογραφησης 
def encClick():
    #διαγαρφη προηγουμενων κουμπιων
    encButton.destroy()
    decButton.destroy()
    
    r = IntVar()
    #προεπιλεγμενη τιμη 1
    r.set("1")
    #κουμπια
    rad1 = Radiobutton(root, text="Generate a random secret key", variable=r, value=1, command=lambda: KeyManager(r.get()))
    rad2 = Radiobutton(root, text="Enter your own secret key", variable=r, value=2, command=lambda: KeyManager(r.get()))
    rad1.pack()
    rad2.pack()

   

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
    SubmitKeyChoice = Button(root, text="Decrypt your text", padx=50, pady=10, command=lambda: Decryption(cipher.get(), key))  
    SubmitKeyChoice.pack() 
 

#συναρτηση για την δημιουργια η εκχωρηση κλειδιου
def KeyManager(value):
    
    if(value == 1): # περιπτωση τυχαιας δημιουργιας
        key = Fernet.generate_key()
        key = key.decode('utf-8') #μετατροπη του κλειδιου απο bytes se string
        cipher_suite = Fernet(key)
        keyText = ("your new key is : "+ key)
        #παραγωγη τυχαιου κλειδιου
        RandomKey = Label(root, text=keyText,bg="red")
        RandomKey.pack()
        print(keyText)
        #πεδιο εισαγωγης κειμενου
        PlainText = Entry(root, width=50)
        PlainText.pack()
        PlainText.insert(0,"Enter text to encrypt")

    elif(value == 2): #περιπτωση εισαγωγης

        #πεδιο για εισοδο κειμενου
        PlainText = Entry(root, width=50)
        PlainText.pack()
        PlainText.insert(0,"Enter text to encrypt")

        #πεδιο για εισοδο κωδικου
        key = Entry(root, width=50)
        key.pack()
        cipher_suite = Fernet(key.get().encode())


    #υποβολη αποφασης χειρισμου κλειδιου και ανακατευθυνση στην σωστη συναρτηση
    SubmitKeyChoice = Button(root, text="Encrypt your text", padx=50, pady=10, command=lambda: Encryption(PlainText.get(), cipher_suite))  
    SubmitKeyChoice.pack() 
    
    return key
    
#συναρτηση για την κρυπτογραφηση κειμενου
def Encryption(PlainText , key):
    
    LabelPlain =Label(root, text="Plain text: "+PlainText)
    LabelPlain.pack()

    encMessage = key.encrypt(PlainText.encode())
    LabelCipher = Label(root, text="Cipher Text: "+encMessage.decode())
    LabelCipher.pack()
    print(encMessage.decode())

def Decryption(cipher, key):

    secKey = Fernet(key.get().encode())
    decMessage = secKey.decrypt(cipher).decode()

    LabelCipher = Label(root, text="Cipher Text: "+cipher)
    LabelCipher.pack()

    LabelPlain = Label(root, text="Decoded Plain text: "+decMessage)
    LabelPlain.pack()


root = Tk()
root.title("Cryptography Tool")

encButton = Button(root, text="Encrypt text", padx=50, pady=10, command=encClick)
decButton = Button(root, text="Decrypt text", padx=50, pady=10, command=decClick)

encButton.pack()
decButton.pack()

root.mainloop()
