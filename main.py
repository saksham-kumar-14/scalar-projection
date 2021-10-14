#scalar projection

import pygame, sys, math 
import pygame.gfxdraw
pygame.init()
WIDTH,HEIGHT = 900,700
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

class Vector:
	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2
		self.constant = 5 
		
	def draw(self,color):
		#pygame.draw.line(SCREEN,color,self.coor1,self.coor2)
		pygame.gfxdraw.filled_polygon(SCREEN,(self.coor1,(self.coor1[0],self.coor1[1]+self.constant),(self.coor2[0],self.coor2[1]+self.constant),self.coor2),color)

class Representation_dots:
	def __init__(self,x,y,color):
		self.x,self.y = x,y 
		self.color = color 
		self.radius = 10

	def draw(self):
		pygame.draw.circle(SCREEN,self.color,(self.x,self.y),self.radius)



if __name__ == '__main__':
	vectors_meet_x,vectors_meet_y = 400,450
	static_vector_x,static_vector_y = 700,450
	static_vector = Vector((vectors_meet_x,vectors_meet_y),(static_vector_x,static_vector_y))
	static_vector_color = (255,0,0)
	dynamic_vector_color = (0,255,0)
	dynamic_projection_vector_color = (0,255,255)

	#static vector representation dot
	vectors_meet_representation_dot = Representation_dots(vectors_meet_x,vectors_meet_y,(255,255,255))
	static_vector_representation_dot = Representation_dots(static_vector_x,static_vector_y,(255,255,255))
	
	while True :
		for event in pygame.event.get():
			if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()

		#dynamic vector
		mouse_pos = pygame.mouse.get_pos()
		dynamic_vector = Vector((vectors_meet_x,vectors_meet_y),(mouse_pos[0],mouse_pos[1]))

		#calculating the angle between lines
		static_vector_slope = (static_vector_y-vectors_meet_y)/(static_vector_x-vectors_meet_x)
		if(mouse_pos[0]-vectors_meet_x == 0):
			dynamic_vector_slope = "infinite"
		else:
			dynamic_vector_slope = (mouse_pos[1]-vectors_meet_y)/(mouse_pos[0]-vectors_meet_x)

		if dynamic_vector_slope == "infinite":
			dynamic_vector_projection_distance = 0 
		else:
			theta = math.atan((dynamic_vector_slope-static_vector_slope)/(1+static_vector_slope*dynamic_vector_slope))
			dynamic_vector_distance = math.sqrt((vectors_meet_x-mouse_pos[0])**2 + (vectors_meet_y-mouse_pos[1])**2)
			dynamic_vector_projection_distance = dynamic_vector_distance*math.cos(theta) 

		#calculating dynamic projection vector x ,y
		if(mouse_pos[0] < vectors_meet_x):
			dynamic_projection_vector_y = static_vector_y
			dynamic_projection_vector_x = - math.sqrt( (dynamic_vector_projection_distance)**2 - (static_vector_y-vectors_meet_y)**2 ) + vectors_meet_x

		else:
			dynamic_projection_vector_y = static_vector_y
			dynamic_projection_vector_x = math.sqrt( (dynamic_vector_projection_distance)**2 - (static_vector_y-vectors_meet_y)**2 ) + vectors_meet_x


		#drawing stuff
		SCREEN.fill((0,0,0))
		static_vector.draw(static_vector_color)
		dynamic_vector.draw(dynamic_vector_color)

		#dynamic projection vector 
		dynamic_projection_vector = Vector((vectors_meet_x,vectors_meet_y),(dynamic_projection_vector_x,dynamic_projection_vector_y))
		dynamic_projection_vector.draw((dynamic_projection_vector_color))

		#dynamic vector and projection vector representation dots
		dynamic_vector_representation_dot = Representation_dots(mouse_pos[0],mouse_pos[1],(255,255,255))
		dynamic_projection_vector_representation_dot = Representation_dots(dynamic_projection_vector_x,dynamic_projection_vector_y,(255,255,255))

		#drawing representation dots
		vectors_meet_representation_dot.draw()
		static_vector_representation_dot.draw()
		dynamic_vector_representation_dot.draw()
		dynamic_projection_vector_representation_dot.draw()

		#drawing the y - component of the dynamic vector
		perpendicular = Vector((mouse_pos[0],mouse_pos[1]),(dynamic_projection_vector_x,dynamic_projection_vector_y))
		perpendicular.draw((255,255,0))

		pygame.display.update()

