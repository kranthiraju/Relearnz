from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
import demo_login

class WelcomePage(Screen):
    pass

sm = ScreenManager()
sm.add_widget(WelcomePage(name="welcome"))
sm.add_widget(demo_login.LoginPage(name="login"))

class Welcometolog(MDApp):
    def build(self):
        Builder.load_file('demo_login.kv')
        return Builder.load_file("welcome.kv")

Welcometolog().run()