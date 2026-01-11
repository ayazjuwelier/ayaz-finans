from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from kivy.utils import platform
from kivy.clock import Clock


# ---------- EKRANLAR ----------

class HomeScreen(Screen):
    pass


class AboutScreen(Screen):
    pass


class PrivacyScreen(Screen):
    pass


# ---------- SCREEN MANAGER ----------

class MainScreenManager(ScreenManager):
    def go_to(self, screen_name):
        self.transition = SlideTransition(direction="left")
        self.current = screen_name

    def go_back(self):
        self.transition = SlideTransition(direction="right")
        self.current = "home"


# ---------- UYGULAMA ----------

class AyazFinansApp(App):

    def build(self):
        self.title = "Ayaz Finans"

        self.sm = MainScreenManager()

        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(AboutScreen(name="about"))
        self.sm.add_widget(PrivacyScreen(name="privacy"))

        # Android geri tuşu yakalama
        if platform == "android":
            Window.bind(on_keyboard=self.android_back_button)

        return self.sm

    def android_back_button(self, window, key, *args):
        # 27 = Android geri tuşu
        if key == 27:
            if self.sm.current != "home":
                self.sm.go_back()
                return True  # uygulama kapanmasın
        return False


# ---------- ÇALIŞTIR ----------

if __name__ == "__main__":
    AyazFinansApp().run()
