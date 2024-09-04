class DraggableMixin:
    def make_draggable(self, player):
        self.canvas.tag_bind(player, "<Button-1>", self.start_drag)
        self.canvas.tag_bind(player, "<B1-Motion>", self.drag)
        self.canvas.tag_bind(player, "<ButtonRelease-1>", self.stop_drag)

    def start_drag(self, event):
        self.currently_dragging = self.canvas.find_closest(event.x, event.y)[0]

    def drag(self, event):
        if self.currently_dragging:
            x, y = event.x, event.y
            self.canvas.coords(self.currently_dragging, x - 10, y - 10, x + 10, y + 10)

    def stop_drag(self, event):
        if self.currently_dragging:
            x, y, _, _ = self.canvas.coords(self.currently_dragging)
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()

            for i, (player, _, _, radius) in enumerate(self.player_positions):
                if player == self.currently_dragging:
                    self.player_positions[i] = (player, (x + radius) / canvas_width, (y + radius) / canvas_height, radius)
            self.currently_dragging = None