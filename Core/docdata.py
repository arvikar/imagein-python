import math

from Core import corefunctions


__author__ = 'Pushkar'


class DocData:
    # p1, p2, p3, p4 are location arrays
    # p1 = [x1,y1]
    #  p2---------p3
    #  |          |
    #  p1---------p4

    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        #calculate some data based on the given values
        self.d12 = corefunctions.distance(self.x1,self.y1,self.x2,self.y2)
        self.d23 = corefunctions.distance(self.x2,self.y2,self.x3,self.y3)
        self.d34 = corefunctions.distance(self.x4,self.y4,self.x3,self.y3)
        self.d14 = corefunctions.distance(self.x1,self.y1,self.x4,self.y4)
        #calculate the proportions
        self.d12d23 = self.d12/self.d23
        self.d23d34 = self.d23/self.d34
        self.d34d14 = self.d34/self.d14
        self.d14d12 = self.d14/self.d12
        self.d12d34 = self.d12/self.d34
        self.d14d23 = self.d14/self.d23
        #calculate the angles
        self.angle1 = corefunctions.angle(0,0,self.x1,self.y1)
        self.angle2 = corefunctions.angle(0,0,self.x2,self.y2)
        self.angle3 = corefunctions.angle(0,0,self.x3,self.y3)
        self.angle4 = corefunctions.angle(0,0,self.x4,self.y4)
        #these will be calculated when we normalize
        self.zoom = 1 #zoom factor
        self.alpha = 0 # angle of fall along x axis
        self.beta = 0 # angle of fall along y axis

    # adapts the current doc to the template
    def adaptToTemplate(self,template):
        # 1. Calculate the zoom

            # For now we assume the zoom is 1

        # 2. Calculate Alpha
            currentVisual12 = self.d12 * math.sin(math.radians(corefunctions.angle(self.x1,self.y1,self.x2,self.y2)))
            templateVisual12 = template.d12 * math.sin(math.radians(corefunctions.angle(template.x1,template.y1,template.x2,template.y2)))
            self.alpha = math.degrees(math.acos(float(currentVisual12)/float(templateVisual12)))
        # 3. Calculate Beta
            currentVisual14 = self.d14 * math.cos(math.radians(corefunctions.angle(self.x1,self.y1,self.x4,self.y4)))
            templateVisual14 = template.d14 * math.cos(math.radians(corefunctions.angle(template.x1,template.y1,template.x4,template.y4)))
            self.beta = math.degrees(math.acos(float(currentVisual14)/float(templateVisual14)))

    # Gets a point in this class when given a point x,y from the template
    def getPoint(self, x, y ):
        newx = self.zoom * x * math.cos(math.radians(self.beta))
        newy = self.zoom * y * math.cos(math.radians(self.alpha))
        return([newx, newy])
        # 1. Normalize distances based on proportions. p1--p4 = 100
        # for now we assume that there is no zoom needed.

        # 2. Move p2 to the correct position based on template, p3 moves accordingly
        # 3. Move p3 to the correct position based on template, p4 moves accordingly
        # 4. Move p4 to the correct position