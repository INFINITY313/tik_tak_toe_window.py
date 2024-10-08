import tkinter as tk

import tkinter.messagebox as tmb

def push(b):
    global turns
    global is_game
    if b ["text"] == "" and is_game:
        if turns % 2 == 1:
            b["text"] = "X"
        else:
            b["text"] = "0"
        turns += 1
        winner = check_winner()
        if winner == "X":
            tmb.showinfo(title="game over",message="game over,X win!")
            is_game = False
        elif winner == "0":
            tmb.showinfo(title="game over",message="game over,0 win!")
            is_game = False
        elif turns == 10:
            tmb.showinfo(title="game over",message="game over,no one win...")
            is_game = False
    elif is_game == False:
        tmb.showwarning(title="game over",message="game over,if you want to continue please restart the game")
        new_game()        
    else:
        tmb.showerror(title="wrong move",message="wrong move,please select empty cell")

def check_winner():
    if game_board [0][0]["text"] ==  game_board [0][1]["text"] ==  game_board [0][2]["text"] != "":
        return game_board[0][0]["text"]
    
    if game_board [1][0]["text"] ==  game_board [1][1]["text"] ==  game_board [1][2]["text"] != "":
        return game_board[1][0]["text"]

    if game_board [2][0]["text"] == game_board [2][1]["text"] ==  game_board [2][2]["text"] != "":
        return game_board[2][0]["text"] 

    if game_board [0][0]["text"] ==  game_board [1][0]["text"] ==  game_board [2][0]["text"] != "":
        return game_board[0][0]["text"]

    if game_board [0][1]["text"] == game_board [1][1]["text"] ==    game_board [2][1]["text"] != "":
        return game_board[0][1]["text"]

    if game_board [0][2]["text"] ==  game_board [1][2]["text"] ==  game_board [2][2]["text"] != "":
        return game_board[0][2]["text"]

    if game_board [0][0]["text"] ==  game_board [1][1]["text"] ==  game_board [2][2]["text"] != "":
        return game_board[0][0]["text"] 

    if game_board [2][1]["text"] ==  game_board [1][1]["text"] ==  game_board [0][2]["text"] != "":
        return game_board[2][1]["text"]
    
def new_game():
    global turns
    turns = 1
    global is_game
    is_game = True
    for line in game_board:
        for bt in line:
            bt["text"] = ""

turns = 1
is_game = True 
game_board = []
window = tk.Tk()
window.title("Tik Tak Toe")
window.geometry("450x450")
window.resizable(False, False)
for i in range(3):
    game_board.append([])
    for j in range(3):
        button = tk.Button(window,text = "",height=10,width=20,borderwidth=10)
        button["command"] = lambda select_button=button:  push(select_button)
        game_board[i].append(button)
        button.place(x=i * 150,y=j * 150)
window.mainloop()