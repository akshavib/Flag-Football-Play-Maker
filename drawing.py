# Author: Akshavi Baskaran 		Purpose: FLAG FOOTBALL PLAY GENERATOR			Date: 09-01-2024
# drawing.py

import tkinter as tk

class DrawingMixin:
    def __init__(self, canvas):
        self.canvas = canvas
        self.drawing = False
        self.erasing = False
        self.last_x, self.last_y = None, None

    def toggle_drawing_mode(self):
        # Toggle the drawing mode on or off.
        self.drawing = not self.drawing
        if self.drawing:
            self.erasing = False  # Disable eraser mode
            self.pencil_button.config(text="Draw!", bg="black", activebackground="black", highlightbackground="black")
            self.canvas.bind("<Button-1>", self.start_drawing)
            self.canvas.bind("<B1-Motion>", self.draw)
        else:
            self.pencil_button.config(text="Pencil", bg="SystemButtonFace", activebackground="SystemButtonFace", highlightbackground="SystemButtonFace")
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<B1-Motion>")
        self.last_x, self.last_y = None, None

    def toggle_eraser_mode(self):
        # Toggle the eraser mode on or off.
        self.erasing = not self.erasing
        if self.erasing:
            self.drawing = False  # Disable drawing mode
            self.eraser_button.config(text="Erase!", bg="black", activebackground="black", highlightbackground="black")
            self.canvas.bind("<Button-1>", self.start_drawing)
            self.canvas.bind("<B1-Motion>", self.erase)
        else:
            self.eraser_button.config(text="Eraser", bg="SystemButtonFace", activebackground="SystemButtonFace", highlightbackground="SystemButtonFace")
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<B1-Motion>")
        self.last_x, self.last_y = None, None

    def start_drawing(self, event):
        # Start drawing or erasing on the canvas.
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        # Draw a line on the canvas.
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill="black", width=2)
        self.last_x, self.last_y = event.x, event.y

    def erase(self, event):
        # Erase part of the drawing by drawing over it with the background color.
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.canvas['bg'], width=10)
        self.last_x, self.last_y = event.x, event.y

    def clear_canvas(self):
        # Clear the entire canvas.
        self.canvas.delete("all")
