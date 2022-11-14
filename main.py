from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import Screen

from helpers import username_helper


class BasicApp(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"
        # username = MDTextField(text='Enter Username',
        #                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                        size_hint_x=None, width=300)

        button = MDRectangleFlatButton(text='Display',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(button)
        screen.add_widget(self.username)
        return screen

    def show_data(self, obj):
        print(self.username.text)


BasicApp().run()
