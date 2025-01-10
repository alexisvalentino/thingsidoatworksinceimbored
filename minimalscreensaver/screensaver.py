import tkinter as tk
from time import strftime

# ScreenSaver Class
class ScreenSaver:
    def __init__(self, root):
        self.root = root
        self.root.title("Minimalist Screensaver Timer")
        self.root.configure(bg="black")  # Black background

        # Allow resizing and minimize
        self.root.resizable(True, True)
        self.root.minsize(400, 200)  # Minimum window size

        # Time Label
        self.time_label = tk.Label(
            root,
            font=("Helvetica Neue", 100, "bold"),  # Use Helvetica Neue if available
            bg="black",  # Background color
            fg="white",  # Text color
        )
        self.time_label.pack(expand=True, fill="both")

        # Check if Helvetica Neue is available, otherwise fallback to Helvetica or Arial
        try:
            self.time_label.config(font=("Helvetica Neue", 100, "bold"))
        except tk.TclError:
            try:
                self.time_label.config(font=("Helvetica", 100, "bold"))  # Fallback to Helvetica
            except tk.TclError:
                self.time_label.config(font=("Arial", 100, "bold"))  # Fallback to Arial

        self.update_time()  # Start updating the time

    # Function to update the time
    def update_time(self):
        current_time = strftime("%H:%M:%S")  # Format: HH:MM:SS
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)  # Update every second


# Main Function
if __name__ == "__main__":
    root = tk.Tk()
    screensaver = ScreenSaver(root)
    root.mainloop()