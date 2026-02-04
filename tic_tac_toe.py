import tkinter as tk    #  which is used for gui applications
from tkinter import messagebox     #  shows the message boxes

def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8],    # horizontal
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],    # vertical
                  [0, 4, 8], [2, 4, 6]]:               # diagonal
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != "":
           buttons[combo[0]].config(bg="green")   # 
           buttons[combo[1]].config(bg="green")
           buttons[combo[2]].config(bg="green")
           winner = buttons[combo[0]]['text']
           messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
           return winner