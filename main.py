from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.widget import Widget

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical")

        # HEADER (HAMBURGER)
        header = BoxLayout(size_hint_y=None, height=56)
        menu_btn = Button(text="☰", size_hint_x=None, width=56)
        menu_btn.bind(on_release=self.open_menu)
        title = Label(text="Ayaz Finans")

        header.add_widget(menu_btn)
        header.add_widget(title)

        # CONTENT
        content = BoxLayout()
        content.add_widget(Label(
            text="GRAM ALTIN\n\nSerbest piyasa\n\nSon güncelleme: --:--",
            halign="center",
            valign="middle",
            font_size="24sp"
        ))

        root.add_widget(header)
        root.add_widget(content)

        self.add_widget(root)

    def open_menu(self, *_):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "about"


class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical")

        # HEADER
        header = BoxLayout(size_hint_y=None, height=56)
        back_btn = Button(text="←", size_hint_x=None, width=56)
        back_btn.bind(on_release=self.go_home)
        title = Label(text="Uygulama Hakkında")

        header.add_widget(back_btn)
        header.add_widget(title)

        body = Label(
            text=(
                "UYGULAMA HAKKINDA\n\n"
                "Ayaz Finans, finansal piyasa verilerini bilgilendirme "
                "amacıyla sunar.\n\n"
                "Uygulama yatırım danışmanlığı içermez."
            ),
            halign="center",
            valign="middle"
        )

        root.add_widget(header)
        root.add_widget(body)
        self.add_widget(root)

    def go_home(self, *_):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "home"


class PrivacyScreen(Screen):
    pass

class AyazFinansApp(App):
    def build(self):
        self.sm = ScreenManager()

        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(AboutScreen(name="about"))
        self.sm.add_widget(PrivacyScreen(name="privacy"))

        Window.bind(on_keyboard=self.on_back)

        return self.sm

    def on_back(self, window, key, *args):
        if key == 27:
            if self.sm.current != "home":
                self.sm.transition = SlideTransition(direction="right")
                self.sm.current = "home"
                return True
        return False

class AyazFinansApp(App):
    def build(self):
        self.sm = ScreenManager()

        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(AboutScreen(name="about"))
        self.sm.add_widget(PrivacyScreen(name="privacy"))

        # ANDROID BACK BUTTON
        Window.bind(on_keyboard=self.on_back)

        return self.sm

    def on_back(self, window, key, *args):
        if key == 27:  # Android back button
            if self.sm.current != "home":
                self.sm.transition = SlideTransition(direction="right")
                self.sm.current = "home"
                return True
        return False


if __name__ == "__main__":
    AyazFinansApp().run()
