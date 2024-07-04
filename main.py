from tkinter import *
from cell import Cell
import settings
import utils

root = Tk() # Create a window

# WINDOW SETTINGS
root.configure(bg='black') # Set background color
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False) # for width and height

top_frame = Frame(
    root, 
    bg='black', 
    width=settings.WIDTH,
    height=utils.height_percent(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='DodgerBlue2',
    text='Minesweeper Game',
    font=('Jokerman', 48)
)

game_title.place(
    x=utils.width_percent(30),
    y=30
)

left_frame = Frame(
    root, 
    bg='black',
    width=utils.width_percent(25),
    height=utils.height_percent(75)
)
left_frame.place(x=0, y=utils.height_percent(25))

instructions = Label(
    left_frame,
    bg='black',
    fg='white',
    text='''HOW TO PLAY: 
    Left click to reveal a cell. 
    Right click to mark a cell as a mine. 
    Find all the mines to win!''',
    font=('Segoe UI', 12)
)

instructions.place(
    x=40,
    y=utils.height_percent(45)

)

center_frame = Frame(
    root, 
    bg='black',
    width=utils.width_percent(75),
    height=utils.height_percent(75)
)
center_frame.place(x=utils.width_percent(25), y=utils.height_percent(25))

for x in range(settings.GRID_SIZE_COLUMNS):
    for y in range(settings.GRID_SIZE_ROWS):
        cell = Cell(x, y)
        cell.create_button(center_frame)
        cell.button.grid(row=y, column=x)

# Create the cell count label
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=40, y=0)

Cell.random_mine()

# RUN THE WINDOW
root.mainloop()