from tkinter import *
from PIL import ImageTk, Image
import random
root=Tk()

root.title("ENDLESS POKEMON CARD GAME")
root.geometry("600x400")

root.configure(background="orange")

img=ImageTk.PhotoImage(Image.open("button.jpg"))

player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score_label = Label(root, bg = "Blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root, bg = "Blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_card_label = Label(root,bg = "Yellow", fg = "black")
random_card_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()