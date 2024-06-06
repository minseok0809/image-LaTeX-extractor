import clipboard
from tkinter import *
import tkinter.filedialog as fd
from pix2tex.cli import LatexOCR
from PIL import Image
import webbrowser


def callback(url):
   webbrowser.open_new_tab(url)

def one():
   file_path = fd.askopenfilename()
   file_path = str(file_path)
   model = LatexOCR()
   with Image.open(file_path) as img:
      latex_text = model(img)
   img.close()
   latex_text = '$ ' + latex_text + ' $' 
   clipboard.copy(latex_text)
   e1.delete(0, len(e1.get()))             
   e1.insert(0, latex_text)  


window = Tk()
window.title('Image LaTeX Extractor')
window_width = 600
window_height = 300
window_pos_x = 500
window_pos_y = 100
window.geometry("{}x{}+{}+{}".format(window_width, window_height, window_pos_x, window_pos_y))
window.resizable(width=False, height=False)

l1 = Label(window, text = 'Image LaTeX Extractor', fg = 'orange', font = 'helvetica 16 bold')
l1.pack()
l1.place(x=20, y=10)

e1 = Entry(window)
e1.pack()
e1.place(x=20, y=60, width=400, height=50)

b1 = Button(window, text = "Load Image File", command=one)  
b1.pack()
b1.place(x=20, y=140)


l2 = Label(window, text = 'Acknowledgment: lukas-blecher/LaTeX-OCR', fg = 'black', font = 'helvetica 12 bold')
l2.pack()
l2.place(x=20, y=200)
l2.bind("<Button-1>", lambda e: callback("https://github.com/lukas-blecher/LaTeX-OCR"))
window.mainloop()