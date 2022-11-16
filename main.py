from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen


class TestApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            size_hint=(0.9, 0.6),
                            check=True,
                            column_data=[
                                ("Num", dp(20)),
                                ("Food", dp(20)),
                                ("Calories", dp(20))
                            ],
                            row_data=[
                                ("1", "Submarines", "350"),
                                ("2", "Bread", "250")
                            ]
                            )

        table.bind(on_check_press=self.check_press)
        table.bind(on_row_press=self.row_press)
        screen.add_widget(table)
        return screen

    def check_press(self, instance_table, current_row):
        print(self, instance_table, current_row)

    def row_press(self, instance_table, instance_row):
        print(self, instance_table, instance_row)


TestApp().run()
