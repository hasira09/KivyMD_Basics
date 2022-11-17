from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp

Window.size = (300, 500)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        
        #can use MDToolBar instead as well
        MDTopAppBar:                
            title: 'Demo App'
            left_action_items: [["menu",lambda x: app.navigation_draw()]]
            right_action_items: [["android",lambda x: app.navigation_draw()]]
            elevation: 2
            
        MDLabel:
            text: 'Hasira Mahel'
            halign: 'center'
            
        MDBottomAppBar:
            MDTopAppBar:
                left_action_items: [["tea",lambda x: app.navigation_draw()]]
                mode: 'end'
                type: 'bottom'
                icon: 'language-python'
                on_action_button: app.navigation_draw()
                elevation: 0
"""


class NavApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("Navigation")


NavApp().run()
