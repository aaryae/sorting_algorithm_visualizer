from tkinter import *
import random
import time
from algorithms.bubble_sort import bubble_sort
from config.settings import BACKGROUND_COLOR, SORTING_ALGORITHMS, BUTTON_STYLE, MAX_BAR_HEIGHT, DEFAULT_BAR_COUNT


class SortingVisualizerUI:
    def __init__(self, root):
        self.root = root
        self.algorithm_menu = None
        self.start_button = None
        self.heading_label = None
        self.canvas = None
        self.bars = []
        self.bar_values = []
        self._create_widgets()

    def _create_widgets(self):
        # Heading
        self.heading_label = Label(self.root, text="Welcome to Sorting Visualizer!", bg="lightgray")
        self.heading_label.pack(pady=10)

        # Control frame
        control_frame = Frame(self.root, bg="lightgray", padx=10, pady=10)
        control_frame.pack(fill=X)

        # Algorithm dropdown
        algorithm_label = Label(control_frame, text="Algorithm:", bg="lightgray")
        algorithm_label.pack(side=LEFT, padx=5)

        self.algorithm_menu = StringVar(self.root)
        self.algorithm_menu.set("Bubble Sort")  # Default value
        dropdown = OptionMenu(control_frame, self.algorithm_menu, "Bubble Sort")
        dropdown.pack(side=LEFT, padx=5)

        # Start button
        self.start_button = Button(control_frame, text="Start Sorting", command=self.start_sorting)
        self.start_button.pack(side=LEFT, padx=5)

        # Canvas for bars
        self.canvas = Canvas(self.root, width=1000, height=400, bg="white")
        self.canvas.pack()

        # Initialize bars
        self._create_bars()

    def _create_bars(self):
        self.bars.clear()
        self.bar_values = [random.randint(50, 400) for _ in range(14)]

        for i, value in enumerate(self.bar_values):
            x0 = i * 55
            y0 = 400 - value
            x1 = x0 + 50
            y1 = 400
            bar = self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue", outline="black")
            self.bars.append(bar)

    def _draw_bars(self, arr, compared_index=None):
        for i, value in enumerate(arr):
            x0 = i * 55
            y0 = 400 - value
            x1 = x0 + 50
            y1 = 400
            
            # Update the position of the bar
            self.canvas.coords(self.bars[i], x0, y0, x1, y1)
            
            # If this bar is being compared, set its color to red
            if compared_index == i:
                self.canvas.itemconfig(self.bars[i], fill="red")
            else:
                self.canvas.itemconfig(self.bars[i], fill="blue")  # Reset color for other bars
        
        self.root.update()
        time.sleep(0.1)

    def start_sorting(self):
        bubble_sort(self.bar_values, self._draw_bars)

    def get_widgets(self):
        return {
            "algorithm_menu": self.algorithm_menu,
            "start_button": self.start_button,
            "heading_label": self.heading_label,
            "canvas": self.canvas,
        }


