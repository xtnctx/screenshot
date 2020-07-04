from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.clock import Clock
import pyautogui
import datetime
Window.size = (100, 50)

file_name = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S")

Builder.load_string("""
#: import NoTransition  kivy.uix.screenmanager.NoTransition 
#: import utils kivy.utils

<Management>:
    transition: NoTransition()
    Assistive_Touch:
    
    
<Assistive_Touch>:
    name: 'main'
    Button:
        text: 'screenshot'
        on_press: root.capture_screen()

    

""")


class Management(ScreenManager):
    pass

class Assistive_Touch(Screen):
    def capture_screen(self):
        pyautogui.screenshot('Screenshots\{}.png'.format(file_name))
        Window.close()

        

class Run_app(App):
    def build(self):
        return Management()

r = Run_app()
r.run()
