from tkinter import *
import random
from config.settings import BACKGROUND_COLOR, SORTING_ALGORITHMS, BUTTON_STYLE,MAX_BAR_HEIGHT,DEFAULT_BAR_COUNT


class SortingVisualizerUI:
    def __init__(self, root):
        self.root = root
        self.algorithm_menu = None
        self.start_button = None
        self.heading_label = None
        self._create_widgets()

    def _create_widgets(self):
        # Heading
        self.heading_label = Label(self.root, text="Welcome to Sorting Visualizer!", bg=BACKGROUND_COLOR)
        self.heading_label.pack(pady=10)

        # this is a frame at the top
        control_frame = Frame(self.root, bg=BACKGROUND_COLOR, padx=10, pady=10)
        control_frame.pack(fill=X)

        #this is a dropdown for sorting algorithms
        algorithm_label = Label(control_frame, text="Algorithm:", bg=BACKGROUND_COLOR)
        algorithm_label.pack(side=LEFT, padx=5)

        self.algorithm_menu = StringVar(self.root)
        self.algorithm_menu.set(SORTING_ALGORITHMS[0])  # Default value
        dropdown = OptionMenu(control_frame, self.algorithm_menu, *SORTING_ALGORITHMS)
        dropdown.pack(side=LEFT, padx=5)

        #this is button to start sorting
        self.start_button = Button(control_frame, text="Start Sorting", **BUTTON_STYLE)
        self.start_button.pack(side=LEFT, padx=5)
        
       # this is canvas for rectangle bars
        canvas = Canvas(self.root, width=1000, height=400, bg="white")
        canvas.pack()

        for i in range(DEFAULT_BAR_COUNT):
            BAR_COORDINATE = i * 55  #this stables in the sameline of the canvas and width
            RANDOM_VALUE=random.randint(50, 400) #this is for the random size of the charts
            canvas.create_rectangle(BAR_COORDINATE, MAX_BAR_HEIGHT - RANDOM_VALUE, BAR_COORDINATE + 50, MAX_BAR_HEIGHT, fill="blue", outline="black")


    def get_widgets(self):
        return {
            "algorithm_menu": self.algorithm_menu,
            "start_button": self.start_button,
            "heading_label": self.heading_label,
        }
