__author__ = 'Pushkar'

import random
import math

# Pass in the initial location x,y
# Mean and std deviation of the euclidean distance
# Mean in degrees corresponding to x axis and kappa for angular
# The degrees can be positive or negative
def getnextlocation( x, y, g_mu, g_sig, v_mu, v_kap ):
    ret_x = 0
    ret_y = 0
    v_mu_rad = math.pi * v_mu / 180
    dist = random.normalvariate( g_mu, g_sig )
    ang = random.vonmisesvariate( abs(v_mu_rad), v_kap )
    sin_val = abs(math.sin( abs( ang ) ))
    cos_val = abs(math.cos( abs( ang ) ))

    add_x = dist * cos_val
    add_y = dist * sin_val

    if v_mu_rad < 0 :
        add_y = -1 * add_y

    if abs( ang ) > ( math.pi / 2) :
        add_x = -1 * add_x

    ret_x = x + add_x
    ret_y = y + add_y
    return ret_x , ret_y

def matches( x, y, x_orig, y_orig, g_mu, g_sig, v_mu, v_kap, conf ) :
    ret_val = False
    return ret_val

# gets the distance between two points
def distance(x1,y1,x2,y2):
    return math.sqrt( math.pow(x1-x2,2) + math.pow(y1-y2,2) )

# gets the angle between two points. 1 is the source and 2 is target
def angle(x1,y1,x2,y2):
    #if x1 == 0:
    #    ang1 = 0 # 90 degree
    #else:
    #    ang1 = math.degrees(math.atan(float(y1)/float(x1)))

    #if x2 == 0:
    #    ang2 = 0 # 90 degree
    #else:
    #    ang2 = math.degrees(math.atan(float(y2)/float(x2)))

    #return ang2 - ang1

    if x2 == x1:
        return 90
    else:
        if y2 == y1:
            return 0
        else:
            return math.degrees(math.atan(float(y2-y1)/float(x2-x1)))
