import os
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'gray90', relief = 'raised')
canvas1.pack()

def myCmd ():
    os.system('cmd /k "cd s1 && python wordpress_bot.py && cd.. && cd s2 && python wordpress_bot.py && cd.. && cd s3 && python wordpress_bot.py && cd.. && cd s4 && python wordpress_bot.py && cd.. && cd s5 && python wordpress_bot.py"')
     
button1 = tk.Button(text='      Run Command      ', command=myCmd, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=button1)

root.mainloop()