from tkinter import *
from tkinter import messagebox

from conf import *
from drawing import *


points = []


def callback(event):
    canvas = event.widget
    x, y = canvas.canvasx(event.x), canvas.canvasx(event.y)
    point = translate_coord_from_canvas(x, y)
    draw_point(canvas, point)
    points.append(point)
    #point.draw(canvas)


def translate_coord_from_canvas(x: int, y: int) -> Point:
    return Point(x - CENTER, -(y - CENTER))


def make_polygon():
    polygon = Polygon(points)
    draw_polygon(canvas, polygon)


def make_simple_polygon():
    polygon = Polygon(points)
    polygon.make_simple()
    draw_polygon(canvas, polygon)


def make_convex_hull():
    polygon = Polygon(points)
    polygon.make_convex_hull()
    draw_polygon(canvas, polygon)


def contains_point():
    polygon = Polygon(points[0 : len(points) - 1])
    draw_polygon(canvas, polygon)
    if polygon.does_contain(points[-1]):
        messagebox.showinfo("Result", "Point is INSIDE polygon")
    else:
        messagebox.showinfo("Result", "Point is OUTSIDE polygon")


def line_segs():
    first = LineSegment(points[0], points[1])
    second = LineSegment(points[2], points[3])
    draw_line_segment(canvas, first)
    draw_line_segment(canvas, second)
    if first.does_intersect(second):
        messagebox.showinfo("Result", "Segments DO intersect")
    else:
        messagebox.showinfo("Result", "Segments DO NOT intersect")


def clear():
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

make_polygon_button = Button(sidebar, text='Make polygon', command=make_polygon, padx=29, pady=5)
make_polygon_button.grid(row=0, column=1)

make_simple_button = Button(sidebar, text='Make simple polygon', command=make_simple_polygon, padx=10, pady=5)
make_simple_button.grid(row=1, column=1)

make_convex_hull_button = Button(sidebar, text='Make convex hull', command=make_convex_hull, padx=21, pady=5)
make_convex_hull_button.grid(row=2, column=1)

contains_point_button = Button(sidebar, text='Contains point', command=contains_point, padx=28, pady=5)
contains_point_button.grid(row=3, column=1)

line_segs = Button(sidebar, text='Does intersect', command=line_segs, padx=30, pady=5)
line_segs.grid(row=4, column=1)

clear_button = Button(sidebar, text='Clear', command=clear, padx=53, pady=5)
clear_button.grid(row=5, column=1)





# Start the window's event-loop
root.mainloop()