from tkinter import *
from config.settings import WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR
from ui.widgets import SortingVisualizerUI


def initialize_main_window():
    root = Tk()
    root.title(WINDOW_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root.configure(bg=BACKGROUND_COLOR)

    # Create the UI class instance
    ui = SortingVisualizerUI(root)

    # Return the root and widget references
    return root, ui.get_widgets()
