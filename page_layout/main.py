from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
"""
Scroll layout

permite usar o scroll da tela
"""


class PageLayoutApp(PageLayout):
    pass


class ScrollLayoutApp(ScrollView):
    pass


class StackLayoutContent(StackLayout):
    pass


class GridLayoutA(GridLayout):
    pass


class AppApp(App):
    pass


if __name__ == '__main__':
    AppApp().run()
