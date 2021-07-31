from cryptography.fernet import Fernet
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo


def StartMenu():

    #καθαρισμα frame
    clear()
    #label εναρξης
    labelStart = Label(main, text="Welcome to Crypto App\n choose wether you want to encrypt or decrypt a file")
    labelStart.pack(side="top", pady=15)
    #αναδημιουργια κουμπιων
    encButton = Button(main, text="Encrypt file", padx=50, pady=10, command=encClick)
    decButton = Button(main, text="Decrypt file", padx=50, pady=10, command=decClick)

    encButton.pack(side="top", pady=10)
    decButton.pack(side="top", pady=10)

def clear():
    #συναρτηση για καταστριοφη του frame και αναδημιουργια του
    global main, bottomFrame, root
    bottomFrame.destroy()
    main.destroy()
    main=Frame(root)
    main.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    
#συναρτηση σε περιπτωση επιλογης κρυπτογραφησης 
def encClick():

    #διαγαρφη προηγουμενων κουμπιων
    clear()
    
    #label για επιλογη κρυπτογραφησης
    labelEnc = Label(main, text="File Encryption")
    labelEnc.pack(side="top", pady=10)

    r = IntVar()
    #προεπιλεγμενη τιμη 1
    r.set("1")
    #κουμπια
    rad1 = Radiobutton(main, text="Generate a random secret key", variable=r, value=1, command=lambda: [clear(), KeyManager(r.get())])
    rad2 = Radiobutton(main, text="Enter your own secret key", variable=r, value=2, command=lambda: [clear(), KeyManager(r.get())])
    rad1.pack(side="top",pady=10)
    rad2.pack(side="top", pady=5)

   

#συναρτηση σε περιπτωση επιλογης αποκρυπτογραφησης
def decClick():

    #διαγραφη προηγουμενων κουμπιων
    clear()
    
    labelDec = Label(main, text="File Decryption")
    labelDec.pack(side="top", pady=10)
    #cancel button
    cancel = Button(bottomFrame, text="Cancel", padx=10, command=StartMenu)
    cancel.pack(side="right", padx=30, pady=10)

    global keyFile 
    keyFile = None
    button_key = Button(main,
                    text = "Browse for key file",
                    command=browseKeyForDec)

    button_key.pack(side="top", pady=10) 


#συναρτηση για την δημιουργια η εκχωρηση κλειδιου
def KeyManager(value):
    
    cancel = Button(bottomFrame, text="Cancel", padx=10, command=StartMenu)
    cancel.pack(side="right", padx=30 , pady=10)

    if(value == 1): # περιπτωση τυχαιας δημιουργιας
        # δημιουργεια κλειδιου
        key = Fernet.generate_key() 
        #αποθηκευση στον ιδιο φακελο
        with open('secret.key', 'wb') as mykey:
            mykey.write(key)

        #ανοιγμα αρχειου που περιεχει το κλειδι και αποθηκευση σε τοπικη μνημη 
        with open('secret.key', 'rb') as mykey:
            key = mykey.read()
        
        labelKeyCreation = Label(main, text="Key file \"secret.key\" now exists in your current working directory")
        labelKeyCreation.pack(side="top", pady=10)
        
        # αποθηκευση κλειδιου σε μεταβλητη f
        f = Fernet(key)

        #λιστα επιλογης επεκτασης αρχειου προς κρυπτογραφηση
        labelExtension = Label(main, text="Choose extension of file you wish to encrypt")
        labelExtension.pack(side="top", pady=10)

        extension = StringVar()
        extension.set(".txt")

        extList = OptionMenu(main, extension, ".txt", ".docx",".odt", ".pdf", ".csv", ".pptx", ".xls")
        extList.pack(side="top", pady=10)

        #ανοιγουμε αρχειο για κρυπτογραφηση
        global filename 
        filename = None
        button_explore = Button(main,
                        text = "Browse File to Encrypt",
                        command=lambda: browseFiles(key, extension.get()))

        button_explore.pack(side="top", pady=10)
        

    elif(value == 2): #περιπτωση εισαγωγης

       #ανοιγουμε αρχειο με κλειδι
       global keyFileExisting 
       filename = None
       button_explore = Button(main,
                        text = "Browse Key File",
                        command= browseKeyForEnc)

       button_explore.pack(side="top", pady=10)
 
    
    
#συναρτηση για την κρυπτογραφηση κειμενου
def Encryption(filename , key, extension):

    #ανοιγμα του αρχειο με τους βαθμους και το διαβαζουμε , αποθηκευση στην μεταβλητη original
    with open(filename, 'rb') as original_file:
        PlainText = original_file.read()

    f = Fernet(key)
    # κανουμε κρυπτογραφηση του αρχειου με χρηση του fernet object 
    encrypted = f.encrypt(PlainText)
    #γραφουμε ενα καινουριο αρχειο οπου ειναι η κρυπτογραφημενη μορφη του αρχικου
    with open ('encrypted_file'+extension, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    
    #ταμπελα για επιτυχης κρυπτογραφηση 
    LabelEncryptionSuccess = Label(main, text="File \"encrypted_file"+extension+"\" now exists in your current working directory")
    LabelEncryptionSuccess.pack(side="top", pady=10)
    
    #κουμπι για επιστροφη σε αρχικο μενου
    ReturnToStart = Button(main, text="Return to main menu", padx=10, pady=10, command= StartMenu)  
    ReturnToStart.pack(side="top", pady=10)


def Decryption(encrypted, key, extension):

    f = Fernet(key)
    
    #αποκρυπτογραφουμε το αρχειο με χρηση του fernet object
    decrypted = f.decrypt(encrypted)
    #γραφουμε ενα καινουριο αρχειο οπου εχει γινει αποκρυπτογραφηση στο κρυπτογραφημενο αρχειο 
    with open('decrypted_file'+extension, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    #----label για επιτυχης αποκρυπτογραφηση αρχειου----
    labelFOrSuccedDecryption = Label(main, text="The file \"decrypted_file"+extension+"\" now exists in your current working directory")
    labelFOrSuccedDecryption.pack(side="top", pady=10)

    #κουμπι για επιστροφη σε αρχικο μενου
    ReturnToStart = Button(main, text="Return to main menu", padx=10, pady=10, command= StartMenu)  
    ReturnToStart.pack(side="top", pady=10)
    
    

def browseFiles(key, extension):

    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = ((extension+" files",
                                                        extension),
                                                       ("all files",
                                                        "*.*")))
    
    #ταμπελα για επιτυχης ανοιγμα αρχειου
    LabelFilename = Label(main, text="Opened file to encrypt: \n"+filename)
    LabelFilename.pack(side="top", pady=10)

    #υποβολη αποφασης χειρισμου κλειδιου και ανακατευθυνση στην σωστη συναρτηση
    SubmitKeyChoice = Button(main, text="Encrypt your file", padx=10, pady=10, command=lambda: Encryption(filename, key, extension))  
    SubmitKeyChoice.pack(side="top", pady=10)

def browseKeyForDec():
        

    keyFile = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Key files",
                                                        "*.key*"),
                                                       ("all files",
                                                        "*.*")))
    #ανοιγμα αρχειου που περιεχει το κλειδι και αποθηκευση σε τοπικη μνημη 
    with open(keyFile, 'rb') as mykey:
        key = mykey.read()

    #----βαλε label για επιτυχης ανοιγμα αρχειου με κλειδι----
    labelKeyFind = Label(main, text="the key was found at : \n" + keyFile)
    labelKeyFind.pack(side="top", pady=10)
    
    #λιστα επιλογης επεκτασης αρχειου προς κρυπτογραφηση
    labelExtension = Label(main, text="Choose extension of file you wish to decrypt")
    labelExtension.pack(side="top", pady=10)

    extension = StringVar()
    extension.set(".txt")

    extList = OptionMenu(main, extension, ".txt", ".docx",".odt", ".pdf", ".csv", ".pptx", ".xls")
    extList.pack(side="top", pady=10)

    #κουμπι για αναζητηση αρχειου προς αποκρυπτγραφηση
    global encFile
    encFile = None
    button_encFile = Button(main,
                    text = "Browse for file to Decrypt",
                    command=lambda: browseFiles2(key, extension.get()))

    button_encFile.pack(side="top", pady=10)

def browseFiles2(key, extension):

    #αποθηκευση παθ κρυπτογραφημενου αρχειου
    encFile = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = ((extension+" files",
                                                        extension),
                                                       ("all files",
                                                        "*.*")))
    
    #ανοιγουμε το κρυπτογραφημενο αρχειο και το εκχωρουμε στην μεταβλητη encrypted
    with open(encFile, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    
    #----label για επιτυχης ανοιγμα κρυπτογραφημενου αρχειου
    labelSuccesOpenEncrypteedFile = Label(main, text="Opened file: \n " +encFile)
    labelSuccesOpenEncrypteedFile.pack(side="top", pady=10)
    #κουμπι για εκτελεση αποκρυπτογραφηση
    SubmitKeyChoice = Button(main, text="Decrypt your text", padx=50, pady=10, command=lambda: Decryption(encrypted, key, extension))  
    SubmitKeyChoice.pack(side="top", pady=10)
    
def browseKeyForEnc():

    #αποθηκευση παθ αρχειου που περιεχει το κλειδι
    keyFile = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Key files",
                                                        "*.key*"),
                                                       ("all files",
                                                        "*.*")))

    #αποθηκευση κλειδιου στη μεταβλητη key                                                    
    with open(keyFile, 'rb') as mykey:
        key = mykey.read()

    #κουμπι για επιτυχης ανοιγμα αρχειου με κλειδι
    LabelKeyFound = Label(main, text="Opened key file: \n"+keyFile)
    LabelKeyFound.pack(side="top", pady=10)

    #λιστα επιλογης επεκτασης αρχειου προς κρυπτογραφηση
    labelExtension = Label(main, text="Choose extension of file you wish to encrypt")
    labelExtension.pack(side="top", pady=10)

    extension = StringVar()
    extension.set(".txt")

    extList = OptionMenu(main, extension, ".txt", ".docx",".odt", ".pdf", ".csv", ".pptx", ".xls")
    extList.pack(side="top", pady=10)

    #κουμπι για αναζητηση αρχειου προς κρυπτογραφηση
    global filename2 
    filename2 = None
    button_explore = Button(main,
                        text = "Browse File for Encryption",
                        command=lambda: browseFiles(key, extension.get()))

    button_explore.pack(side="top", pady=10)   


root = Tk()
root.geometry("750x700")
root.title("Cryptography Tool")

#κυριο frame
main=Frame(root)    
main.pack()

#bottom frame (για το κουμπι cancel)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

StartMenu()

root.mainloop()
