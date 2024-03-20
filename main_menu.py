from widget_format import Widget_Format as WF

class Main_Menu:
    def __init__(self, main_window):
        self.mw = main_window

    def main_menu_screen(self):
        WF.push_button(self.mw, "example", 50,50, WF.message_box())