from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor=(1,0,0,1)
class Widget_Example(BoxLayout):
    count=1
    my_text=StringProperty("")
    
    def On_button_click(self):
        
        self.my_text=str ("I Love You ") +str( self.count)
        self.count+=1

class Button_click(App):
    def build(self):
        pass

Button_click().run()