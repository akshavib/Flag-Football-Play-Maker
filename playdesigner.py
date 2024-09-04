# Author: Akshavi Baskaran 		Purpose: FLAG FOOTBALL PLAY GENERATOR			Date: 09-01-2024
# playdesigner.py

import tkinter as tk
from popup import IntroPopup
from draggable import DraggableMixin
from drawing import DrawingMixin

class PlayDesigner(DraggableMixin, DrawingMixin):
    def __init__(self, root):
        self.root = root
        self.root.title("Flag Football Play Maker")

        # Make the window resizable in both directions
        self.root.resizable(True, True)

        # Initialize the canvas with a default background color
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Initialize DrawingMixin properly
        DrawingMixin.__init__(self, self.canvas)

        # Bind the resize event to a method
        self.canvas.bind("<Configure>", self.resize_players)
        
        # Display a pop-up menu 
        self.intro_popup()

        # Frame for the bottom buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Buttons
        self.qb_button = tk.Button(self.button_frame, text="Add Quarter Back", command=self.add_qb)
        self.qb_button.pack(side=tk.LEFT)

        self.wr_button = tk.Button(self.button_frame, text="Add Wide Receiver (R)", command=self.add_wr)
        self.wr_button.pack(side=tk.LEFT)
        
        self.wrL_button = tk.Button(self.button_frame, text="Add Wide Receiver (L)", command=self.add_wrL)
        self.wrL_button.pack(side=tk.LEFT)

        self.slot_button = tk.Button(self.button_frame, text="Add Slot (R)", command=self.add_slot)
        self.slot_button.pack(side=tk.LEFT)
        
        self.slotL_button = tk.Button(self.button_frame, text="Add Slot (L)", command=self.add_slotL)
        self.slotL_button.pack(side=tk.LEFT)      
        
        self.rb_button = tk.Button(self.button_frame, text="Add Running Back (R)", command=self.add_rb)
        self.rb_button.pack(side=tk.LEFT)
        
        self.rbL_button = tk.Button(self.button_frame, text="Add Running Back (L)", command=self.add_rbL)
        self.rbL_button.pack(side=tk.LEFT)
        
        # Load the pencil icon image
        self.pencil_icon = tk.PhotoImage(file="pencil.png")  
        self.eraser_icon = tk.PhotoImage(file="eraser.png")    
        

        # Create the pencil button with an image
        self.pencil_button = tk.Button(root, text="Pencil", image=self.pencil_icon, compound="top", command=self.toggle_drawing_mode)
        self.pencil_button.pack(side=tk.LEFT)
        
        self.eraser_button = tk.Button(root, text="Eraser", image=self.eraser_icon, compound="top",
                                       command=self.toggle_eraser_mode)
        self.eraser_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(root, text="Clear All", compound="top", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)
        
        # List to track player positions (as a percentage of the canvas)
        self.player_positions = []
        self.currently_dragging = None
    
    def intro_popup(self):
            popup = IntroPopup(self)
            popup.display()    
    
    def set_team_color(self, color):
        # Set the canvas background to the selected team color
        self.canvas.config(bg=color)
  
    def add_qb(self):
        # Calculate the center of the canvas
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x_center = canvas_width / 2
        y_bottom = canvas_height * (3 / 4)
        radius = 10

        # Create the QB circle in the center of the canvas
        qb = self.canvas.create_oval(x_center - radius, y_bottom - radius,
                                     x_center + radius, y_bottom + radius,
                                     fill="gold")

        # Store the player and its relative position
        self.player_positions.append((qb, x_center / canvas_width, y_bottom / canvas_height, radius))
        self.make_draggable(qb)

    def add_wr(self):
        # Set an arbitrary position and size for the WR
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x_pos = canvas_width * 0.9
        y_pos = canvas_height * 0.75
        radius = 10

        # Create the WR circle
        wr = self.canvas.create_oval(x_pos - radius, y_pos - radius,
                                     x_pos + radius, y_pos + radius,
                                     fill="red")

        # Store the player and its relative position
        self.player_positions.append((wr, x_pos / canvas_width, y_pos / canvas_height, radius))
        self.make_draggable(wr)
    
    def add_wrL(self):
        # Set an arbitrary position and size for the WR left side
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x_pos = canvas_width * 0.1
        y_pos = canvas_height * 0.75
        radius = 10

        # Create the WR circle
        wrL = self.canvas.create_oval(x_pos - radius, y_pos - radius,
                                     x_pos + radius, y_pos + radius,
                                     fill="red")

        # Store the player and its relative position
        self.player_positions.append((wrL, x_pos / canvas_width, y_pos / canvas_height, radius))
        self.make_draggable(wrL)
    
    def add_slot(self):
        # Position for slot on right side 
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x_pos = canvas_width * 0.75
        y_pos = canvas_height * 0.75
        radius = 10
        
        # Create the slot circle
        slot = self.canvas.create_oval(x_pos - radius, y_pos - radius,
                                     x_pos + radius, y_pos + radius,
                                     fill="cyan")

        # Store the player and its relative position
        self.player_positions.append((slot, x_pos / canvas_width, y_pos / canvas_height, radius))   
        self.make_draggable(slot)
    
    def add_slotL(self):
        # Position for slot on left side 
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x_pos = canvas_width * 0.25
        y_pos = canvas_height * 0.75
        radius = 10
        
        # Create the slot circle
        slotL = self.canvas.create_oval(x_pos - radius, y_pos - radius,
                                     x_pos + radius, y_pos + radius,
                                     fill="cyan")

        # Store the player and its relative position
        self.player_positions.append((slotL, x_pos / canvas_width, y_pos / canvas_height, radius))     
        self.make_draggable(slotL)
        
    def add_rb(self):
        # Position for running back on right side 
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x_pos = canvas_width * 0.6
        y_pos = canvas_height * 0.75
        radius = 10
        
        # Create the running back circle
        rb = self.canvas.create_oval(x_pos - radius, y_pos - radius,
                                     x_pos + radius, y_pos + radius,
                                     fill="Chocolate")

        # Store the player and its relative position
        self.player_positions.append((rb, x_pos / canvas_width, y_pos / canvas_height, radius))     
        self.make_draggable(rb)    
        
    def add_rbL(self):
        # Position for running back on right side 
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x_pos = canvas_width * 0.4
        y_pos = canvas_height * 0.75
        radius = 10
        
        # Create the running back circle
        rbL = self.canvas.create_oval(x_pos - radius, y_pos - radius,
                                     x_pos + radius, y_pos + radius,
                                     fill="Chocolate")

        # Store the player and its relative position
        self.player_positions.append((rbL, x_pos / canvas_width, y_pos / canvas_height, radius))     
        self.make_draggable(rbL)        

    def resize_players(self, event):
        # Iterate through all players and reposition them
        for player, rel_x, rel_y, radius in self.player_positions:
            new_x_center = rel_x * event.width
            new_y_center = rel_y * event.height

            # Update the position of the player circle
            self.canvas.coords(player, new_x_center - radius, new_y_center - radius,
                               new_x_center + radius, new_y_center + radius)
    
   