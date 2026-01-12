from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivy.uix.button import Button

from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.menu_open = False

        root = BoxLayout(orientation="horizontal")

        # -------- SOL MENU --------
        self.menu_container = BoxLayout(
            orientation="vertical",
            size_hint_x=None,
            width=0
        )

        scroll = ScrollView()
        menu = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10,
            size_hint_y=None
        )
        menu.bind(minimum_height=menu.setter("height"))

        def menu_button(text, action):
            btn = Button(
                text=text,
                size_hint_y=None,
                height="48dp",
                halign="left",
                valign="middle",
                background_normal="",
                background_color=(0, 0, 0, 0)
            )
            btn.text_size = (200, None)
            btn.bind(on_release=action)
            return btn

        menu.add_widget(menu_button("Ana Ekran", lambda x: self.close_menu()))
        menu.add_widget(menu_button("Uygulama Hakkında", lambda x: self.go("about")))
        menu.add_widget(menu_button("Gizlilik Politikası", lambda x: self.go("privacy")))

        scroll.add_widget(menu)
        self.menu_container.add_widget(scroll)
        root.add_widget(self.menu_container)

        # -------- ANA İÇERİK --------
        content = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        # ÜST BAR
        top_bar = BoxLayout(size_hint_y=None, height="48dp")

        burger = Button(
            text="MENU",
            font_size="14sp",
            size_hint_x=None,
            width="64dp",
            background_normal="",
            background_color=(0, 0, 0, 0)
        )
        burger.bind(on_release=self.toggle_menu)

        refresh = Button(
            text="YENİLE",
            font_size="14sp",
            size_hint_x=None,
            width="64dp",
            background_normal="",
            background_color=(0, 0, 0, 0)
        )

        top_bar.add_widget(burger)
        top_bar.add_widget(Label())
        top_bar.add_widget(refresh)

        content.add_widget(top_bar)

        # ORTA
        market = Label(
            text="GRAM ALTIN",
            font_size="36sp",
            bold=True,
            halign="center"
        )
        market.bind(size=market.setter("text_size"))

        info = Label(
            text="Serbest piyasa",
            font_size="16sp",
            halign="center"
        )
        info.bind(size=info.setter("text_size"))

        content.add_widget(market)
        content.add_widget(info)

        # ALT
        footer = Label(
            text="Son güncelleme: --:--",
            font_size="14sp",
            size_hint_y=None,
            height="32dp",
            halign="center"
        )
        footer.bind(size=footer.setter("text_size"))

        content.add_widget(footer)

        root.add_widget(content)
        self.add_widget(root)

    def toggle_menu(self, *args):
        if self.menu_open:
            self.menu_container.width = 0
            self.menu_open = False
        else:
            self.menu_container.width = 260
            self.menu_open = True

    def close_menu(self):
        self.menu_container.width = 0
        self.menu_open = False

    def go(self, screen):
        self.manager.go_to(screen)
        self.close_menu()

    def go(self, screen):
        self.manager.go_to(screen)
        self.close_menu()



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

        scroll = ScrollView()
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            size_hint_y=None
        )
        layout.bind(minimum_height=layout.setter("height"))

        text = (
            "Gizlilik Politikası\n\n"

            "Ayaz Finans, kullanıcı gizliliğine önem verir. "
            "Uygulama herhangi bir kullanıcı hesabı oluşturmaz ve "
            "kullanıcıdan kişisel veri talep etmez.\n\n"

            "Uygulama kapsamında; ad, soyad, e-posta adresi, telefon "
            "numarası, konum bilgisi veya cihaz kimliği gibi kişisel "
            "veriler toplanmaz, işlenmez ve saklanmaz.\n\n"

            "Uygulamada gösterilen finansal veriler, yalnızca üçüncü taraf "
            "açık ve yasal piyasa veri sağlayıcılarından anlık olarak "
            "alınmaktadır. Bu veriler uygulama içinde kalıcı olarak "
            "saklanmaz.\n\n"

            "Ayaz Finans, yatırım danışmanlığı hizmeti sunmaz. "
            "Uygulamada yer alan tüm bilgiler yalnızca bilgilendirme "
            "amaçlıdır. Kullanıcıların uygulamada yer alan bilgilere "
            "dayanarak aldıkları finansal kararlardan doğabilecek "
            "zararlardan uygulama geliştiricisi sorumlu tutulamaz.\n\n"

            "Uygulama, arka planda veri toplamaz ve uygulama kapalıyken "
            "herhangi bir veri güncellemesi yapmaz.\n\n"

            "Bu gizlilik politikası, uygulamanın mevcut sürümü için "
            "geçerlidir ve ileride yapılabilecek güncellemelerle "
            "değiştirilebilir."
        )

        label = Label(
            text=text,
            halign="left",
            valign="top",
            size_hint_y=None,
            text_size=(Window.width - 40, None)
        )
        label.bind(texture_size=label.setter("size"))

        layout.add_widget(label)
        scroll.add_widget(layout)
        self.add_widget(scroll)



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
