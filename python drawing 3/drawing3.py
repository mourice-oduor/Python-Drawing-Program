from tkinter import *
from tkinter import ttk, colorchooser, filedialog

try:
    import PIL
except:
    from PIL import ImageGrab


class main:
    def __init__(paint,master):
        paint.master = master
        paint.color_fg = 'black'
        paint.color_bg = 'white'
        paint.old_x = None
        paint.old_y = None
        paint.penwidth = 5
        paint.drawWidgets()
        paint.c.bind('<B1-Motion>',paint.paint)
        paint.c.bind('<ButtonRelease-1>',paint.reset)

    def paint(paint,e):
        if paint.old_x and paint.old_y:
            paint.c.create_line(paint.old_x,paint.old_y,e.x,e.y,width=paint.penwidth,fill=paint.color_fg,capstyle=ROUND,smooth=True)

        paint.old_x = e.x
        paint.old_y = e.y

    def reset(paint,e):
        paint.old_x = None
        paint.old_y = None      

    def changeW(paint,e):
        paint.penwidth = e

    def save(paint):
        file = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png')])
        if file:
            x = paint.master.winfo_rootx() + paint.c.winfo_x()
            y = paint.master.winfo_rooty() + paint.c.winfo_y()
            x1 = x + paint.c.winfo_width()
            y1 = y + paint.c.winfo_height()

            PIL.ImageGrab.grab().crop((x,y,x1,y1)).save(file + '.png')
            
           

    def clear(paint):
        paint.c.delete(ALL)

    def change_fg(paint):
        paint.color_fg=colorchooser.askcolor(color=paint.color_fg)[1]

    def change_bg(paint):
        paint.color_bg=colorchooser.askcolor(color=paint.color_bg)[1]
        paint.c['bg'] = paint.color_bg

    def drawWidgets(paint):
        paint.controls = Frame(paint.master,padx = 5,pady = 5)
        Label(paint.controls, text='Pen Width: ',font=('',15)).grid(row=0,column=0)
        paint.slider = ttk.Scale(paint.controls,from_= 5, to = 100, command=paint.changeW,orient=HORIZONTAL)
        paint.slider.set(paint.penwidth)
        paint.slider.grid(row=0,column=1,ipadx=30)
        paint.controls.pack()
        
        paint.c = Canvas(paint.master,width=500,height=400,bg=paint.color_bg,)
        paint.c.pack(fill=BOTH,expand=True)

        menu = Menu(paint.master)
        paint.master.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='File..',menu=filemenu)
        filemenu.add_command(label='Export..',command=paint.save)
        colormenu = Menu(menu)
        menu.add_cascade(label='Colors',menu=colormenu)
        colormenu.add_command(label='Brush Color',command=paint.change_fg)
        colormenu.add_command(label='Background Color',command=paint.change_bg)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Options',menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas',command=paint.clear)
        optionmenu.add_command(label='Exit',command=paint.master.destroy) 
        
        

if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Python DrawingApp')
    root.mainloop()
