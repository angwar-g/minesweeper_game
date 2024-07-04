from tkinter import Button, Label, messagebox
import settings
import random 
import sys

class Cell:
    all = []
    cell_count_label_object = None
    cell_count = settings.TOTAL_CELLS

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.is_mine_candidate = False
        self.button = None
        self.x = x
        self.y = y

        # Add the cell to the list of all cells
        Cell.all.append(self)

    def create_button(self, location):
        btn = Button(
            location,
            width=3,
            height=2
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self.button = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text = f"Cells Left: {Cell.cell_count}", 
            width=12, 
            height=4,
            font=('Harrington', 22)
        )
        Cell.cell_count_label_object = lbl
    
    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.count_surrounding_mines == 0:
                for cell in self.surrounding_cells:
                    cell.show_cell()
            self.show_cell()
        
            # PLAYER WON
            if Cell.cell_count == settings.NUM_MINES:
                messagebox.showinfo(title="Congratulations!", message="YOU WON!")
                sys.exit()

        
        #Cancel button click actions
        self.button.unbind('<Button-1>')
        self.button.unbind('<Button-3>')
    
    @property
    def surrounding_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y),  
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1), 
            self.get_cell_by_axis(self.x + 1, self.y + 1) 
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def count_surrounding_mines(self):
        count = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                count += 1
        return count
    
    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1
            self.button.configure(text=self.count_surrounding_mines, bg='lightgray')
            # Update Cell Count Label
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells Left: {Cell.cell_count}")
            self.button.configure(bg='SYSTEMBUTTONFACE')

        # Mark the cell as open
        self.is_open = True


    def get_cell_by_axis(self, x, y):
        # return the cell object by x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_mine(self):
        self.button.configure(text='M', bg='red')
        messagebox.showinfo(title="Game Over", message="You clicked on a mine :(")
        sys.exit()

    
    def right_click_action(self, event):
        # SELECTING
        if not self.is_mine_candidate:
            self.button.configure(bg='orange')
            self.is_mine_candidate = True
        # UNSELECTING
        else:
            self.button.configure(text='', bg='SystemButtonFace')
            self.is_mine_candidate = False

    @staticmethod
    def random_mine():
        picked_cells = random.sample(Cell.all, settings.NUM_MINES)
        for cell in picked_cells:
            cell.is_mine = True

    # Better representation of the object
    def __repr__(self):
        return f'Cell{self.x}, {self.y}'

