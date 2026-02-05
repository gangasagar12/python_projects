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
           root.quit()   # close the game window

def button_click(index):
    if buttons[index]["text"]=="" and not winner:
         buttons[index]["text"]=current_player
         check_winner()
         toggle_player()
    
def toggle_player():
    global current_player
    current_player = "x" if current_player =="0" else "0"
    lable.config(text=f" player {current_player} 's turn")

root=tk.Tk()  # create the main window
root.title("tic_tac_toe")  # 

buttons=[tk.Button(root,text="",font=('"normal',25),width=6 , height=3,command=lambda i=i: button_click(i)) for i in range(9)]
    
for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)    # arrange the buttons in a 3x3 grid

current_player="x"    
winner=False   # to keep track of the winner
lable=tk.Label(root,text=f"player {current_player} 's turn", font=("normal",20))     
lable.grid(row=3, column=0, columnspan=3)  # display the current player's turn

root.mainloop()  # start the GUI event loop