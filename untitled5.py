# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:21:29 2023

@author: JSS-SHN
"""

import hashlib
from tkinter import *
from tkinter import filedialog

# create a tkinter window
root = Tk()
root.title("File Encryption System")
root.geometry("500x300")
root.config(bg="#e6e6e6")

# function to apply MD5 hash algorithm
def apply_md5():
    # open file dialog to select a text file
    text_file = filedialog.askopenfilename(title="Select a Text File", filetypes=(("Text Files", "*.txt"),))
    print(f"Selected File: {text_file}")

    # read the contents of the file
    with open(text_file, 'r') as f:
        contents = f.read()
        contents = contents.encode('utf-8')

    # apply md5 algorithm on the contents of the file
    md5_hash = hashlib.md5(contents).hexdigest()
    print(f"MD5 Hash: {md5_hash}")

    # create a new file to store the md5 hash
    with open('md5.txt', 'w') as f:
        f.write(md5_hash)

# function to apply SHA256 hash algorithm
def apply_sha256():
    # open file dialog to select a text file
    text_file = filedialog.askopenfilename(title="Select a Text File", filetypes=(("Text Files", "*.txt"),))
    print(f"Selected File: {text_file}")

    # read the contents of the file
    with open(text_file, 'r') as f:
        contents = f.read()
        contents = contents.encode('utf-8')

    # apply sha256 algorithm on the contents of the file
    sha256_hash = hashlib.sha256(contents).hexdigest()
    print(f"SHA256 Hash: {sha256_hash}")

    # create a new file to store the sha256 hash
    with open('sha256.txt', 'w') as f:
        f.write(sha256_hash)

# create a button to apply md5 algorithm
btn = Button(root, text="Apply MD5", bg="gray", fg="white", relief=FLAT, command=apply_md5)
btn.pack(pady=10)

# create a button to apply sha256 algorithm
btn1 = Button(root, text="Apply SHA256", bg="gray", fg="white", relief=FLAT, command=apply_sha256)
btn1.pack(pady=10)

root.mainloop()
