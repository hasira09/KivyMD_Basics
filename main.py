from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.screen import Screen


class TestApp(MDApp):

    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        for i in range(20):
            items = OneLineListItem(text='Item ' + str(i))
            list_view.add_widget(items)

        screen.add_widget(scroll)
        return screen


TestApp().run()
