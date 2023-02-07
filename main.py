from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from libs.screen.home_page import HomePage


class DemoKivyProject(MDApp):
    def build(self):
        Window.size = [300, 600]
        self.load_all_kv_files()
        return HomePage()

    def load_all_kv_files(self):
        Builder.load_file('libs/screen/home_page.kv')


if __name__ == "__main__":
    DemoKivyProject().run()