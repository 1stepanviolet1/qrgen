from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

from kivy.core.window import Window

Window.size = (270, 585)
Window.clearcolor = (1, 1, 1, 1)

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

import os
from genQR import gen_qrcode


class Container(GridLayout):
    input = ObjectProperty()
    img = ObjectProperty()
    
    i = 0

    def show_qr(self):
        if self.i >= 100:
            self.clear_widgets()
            self.add_widget(
                Label(
                    text='Please,\nreload this app.',
                    font_size='85sp',
                    color='black'
                )
            )
            return None
        
        file = f'./data/qr{self.i}.png'
        self.i += 1
        gen_qrcode(self.input.text, file)
        self.img.source = file
        self.input.text = ''


class GenerateQRApp(App):
    def build(self):
        return Container()
    
    def __del__(self):
        try:
            for i in range(100):
                os.remove(f'./data/qr{i}.png')
        except FileNotFoundError:
            ...


if __name__ == '__main__':
    GenerateQRApp().run()
