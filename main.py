from tkinter import *
import numpy as np
from math import *
import time

class MainWindow(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title('Tables de multiplication')
		self._drawing = Drawing(self,width=700,height=700)
		self._rightCommands = Frame(self)
		self._nSetScaleFrame = LabelFrame(self._rightCommands,text='Table')
		self._nSetScale = Scale(self._nSetScaleFrame,variable=self._drawing._n,from_=2,to=100,command=self._drawing.updateDrawing,orient='horizontal')
		self._modSetScaleFrame = LabelFrame(self._rightCommands,text='Modulo')
		self._modSetScale = Scale(self._modSetScaleFrame,variable=self._drawing._mod,from_=10,to=400,command=self._drawing.updateTheta,orient='horizontal')
		self._motionFrame = LabelFrame(self._rightCommands,text='Animation')
		self._nStartEntry = Entry(self._motionFrame,textvariable=self._drawing._nStart)
		self._nEndEntry = Entry(self._motionFrame,textvariable=self._drawing._nEnd)
		self._nMotionButtonStart = Button(self._motionFrame,command=self._drawing.startMotion,text='Start')
		self._nMotionButtonStop = Button(self._motionFrame,command=self._drawing.stopMotion,text='Stop')
		
		self._drawing.pack(side=LEFT,padx=10)
		self._rightCommands.pack(side=LEFT,padx=10)
		self._nSetScaleFrame.pack(side=TOP,pady=10)
		self._nSetScale.pack()
		self._modSetScaleFrame.pack(side=TOP,pady=10)
		self._modSetScale.pack()
		self._motionFrame.pack(side=TOP,pady=10)
		self._nStartEntry.pack(side=LEFT)
		self._nEndEntry.pack(side=LEFT)
		self._nMotionButtonStart.pack(side=LEFT)
		self._nMotionButtonStop.pack(side=LEFT)

class Drawing(Canvas):
	def __init__(self, *args, **kwargs):
		Canvas.__init__(self, **kwargs)
		self._centerPosition = 350
		self._radius = 300
		self.drawCircle()
		self._n = IntVar()
		self._n.set(2)
		self._mod = IntVar()
		self._mod.set(200)
		self._linesIds = []
		self.updateTheta()
		# self.config(scrollregion=(-1,-1,1,1))
		self._nStart = StringVar()
		self._nStart.set('2')
		self._nEnd = StringVar()
		self._nEnd.set('10')
		self._dn = 1
		self._dt = 200 #ms
		self._motionActive = False

	def updateTheta(self,_=None):
		self._theta = 2*pi/self._mod.get()
		self.updateDrawing()

	def drawCircle(self):
		self.create_oval(self._centerPosition - self._radius,self._centerPosition - self._radius,self._centerPosition + self._radius,self._centerPosition + self._radius)

	def drawLine(self,n1,n2):
		self._linesIds.append(self.create_line(self._centerPosition + self._radius*np.cos(self._theta*n1),self._centerPosition + self._radius*np.sin(self._theta*n1),self._centerPosition + self._radius*np.cos(self._theta*n2),self._centerPosition + self._radius*np.sin(self._theta*n2)))

	def drawTable(self):
		for k in range(self._mod.get()):
			self.drawLine(k,k*self._n.get())

	def deleteTable(self):
		for line in self._linesIds:
			self.delete(line)
		self._linesIds = []

	def updateDrawing(self,_=None):
		self.deleteTable()
		self.drawTable()

	def startMotion(self):
		self._motionActive = True
		self._n.set(int(self._nStart.get()))
		self._n2 = int(self._nEnd.get())
		self.playMotion()

	def playMotion(self):
		t1 = time.time()
		self.updateDrawing()
		self._n.set(self._n.get() + self._dn)
		t2 = time.time()
		if self._n.get() < self._n2 and self._motionActive:
			self.after(max(int(self._dt-1000*(t2-t1)),1),self.playMotion)

	def stopMotion(self):
		self._motionActive = False


class Table:
	def __init__(self, n, modulo):
		self._n = n
		self._modulo = modulo

w = MainWindow()
w.attributes('-zoomed',True)
w.mainloop()