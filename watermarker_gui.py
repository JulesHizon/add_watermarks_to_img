import tkinter as tk
from tkinter.filedialog import askopenfilenames
import watermarker as wm
import cv2

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 250

root = tk.Tk()
root.title('Watermarker App')
root.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

def update_instructions():
    instructions.config(text=f'{len(files)} picture(s) loaded')

def add_files_to_watermark():
    global files

    filetypes = [('All files', '*.*')]
    files = askopenfilenames(filetypes=filetypes)
    if files:
        instructions.config(text=f'{len(files)} picture(s) loaded')

def watermark_files():
    
    if files:
        for file in files:
            wm_img = wm.add_watermark(file)
            file_path = file.split("/")[-1]
            cv2.imwrite(f"watermarked_{file_path}", wm_img)
        instructions.config(text=f"{len(files)} picture(s) successfully watermarked!")

instructions = tk.Label(text = "Choose your image(s) to watermark!", font = ('Calibri', 20,))
add_files = tk.Button(root, text="Add Pictures", command=add_files_to_watermark)
watermark_btn = tk.Button(root, text="Watermark!", command=watermark_files)

instructions.place(x=25, y=20)
add_files.place(x=200, y=70)
watermark_btn.place(x=200, y=100)

root.mainloop()