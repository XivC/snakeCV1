from graph import *
import random
import numpy as np
import cv2
import cognitive_face as CF
import math
import glob

WIDTH = 20
HEIGHT = 20
SCALE = 25   # Size of square
GameSpeed = 10 # Ticks per second
TICKS = 0



LoseLabel = 0
windowSize(h = HEIGHT*SCALE,w = WIDTH*SCALE)
canvasSize(h = HEIGHT*SCALE,w = WIDTH*SCALE)

OBJECTS = []

brushColor("black")
rectangle(0,0,WIDTH*SCALE,HEIGHT*SCALE)


def drawField():

	penColor("white")

	global SCALE,WIDTH,HEIGHT
	
	for i in range(HEIGHT):
		line(0,i*SCALE-1,HEIGHT*SCALE,i*SCALE-1)
		
	for j in range(WIDTH):
		line(j*SCALE-1,0,j*SCALE-1,WIDTH*SCALE)
		
		
	
	
def rangeCollision(x1,y1,x2,y2,xrange,yrange):

	return x1-x2 in range(-xrange+1,xrange-1) and y1-y2 in range(-yrange+1,yrange-1)

def tick():
	

	global TICKS
	global fxp,fyp
	TICKS += 1

	a,frame = cap1.read()
    #cv2.imshow('frame',frame)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faceCascade = cv2.CascadeClassifier(r'C:\Users\XivS\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
	faces = faceCascade.detectMultiScale(
        gray,     

		minNeighbors=5,     
		minSize=(10, 10)
	)
	cv2.imshow('a',gray)
	if(len(faces) > 0) :


		face = faces[0]
		#print(face)
		fx = face[0]
		fy = face[1]
		deltaX = fx-fxp
		deltaY = fy-fyp
		deltaXY = abs(deltaX)-abs(deltaY)
		print(deltaXY)
		if deltaXY > 0:
			if abs(deltaX) > 25 and TICKS > 1 :
				
				if(deltaX > 0): #left
					emulatedMove('left')

				if(deltaX < 0): #right
					emulatedMove('right')

		else:
			if abs(deltaY) > 15 and TICKS > 1:
				
				if(deltaY > 0): #left
					emulatedMove('down')

				if(deltaY < 0): #right
					emulatedMove('up')


		fxp = fx
		fyp = fy






	for i in OBJECTS:
		i.tickEvent()

	

def getRectangleObject(x1,y1,x2,y2,pcolor,bcolor,psize):

	brushColor(bcolor)
	penColor(pcolor)
	penSize(psize)
	
	return rectangle(x1,y1,x2,y2)


class Object():

	x = None
	y = None
	sprite = None
	name = "OBJECT"
	args = {}
	
	def __init__(self,x = 0,y = 0, args = {}):
	
		global OBJECTS
	
		self.x = x
		self.y = y
		self.args = args
		OBJECTS.append(self)
		self.__createEvent__()
		
	def __createEvent__(self):
		pass
		
	def tickEvent(self):
		pass
	def destroy(self):
		deleteObject(self.sprite)
		OBJECTS.remove(self)
		del self
		


class apple(Object):

	color = ''

	def __createEvent__(self):
	
		self.name = "apple"
		self.sprite = getRectangleObject(self.x*SCALE,self.y*SCALE,self.x*SCALE+SCALE,self.y*SCALE+SCALE,"black","red",0)
		self.respawn()
		
	def respawn(self):
		
		self.x = random.randint(0,WIDTH-1)
		self.y = random.randint(0,HEIGHT-1)
		
		for i in OBJECTS:
			while (self.x == i.x and self.y == i.y and i.name != "apple"):
				self.x = random.randint(0,WIDTH-1)
				self.y = random.randint(0,HEIGHT-1)

				
		deleteObject(self.sprite)
		print(str(self.x)+" "+str(self.y))
		self.sprite = getRectangleObject(self.x*SCALE,self.y*SCALE,self.x*SCALE+SCALE,self.y*SCALE+SCALE,"black","red",0)
	
	
		
		
class block(Object):
	color = None
	def __createEvent__(self):
		self.name = "block"
		self.color = self.args['color']
		self.sprite = getRectangleObject(self.x*SCALE,self.y*SCALE,self.x*SCALE+SCALE-1,self.y*SCALE+SCALE-1,(0,0,0),self.color,0)

		
		
class snake(Object):

	blocks = []
	
	dx = None
	dy = None
	plr = None
	color = None
	def __createEvent__(self):
		self.plr = self.args['player']
		self.dy = -1
		self.dx = 0
		self.color = self.args['color']
		self.sprite = getRectangleObject(self.x*SCALE,self.y*SCALE,self.x*SCALE+SCALE-1,self.y*SCALE+SCALE-1,(0,0,0),self.color,0)
		
		self.blocks.append(self)
		
		for i in range(1,5):
			#self.blocks.append(block(x = self.blocks[i-1].x,y = self.blocks[i-1].y-self.dy))
			self.blocks.append(block(x = -1,y = -1,args = {'color': self.color}))
			
	def tickEvent(self):
		
	

	
	
		self.x = (self.x + self.dx)%(WIDTH+1)
		self.y = (self.y + self.dy)%(HEIGHT+1)
		
		if self.x < 0:
			self.x = WIDTH
		if self.y < 0:
			self.y = HEIGHT
		moveObjectTo(self.sprite,self.x*SCALE,self.y*SCALE)
		
		for i in range(len(self.blocks)-1,0,-1):
			
			self.blocks[i].x = self.blocks[i-1].x
			self.blocks[i].y = self.blocks[i-1].y
			moveObjectTo(self.blocks[i].sprite,self.blocks[i].x*SCALE,self.blocks[i].y*SCALE)
		blk = [x for x in self.blocks]
		blk.remove(self)
		blk.remove(blk[0])
		for i in OBJECTS:
			if self.x == i.x and self.y == i.y:
				if i.name == "apple":
				
					self.blocks.append(block(x = -1,y = -1,args = {'color': self.color}))
					i.respawn()
				else:
				
					if i.color != self.color or i in blk:
					
					
						for i in self.blocks:
					
							i.destroy()
						for i in OBJECTS:
							i.destroy()
					
						killTimer(Ttimer)
					
						
						LoseLabel = label("You lose",(WIDTH-1)*SCALE//2,(HEIGHT-1)*SCALE//2)
				
				
				
				
			
			
def emulatedMove(key):
	global snakee
		
	if key == 'left':
	
		if snakee.dx != 1:
		
			snakee.dy = 0
			snakee.dx = -1
	if key == 'right':
		
		if snakee.dx != -1:
		
			snakee.dy = 0
			snakee.dx = 1
	if key == 'up':
		
		if snakee.dy != 1:
			snakee.dy = -1
			snakee.dx = 0
	if key == 'down':
	
		if snakee.dy != -1:
		
			snakee.dy = 1
			snakee.dx = 0
		
					
			
	
def keyPressed(key):
	global snakee
		
	if key.keycode == VK_LEFT:
	
		if snakee.dx != 1:
		
			snakee.dy = 0
			snakee.dx = -1
	if key.keycode == VK_RIGHT:
		
		if snakee.dx != -1:
		
			snakee.dy = 0
			snakee.dx = 1
	if key.keycode == VK_UP:
		
		if snakee.dy != 1:
			snakee.dy = -1
			snakee.dx = 0
	if key.keycode == VK_DOWN:
	
		if snakee.dy != -1:
		
			snakee.dy = 1
			snakee.dx = 0
		
		
def game_start():

	







	global snakee,ap,Ttimer,LoseLabel,RestartButton,OBJECTS
	

	LoseLabel = 0
	RestartButton = 0
	
	
	snakee = snake(x = WIDTH//2,y = HEIGHT,args = {

		'color': 'yellow',
		'player': 'asd'

		})
	ap = apple()


	kkey = onKey(keyPressed)

		
	drawField()
	

	Ttimer = onTimer(tick,1000//GameSpeed)
	


 
def registration():


	global cap1


	key = '4aafb44ca79a4eac8b423f9bd6d018f4'  # Replace with a valid Subscription Key here.
	CF.Key.set(key)

	base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
	CF.BaseUrl.set(base_url)
	faces = []
	while len(faces) != 1:
		a,frame = cap1.read()
	    #cv2.imshow('frame',frame)
		gray = frame#cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faceCascade = cv2.CascadeClassifier('C:\\Users\\XivS\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\data\\haarcascade_frontalface_default.xml')
		faces = faceCascade.detectMultiScale(
	        gray,     

			minNeighbors=5,     
			minSize=(10, 10)
		)
	cv2.imshow('registration',gray)
	if(len(faces) == 1) :

		imgs = glob.glob('C:\\Users\\Xiv\\Desktop\\itstart\\images\\*.*')
		print (imgs)
		cv2.imwrite('temp.jpg', frame)

		for i in imgs:
			
			img_urls = [
	    	'temp.jpg',
	   		 i ]

			faces = [CF.face.detect(img_url) for img_url in img_urls]
			nick = i.split('\\')[-1].split('.')[0]
			similarity = CF.face.verify(faces[0][0]['faceId'], faces[1][0]['faceId'])
			print(i.split('\\')[-1].split('.')[0] +' ' + str(similarity['isIdentical']))
			if similarity['isIdentical'] == True:

				print('founded ' + i.split('\\')[-1].split('.')[0])
				player1_nick = nick
				break
			



	pass

	
#snakee,ap,Ttimer = 0,0,0
cap1 = cv2.VideoCapture(0)
fxp,fyp = 0,0
player1_nick,player2_nick = '',''
registration()
game_start()
run()


	
	
