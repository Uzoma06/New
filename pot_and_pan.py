from tkinter import*
from tkinter import messagebox
from random import*
import json

window = Tk()
window.minsize(width= 400, height = 400)
window.title("Pot and Pan")
window.config(padx=50, pady=50)


a = randint(0,3)
b = a + 1
c = b + randint(1,2)
d = c + randint(1,3)

pin = [a,b,c,d]
print (pin)
bigfont = ["Calibri" , 32]
avgfont = ["Calibri", 22]

# #opening welcome page
# def WelcomePageFrame():
#     Welcomepageframe.grid(row=0, column=0)
    
# #closing welcome page
# def CloseWelcomePage():
#     Welcomepageframe.grid_forget()
    
#opening entrance page
def EntrancePageFrame():
    # CloseWelcomePage()
    Entrancepageframe.grid(row=0, column=0)
    
#closing entrance page
def CloseEntrancePage():
    Entrancepageframe.grid_forget()

# #opening entrance2 page
# def EntrancePage2Frame():
#     CloseWelcomePage()
#     Entrancepage2frame.grid(row=0, column=0)
    
# #closing entrance page
# def CloseEntrance2Page():
#     Entrancepage2frame.grid_forget()
    
#opening options page
def OptionsPageFrame():
    # CloseEntrance2Page()
    CloseEntrancePage()
    # CloseWelcomePage()
    Optionspageframe.grid(row=0, column=0)

#closing options frame
def CloseOptionsPage():
    Optionspageframe.grid_forget()

#Opening Computer page
def ComputerPageFrame():
    CloseOptionsPage()
    Computerpageframe.grid(row=0, column=0)
    
#opening 2users
def UsersPageFrame():
    CloseOptionsPage()
    Userspageframe.grid(row= 0, column= 0)
    
#closing 2users
def CloseUserspage():
    Userspageframe.grid_forget()
    
#userstooptions
def UserstoOptions():
    CloseUserspage()
    OptionsPageFrame()
    

    

#the rules
def Rules():
   messagebox.showinfo(title= Rules ,  message=("""
    The aim is to get the opponent's code
    In the game;
    -The code is meant to be 4 digits of different numbers
    e.g 1234, 0923, 4592, etc.
    -So when you save your code to the program,
    the program will use it and be giving the results................"""))
    
def CheckToHome():
    CloseOptionsPage()
    my_code_entry.delete(0, END)
    EntrancePageFrame()
    # CloseEntrance2Page()
    # WelcomePageFrame()
    
def Guesschecking():
    t = Guess_entry.get()
    t.split(",")
    
    if len(t)== 0 :
        messagebox.showerror(title="Empty Fields", message="Please fill in the four digit code")
        my_code_entry.delete(0, END)
    elif len(t)== 4 :
        if int(t[0]) == int(t[1]) :
            messagebox.showerror(title="Incorrect format", message="You didn't read the rules")
            my_code_entry.delete(0, END)
        elif int(t[0]) == int(t[2]) :
            messagebox.showerror(title="Incorrect format", message="You didn't read the rules")
            my_code_entry.delete(0, END)
        elif int(t[0]) == int(t[3]) :
            messagebox.showerror(title="Incorrect format", message="You didn't read the rules")
            my_code_entry.delete(0, END)
        elif int(t[1]) == int(t[2]) :
            messagebox.showerror(title="Incorrect format", message="You didn't read the rules")
            my_code_entry.delete(0, END)
        elif int(t[1]) == int(t[3]) :
            messagebox.showerror(title="Incorrect format", message="You didn't read the rules")
            my_code_entry.delete(0, END)
        elif int(t[2]) == int(t[3]) :
            messagebox.showerror(title="Incorrect format", message="You didn't read the rules")
            my_code_entry.delete(0, END)
        
        else :
            p1 = 0
            p2 = 0
            if int(t[0]) == a:
                p1 = p1 + 1
                if int(t[1]) == b:
                    p1 = p1 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            if p1 == 4:
                                messagebox.showinfo(title="Gaming", message=f"""{p1} pot, {p2} pan
You won""")
                            else:
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == a :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                                                                      
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                           
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == c :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")                            
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                            if int(t[3]) == d:
                                p1 = p1 + 1
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                            elif int(t[3]) == a :
                                p2 = p2 + 1
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                            elif int(t[3]) == b :
                                p2 = p2 + 1
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                            elif int(t[3]) == c :
                                p2 = p2 + 1
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                            else:
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == d :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                            if int(t[3]) == d:
                                p1 = p1 + 1
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                            elif int(t[3]) == a :
                                p2 = p2 + 1
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                            elif int(t[3]) == b :
                                p2 = p2 + 1
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                            elif int(t[3]) == c :
                                p2 = p2 + 1
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                            else:
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                else:
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                            if int(t[3]) == d:
                                p1 = p1 + 1
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                            elif int(t[3]) == a :
                                p2 = p2 + 1
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                            elif int(t[3]) == b :
                                p2 = p2 + 1
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                            elif int(t[3]) == c :
                                p2 = p2 + 1
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                            else:
                                messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
            elif int(t[0]) == b :
                p2 = p2 + 1
                if int(t[1]) == b:
                    p1 = p1 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == a :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == c :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == d :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                else:
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
            elif int(t[0]) == c :
                p2 = p2 + 1
                if int(t[1]) == b:
                    p1 = p1 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == a :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == c :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == d :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
            elif int(t[0]) == d :
                p2 = p2 + 1
                if int(t[1]) == b:
                    p1 = p1 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == a :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == c :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == d :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                else:
                    messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
            else:
                if int(t[1]) == b:
                    p1 = p1 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == a :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == c :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                elif int(t[1]) == d :
                    p2 = p2 + 1
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                else:
                    if int(t[2]) == c:
                        p1 = p1 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == a :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == b :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    elif int(t[2]) == d :
                        p2 = p2 + 1
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")    
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                    else:
                        if int(t[3]) == d:
                            p1 = p1 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == a :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == b :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        elif int(t[3]) == c :
                            p2 = p2 + 1
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")
                        else:
                            messagebox.showinfo(title="Gaming", message=f"{p1} pot, {p2} pan")  
            
    else:
        messagebox.showerror(title="Incorrect format", message="Please read the rules")
        my_code_entry.delete(0, END)

    
def codenchecking():
    n = my_code_entry.get()
    n.split(",")
   
    
    if len(n)== 0 :
        messagebox.showerror(title="Empty Fields", message="Please fill in your four digit code")
        my_code_entry.delete(0, END)
    elif len(n)== 4 :
        if int(n[0]) == int(n[1]) :
            messagebox.showerror(title="Incorrect format", message="Please read the rules")
            my_code_entry.delete(0, END)
        elif int(n[0]) == int(n[2]) :
            messagebox.showerror(title="Incorrect format", message="Please read the rules")
            my_code_entry.delete(0, END)
        elif int(n[0]) == int(n[3]) :
            messagebox.showerror(title="Incorrect format", message="Please read the rules")
            my_code_entry.delete(0, END)
        elif int(n[1]) == int(n[2]) :
            messagebox.showerror(title="Incorrect format", message="Please read the rules")
            my_code_entry.delete(0, END)
        elif int(n[1]) == int(n[3]) :
            messagebox.showerror(title="Incorrect format", message="Please read the rules")
            my_code_entry.delete(0, END)
        elif int(n[2]) == int(n[3]) :
            messagebox.showerror(title="Incorrect format", message="Please read the rules")
            my_code_entry.delete(0, END)
        else:
            OptionsPageFrame()
                   
    else:
        messagebox.showerror(title="The wrong amount of digits", message="Please fill in your four digit code")
        my_code_entry.delete(0, END)


#Entrance page frame
Entrancepageframe = LabelFrame(window, text="Enter code", padx= 80, pady= 80)
Entrancepageframe.grid_forget()
# Entrance page
Entrance= Label(Entrancepageframe, text="Please the required details", font= bigfont)
Entrance.grid(row =0, column= 0)
my_code= Label(Entrancepageframe, text="Please enter your personal code: ", font=avgfont)
my_code.grid(row =2, column= 0)
my_code_entry= Entry(Entrancepageframe,show="*")
my_code_entry.grid(row=2, column=1)
smy_code_button= Button(Entrancepageframe, text="Start Game", fg = "white",font= avgfont, bg= "red", command= codenchecking)
smy_code_button.grid(row= 4, column= 1)
smy_code_button.config(width=9, height=1)
rmy_code_button= Button(Entrancepageframe, text="Rules", fg = "white",font= avgfont, bg= "red", command= Rules )
rmy_code_button.grid(row= 4, column= 2)
rmy_code_button.config(width=9, height=1)


                                                                                                                                        
#options page frame
Optionspageframe =  LabelFrame(window, text="Enjoy", padx= 80, pady= 80)
Optionspageframe.grid_forget()

#optionspage
User_button= Button(Optionspageframe, text="2 Users", fg = "white",font= avgfont, bg= "red", command=UsersPageFrame)
User_button.grid(row= 2, column= 1)
User_button.config(width=9, height=1)
Computer_button= Button(Optionspageframe, text="Play with computer", fg = "white",font= avgfont, bg= "red", command= ComputerPageFrame )
Computer_button.grid(row= 3, column= 1)
Computer_button.config(width=15, height=1)
Backbutton= Button(Optionspageframe, text="Back", fg = "white",font= avgfont, bg= "red", command= CheckToHome )
Backbutton.grid(row= 4, column= 1)
Backbutton.config(width=15, height=1)



 #Computer page frame
Computerpageframe = LabelFrame(window, text="Playing", padx= 80, pady= 80)
Computerpageframe.grid_forget()

 #Computer page
Me_lbl = Label(Computerpageframe, text="Guess: ", font= bigfont)
Me_lbl.grid(row =0, column=0 )
Guess_entry = Entry(Computerpageframe)
Guess_entry.grid(row=0, column=1)
Comp_btn = Button(Computerpageframe, text="Submit", fg = "white",font= avgfont, bg= "red", command= Guesschecking )
Comp_btn.grid(row =1, column=1 )
Comp_btn.config(width=9, height=1)
comp_code_button= Button(Computerpageframe, text="Rules", fg = "white",font= avgfont, bg= "red", command= Rules )
comp_code_button.grid(row= 1, column= 2)
comp_code_button.config(width=9, height=1)

#2usersframe
Userspageframe = LabelFrame(window, text="Conecting", padx= 80, pady= 80)
Userspageframe.grid_forget()

#2users
C_lbl = Label(Userspageframe, text="Ensure you are connected to the internet", font= bigfont)
C_lbl.grid(row =0, column=0 )
Contbutton= Button(Userspageframe, text="Continue", fg = "white",font= avgfont, bg= "red", command= "" )
Contbutton.grid(row= 1, column= 0)
Contbutton.config(width=15, height=1)
Back_button= Button(Userspageframe, text="Back", fg = "white",font= avgfont, bg= "red", command= UserstoOptions)
Back_button.grid(row= 2, column= 0)
Back_button.config(width=15, height=1)



EntrancePageFrame()
window.mainloop()