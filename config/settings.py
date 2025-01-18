# Window Settings
WINDOW_TITLE = "Sorting Algorithm Visualizer"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = "#f0f0f0"  # Light gray background

# Visualization Settings
BAR_COLOR_DEFAULT = "#3498db"  # Blue for unsorted bars
BAR_COLOR_SORTED = "#2ecc71"  # Green for sorted bars
BAR_COLOR_HIGHLIGHT = "#e74c3c"  # Red for the current bar being compared
BAR_WIDTH = 20  # Width of each bar
BAR_SPACING = 5  # Space between bars

# Animation Settings
ANIMATION_SPEED = 100  # Default speed in milliseconds (lower is faster)
MIN_SPEED = 10         # Minimum speed (fastest)
MAX_SPEED = 1000       # Maximum speed (slowest)

# Data Settings
MIN_BAR_HEIGHT = 10    # Minimum height of a bar
MAX_BAR_HEIGHT = 400   # Maximum height of a bar
DEFAULT_BAR_COUNT = 20 # Default number of bars to visualize

# Font Settings
FONT_FAMILY = "Arial"
FONT_SIZE = 12
FONT_COLOR = "#333333"  # Dark gray for text

# Logging Settings (Optional)
LOGGING_ENABLED = True
LOG_FILE = "visualizer.log"

# Other Settings
BUTTON_STYLE = {
    "font": (FONT_FAMILY, 10, "bold"),
    "bg": "#ffffff",
    "fg": "#333333",
    "activebackground": "#dddddd",
    "activeforeground": "#000000",
    "relief": "raised",
    "bd": 2,
}

# Dropdown Options
SORTING_ALGORITHMS = [
    "Bubble Sort",
    "Selection Sort",
    "Insertion Sort",
    "Merge Sort",
    "Quick Sort",
]
