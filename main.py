# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
# Override the setting of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_prect(25)
)
top_frame.place(x=0, y=0)
game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(
    x=utils.width_prect(25), y=0
)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prect(25),
    height=utils.height_prect(75)  # 720-180=540
)
left_frame.place(x=0, y=utils.height_prect(25))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prect(75),
    height=utils.height_prect(75)
)
center_frame.place(
    x=utils.width_prect(25),
    y=utils.height_prect(25)
)
# btn1 = Button(
#     center_frame,
#     bg='blue',
#     text='First Button'
# )
# btn1.place(x=0, y=0)
# c1 = Cell()
# c1.create_btn_object(center_frame)
# c1.cell_btn_object.grid(
#     column=0, row=0
# )
# c2 = Cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_object.grid(
#     column=1, row=0
# )
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)

Cell.randomize_mines()
# for c in Cell.all: //Testing for added mines
#     print(c.is_mine)


# Run the window
root.mainloop()
