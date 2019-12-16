from math import floor

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WireSegment:
    def __init__(self, start, end, length, isOrthogonal):
        self.start = start
        self.end = end
        self.length = length
        self.isOrthogonal = isOrthogonal

def parse(lines):
    ans = []
    for line in lines:
        if line:
            ans.append([x for x in line.strip().split(",")])
    return ans

def solve(data):
    wirearrays = []
    for wire in data:
        wirearray = [WireSegment(Point(0,0), Point(0,0), 0, True)]
        for segment in wire:
            length = int(segment[1:])
            previousEnd = Point(wirearray[len(wirearray) - 1].end.x, wirearray[len(wirearray) - 1].end.y)
            if(segment[0] == "R"):
                wirearray.append(WireSegment(previousEnd, Point(previousEnd.x + length, previousEnd.y), length, False))
            elif(segment[0] == "L"):
                wirearray.append(WireSegment(previousEnd, Point(previousEnd.x - length, previousEnd.y), length, False))
            elif(segment[0] == "D"):
                wirearray.append(WireSegment(previousEnd, Point(previousEnd.x, previousEnd.y - length), length, True))
            elif(segment[0] == "U"):
                wirearray.append(WireSegment(previousEnd, Point(previousEnd.x, previousEnd.y + length), length, True))
        wirearray.pop(0)
        wirearrays.append(wirearray)
    intersections = []
    for wireSegment1 in wirearrays[0]:
        for wireSegment2 in wirearrays[1]:
            if((wireSegment1.isOrthogonal and not wireSegment2.isOrthogonal) or (not wireSegment1.isOrthogonal and wireSegment2.isOrthogonal)):
                if(wireSegment1.isOrthogonal):
                    findIntersections(wireSegment1, wireSegment2, intersections)
                elif(wireSegment2.isOrthogonal):
                    findIntersections(wireSegment2, wireSegment1, intersections)
    distances = [abs(point.x) + abs(point.y) for point in intersections if abs(point.x) + abs(point.y) != 0]
    return min(distances)

def findIntersections(orthogonalWireSegment, horizontalWireSegment, intersections):
    wireSegment2xCoordinates = [horizontalWireSegment.start.x, horizontalWireSegment.end.x]
    wireSegment1yCoordinates = [orthogonalWireSegment.start.y, orthogonalWireSegment.end.y]
    if(orthogonalWireSegment.start.x >= min(wireSegment2xCoordinates) and orthogonalWireSegment.start.x <= max(wireSegment2xCoordinates) and horizontalWireSegment.start.y >= min(wireSegment1yCoordinates) and horizontalWireSegment.start.y <= max(wireSegment1yCoordinates)):
        intersections.append(Point(orthogonalWireSegment.start.x, horizontalWireSegment.start.y))