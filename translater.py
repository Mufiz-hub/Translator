from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data=pandas.read_csv("french_words.csv")
convert=data.to_dict(orient="records")
choose={}

def wrong():
    global choose
    global flip_time
    
    choose=random.choice(convert)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,text=choose["French"],fill="black")
    canvas.itemconfig(backgroung,image=create)
    window.after(8000,func=flip)
    

def flip():
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=choose["English"],fill="white")
    canvas.itemconfig(backgroung,image=back)





window=Tk()
window.title("Translater")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_time=window.after(3000,func=flip)
    

canvas=Canvas(width=800,height=526)
create=PhotoImage(file="card_front.png")
back=PhotoImage(file="card_back.png")

backgroung=canvas.create_image(400,263,image=create)

title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
word=canvas.create_text(400,263,text="Word",font=("Ariel",40,"italic"))


canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

wrong_image= PhotoImage(file="wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,command=wrong)
wrong_button.grid(row=1,column=0)

right_image= PhotoImage(file="right.png")
right_button=Button(image=right_image,highlightthickness=0,command=wrong)
right_button.grid(row=1,column=1)


wrong()
window.mainloop()
