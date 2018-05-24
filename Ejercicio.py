import winsound
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width = 750, height = 250)
canvas.pack()

my_image = PhotoImage(file= "cancha.gif")
canvas.create_image(0,0, anchor =NW, image=my_image)

my_image2 = PhotoImage(file="arco.gif")
canvas.create_image(0,70, anchor =NW, image=my_image2)

#my_image3 = PhotoImage(file="Score.gif")
#canvas.create_image(40,90, anchor =NW, image=my_image3)

my_image4 = PhotoImage(file= "balon.gif")
canvas.create_image(600,90,anchor = NW,image = my_image4)

def movebalon(event):
    canvas.move(3,5,0)

canvas.bind_all('<KeyPress-Right>', movebalon)
canvas.move(1,5,0)
canvas.move(2,5,0)
canvas.move(4,5,0)

def movebalon1(event):
    canvas.move(3,0,5)

canvas.bind_all('<KeyPress-Down>', movebalon1)

def movebalon2(event):
    canvas.move(3,0,-5)
canvas.bind_all('<KeyPress-Up>', movebalon2)

def movebalon3(event):
    canvas.move(3,-5,0)
canvas.bind_all('<KeyPress-Left>', movebalon3)

#Sonido Y Gol:
if my_image4:
    print("GOL")

    def play(path):
        winsound.PlaySound(path, winsound.SND_FILENAME)
sonido = 'test.wav'
play(sonido)

tk.mainloop()





