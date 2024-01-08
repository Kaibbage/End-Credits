#Kai Sundararaj
#101240325

import string
import pygame

#initializing pygame, font, display, and background
pygame.init()

white = (255, 255, 255)

X, Y = 1000, 800

myfont = pygame.font.SysFont('Comic Sans MS', 50)

display_window = pygame.display.set_mode((X, Y))
display_window.fill(white)

s = pygame.image.load('star1.jpeg')

pygame.Surface.blit(display_window, s, (0, 0))
pygame.display.update()

#func to show end credits
def show_words(words, counter1):
	
	#for first 5 lines
	if(counter1 == 0):
		for a in range(Y):
			pygame.Surface.blit(display_window, s, (0, 0))


			text1 = myfont.render(words[counter1], True, (255*a/800, 255*a/800, 255 - 255*a/800))
			text1rect = text1.get_rect()
			text1rect.center = (X/2, Y-a)
			display_window.blit(text1, text1rect)

			if(a > 160):
				text2 = myfont.render(words[counter1+1], True, (255*(a-160)/800, 255*(a-160)/800, 255 - 255*(a-160)/800))
				text2rect = text2.get_rect()
				text2rect.center = (X/2, Y-a+160)
				display_window.blit(text2, text2rect)
			if(a > 320):
				text3 = myfont.render(words[counter1+2], True, (255*(a-320)/800, 255*(a-320)/800, 255 - 255*(a-320)/800))
				text3rect = text3.get_rect()
				text3rect.center = (X/2, Y-a+320)
				display_window.blit(text3, text3rect)
			if(a > 480):
				text4 = myfont.render(words[counter1+3], True, (255*(a-480)/800, 255*(a-480)/800, 255 - 255*(a-480)/800))
				text4rect = text4.get_rect()
				text4rect.center = (X/2, Y-a+480)
				display_window.blit(text4, text4rect)
			if(a > 640):
				text5 = myfont.render(words[counter1+4], True, (255*(a-640)/800, 255*(a-640)/800, 255 - 255*(a-640)/800))
				text5rect = text5.get_rect()
				text5rect.center = (X/2, Y-a+640)
				display_window.blit(text5, text5rect)

		
			pygame.display.update()

			pygame.time.delay(2)


	#for everything not first 5 lines
	elif(counter1 < len(words)-4):
		for a in range(Y-640):

			#redrawing background
			pygame.Surface.blit(display_window, s, (0, 0))

			#choosing colours and what to write, colours go from blue to yellow as the lines rise
			text1 = myfont.render(words[counter1], True, (255*(a+640)/800, 255*(a+640)/800, 255 - 255*(a+640)/800))
			text2 = myfont.render(words[counter1+1], True, (255*(a+480)/800, 255*(a+480)/800, 255 - 255*(a+480)/800))
			text3 = myfont.render(words[counter1+2], True, (255*(a+320)/800, 255*(a+320)/800, 255 - 255*(a+320)/800))
			text4 = myfont.render(words[counter1+3], True, (255*(a+160)/800, 255*(a+160)/800, 255 - 255*(a+160)/800))
			text5 = myfont.render(words[counter1+4], True, (255*a/800, 255*a/800, 255 - 255*a/800))

			#making rectangles
			text1rect = text1.get_rect()
			text2rect = text2.get_rect()
			text3rect = text3.get_rect()
			text4rect = text4.get_rect()
			text5rect = text5.get_rect()

			#centering rectangles
			text1rect.center = (X/2, Y-(800-(160-a)))
			text2rect.center = (X/2, Y-(640-(160-a)))
			text3rect.center = (X/2, Y-(480 -(160-a)))
			text4rect.center = (X/2, Y-(320 -(160-a)))
			text5rect.center = (X/2, Y-(160 -(160-a)))

			#blitting the text in rectangles onto screen
			display_window.blit(text1, text1rect)
			display_window.blit(text2, text2rect)
			display_window.blit(text3, text3rect)
			display_window.blit(text4, text4rect)
			display_window.blit(text5, text5rect)

			#updating display
			pygame.display.update()

			#displaying for a tiny amount of time
			pygame.time.delay(2)

	#for last 4 lines
	else:
		if(counter1 == len(words)-4):
			for a in range (Y-640):
				pygame.Surface.blit(display_window, s, (0, 0))

				text1 = myfont.render(words[counter1], True, (255*(a+640)/800, 255*(a+640)/800, 255 - 255*(a+640)/800))
				text2 = myfont.render(words[counter1+1], True, (255*(a+480)/800, 255*(a+480)/800, 255 - 255*(a+480)/800))
				text3 = myfont.render(words[counter1+2], True, (255*(a+320)/800, 255*(a+320)/800, 255 - 255*(a+320)/800))
				text4 = myfont.render(words[counter1+3], True, (255*(a+160)/800, 255*(a+160)/800, 255 - 255*(a+160)/800))
			
				text1rect = text1.get_rect()
				text2rect = text2.get_rect()
				text3rect = text3.get_rect()
				text4rect = text4.get_rect()

				text1rect.center = (X/2, Y-(800-(160-a)))
				text2rect.center = (X/2, Y-(640-(160-a)))
				text3rect.center = (X/2, Y-(480 -(160-a)))
				text4rect.center = (X/2, Y-(320 -(160-a)))

				display_window.blit(text1, text1rect)
				display_window.blit(text2, text2rect)
				display_window.blit(text3, text3rect)
				display_window.blit(text4, text4rect)


				pygame.display.update()

				pygame.time.delay(2)

		elif(counter1 == len(words)-3):
			for a in range (Y-640):
				pygame.Surface.blit(display_window, s, (0, 0))

				text1 = myfont.render(words[counter1], True, (255*(a+640)/800, 255*(a+640)/800, 255 - 255*(a+640)/800))
				text2 = myfont.render(words[counter1+1], True, (255*(a+480)/800, 255*(a+480)/800, 255 - 255*(a+480)/800))
				text3 = myfont.render(words[counter1+2], True, (255*(a+320)/800, 255*(a+320)/800, 255 - 255*(a+320)/800))
			
				text1rect = text1.get_rect()
				text2rect = text2.get_rect()
				text3rect = text3.get_rect()

				text1rect.center = (X/2, Y-(800-(160-a)))
				text2rect.center = (X/2, Y-(640-(160-a)))
				text3rect.center = (X/2, Y-(480 -(160-a)))

				display_window.blit(text1, text1rect)
				display_window.blit(text2, text2rect)
				display_window.blit(text3, text3rect)


				pygame.display.update()

				pygame.time.delay(2)

		elif(counter1 == len(words)-2):
			for a in range (Y-640):
				pygame.Surface.blit(display_window, s, (0, 0))

				text1 = myfont.render(words[counter1], True, (255*(a+640)/800, 255*(a+640)/800, 255 - 255*(a+640)/800))
				text2 = myfont.render(words[counter1+1], True, (255*(a+480)/800, 255*(a+480)/800, 255 - 255*(a+480)/800))

				text1rect = text1.get_rect()
				text2rect = text2.get_rect()

				text1rect.center = (X/2, Y-(800-(160-a)))
				text2rect.center = (X/2, Y-(640-(160-a)))

				display_window.blit(text1, text1rect)
				display_window.blit(text2, text2rect)


				pygame.display.update()

				pygame.time.delay(2)

		elif(counter1 == len(words)-1):
			for a in range (Y-640):
				pygame.Surface.blit(display_window, s, (0, 0))

				text1 = myfont.render(words[counter1], True, (255*(a+640)/800, 255*(a+640)/800, 255 - 255*(a+640)/800))
			
				text1rect = text1.get_rect()

				text1rect.center = (X/2, Y-(800-(160-a)))

				display_window.blit(text1, text1rect)


				pygame.display.update()

				pygame.time.delay(2)



	

def main():

	#opening and reading file
	try:
		f = open("end_credits.txt", "r")
	except:
		print("no file named 'end_credits.txt'")
		exit()

	#initializing variables
	a = []
	c = 0
	b = 0

	#making list of end credit lines
	while(True):
		a.append(f.readline())
	
		#stopping at eof
		if(a[c] == ''):
			break
		c+=1

	#removing \n from end credit lines
	for g in range(len(a)):
		a[g] = a[g].strip("\n")

	#starting from last point seen
	try:
		f2 = open("blonglo.txt", "r")
		last_line = f2.readline()

		#finding where last point is (assuming no 2 lines are identical)
		for d in range(len(a)):
			if(a[d] == last_line):
				b = d

		if(last_line == ''):
			b = 0
			
	except:
		b = 0


	#loop to keep going until user closes it 
	exit_flag = False 
	while not exit_flag: 
		#sending info about which lines to func show_words
		show_words(a, b)
		if(b < len(a)):
			b+=1
		for e in pygame.event.get(): 
			if e.type == pygame.QUIT: 
				exit_flag = True

				#when exited writing down which line it was ended on
				file_write = open("blonglo.txt", "w")
				file_write.write(a[b-1])

		
	
#calling main
main()

		

	
