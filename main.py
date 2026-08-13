from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text='سلام! این اولین اپ منه'))
        self.add_widget(Button(text='کلیک کن', on_press=self.on_click))

    def on_click(self, instance):
        instance.text = 'دکمه کار می‌کنه! 🎉'

class ChatApp(App):
    def build(self):
        return MainScreen()

ChatApp().run()

