from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.clock import Clock


class RezzonixPlatformApp(MDApp):
    def build(self):
        self.title = "Rezzonix Platform"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"

        screen = MDScreen()

        layout = MDBoxLayout(
            orientation="vertical",
            spacing=20,
            padding=40
        )

        title = MDLabel(
            text="REZZONIX PLATFORM",
            halign="center",
            font_style="H4"
        )

        subtitle = MDLabel(
            text="Human Analyzer\nBLE El Sensörü Hazır",
            halign="center"
        )

        start_btn = MDRaisedButton(
            text="Analizi Başlat",
            pos_hint={"center_x": 0.5},
            on_release=self.start_analysis
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(start_btn)

        screen.add_widget(layout)
        return screen

    def start_analysis(self, instance):
        instance.text = "Analiz Başladı..."
        Clock.schedule_once(lambda dt: self.analysis_done(instance), 3)

    def analysis_done(self, instance):
        instance.text = "Analiz Tamamlandı"


if __name__ == "__main__":
    RezzonixPlatformApp().run()
