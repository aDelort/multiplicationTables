from tkinter import *
import numpy as np
from math import *

class MainWindow(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title('Tables de multiplication')
		self._drawing = Drawing(self,width=700,height=700)
		
		self._drawing.pack()

class Drawing(Canvas):
	def __init__(self, *args, **kwargs):
		Canvas.__init__(self, **kwargs)
		self._centerPosition = 350
		self._radius = 300
		self._n = 47
		self._mod = 200
		self._theta = 2*pi/self._mod
		# self.config(scrollregion=(-1,-1,1,1))
		self.drawCircle()
		self.drawTable()

	def drawCircle(self):
		self.create_oval(self._centerPosition - self._radius,self._centerPosition - self._radius,self._centerPosition + self._radius,self._centerPosition + self._radius)

	def drawLine(self,n1,n2):
		self.create_line(self._centerPosition + self._radius*np.cos(self._theta*n1),self._centerPosition + self._radius*np.sin(self._theta*n1),self._centerPosition + self._radius*np.cos(self._theta*n2),self._centerPosition + self._radius*np.sin(self._theta*n2))

	def drawTable(self):
		for k in range(self._mod):
			self.drawLine(k,k*self._n)

class Table:
	def __init__(self, n, modulo):
		self._n = n
		self._modulo = modulo

w = MainWindow()
w.attributes('-zoomed',True)
w.mainloop()