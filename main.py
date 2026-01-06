from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.progressbar import MDProgressBar
from kivy.clock import Clock


class RezzonixHumanApp(MDApp):
    def build(self):
        self.title = "Rezzonix Human Analyzer"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"

        self.screen = MDScreen()
        self.layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        self.status = MDLabel(
            text="Hazır – Analiz Başlatılmadı",
            halign="center",
            font_style="H6"
        )

        self.progress = MDProgressBar(
            value=0,
            max=100
        )

        self.button = MDRaisedButton(
            text="ANALİZİ BAŞLAT",
            pos_hint={"center_x": 0.5},
            on_release=self.start_analysis
        )

        self.layout.add_widget(self.status)
        self.layout.add_widget(self.progress)
        self.layout.add_widget(self.button)

        self.screen.add_widget(self.layout)
        return self.screen

    def start_analysis(self, instance):
        self.progress.value = 0
        self.status.text = "Analiz yapılıyor..."
        Clock.schedule_interval(self.update_progress, 0.05)

    def update_progress(self, dt):
        if self.progress.value >= 100:
            self.status.text = "Analiz tamamlandı"
            return False
        self.progress.value += 1


if __name__ == "__main__":
    RezzonixHumanApp().run()
