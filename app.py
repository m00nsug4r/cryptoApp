from cryptography.fernet import Fernet
from tkinter import *


#συναρτηση σε περιπτωση επιλογης κρυπτογραφησης 
def encClick():
    #διαγαρφη προηγουμενων κουμπιων
    encButton.destroy()
    decButton.destroy()
    
    r = IntVar()
    #προεπιλεγμενη τιμη 1
    r.set("1")
    #κουμπια
    Radiobutton(root, text="Generate a random secret key", variable=r, value=1, command=lambda: KeyManager(r.get())).pack()
    Radiobutton(root, text="Enter your own secret key", variable=r, value=2, command=lambda: KeyManager(r.get())).pack()


   

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


#συναρτηση για την δημιουργια η εκχωρηση κλειδιου
def KeyManager(value):
    
    if(value == 1): # περιπτωση τυχαιας δημιουργιας
        key = Fernet.generate_key()
        key = key.decode('utf-8') #μετατροπη του κλειδιου απο bytes se string
        cipher_suite = Fernet(key)
        keyText = ("your new key is : "+ key)
        RandomKey = Label(root, text=keyText,bg="red")
        RandomKey.pack()

    elif(value == 2): #περιπτωση εισαγωγης

        #πεδιο για εισοδο κειμενου
        PlainText = Entry(root, width=50)
        PlainText.pack()
        PlainText.insert(0,"Enter text to encrypt")

        #πεδιο για εισοδο κωδικου
        key = Entry(root, width=50)
        key.pack()
        key.insert(0,"Enter your secret key")

        
        #εμφανισει κρυπτογραφημενου μhνyματος
        #ShowChiperText = Label(root, text=cipher_text)
        #ShowChiperText.pack()
       

    #υποβολη αποφασης χειρισμου κλειδιου και ανακατευθυνση στην σωστη συναρτηση
    SubmitKeyChoice = Button(root, text="Encrypt your text", padx=50, pady=10, command=encClick)  
    SubmitKeyChoice.pack() 
    
    return key
    
#συναρτηση για την κρυπτογραφηση κειμενου
def Encryption():
    #οταν μπαινουμε εδω θα πρεπει να διαγραφουμε τα radio buttons 
    print("p")
    








root = Tk()
root.title("Cryptography Tool")

encButton = Button(root, text="Encrypt text", padx=50, pady=10, command=encClick)
decButton = Button(root, text="Decrypt text", padx=50, pady=10, command=decClick)

encButton.pack()
decButton.pack()

root.mainloop()
