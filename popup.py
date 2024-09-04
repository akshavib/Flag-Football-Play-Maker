# Author: Akshavi Baskaran 		Purpose: FLAG FOOTBALL PLAY GENERATOR			Date: 09-01-2024
# popup.py

import tkinter as tk
from tkinter import ttk

class IntroPopup:
    def __init__(self, app):
        self.app = app
        
    def display(self):
        popup = tk.Toplevel()  # Use Toplevel to create a new window
        popup.title("Welcome")
        
        intro_label = tk.Label(popup, text= f"Welcome to the Flag Football Play Maker!\nPlease select your team color to get started.")
        intro_label.pack(pady=10)
        
        # Dropdown for selecting team color
        team_color_var = tk.StringVar(popup)
        team_color_var.set("White")  # default value
        
        team_colors = ["Red", "Orange", "Yellow", "Dark Green", "Blue", "Purple", "White"]
        team_color_menu = ttk.OptionMenu(popup, team_color_var, *team_colors)
        team_color_menu.pack(pady=10)
        
        # Confirm button to apply the selected color
        confirm_button = tk.Button(popup, text="Confirm", command=lambda: [self.app.set_team_color(team_color_var.get()), popup.destroy()])
        confirm_button.pack(pady=10)    