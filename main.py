from ui.main_windows import initialize_main_window

def main():
    root, widgets = initialize_main_window()
    print("Selected Algorithm:", widgets["algorithm_menu"].get())
    root.mainloop()

if __name__ == "__main__":
    main()
