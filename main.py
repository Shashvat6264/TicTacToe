from tkinter import *
from tkinter.ttk import *

global clicked, states, buttons, steps, var


def checkwinner():
    global states
    checker = [[0, 3, 6],
               [1, 4, 7],
               [2, 5, 8],
               [0, 1, 2],
               [3, 4, 5],
               [6, 7, 8],
               [0, 4, 8],
               [2, 4, 6]]
    for i in checker:
        if ((states[int(i[0] / 3)][i[0] % 3] == states[int(i[1] / 3)][i[1] % 3]) and (
                states[int(i[0] / 3)][i[0] % 3] == states[int(i[2] / 3)][i[2] % 3]) and (
                states[int(i[0] / 3)][i[0] % 3] != " ")):
            var.set("Winner is " + states[int(i[0] / 3)][i[0] % 3])
            return True
    return False

def tiechecker():
    global states
    for i in range(0, 3):
        for j in range(0, 3):
            if states[i][j] == " ":
                return False
    return True

def grid_press(state, i, j):
    if not checkwinner():
        global clicked, buttons, steps
        if buttons[i][j]['text'] == " ":
            buttons[i][j]['text'] = state
            states[i][j] = state
            steps += 1
        if steps % 2 == 0:
            changestatus('X')
            if not checkwinner() and not tiechecker():
                var.set('Turn of X')
            elif tiechecker():
                var.set('It is a Tie')
        else:
            changestatus('O')
            if not checkwinner() and not tiechecker():
                var.set('Turn of O')
            elif tiechecker():
                var.set('It is a Tie')


def render_grid(frame):
    global buttons
    buttons[0][0] = Button(frame, text=states[0][0], command=lambda: grid_press('X', 0, 0))
    buttons[0][0].grid(row=0, column=0)
    buttons[0][1] = Button(frame, text=states[0][1], command=lambda: grid_press('X', 0, 1))
    buttons[0][1].grid(row=0, column=1)
    buttons[0][2] = Button(frame, text=states[0][2], command=lambda: grid_press('X', 0, 2))
    buttons[0][2].grid(row=0, column=2)
    buttons[1][0] = Button(frame, text=states[1][0], command=lambda: grid_press('X', 1, 0))
    buttons[1][0].grid(row=1, column=0)
    buttons[1][1] = Button(frame, text=states[1][1], command=lambda: grid_press('X', 1, 1))
    buttons[1][1].grid(row=1, column=1)
    buttons[1][2] = Button(frame, text=states[1][2], command=lambda: grid_press('X', 1, 2))
    buttons[1][2].grid(row=1, column=2)
    buttons[2][0] = Button(frame, text=states[2][0], command=lambda: grid_press('X', 2, 0))
    buttons[2][0].grid(row=2, column=0)
    buttons[2][1] = Button(frame, text=states[2][1], command=lambda: grid_press('X', 2, 1))
    buttons[2][1].grid(row=2, column=1)
    buttons[2][2] = Button(frame, text=states[2][2], command=lambda: grid_press('X', 2, 2))
    buttons[2][2].grid(row=2, column=2)


def changestatus(state):
    global buttons
    buttons[0][0]['command'] = lambda: grid_press(state, 0, 0)
    buttons[0][1]['command'] = lambda: grid_press(state, 0, 1)
    buttons[0][2]['command'] = lambda: grid_press(state, 0, 2)
    buttons[1][0]['command'] = lambda: grid_press(state, 1, 0)
    buttons[1][1]['command'] = lambda: grid_press(state, 1, 1)
    buttons[1][2]['command'] = lambda: grid_press(state, 1, 2)
    buttons[2][0]['command'] = lambda: grid_press(state, 2, 0)
    buttons[2][1]['command'] = lambda: grid_press(state, 2, 1)
    buttons[2][2]['command'] = lambda: grid_press(state, 2, 2)


def startgame(frame):
    global steps, states, clicked, buttons, var
    states = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]
    buttons = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]
    clicked = False
    steps = 0
    var.set("Welcome Let's Play.. X goes first")
    render_grid(frame)


root = Tk()
root.title("Tic Tac Toe")
root.geometry("300x300")

frame = Frame(root)
frame.pack()

var = StringVar()
label = Label(root, textvariable=var)
label.pack()

clearall = Button(root, text="Clear all", command=lambda: startgame(frame))
clearall.pack()

startgame(frame)

root.mainloop()
