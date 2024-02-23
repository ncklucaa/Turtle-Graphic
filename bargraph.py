from turtle import *

def drawBar(height):
    begin_fill()
    left(90)
    forward(height)
    write(str(height), align="center")
    right(90)
    forward(40)
    right(90)
    forward(height)
    left(90)
    end_fill()

def sort(a):
    a.sort()
    return a

def readData():
    with open('data.txt', 'r') as file:
        myList = [int(line) for line in file.readlines()]
    return myList

def main():
    data = readData()
    print("Original Data:", data)

    maxheight = max(data)
    numBars = len(data)

    screen = Screen()
    screen.setworldcoordinates(0, 0, 40 * numBars + 10, maxheight + 10)
    speed('fastest')
    
    for value in data:
        drawBar(value)

    data = sort(data)
    print("Sorted Data:", data)

    reset()
    speed('fastest')

    for value in data:
        drawBar(value)

    screen.exitonclick()

if __name__ == "__main__":
    main()
