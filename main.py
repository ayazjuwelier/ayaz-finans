from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import platform


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(
            text="AYAZ FINANS\nHOME SCREEN",
            halign="center",
            valign="middle",
            font_size="24sp"
        ))


class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(
            text="Uygulama Hakkında",
            halign="center",
            valign="middle",
            font_size="20sp"
        ))


class PrivacyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(
            text="Gizlilik Politikası",
            halign="center",
            valign="middle",
            font_size="20sp"
        ))


class MainScreenManager(ScreenManager):

    def go_to(self, screen_name):
        self.transition = SlideTransition(direction="left")
        self.current = screen_name

    def go_back(self):
        self.transition = SlideTransition(direction="right")
        self.current = "home"


class AyazFinansApp(App):

    def build(self):
        self.sm = MainScreenManager()
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(AboutScreen(name="about"))
        self.sm.add_widget(PrivacyScreen(name="privacy"))

        if platform == "android":
            Window.bind(on_keyboard=self.android_back)

        return self.sm

    def android_back(self, window, key, *args):
        if key == 27:
            if self.sm.current != "home":
                self.sm.go_back()
                return True
        return False


if __name__ == "__main__":
    AyazFinansApp().run()
