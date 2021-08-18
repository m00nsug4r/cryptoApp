from cryptography.fernet import Fernet
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
import tkinter.font as font


def StartMenu():

    clear()
    labelStart = Label(main, text="Welcome to Crypto App\n choose wether you want to encrypt or decrypt a file",font="Times 17 italic")
    labelStart.pack(side="top", pady=15)
    encButton = Button(main, text="Encrypt file", padx=50, pady=10, command=encClick)
    decButton = Button(main, text="Decrypt file", padx=50, pady=10, command=decClick)
    
    

    encButton.pack(side="top", pady=10)
    decButton.pack(side="top", pady=10)

def clear():
    global main, bottomFrame, root
    bottomFrame.destroy()
    main.destroy()
    main=Frame(root)
    main.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    
def encClick():

    clear()
    
    labelEnc = Label(main, text="File Encryption",font="Times 17 italic")
    labelEnc.pack(side="top", pady=10)

    r = IntVar()
    r.set("1")
    rad1 = Radiobutton(main, text="Generate a random secret key", variable=r, value=1, command=lambda: [clear(), KeyManager(r.get())])
    rad2 = Radiobutton(main, text="Enter your own secret key", variable=r, value=2, command=lambda: [clear(), KeyManager(r.get())])
    rad1.pack(side="top",pady=10)
    rad2.pack(side="top", pady=5)

   

def decClick():

    clear()
    
    labelDec = Label(main, text="File Decryption",font="Times 17 italic")
    labelDec.pack(side="top", pady=10)
    cancel = Button(bottomFrame, text="Cancel", padx=10, command=StartMenu,bg="red")
    cancel.pack(side="right", padx=30, pady=10)

    global keyFile 
    keyFile = None
    button_key = Button(main,
                    text = "Browse for key file",
                    command=browseKeyForDec)

    button_key.pack(side="top", pady=10) 


def KeyManager(value):
    
    cancel = Button(bottomFrame, text="Cancel", padx=10, command=StartMenu,bg="red")
    cancel.pack(side="right", padx=30 , pady=10)

    if(value == 1): # περιπτωση τυχαιας δημιουργιας
        key = Fernet.generate_key() 
        with open('secret.key', 'wb') as mykey:
            mykey.write(key)

        with open('secret.key', 'rb') as mykey:
            key = mykey.read()
        
        labelKeyCreation = Label(main, text="Key file \"secret.key\" now exists in your current working directory",font="Times 17 italic")
        labelKeyCreation.pack(side="top", pady=10)
        
        f = Fernet(key)

        labelExtension = Label(main, text="Choose extension of file you wish to encrypt",font="Times 17 italic")
        labelExtension.pack(side="top", pady=10)

        extension = StringVar()
        extension.set(".txt")

        extList = OptionMenu(main, extension, ".txt", ".docx",".odt", ".pdf", ".csv", ".pptx", ".xls")
        extList.pack(side="top", pady=10)

        global filename 
        filename = None
        button_explore = Button(main,
                        text = "Browse File to Encrypt",
                        command=lambda: browseFiles(key, extension.get()))

        button_explore.pack(side="top", pady=10)
        

    elif(value == 2): #περιπτωση εισαγωγης

       global keyFileExisting 
       filename = None
       button_explore = Button(main,
                        text = "Browse Key File",
                        command= browseKeyForEnc)

       button_explore.pack(side="top", pady=10)
 
    
    
def Encryption(filename , key, extension):

    with open(filename, 'rb') as original_file:
        PlainText = original_file.read()

    f = Fernet(key)
    encrypted = f.encrypt(PlainText)
    with open ('encrypted_file'+extension, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    
    LabelEncryptionSuccess = Label(main, text="File \"encrypted_file"+extension+"\" now exists in your current working directory",font="Times 17 italic")
    LabelEncryptionSuccess.pack(side="top", pady=10)
    
    ReturnToStart = Button(main, text="Return to main menu", padx=10, pady=10, command= StartMenu)  
    ReturnToStart.pack(side="top", pady=10)


def Decryption(encrypted, key, extension):

    f = Fernet(key)
    
    decrypted = f.decrypt(encrypted)
    with open('decrypted_file'+extension, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    labelFOrSuccedDecryption = Label(main, text="The file \"decrypted_file"+extension+"\" now exists in your current working directory",font="Times 17 italic")
    labelFOrSuccedDecryption.pack(side="top", pady=10)

    ReturnToStart = Button(main, text="Return to main menu", padx=10, pady=10, command= StartMenu)  
    ReturnToStart.pack(side="top", pady=10)
    
    

def browseFiles(key, extension):

    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = ((extension+" files",
                                                        extension),
                                                       ("all files",
                                                        "*.*")))
    
    LabelFilename = Label(main, text="Opened file to encrypt: \n"+filename+"\"",font="Times 17 italic")
    LabelFilename.pack(side="top", pady=10)

    SubmitKeyChoice = Button(main, text="Encrypt your file", padx=10, pady=10, command=lambda: Encryption(filename, key, extension))  
    SubmitKeyChoice.pack(side="top", pady=10)

def browseKeyForDec():
        

    keyFile = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Key files",
                                                        "*.key*"),
                                                       ("all files",
                                                        "*.*")))
    with open(keyFile, 'rb') as mykey:
        key = mykey.read()

    labelKeyFind = Label(main, text="the key was found at : \n" + keyFile+"\"",font="Times 17 italic")
    labelKeyFind.pack(side="top", pady=10)
    
    labelExtension = Label(main, text="Choose extension of file you wish to decrypt",font="Times 17 italic")
    labelExtension.pack(side="top", pady=10)

    extension = StringVar()
    extension.set(".txt")

    extList = OptionMenu(main, extension, ".txt", ".docx",".odt", ".pdf", ".csv", ".pptx", ".xls")
    extList.pack(side="top", pady=10)

    global encFile
    encFile = None
    button_encFile = Button(main,
                    text = "Browse for file to Decrypt",
                    command=lambda: browseFiles2(key, extension.get()))

    button_encFile.pack(side="top", pady=10)

def browseFiles2(key, extension):

    encFile = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = ((extension+" files",
                                                        extension),
                                                       ("all files",
                                                        "*.*")))
    
    with open(encFile, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    
    labelSuccesOpenEncrypteedFile = Label(main, text="Opened file: \n " +encFile+"\"",font="Times 17 italic")
    labelSuccesOpenEncrypteedFile.pack(side="top", pady=10)
    SubmitKeyChoice = Button(main, text="Decrypt your text", padx=50, pady=10, command=lambda: Decryption(encrypted, key, extension))  
    SubmitKeyChoice.pack(side="top", pady=10)
    
def browseKeyForEnc():

    keyFile = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Key files",
                                                        "*.key*"),
                                                       ("all files",
                                                        "*.*")))

    with open(keyFile, 'rb') as mykey:
        key = mykey.read()

    LabelKeyFound = Label(main, text="Opened key file: \n"+keyFile+"\"",font="Times 17 italic")
    LabelKeyFound.pack(side="top", pady=10)

    labelExtension = Label(main, text="Choose extension of file you wish to encrypt",font="Times 17 italic")
    labelExtension.pack(side="top", pady=10)

    extension = StringVar()
    extension.set(".txt")

    extList = OptionMenu(main, extension, ".txt", ".docx",".odt", ".pdf", ".csv", ".pptx", ".xls")
    extList.pack(side="top", pady=10)

    global filename2 
    filename2 = None
    button_explore = Button(main,
                        text = "Browse File for Encryption",
                        command=lambda: browseFiles(key, extension.get()))

    button_explore.pack(side="top", pady=10)   


root = Tk()
root.geometry("750x700")
root.title("Cryptography Tool")
main=Frame(root)    
main.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

myFont = font.Font(family='Script')
StartMenu()

root.mainloop()
