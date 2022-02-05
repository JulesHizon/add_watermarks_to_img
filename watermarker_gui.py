from tkinter import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

window = Tk()
window.title('Watermarker App')
window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.grid_rowconfigure(0, weight=1)

#Steps
# 1) Build the window GUI
# 2) Build out the buttons to be pressed, to upload/browse files to watermark
# 3) Build the watermarking algorithm using OpenCV2
# 4) Link the GUI with the algorithm
# 5) Build path variables to append '_watermarked' to watermarked_images and put in new folder


#STEP 1
instructions = Label(text = "Choose your image(s) to watermark!", font = ('Calibri', 20,))


#CREATING BUTTONS
def add_files_to_watermark():
    filenames = window.filedialog.askopenfilenames('r')
    print(filenames)

add_files = Button(text="Add Pictures", command=add_files_to_watermark)

#CREATING ENTRY COMPONENT

input = Entry(width = 10)

#GRID
instructions.place(x=0, y=20)
add_files.place(x=0, y=70)
input.place(x=0, y=100)


window.mainloop()