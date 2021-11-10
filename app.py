import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#FFFFFF")
canvas.pack()

frame = tk.Frame(root, bg="#000000")
frame.place(relwidth=1, relheight=1)

label = tk.Label(frame, text="Tkinter Test Program")
label.pack(fill='x')


button = tk.Button(frame, text="Test Button", bg='white', fg='black')
button.pack(fill='x')

root.mainloop()
