import tkinter as tk
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfilename
import watermarker as wm
import cv2

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

root = tk.Tk()
root.title('Watermarker App')
root.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

#Steps
# 1) Build the window GUI
# 2) Build out the buttons to be pressed, to upload/browse files to watermark
# 3) Build the watermarking algorithm using OpenCV2
# 4) Link the GUI with the algorithm
# 5) Build path variables to append '_watermarked' to watermarked_images and put in new folder

def add_files_to_watermark():
    global files

    added_files = False

    filetypes = [('All files', '*.*')]
    files = askopenfilenames(filetypes=filetypes)

def watermark_files():
    
    if files:
        for file in files:
            wm_img = wm.add_watermark('watermark-01.png', file, opacity=1, pos=(0,0))
            file_path = file.split("/")[-1]
            cv2.imwrite(f"watermarked_{file_path}", wm_img)

#STEP 1
instructions = tk.Label(text = "Choose your image(s) to watermark!", font = ('Calibri', 20,))
add_files = tk.Button(root, text="Add Pictures", command=add_files_to_watermark)
watermark_btn = tk.Button(root, text="Watermark!", command=watermark_files)

#PLACE
instructions.place(x=0, y=20)
add_files.place(x=0, y=70)
watermark_btn.place(x=0, y=100)

root.mainloop()