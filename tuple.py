"""Tuple Unpacking


You are working on a mapping software. The map is stored as a list of points, where each item is represented as a tuple, containing the X and Y coordinates of the point.
You need to calculate and output the distance to the closest point from the point (0, 0).
To calculate the distance of the point (x, y) from (0, 0), use the following formula: √(x²+y²)
You can iterate over the list and use tuple unpacking to get the x and y coordinates of each point: for (x, y) in points: and output the smallest value."""

import math
points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]
#your code goes here
distance=list(range(len(points)))
n=0
for (x,y) in points:
    distance[n]=math.sqrt((x**2)+(y**2))
    n+=1
print(min(distance))
    
