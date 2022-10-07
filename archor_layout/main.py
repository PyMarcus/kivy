from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

"""
Archor layout

for X: (archor_x)
right, left, center

for Y: (archor_y)
bottom, top, center
"""


class ArchorLayout(AnchorLayout):
    pass


class BoxLayoutApp(BoxLayout):
    pass


class AppApp(App):
    pass


if __name__ == '__main__':
    AppApp().run()
