from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.widget import Widget

# ANDROID ORIENTATION FIX
if platform == "android":
    Window.rotation = 0


class HomeScreen(Screen):
    pass


class AboutScreen(Screen):
    pass


class PrivacyScreen(Screen):
    pass


class MainLayout(BoxLayout):
    def __init__(self, sm, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.sm = sm

        # HEADER
        header = BoxLayout(size_hint_y=None, height=50)
        menu_btn = Button(text="☰", size_hint_x=None, width=60)
        menu_btn.bind(on_release=self.open_menu)
        header.add_widget(menu_btn)
        header.add_widget(Label(text="Ayaz Finans"))
        self.add_widget(header)

        # CONTENT
        self.content = BoxLayout()
        self.add_widget(self.content)
        self.update_content()

    def open_menu(self, *_):
        self.sm.transition = SlideTransition(direction="right")
        self.sm.current = "about"

    def update_content(self):
        self.content.clear_widgets()
        self.content.add_widget(Label(
            text="GRAM ALTIN\n\nSerbest piyasa\n\nSon güncelleme: --:--",
            halign="center",
            valign="middle",
            font_size="24sp"
        ))


class AyazFinansApp(App):
    def build(self):
        self.sm = ScreenManager()

        home = HomeScreen(name="home")
        about = AboutScreen(name="about")
        privacy = PrivacyScreen(name="privacy")

        home.add_widget(MainLayout(self.sm))

        about.add_widget(Label(
            text=(
                "UYGULAMA HAKKINDA\n\n"
                "Ayaz Finans, döviz, kıymetli maden ve dijital varlık fiyatlarını "
                "bilgilendirme amacıyla sunar.\n\n"
                "Veriler üçüncü taraf açık ve yasal piyasa servislerinden "
                "anlık olarak alınır, kaydedilmez.\n\n"
                "Uygulama yatırım danışmanlığı içermez."
            )
        ))

        privacy.add_widget(Label(
            text=(
                "GİZLİLİK POLİTİKASI\n\n"
                "Bu uygulama kişisel veri toplamaz.\n"
                "Hesap, konum, cihaz veya reklam kimliği kullanılmaz.\n\n"
                "Veriler yalnızca anlık görüntülenir ve saklanmaz."
            )
        ))

        self.sm.add_widget(home)
        self.sm.add_widget(about)
        self.sm.add_widget(privacy)

        # ANDROID BACK BUTTON FIX
        Window.bind(on_keyboard=self.on_back)

        return self.sm

    def on_back(self, window, key, *args):
        if key == 27:
            if self.sm.current != "home":
                self.sm.transition = SlideTransition(direction="left")
                self.sm.current = "home"
                return True
        return False


if __name__ == "__main__":
    AyazFinansApp().run()
