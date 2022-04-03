import threading

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window

import capture



Window.size = (450,100)

class MainWidget(BoxLayout):

    btn = ObjectProperty()
    name_input = ObjectProperty()
    def say_hello(self):
        xyp = self.name_input.text
        ih = False
        try:
            capf = open(xyp, "r")
            capf.close()
            ih = True
        except: 
            self.btn.color = (1,0,0,1)
            self.name_input.text = ""
            self.btn.text = "Что-то не так..."
        if ih:
            self.name_input.text = ""
            thread = threading.Thread(target = capture.start_cv(xyp))
            thread.start()

class MainApp(App):

    def build(self):
        return MainWidget()


if __name__  ==  '__main__':
    app = MainApp()
    app.run()