import math
from math import cos,sin,radians
val = 0

# This is the function for calculating distance of point from the 3 distances given by 3 different sensors
# We have decided to take mean of the 2 closest values

def value(a,b,c) :
    f=abs(a-b)
    g=abs(b-c)
    h=abs(a-c)
    if f<g :
        if f<h :
            return (a+b)/2
        else :
            return (a+c)/2
    else :
        if g<h :
            return (b+c)/2
        else :
            return (a+c)/2

# final_array stores the distance of points from origin 
# final_array[height][angle]

final_array = [[0]*360 for i in range(151)]

# arr stores the distances given by sensors in the order sensor 1, sensor 2, sensor 3
# arr[height][360*3 distances given by all 3 sensors at that height]

arr = [[0]*1080 for i in range(151)]

# We have incremented by 2 because the sensor platform moves up by 2mm

for h in range(0,151,2) :
    not_empty = 0;
    for i in range(1080) :
         if val>= 275 :
            val = 200;
         arr[h][i] = val;
         if val!=200 :
	        not_empty = 1;
    if not_empty == 0 :
         break;    

# At a particular height:
# arr1[i],arr2[i],arr3[i] stores distance shown by sensor at angle i

for x in range(0,h,2) :
    arr1 = [[0] for i in range(360)]
    arr2 = [[0] for i in range(360)]
    arr3 = [[0] for i in range(360)]
    var = 0
    for i in range(360) :
        arr1[i] = arr[x][var]
        var = var + 3
    var = 1
    for i in range(60,360) :
        arr2[i] = arr[x][var]
        var = var + 3
    for i in range(0,60) :
        arr2[i] = arr[x][var]
        var = var + 3
    var = 2
    for i in range(120,360) :
        arr3[i] = arr[x][var]
        var = var + 3
    for i in range(0,120) :
        arr3[i] = arr[x][var]
        var = var +3
    for i in range(360) :
        final_array[x][i] = 200-value(arr1[i],arr2[i],arr3[i])

# Eliminating error using value fn and getting distance from origin

# Converting from cylindrical coordinates to cartesian coordinates and storing in text file

output = open(r"/Users/ishu/Desktop/points.txt","w")
   
for h in range(0,h,2) :
    for a in range(360) :
        x = float(0)
        y = float(0)
        z = float(0)
        r = float(0)
        z=h
        r=final_array[h][a]
        x=r*cos(radians(a))
        y=r*sin(radians(a))
        str = "{}   {}  {}"
        output.write(str.format(x,y,z))
        output.write("\n")

output.close()
    


    

    
