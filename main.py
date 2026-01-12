from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.utils import platform
from kivy.core.window import Window

from datetime import datetime
import requests

# ------------------------
# HOME SCREEN
# ------------------------

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.last_price = None

        # ROOT
        root = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        # ---------------- TOP BAR ----------------
        top_bar = BoxLayout(
            size_hint_y=None,
            height=50
        )

        top_bar.add_widget(Label())  # spacer

        self.refresh_button = Button(
            text="↻",
            size_hint=(None, None),
            size=(48, 48),
            font_size="24sp",
            background_normal="",
            background_color=(0.2, 0.2, 0.2, 1)
        )
        self.refresh_button.bind(on_press=self.on_refresh_pressed)

        top_bar.add_widget(self.refresh_button)

        # ---------------- CENTER ----------------
        center = BoxLayout(
            orientation="vertical",
            spacing=10
        )

        self.price_label = Label(
            text="0,00 ₺",
            font_size="48sp",
            bold=True,
            color=(1, 1, 1, 1)
        )

        self.trend_label = Label(
            text="",
            font_size="32sp",
            color=(1, 1, 1, 1)
        )

        center.add_widget(self.price_label)
        center.add_widget(self.trend_label)

        # ---------------- BOTTOM ----------------
        bottom = BoxLayout(
            size_hint_y=None,
            height=40
        )

        self.refresh_label = Label(
            text="Son güncelleme: —",
            font_size="14sp",
            color=(1, 1, 1, 0.7)
        )

        bottom.add_widget(self.refresh_label)

        # ADD ALL
        root.add_widget(top_bar)
        root.add_widget(center)
        root.add_widget(bottom)

        self.add_widget(root)

    # ------------------------
    # REFRESH FLOW
    # ------------------------

    def on_enter(self):
        self.on_refresh_pressed()

    def on_refresh_pressed(self, *args):
        self.fake_refresh()
        self.start_real_refresh()

    def fake_refresh(self):
        self.refresh_label.text = "Güncelleniyor…"
        Clock.schedule_once(self.finish_fake_refresh, 1.2)

    def finish_fake_refresh(self, dt):
        now = datetime.now().strftime("%H:%M")
        self.refresh_label.text = f"Son güncelleme: {now}"

    # ------------------------
    # REAL DATA (BINANCE)
    # ------------------------

    def start_real_refresh(self):
        Clock.schedule_once(self.fetch_real_data, 0)

    def fetch_real_data(self, dt):
        try:
            price = self.fetch_binance_price()
            self.update_price(price)
        except Exception:
            self.refresh_label.text = "Bağlantı yok"

    def fetch_binance_price(self):
        url = "https://api.binance.com/api/v3/ticker/price?symbol=XAUTRY"
        r = requests.get(url, timeout=5)
        return float(r.json()["price"])

    def update_price(self, price):
        if self.last_price:
            if price > self.last_price:
                self.trend_label.text = "↑"
                self.trend_label.color = (0, 1, 0, 1)
            elif price < self.last_price:
                self.trend_label.text = "↓"
                self.trend_label.color = (1, 0, 0, 1)

        self.last_price = price
        self.price_label.text = f"{price:,.2f} ₺".replace(",", ".")


# ------------------------
# APP
# ------------------------

class AyazFinansApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)

        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        return sm


if __name__ == "__main__":
    AyazFinansApp().run()
