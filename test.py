import math
from random import choice, uniform
import pygame
from pygame.locals import *

if not __name__ == '__main__':
    print('Run this script directly')
    exit(0)

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()
print('PyGame Initiated: ' + str(pygame.get_init()))
print('PyGame Version ' + str(pygame.get_sdl_version()))
(width, height) = (50, 20)
size = [500, 500]  # height and width of the screen
screen = pygame.display.set_mode(size, RESIZABLE)
# background_colour = (0, 0, 128)  # rgb color code - blue
background_colour = white
screen.fill(background_colour)
pygame.display.set_caption('Flock Algorithm Implementation')
# Frame Lock, otherwise it starts to get very processing demanding.
clock = pygame.time.Clock()
clock.tick(30)  # 30 fps lock


class MakiParticle:
    def __init__(self):
        self.x = round(screen.get_width() / 2 - ((screen.get_width() / 2) / uniform(1.5, 2.5)) * uniform(0.1, 1.0))
        self.y = round(screen.get_height() / 2 - ((screen.get_height() / 2) / uniform(1.5, 2.5)) * uniform(0.1, 1.0))
        self.prevx = 0
        self.prevy = 0
        self.size = 5
        self.colour = black
        self.hasdone = False
        self.thickness = 0
        self.headingind = uniform(0, 360)
        self.accmagnitude = None
        self.magnitude = choice([4, 5, 6, 7, 8])
        print('Random heading : ' + str(self.headingind))

        if self.headingind == 0 or 360 and not self.hasdone:
            self.velocityx = 0
            self.velocityy = -self.magnitude

        if 0 < self.headingind < 90 and not self.hasdone:
            angle = 90 - self.headingind
            self.velocityx = round(self.magnitude * math.cos(math.radians(angle)))
            self.velocityy = -round(self.magnitude * math.sin(math.radians(angle)))
            self.accmagnitude = math.sqrt((self.velocityx ** 2 + self.velocityy ** 2))  # readjusted magnitude
            self.headingind = round(math.degrees(math.asin((1/self.accmagnitude)*self.velocityx)))  # WORKS

        if self.headingind == 90 and not self.hasdone:
            self.velocityx = self.magnitude
            self.velocityy = 0

        if 90 < self.headingind < 180 and not self.hasdone:
            angle = self.headingind - 90
            print(self.magnitude * math.cos(math.radians(angle)))
            print(self.magnitude * math.sin(math.radians(angle)))
            self.velocityx = round(self.magnitude * math.cos(math.radians(angle)))
            self.velocityy = round(self.magnitude * math.sin(math.radians(angle)))
            self.accmagnitude = (self.velocityx ** 2 + self.velocityy ** 2)**0.5  # readjusted magnitude
            print(self.velocityy)
            print(self.accmagnitude)
            self.headingind = round(math.degrees(math.asin(self.velocityy/self.accmagnitude))+90)  # WORKS

        if self.headingind == 180 and not self.hasdone:
            self.velocityx = 0
            self.velocityy = self.magnitude

        if 180 < self.headingind < 270 and not self.hasdone:
            angle = self.headingind - 180
            self.velocityy = round(self.magnitude * math.cos(math.radians(angle)))
            self.velocityx = -round(self.magnitude * math.sin(math.radians(angle)))
            self.accmagnitude = math.sqrt((self.velocityx ** 2 + self.velocityy ** 2))  # readjusted magnitude
            self.headingind = round(math.degrees(math.asin(abs(self.velocityx)/self.accmagnitude)) + 180)

        if self.headingind == 270 and not self.hasdone:
            self.velocityx = -self.magnitude
            self.velocityy = 0

        if 270 < self.headingind < 360 and not self.hasdone:
            print(self.magnitude * math.sin(math.radians(self.headingind)))
            print(- self.magnitude * math.cos(math.radians(self.headingind)))
            self.velocityx = round(self.magnitude * math.sin(math.radians(self.headingind)))
            self.velocityy = - round(self.magnitude * math.cos(math.radians(self.headingind)))
            self.accmagnitude = (self.velocityx ** 2 + self.velocityy ** 2)**0.5  # readjusted magnitude
            self.headingind = round(math.degrees(math.asin(abs(self.velocityy)/self.accmagnitude)))+270  # WORKS

        print('Orginal Magnitude is ' + str(self.magnitude))
        self.magnitude = math.sqrt((self.velocityx ** 2 + self.velocityy ** 2))  # readjusted magnitude
        self.radiusrange = {}
        self.skipone = False
        self.hasleftx = False
        self.haslefty = False
        self.target_speed = None
        print('Readjusted heading : '+str(self.headingind))
        print('Velocity x and y are '+str(self.velocityx) + ' '+str(self.velocityy))
        print('Readjusted Magnitude is '+str(self.magnitude))

    def display(self):
        pygame.draw.circle(screen, background_colour, (self.prevx, self.prevy), self.size, self.thickness)
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

    def update(self):  # need to look at calculations again and make sure it bounces properly given the heading... currently going to 360.
        if self.skipone:
            self.hasleftx = False
            self.haslefty = False
            self.skipone = False
        orginx = 0
        orginy = 0
        self.prevx = self.x
        self.prevy = self.y
        endx = int(screen.get_width())
        endy = int(screen.get_height())
        if self.x >= endx or self.x <= orginx:
            self.hasleftx = True
            print((360 - self.headingind))
            self.changeheading(360-self.headingind)
        if self.y >= endy or self.y <= orginy:
            self.haslefty = True
            if self.velocityx > 0:
                print((180 - self.headingind))
                self.changeheading(180-self.headingind)
            elif self.velocityx < 0:
                print((180+self.headingind))
                self.changeheading(180+self.headingind)
        if self.hasleftx:
            self.skipone = True
        if self.haslefty:
            self.skipone = True
        if not self.hasleftx:
            pass
        if not self.haslefty:
            pass
        self.y = self.y + self.velocityy
        self.x = self.x + self.velocityx
        print(self.x)
        print('Point y;'+str(self.y))
        # print(self.x, self.y)
        return self.x, self.y, self.prevx, self.prevy

    def radius(self, objectsdict, objectindexdict, rangeradius=50):  # parameters is the dictionary and the object identifier. [ALGORITHM START]
        global hastargetspeed
        global hascohesion
        global requiredcohesiony
        global requiredcohesionx
        '''for x_index in range(self.x-rangeradius, self.x+rangeradius+1): # attempt the radius of circle
            a = 1
            b = -2*self.y
            c = (rangeradius**2 - (x_index - self.x)**2+self.y**2)
            d = (b ** 2) - (4 * a * c)
            sol1 = (-b - cmath.sqrt(d)) / (2 * a)
            sol2 = (-b + cmath.sqrt(d)) / (2 * a)
            print('1 Y-coord: ' + str(sol1))
            print('2 Y-coord '+str(sol2))'''
        x_radius = range(self.x-rangeradius, self.x+rangeradius)
        y_radius = range(self.y-rangeradius, self.y+rangeradius)  # made a box range instead.
        # print('Exported ' + str(objectsdict))
        hastargetspeed = False
        hascohesion = False
        cohesionx = [self.x]
        cohesiony = [self.y]
        meanxcohesion = 0
        meanycohesion = 0
        for dictindex in range(len(objectsdict)):
            if dictindex != objectindexdict:
                (objx_position, objy_position) = objectsdict.get(dictindex)
                # print(objx_position)
                # print(x_radius)
                if objx_position in x_radius:
                    # print(objy_position)
                    # print(y_radius)
                    if objy_position in y_radius:
                        print('This object is in range')
                        cohesionx.append(objx_position)
                        cohesiony.append(objy_position)
                        for meanxcohesionindex in range(len(cohesionx)):
                            meanxcohesion = meanxcohesion + cohesionx[meanxcohesionindex]
                        for meanycohesionindex in range(len(cohesiony)):
                            meanycohesion = meanycohesion + cohesiony[meanycohesionindex]
        if len(cohesionx) > 1:
            meanycohesion = meanycohesion / len(cohesiony)  # need to find more than one case and then take an average then, for location, [Stage One of Algorithm: Cohesion]
            meanxcohesion = meanxcohesion / len(cohesionx)  # need to find more than one case and then take an average then, for location, [Stage One of Algorithm: Cohesion]
            requiredcohesionx = round(meanxcohesion) - self.x
            requiredcohesiony = round(meanycohesion) - self.y
            print('Object needs to go '+str(requiredcohesionx) + ' in x to get to mean cohesion zone')
            print('Object needs to go '+str(requiredcohesiony) + ' in y to get to mean cohesion zone')  # Works.
            # pygame.draw.line(screen, red, (self.x, self.y), (self.x+requiredcohesionx, self.y+requiredcohesiony), 3)  # Shows the lines of attraction to mean Cohesion zone
            self.target_speed = (((requiredcohesiony**2)+(requiredcohesionx**2))**0.5)*0.75  # speed object needs to travel to get there.
            hastargetspeed = True
            hascohesion = True
            return hastargetspeed, hascohesion, requiredcohesiony, requiredcohesionx

    def heading(self):
        debug = False
        gain_x = self.x-self.prevx
        gain_y = self.y-self.prevy
        pygame.draw.line(screen, background_colour, (self.x-gain_x*3, self.y-gain_y*3), (self.x, self.y), 3)  # Determine Heading and Then Find Average Heading for that range... [Stage Two of Algorithm: Alignment]
        pygame.draw.line(screen, green, (self.x, self.y), (self.x+gain_x*3, self.y+gain_y*3), 3)              # Determine Heading and Then Find Average Heading for that range... [Stage Two of Algorithm: Alignment]
        magnitude = (gain_x**2+gain_y**2)**0.5
        if gain_x > 0:
            if gain_y < 0:
                # positive x and positive y
                if debug:
                    print('Angle: ' + str(round(math.degrees(math.asin((1 / magnitude) * gain_x)))))
                self.headingind = 0 + abs(round(math.degrees(math.asin((1 / magnitude) * gain_x))))
                print('Degrees: ' + str(self.headingind))
            else:
                # positive x and negative y
                if debug:
                    print('Angle: ' + str(round(math.degrees(math.asin((1 / magnitude) * gain_x)))))
                self.headingind = 180 - abs(round(math.degrees(math.asin(((1 / magnitude) * gain_x)))))
                print('Degree: ' + str(self.headingind))
        else:
            if gain_y < 0:
                # negative x and positive y
                if debug:
                    print('Angle: ' + str(round(math.degrees(math.asin((1 / magnitude) * gain_x)))))
                self.headingind = 360 - abs(round(math.degrees(math.asin((1 / magnitude) * gain_x))))
                print('Degree: ' + str(self.headingind))
            else:
                # negative x and negative y
                if debug:
                    print('Angle: ' + str(round(math.degrees(math.asin((1 / magnitude) * gain_x)))))
                self.headingind = 180 + abs(round(math.degrees(math.asin((1 / magnitude) * gain_x))))
                print('Degree: ' + str(self.headingind))

    def objectdetection(self, rangeradius=15):
        x_radius = range(self.x - rangeradius, self.x + rangeradius)
        y_radius = range(self.y - rangeradius, self.y + rangeradius)
        # should be used every loop at the very start of position function call to see nearby objects and avoid them by using random function...
        # if there is a object detected changeheading() in random of 180 to 360...
        randomheading = uniform(120, 240)
        self.headingind +=randomheading

    def changeheading(self, heading):  # this function needs to know change velocities using just an heading...
        self.hasdone = False
        self.headingind = self.headingind + heading
        # to be continued later on with new code...
        # if the new heading is here we need to find out what the magnitude was beforehand and then adjust this.
        if self.headingind == 0 or 360 and not self.hasdone:
            self.velocityx = 0
            self.velocityy = -self.magnitude
            self.hasdone = True
        if 0 < self.headingind < 90 and not self.hasdone:
            self.hasdone = True

        if self.headingind == 90 and not self.hasdone:
            self.velocityx = self.magnitude
            self.velocityy = 0
            self.hasdone = True
        if 90 < self.headingind < 180 and not self.hasdone:
            self.hasdone = True

        if self.headingind == 180 and not self.hasdone:
            self.hasdone = True

        if 180 < self.headingind < 270 and not self.hasdone:
            self.hasdone = True

        if self.headingind == 270 and not self.hasdone:
            self.velocityx = -self.magnitude
            self.velocityy = 0
            self.hasdone = True
        if 270 < self.headingind < 360 and not self.hasdone:
            self.hasdone = True


        # this is where we will adjust the velocities in order to make the object change heading:
        # --> Change direction of object in order to fit new heading, this will lead to float values for velocities...
        # --> We then keep the heading the same but change the magnitude in order to keep the same overall integer values and heading...
        # --> Then we call the target manager that will implement the alogrithm correctly...

    def targettedmanager(self):  # this will move the particle in the correct placement...
        if hastargetspeed:
            print(self.target_speed)
            # continue to change objects attributes to match this heading speed.
        if hascohesion:
            print(requiredcohesiony + requiredcohesionx)
            # continue to change objects attributes to match this coord target.


print('This is the implementation of the Flock Algorithm')
num_of_object = int(input('How many objects do you want in this simulation? '))
Objects_collection = []
for n in range(num_of_object):
    Objects_collection.append(MakiParticle())
objectdict = {}
headingdict = {}
pygame.display.flip()  # this updates screen with previous settings
running = True
objects_registered = 0
while running:
    for object_index in range(len(Objects_collection)):
        Objects_collection[object_index].display()
        Objects_collection[object_index].update()
        objectdict[object_index] = (Objects_collection[object_index].x, Objects_collection[object_index].y)  # updating an database of point locations for reference...
        objects_len = int(len(Objects_collection) + 1)
        Objects_collection[object_index].heading()
        headingdict[object_index] = Objects_collection[object_index].headingind
        if objects_registered >= objects_len:
            # wait until all objects have been registered and then proceed to look at radius...
            Objects_collection[object_index].radius(objectdict, object_index)
            Objects_collection[object_index].targettedmanager()
            # Objects_collection[object_index].changeheading(30)
        else:
            objects_registered += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('User has closed the window.')
            running = False
        if event.type == pygame.VIDEORESIZE:
            print('\r')  # this will delete previous line
            print('\r')
            print('New Height: ' + str(event.h))
            print('New Width: ' + str(event.w))
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            screen.fill(background_colour)
        # x = screen.get_width() / 2
        # y = screen.get_height() / 2
        # pygame.draw.circle(screen, white, (int(x), int(y)), 5, 0)
    pygame.display.flip()
    # print(objectdict)     # DEBUG TOOL DON'T USE WITH MORE THAN 5 OBJECTS UNLESS YOU WANT TO BURN YOUR CPU
    pygame.time.delay(40)   # DEBUG TOOL DON'T USE WITH LESS THAN 20 UNLESS YOU WANT TO BURN YOUR CPU [MAX:15]
