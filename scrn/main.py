from concurrent.futures import thread
from pickle import TRUE
import threading
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import time
from kivy.clock import Clock, mainthread
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
import cv2 as cv
from check import recognize
    
Builder.load_file('main1.kv')
class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        ret, frame = self.capture.read()
        frame = recognize(frame)
        
        if ret:
            # convert it to texture
            buf1 = cv.flip(frame, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture

class CameraClick(BoxLayout):
    def exitapp(self):
        Window.close()
    
    
    def good_state(self):
            
        self.btn.text = "Видеопоток запущен"
        self.lbl.text = 'Для завершения работы нажмите на кнопку "Выйти из программы"'
        self.lbl.font_size= 15
        self.btn.color = (0,1,1,1)
        
        
        
        return True
        
    
    def bad_state(self):
        self.btn.color = (15,170,170,1)
        self.name_input.text = ""
        self.btn.text = "Введено неверное значение"
        self.lbl.text = "Видеопоток запустить не удалось. Повторите попытку"
        
        
        
        return True
    
    @mainthread
    def say_hello(self):
        xyp = self.name_input.text
        
        try:
            self.add_widget(KivyCamera(capture=cv.VideoCapture(int(xyp)), fps = 30))
            f1 = self.good_state()
        except:
            f1 = self.bad_state()
        
        # if f1:
        #     threading.Thread(target=start_cv(xyp)).start()
            
class MainApp(App):

    def build(self):
        return CameraClick()
    


if __name__  ==  '__main__':
    app = MainApp()
    app.run()