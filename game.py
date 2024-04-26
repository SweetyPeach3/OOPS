import tkinter
import tkinter.messagebox
pip install pygame
tkinter.messagebox.showinfo('HI',message='您好')
tkinter.messagebox.showerror('Why',message='你为什么要打开我......')
tkinter.messagebox.showerror('Why',message='我还没有把这个程序做完呢！！！')
tkinter.messagebox.showerror('Why',message='好吧......')
tkinter.messagebox.showinfo('......',message='......')
tkinter.messagebox.showinfo('ok',message='那我试着运行一下吧......')
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("还没做完的小游戏")
