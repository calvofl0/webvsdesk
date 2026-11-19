"""Minimal desktop app example using Tkinter."""
import tkinter as tk


def main():
    """Entry point for the desktop app."""
    # Create the main window
    root = tk.Tk()
    root.title("Hello World Desktop App")
    root.geometry("300x100")

    # Create a label with "Hello World"
    label = tk.Label(root, text="Hello World", font=("Arial", 24))
    label.pack(expand=True)

    # Start the GUI event loop
    root.mainloop()


if __name__ == '__main__':
    main()
