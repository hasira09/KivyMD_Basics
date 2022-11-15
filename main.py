from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.list import MDList, ThreeLineListItem, ThreeLineIconListItem
from kivymd.uix.list import IconLeftWidget
from kivymd.uix.screen import Screen


class TestApp(MDApp):

    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        for i in range(20):
            icons = IconLeftWidget(icon="android")
            items = ThreeLineIconListItem(text='Item ' + str(i), secondary_text='KivyMD',
                                      tertiary_text='Hello World')

            items.add_widget(icons)
            list_view.add_widget(items)

        screen.add_widget(scroll)
        return screen


TestApp().run()
