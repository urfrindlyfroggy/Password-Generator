from tkinter import *
import random

def click():
    lower_case = "abcdefghajklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHAJKLMNOPQRSTUVWXWZ"
    numbers = "1234567890"
    symbols = "{}[]()~`!@#$%^&*_"

    ans = lower_case + upper_case + numbers + symbols

    password_topic = input("what is this password for? ")
    length = 9
    password = "".join(random.sample(ans, length))
    fh = open('passwords.txt', 'a')
    fh.write(password_topic + " password: " + password)
    fh.write("\n")
    fh.close()
    print("Your password is",password)

 
window = Tk()

button = Button(window, text="click for password", command=click, font=("Comic Sans", 30))
button.pack()

window.mainloop()