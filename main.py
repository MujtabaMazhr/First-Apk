from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton

class FirstApplication(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        layout = MDFloatLayout()
        button = MDFlatButton(text="Hello",pos_hint={"center_x":.5,"center_y":.5})
        layout.add_widget(button)
        return layout

FirstApplication().run()