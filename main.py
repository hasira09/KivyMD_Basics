from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp

Window.size = (300, 500)

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    #can use MDToolBar instead as well
                    MDTopAppBar:                
                        title: 'Demo App'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                        elevation: 2

                    Widget:

        MDNavigationDrawer
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '15dp'
                padding: '5dp'
                
                Image:
                    source: 'Hasira_PP.jpg'
                
                MDLabel:
                    text: '     Hasira Mahel'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                MDLabel:
                    text: '       hasiramahel09@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'account-check'
                        OneLineIconListItem:
                            text: 'Payment'
                            IconLeftWidget:
                                icon: 'cash'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'
"""


class NavApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        screen = Builder.load_string(navigation_helper)
        return screen


NavApp().run()
