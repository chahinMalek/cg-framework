from tkinter import *
from tkinter import messagebox

from conf import *

from structures.line_segment import LineSegment
from structures.point import Point
from structures.polygon import Polygon

points = []


def callback(event):
    canvas = event.widget
    x, y = canvas.canvasx(event.x), canvas.canvasx(event.y)
    point = translate_coord_from_canvas(x, y)
    point.draw(canvas)
    points.append(point)


def translate_coord_from_canvas(x: int, y: int) -> Point:
    return Point(x - CENTER, -(y - CENTER))


def make_polygon() -> None:
    polygon = Polygon(points)
    polygon.draw(canvas)


def make_simple_polygon() -> None:
    polygon = Polygon(points)
    polygon.make_simple()
    polygon.draw(canvas)

def is_convex() -> None:
    polygon = Polygon(points)
    polygon.draw(canvas)
    if polygon.is_convex():
        messagebox.showinfo("Result", "Polygon IS convex")
    else:
        messagebox.showinfo("Result", "Point IS NOT convex")

def make_convex_hull() -> None:
    polygon = Polygon(points)
    polygon.make_convex_hull()
    polygon.draw(canvas)


def contains_point() -> None:
    polygon = Polygon(points[0: len(points) - 1])
    polygon.draw(canvas)
    if polygon.does_contain(points[-1]):
        messagebox.showinfo("Result", "Point is INSIDE polygon")
    else:
        messagebox.showinfo("Result", "Point is OUTSIDE polygon")


def line_segs() -> None:
    first = LineSegment(points[0], points[1])
    second = LineSegment(points[2], points[3])
    first.draw(canvas)
    second.draw(canvas)
    if first.does_intersect(second):
        messagebox.showinfo("Result", "Segments DO intersect")
    else:
        messagebox.showinfo("Result", "Segments DO NOT intersect")


def clear() -> None:
    del points[:]
    canvas.delete("all")
    canvas.create_line(0, CENTER, CANVAS_DIM, CENTER, width=1, fill="black")
    canvas.create_line(CENTER, 0, CENTER, CANVAS_DIM, width=1, fill="black")


root = Tk()

root.title("CG framework")
root.geometry(SCREEN_RESOLUTION)

canvas = Canvas(root, width=CANVAS_DIM, height=CANVAS_DIM)
canvas.grid(row=0, column=0)
canvas.bind("<Button-1>", callback)
canvas.create_line(0, CENTER, CANVAS_DIM, CENTER, width=1, fill="black")
canvas.create_line(CENTER, 0, CENTER, CANVAS_DIM, width=1, fill="black")

sidebar = Frame(root, width=160, height=SCREEN_HEIGHT)
sidebar.grid(row=0, column=1)

Button(sidebar, text='Make polygon', command=make_polygon, padx=29, pady=5).grid(row=0, column=1)
Button(sidebar, text='Make simple polygon', command=make_simple_polygon, padx=10, pady=5).grid(row=1, column=1)
Button(sidebar, text='Is convex?', command=is_convex, padx=41, pady=5).grid(row=2, column=1)
Button(sidebar, text='Make convex hull', command=make_convex_hull, padx=21, pady=5).grid(row=3, column=1)
Button(sidebar, text='Contains point', command=contains_point, padx=28, pady=5).grid(row=4, column=1)
Button(sidebar, text='Does intersect?', command=line_segs, padx=27, pady=5).grid(row=5, column=1)
Button(sidebar, text='Clear', command=clear, padx=53, pady=5).grid(row=6, column=1)


root.mainloop()
