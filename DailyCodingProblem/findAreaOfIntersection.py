"""
Daily Coding Problem #185

This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their intersection. 
If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.

"""

def find_intersection_area(fig1,fig2):
    #first rectangle
    x1 = fig1['top_left'][0]
    y1 = fig1['top_left'][1]
    
    #second rectangle
    x2 = fig2['top_left'][0]
    y2 = fig2['top_left'][1]
    
    #width and heights of 2 rectangles
    w1 = fig1['dimensions'][0]
    w2 = fig2['dimensions'][0]
    
    h1 = fig1['dimensions'][1]
    h2 = fig2['dimensions'][1]
    
    #Logic starts here
    xmin = max(x1,x2)
    xmax1 = x1 + w1
    xmax2 = x2 + w2
    xmax = min(xmax1,xmax2)
    if (xmax > xmin):
        ymin = max(y1,y2)
        ymax1 = y1 + h1
        ymax2 = y2 + h2
        ymax = min(ymax1,ymax2)
        if (ymax > ymin):
            out_x = xmin
            out_y = ymin
            out_width = xmax - xmin
            out_height = ymax - ymin
            return (out_width * out_height)
    return 0

fig1 = {
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}

fig2 = {
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}

print (find_intersection_area(fig1, fig2))