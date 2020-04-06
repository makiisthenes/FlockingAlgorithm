import pygame
from pygame.locals import *
from random import choice, uniform
import math

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
clock.tick(30)  # 60 fps lock


class MakiParticle:
    def __init__(self):
        self.x = round(screen.get_width() / 2 - ((screen.get_width() / 2) / uniform(1.5, 2.5)) * uniform(0.1, 1.0))
        self.y = round(screen.get_height() / 2 - ((screen.get_height() / 2) / uniform(1.5, 2.5)) * uniform(0.1, 1.0))
        self.prevx = 0
        self.prevy = 0
        self.size = 5
        self.colour = black
        self.thickness = 0
        self.velocityx = choice([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        self.velocityy = choice([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        self.magnitude = (self.velocityx**2+self.velocityy**2)**1/2
        self.radiusrange = {}
        self.skipone = False
        self.hasleftx = False
        self.haslefty = False
        self.headingind = None
        self.target_speed = None

    def display(self):
        pygame.draw.circle(screen, background_colour, (self.prevx, self.prevy), self.size,
                           self.thickness)  # removes previous item by colouring it the same color as the background...
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size,
                           self.thickness)  # - will be on flock_algo.py

    def update(self):
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
        print(endy)
        print(endx)
        if self.x >= endx or self.x <= orginx:
            self.hasleftx = True
        if self.y >= endy or self.y <= orginy:
            self.haslefty = True
        if self.hasleftx:
            self.velocityx = -self.velocityx
            self.skipone = True
        if not self.hasleftx:
            pass
        self.x = self.x + self.velocityx
        if self.haslefty:
            self.velocityy = - self.velocityy
            self.skipone = True
        if not self.haslefty:
            pass
        self.y = self.y + self.velocityy
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
        self.headingind = 0
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
                self.headingind = 0 + abs(round(math.degrees(math.asin((1/magnitude)*gain_x))))
                print('Degree: ' + str(self.headingind))
            else:
                # positive x and negative y
                if debug:
                    print('Angle: ' + str(round(math.degrees(math.asin((1 / magnitude) * gain_x)))))
                self.headingind = 180 - abs(round(math.degrees(math.asin(((1/magnitude)*gain_x)))))
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

    def headingmodifier(self, heading_dict, objectindex, objectsdict, rangeradius=50):  # parameters: dictionary with heading and index, current index of object, dictionary with position,
        global hasmeanheading
        global mean_heading
        hasmeanheading = False
        rangedindexlist = [objectindex]
        meanheadinglist = []
        count = 0
        x_radius = range(self.x - rangeradius, self.x + rangeradius)  # radius
        y_radius = range(self.y - rangeradius, self.y + rangeradius)  # radius
        for dictindex in range(len(objectsdict)):
            if dictindex != objectindex:
                (objx_position, objy_position) = objectsdict.get(dictindex)
                if objx_position in x_radius:
                    if objy_position in y_radius:
                        rangedindexlist.append(dictindex)
        if len(rangedindexlist) > 1:
            for rangedheadingindex in range(len(rangedindexlist)):
                meanheadinglist.append(heading_dict.get(rangedindexlist[rangedheadingindex]))
            for meanheadinglist_index in range(len(meanheadinglist)):
                count = count + meanheadinglist[meanheadinglist_index]
            mean_heading = count//len(meanheadinglist)
            print('These objects in this range need to go through heading ' + str(mean_heading) + ' for average.')  # Determine Heading and Then Find Average Heading for that range... [Stage Two of Algorithm: Alignment]
            hasmeanheading = True
            return hasmeanheading, mean_heading

    def targettedmanager(self):  # this will move the particle in the correct placement...
        if hasmeanheading:
            print(mean_heading)
            self.headingind = None
            # self.velocityx = choice([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
            # self.velocityy = choice([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
            # self.magnitude = (self.velocityx ** 2 + self.velocityy ** 2) ** 1 / 2
        if hastargetspeed:
            print(self.target_speed)
            # continue to change objects attributes to match this heading speed.
        if hascohesion:
            print(requiredcohesiony + requiredcohesionx)
            # continue to change objects attributes to match this coord target.

    def objectdetection(self, rangeradius=15):
        x_radius = range(self.x - rangeradius, self.x + rangeradius)
        y_radius = range(self.y - rangeradius, self.y + rangeradius)
        # should be used every loop at the very start of position function call to see nearby objects and avoid them by using random function...



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
            Objects_collection[object_index].headingmodifier(headingdict, object_index, objectdict)
            Objects_collection[object_index].targettedmanager()
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

