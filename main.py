from concurrent.futures import thread
from pickle import TRUE
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
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
from scrn.check import recognize
import os

Builder.load_file('main1.kv') #импорт разметки виджетов

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



class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    

class CameraClick(BoxLayout):

    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Загрузка файла", content=content,
                        size_hint=(0.9, 0.9))
        self._popup.open()
        
 
    def load(self, path, filename): #работа с выбранным файлом
        
        with open(os.path.join(path, filename[0])) as stream:
            
            CameraClick.file_hello(self, filename[0])
            
            # self.text_input.text = stream.read()

        self.dismiss_popup()
        

    ###############################


    def exitapp(self):
        Window.close()
    

    def index_chooser(self):
        self.name_input.size = (80, 80)

        self.btn1.color = (1,1,1,1)
        self.btn1.background_color = (0, 0, 0, 0)
        self.btn1.text = ""
        self.btn2.size= (0, 0)
        self.btn1.size= (0, 0)
        self.btn2.text = ""
        self.btn2.background_color = (0, 0, 0, 0)
        self.btn3.size= (0, 0)
        self.btn3.text = ""
        self.btn3.background_color = (0, 0, 0, 0)
        self.btn4.size = (70, 70)

        self.btn4.background_color = (1, 89/255, 0, 0.7)
        self.btn4.font_size = 20
        self.lbl.text = "Введите индекс видеопотока"   
        return True
        

    def good_state(self):
            
        self.btn1.text = "Видеопоток запущен"
        self.lbl.text = 'Для завершения работы нажмите на кнопку "Выйти из программы"'
        self.lbl.font_size= 15
        self.name_input.size = (0, 0)
        self.btn1.size= (0, 0)
        self.btn1.text = ""
        self.btn2.size= (0, 0)
        self.btn2.text = ""
        self.btn3.size= (0, 0)
        self.btn3.text = ""
        self.btn4.size= (0, 0)
        self.btn4.text = ""
        self.name_input.background_color = (0, 0, 0, 0)
        self.btn1.background_color = (0, 0, 0, 0)
        self.btn2.background_color = (0, 0, 0, 0)
        self.btn3.background_color = (0, 0, 0, 0)
        self.btn4.background_color = (0, 0, 0, 0)
        
        
        return True
        
    
    def bad_state(self):
        self.btn1.color = (15,170,170,1)
        self.name_input.text = ""
        self.btn1.text = "Введено неверное значение"
        self.lbl.text = "Видеопоток запустить не удалось. Повторите попытку"
        
        
        
        return False

    @mainthread
    def translation_hello(self):
        xyp = 1
        
        try:
            self.add_widget(KivyCamera(capture=cv.VideoCapture(int(xyp)), fps = 60))
            f1 = self.good_state()
        except:
            f1 = self.bad_state()
        
    @mainthread
    def file_hello(self, path):
        
        
        try:
            self.add_widget(KivyCamera(capture=cv.VideoCapture(path), fps = 60))
            f1 = self.good_state()
        except:
            f1 = self.bad_state()
     

    @mainthread
    def say_hello(self):
        xyp = self.name_input.text
        
        try:
            self.add_widget(KivyCamera(capture=cv.VideoCapture(int(xyp)), fps = 60))
            f1 = self.good_state()
        except:
            f1 = self.bad_state()
        
        # if f1:
        #     threading.Thread(target=start_cv(xyp)).start()






class MainApp(App):

    def build(self):
        return CameraClick()
    
Factory.register('Root', cls=CameraClick)
Factory.register('LoadDialog', cls=LoadDialog)

if __name__  ==  '__main__':
    app = MainApp()
    app.run()