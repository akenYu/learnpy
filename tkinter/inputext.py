# 加入文本框，让用户可以输入文本，然后点按钮后，弹出消息对话框

from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createwidgets()

	def createwidgets(self):
		self.nameinput = Entry(self)
		self.nameinput.pack()
		self.alertbutton = Button(self, text='hello', command=self.hello)
		self.alertbutton.pack()

	def hello(self):
		name = self.nameinput.get() or 'world'
		messagebox.showinfo('message', 'hello, %s' % name)


if __name__ == '__main__':
	app = Application()
	app.master.title('hello world')
	app.mainloop()