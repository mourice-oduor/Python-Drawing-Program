from tkinter import *
from tkinter import ttk, colorchooser

class main:
    def __init__(painter,master):
        painter.master = master
        painter.color_fg = 'black'
        painter.color_bg = 'white'
        painter.old_x = None
        painter.old_y = None
        painter.penwidth = 5
        painter.drawWidgets()
        painter.c.bind('<B1-Motion>',painter.paint)#drwaing the line 
        painter.c.bind('<ButtonRelease-1>',painter.reset)

    def paint(painter,e):
        if painter.old_x and painter.old_y:
            painter.c.create_line(painter.old_x,painter.old_y,e.x,e.y,width=painter.penwidth,fill=painter.color_fg,capstyle=ROUND,smooth=True)

        painter.old_x = e.x
        painter.old_y = e.y

    def reset(painter,e):    #reseting or cleaning the canvas 
        painter.old_x = None
        painter.old_y = None      

    def changeW(painter,e): #change Width of pen through slider
        painter.penwidth = e
           

    def clear(painter):
        painter.c.delete(ALL)

    def change_fg(painter):  #changing the pen color
        painter.color_fg=colorchooser.askcolor(color=painter.color_fg)[1]

    def change_bg(painter):  #changing the background color canvas
        painter.color_bg=colorchooser.askcolor(color=painter.color_bg)[1]
        painter.c['bg'] = painter.color_bg

    def drawWidgets(painter):
        painter.controls = Frame(painter.master,padx = 5,pady = 5)
        Label(painter.controls, text='Pen Width:',font=('arial 18')).grid(row=0,column=0)
        painter.slider = ttk.Scale(painter.controls,from_= 5, to = 100,command=painter.changeW,orient=VERTICAL)
        painter.slider.set(painter.penwidth)
        painter.slider.grid(row=0,column=1,ipadx=30)
        painter.controls.pack(side=LEFT)
        
        painter.c = Canvas(painter.master,width=500,height=400,bg=painter.color_bg,)
        painter.c.pack(fill=BOTH,expand=True)

        menu = Menu(painter.master)
        painter.master.config(menu=menu)
        filemenu = Menu(menu)
        colormenu = Menu(menu)
        menu.add_cascade(label='Colors',menu=colormenu)
        colormenu.add_command(label='Brush Color',command=painter.change_fg)
        colormenu.add_command(label='Background Color',command=painter.change_bg)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Options',menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas',command=painter.clear)
        optionmenu.add_command(label='Exit',command=painter.master.destroy) 
        
        

if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Python Drawing Application')
    root.mainloop()
