from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


"""
Box Layout


- medidas em dp ajustam de acordo com a tela
size_hint
pos_hint {center_x, center_y, x, y, top, left, right}
pos
size
label
button
text
color
"""


class LayoutApp(BoxLayout):
    """A calculator layout"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ButtonsLayoutApp(BoxLayout):
    pass


class ButtonsLayout2App(BoxLayout):
    pass


class ButtonsLayout3App(BoxLayout):
    pass


class ButtonsLayout4App(BoxLayout):
    pass


class MainWidget(Widget):
    pass


class AppApp(App):
    pass


if __name__ == '__main__':
    AppApp().run()
