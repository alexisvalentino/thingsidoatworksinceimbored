import tkinter as tk
from time import strftime

# ScreenSaver Class
class ScreenSaver:
    def __init__(self, root):
        self.root = root
        self.root.attributes("-fullscreen", True)  # Fullscreen mode
        self.root.configure(bg="black")  # Black background
        self.root.bind("<Escape>", self.close)  # Press Escape to exit

        # Time Label
        self.time_label = tk.Label(
            root,
            font=("Helvetica Neue", 150, "bold"),  # Use Helvetica Neue if available
            bg="black",  # Background color
            fg="white",  # Text color
        )
        self.time_label.pack(expand=True)

        # Check if Helvetica Neue is available, otherwise fallback to Helvetica or Arial
        try:
            self.time_label.config(font=("Helvetica Neue", 150, "bold"))
        except tk.TclError:
            try:
                self.time_label.config(font=("Helvetica", 150, "bold"))  # Fallback to Helvetica
            except tk.TclError:
                self.time_label.config(font=("Arial", 150, "bold"))  # Fallback to Arial

        self.update_time()  # Start updating the time

    # Function to update the time
    def update_time(self):
        current_time = strftime("%H:%M")  # Format: HH:MM
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)  # Update every second

    # Function to close the screensaver
    def close(self, event=None):
        self.root.destroy()


# Main Function
if __name__ == "__main__":
    root = tk.Tk()
    screensaver = ScreenSaver(root)
    root.mainloop()