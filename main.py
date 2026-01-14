from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import platform

# ANDROID ORIENTATION FIX
if platform == "android":
    Window.rotation = 0


# ---------- HOME SCREEN ----------

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        # Top bar
        top = BoxLayout(size_hint_y=None, height=50)

        menu_btn = Button(text="≡", size_hint_x=None, width=60)
        menu_btn.bind(on_release=lambda x: self.open_menu())

        title = Label(text="AYAZ FINANS", bold=True)

        refresh = Button(text="↻", size_hint_x=None, width=60)

        top.add_widget(menu_btn)
        top.add_widget(title)
        top.add_widget(refresh)

        # Content
        content = BoxLayout(orientation="vertical", spacing=10)

        content.add_widget(Label(
            text="GRAM ALTIN",
            font_size="32sp",
            bold=True
        ))

        content.add_widget(Label(
            text="Serbest piyasa",
            font_size="16sp"
        ))

        content.add_widget(Label(
            text="Son güncelleme: --:--",
            font_size="14sp"
        ))

        root.add_widget(top)
        root.add_widget(content)

        self.add_widget(root)

    def open_menu(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "about"


# ---------- ABOUT SCREEN ----------

class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        title = Label(
            text="Uygulama Hakkında",
            font_size="22sp",
            bold=True,
            size_hint_y=None,
            height=50
        )

        text = Label(
            text=(
                "Ayaz Finans, döviz, altın, gümüş ve kripto para gibi finansal "
                "piyasa verilerini bilgilendirme amacıyla sunan bir mobil uygulamadır.\n\n"
                "Uygulama içerisinde gösterilen tüm veriler, üçüncü taraf açık ve yasal "
                "piyasa veri sağlayıcılarından anlık olarak alınmaktadır. Sunulan bilgiler "
                "yalnızca genel bilgilendirme amaçlıdır.\n\n"
                "Ayaz Finans herhangi bir yatırım danışmanlığı, alım-satım yönlendirmesi "
                "veya finansal tavsiye hizmeti sunmaz. Uygulamada yer alan veriler "
                "doğrultusunda alınacak yatırım kararlarının sorumluluğu tamamen "
                "kullanıcıya aittir.\n\n"
                "Uygulama, kullanıcı deneyimini ön planda tutarak sade, hızlı ve "
                "erişilebilir bir arayüz sunmayı hedefler."
            ),
            text_size=(Window.width - 40, None),
            halign="left",
            valign="top"
        )

        btns = BoxLayout(size_hint_y=None, height=50, spacing=10)

        privacy_btn = Button(text="Gizlilik Politikası")
        privacy_btn.bind(on_release=lambda x: self.go_privacy())

        back_btn = Button(text="Geri")
        back_btn.bind(on_release=lambda x: self.go_home())

        btns.add_widget(privacy_btn)
        btns.add_widget(back_btn)

        root.add_widget(title)
        root.add_widget(text)
        root.add_widget(btns)

        self.add_widget(root)

    def go_home(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "home"

    def go_privacy(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "privacy"


# ---------- PRIVACY SCREEN ----------

class PrivacyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        title = Label(
            text="Gizlilik Politikası",
            font_size="22sp",
            bold=True,
            size_hint_y=None,
            height=50
        )

        text = Label(
            text=(
                "Ayaz Finans, kullanıcı gizliliğine saygı duyar ve kişisel verilerin "
                "korunmasını öncelik olarak kabul eder.\n\n"
                "Bu uygulama herhangi bir kullanıcı hesabı oluşturmaz, kullanıcıdan "
                "isim, e-posta, telefon numarası, konum bilgisi veya cihaz tanımlayıcı "
                "bilgileri toplamaz, saklamaz veya işlemez.\n\n"
                "Uygulama içerisinde görüntülenen finansal veriler, yalnızca üçüncü "
                "taraf açık ve yasal veri sağlayıcılarından anlık olarak alınmakta "
                "olup, kalıcı olarak saklanmaz.\n\n"
                "Ayaz Finans, reklam, analiz veya takip teknolojileri kullanmaz.\n\n"
                "Uygulama herhangi bir yatırım danışmanlığı sunmaz. Sunulan bilgiler "
                "yalnızca bilgilendirme amaçlıdır ve yatırım kararlarının sorumluluğu "
                "tamamen kullanıcıya aittir."
            ),
            text_size=(Window.width - 40, None),
            halign="left",
            valign="top"
        )

        back_btn = Button(
            text="Geri",
            size_hint_y=None,
            height=50
        )
        back_btn.bind(on_release=lambda x: self.go_about())

        root.add_widget(title)
        root.add_widget(text)
        root.add_widget(back_btn)

        self.add_widget(root)

    def go_about(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "about"


# ---------- APP ----------

class AyazFinansApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(AboutScreen(name="about"))
        self.sm.add_widget(PrivacyScreen(name="privacy"))

        Window.bind(on_keyboard=self.on_back)
        return self.sm

    def on_back(self, window, key, *args):
        if key == 27:  # Android back
            if self.sm.current != "home":
                self.sm.transition = SlideTransition(direction="right")
                self.sm.current = "home"
                return True
        return False


if __name__ == "__main__":
    AyazFinansApp().run()
