from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem, MDList
from kivymd.uix.screen import Screen


class TestApp(MDApp):

    def build(self):
        screen = Screen()

        list_view = MDList()

        item1 = OneLineListItem(text='Item 1')
        item2 = OneLineListItem(text='Item 2')

        list_view.add_widget(item1)
        list_view.add_widget(item2)

        screen.add_widget(item1)
        screen.add_widget(item2)
        return screen


TestApp().run()
