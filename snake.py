from turtle import Turtle, Screen
import time
screen = Screen()
class Snake:
    def __init__(self):
        self.segment = []
        self.segment_1 = None
        self.segment_2 = None
        self.segment_3 = None
        self.new_segment = None

    def create_snake(self):
        self.segment_1 = Turtle("square")
        self.segment_1.color("white")
        self.segment_1.penup()

        self.segment_2 = Turtle("square")
        self.segment_2.color("white")
        self.segment_2.penup()
        self.segment_2.goto(x=-20, y=0)

        self.segment_3 = Turtle("square")
        self.segment_3.color("white")
        self.segment_3.penup()
        self.segment_3.goto(x=-40, y=0)

        self.new_segment = [self.segment_1, self.segment_2, self.segment_3]
        self.add_snake()

    def add_snake(self):
        for seg in range(0,1):
            new_x = self.new_segment[-1].xcor()
            new_y = self.new_segment[-1].ycor()
        self.segment = Turtle()
        self.segment.penup()
        self.segment.hideturtle()
        self.segment.speed("fastest")
        self.segment.shape("square")
        self.segment.color("white")
        self.segment.goto(new_x, new_y)
        self.new_segment.append(self.segment)
        self.segment.showturtle()


    def move(self):
        for seg in range(len(self.new_segment) - 1, 0, -1):
            new_x = self.new_segment[seg - 1].xcor()
            new_y = self.new_segment[seg - 1].ycor()
            self.new_segment[seg].goto(new_x, new_y)
        self.new_segment[0].forward(20)

    def up(self):
        if self.new_segment[0].heading() != 270:
            self.new_segment[0].setheading(90)

    def down(self):
        if self.new_segment[0].heading() != 90:
            self.new_segment[0].setheading(270)

    def left(self):
        if self.new_segment[0].heading() != 0:
            self.new_segment[0].setheading(180)

    def right(self):
        if self.new_segment[0].heading() != 180:
            self.new_segment[0].setheading(0)

    def reset(self):
        for _ in self.new_segment:
            _.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()