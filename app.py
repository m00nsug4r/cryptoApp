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
    #-------BROWSING σε 2 φακελους 1)αρχειο κρυπτογραφημενο 2) κλειδι----------

    #ανοιγμα αρχειου που περιεχει το κλειδι και αποθηκευση σε τοπικη μνημη 
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()

    #ανοιγουμε το κρυπτογραφημενο αρχειο και το εκχωρουμε στην μεταβλητη encrypted
    with open('enc_grades.csv', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    


    SubmitKeyChoice = Button(root, text="Decrypt your text", padx=50, pady=10, command=lambda: Decryption(encrypted, key))  
    SubmitKeyChoice.pack() 
 

#συναρτηση για την δημιουργια η εκχωρηση κλειδιου
def KeyManager(value):
    
    if(value == 1): # περιπτωση τυχαιας δημιουργιας
        # δημιουργεια κλειδιου
        key = Fernet.generate_key() 
        #αποθηκευση στον ιδιο φακελο
        with open('mykey.key', 'wb') as mykey:
            mykey.write(key)

        #ανοιγμα αρχειου που περιεχει το κλειδι και αποθηκευση σε τοπικη μνημη 
        with open('mykey.key', 'rb') as mykey:
            key = mykey.read()

        #---------------FILE BROWSING | εγω το βαζω απο αυτοματο αρχειο------------------

        # αποθηκευση κλειδιου σε μεταβλητη f
        f = Fernet(key)
        #ανοιγμα του αρχειο με τους βαθμους και το διαβαζουμε , αποθηκευση στην μεταβλητη original
        with open('grades.csv', 'rb') as original_file:
            PlainText = original_file.read()
        

    elif(value == 2): #περιπτωση εισαγωγης

      print("lol")

    #υποβολη αποφασης χειρισμου κλειδιου και ανακατευθυνση στην σωστη συναρτηση
    SubmitKeyChoice = Button(root, text="Encrypt your file", padx=50, pady=10, command=lambda: Encryption(PlainText, key))  
    SubmitKeyChoice.pack() 
    
    return key
    
#συναρτηση για την κρυπτογραφηση κειμενου
def Encryption(PlainText , key):
    f = Fernet(key)
    # κανουμε κρυπτογραφηση του αρχειου με χρηση του fernet object 
    encrypted = f.encrypt(PlainText)
    #γραφουμε ενα καινουριο αρχειο οπου ειναι η κρυπτογραφημενη μορφη του αρχικου
    with open ('enc_grades.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def Decryption(encrypted, key):

    f = Fernet(key)
    
    #αποκρυπτογραφουμε το αρχειο με χρηση του fernet object
    decrypted = f.decrypt(encrypted)
    #γραφουμε ενα καινουριο αρχειο οπου εχει γινει αποκρυπτογραφηση στο κρυπτογραφημενο αρχειο 
    with open('dec_grades.csv', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


root = Tk()
root.title("Cryptography Tool")

encButton = Button(root, text="Encrypt text", padx=50, pady=10, command=encClick)
decButton = Button(root, text="Decrypt text", padx=50, pady=10, command=decClick)

encButton.pack()
decButton.pack()

root.mainloop()
