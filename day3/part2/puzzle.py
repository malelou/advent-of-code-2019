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
    wire1length = 0
    for wireSegment1 in wirearrays[0]:
        wire2length = 0
        wire1length += wireSegment1.length
        for wireSegment2 in wirearrays[1]:
            wire2length += wireSegment2.length
            if((wireSegment1.isOrthogonal and not wireSegment2.isOrthogonal) or (not wireSegment1.isOrthogonal and wireSegment2.isOrthogonal)):
                if(wireSegment1.isOrthogonal):
                    findIntersection(wireSegment1, wireSegment2, intersections, wire1length, wire2length)
                elif(wireSegment2.isOrthogonal):
                    findIntersection(wireSegment2, wireSegment1, intersections, wire2length, wire1length)
    return min([x for x in intersections if x != 0])

def findIntersection(orthogonalWire1Segment, horizontalWire2Segment, intersections, wire1length, wire2length):
    wireSegment2xCoordinates = [horizontalWire2Segment.start.x, horizontalWire2Segment.end.x]
    wireSegment1yCoordinates = [orthogonalWire1Segment.start.y, orthogonalWire1Segment.end.y]
    if(orthogonalWire1Segment.start.x >= min(wireSegment2xCoordinates) and orthogonalWire1Segment.start.x <= max(wireSegment2xCoordinates) and horizontalWire2Segment.start.y >= min(wireSegment1yCoordinates) and horizontalWire2Segment.start.y <= max(wireSegment1yCoordinates)):
        intersections.append(wire1length - (abs(orthogonalWire1Segment.end.y - horizontalWire2Segment.start.y)) + wire2length - (abs(horizontalWire2Segment.end.x - orthogonalWire1Segment.start.x)))
