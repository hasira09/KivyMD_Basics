from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen

username_helper = """
MDTextField:
    hint_text: "Enter Username"
    helper_text: "or Click on Forgot Username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300
"""


class BasicApp(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"
        # username = MDTextField(text='Enter Username',
        #                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                        size_hint_x=None, width=300)

        username = Builder.load_string(username_helper)
        screen.add_widget(username)
        return screen


BasicApp().run()
