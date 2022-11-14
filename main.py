from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import Screen


class BasicApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        btn_f = MDRectangleFlatButton(text='Hello World',
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5})

        screen.add_widget(btn_f)
        return screen


BasicApp().run()
