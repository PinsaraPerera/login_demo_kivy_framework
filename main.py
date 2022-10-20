from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

from database import Database


class LoginWindow(Screen):
    passw = ObjectProperty(None)
    username = ObjectProperty(None)

    def login_btn(self):
        db = Database(self.username.text, self.passw.text)
        validity = db.validate_user()
        if validity:
            App.get_running_app().root.current = "user"
            self.username.text = ""
            self.passw.text = ""
        else:
            show_invalid_login_popup()
            self.username.text = ""
            self.passw.text = ""


class Invalid_popup(FloatLayout):
    pass


def show_invalid_login_popup():
    show = Invalid_popup()
    popupWindow = Popup(title="Alert => Invalid login", content=show, size_hint=(None, None), size=(400, 200))
    popupWindow.open()


class Registration_successful(FloatLayout):
    pass


def Registration_successful_popup():
    show = Registration_successful()
    popupWindow = Popup(title="Congratulations!!!", content=show, size_hint=(None, None), size=(400, 200))
    popupWindow.open()


class Registration_unsuccessful(FloatLayout):
    pass


def Registration_unsuccessful_popup():
    show = Registration_unsuccessful()
    popupWindow = Popup(title="ooops!! something went wrong", content=show, size_hint=(None, None), size=(400, 200))
    popupWindow.open()


class Null_value(FloatLayout):
    pass


def null_value_popup():
    show = Null_value()
    popupWindow = Popup(title="Alert!!", content=show, size_hint=(None, None), size=(400, 200))
    popupWindow.open()


class RegisterWindow(Screen):
    new_passw = ObjectProperty(None)
    new_username = ObjectProperty(None)
    new_email = ObjectProperty(None)

    def register_btn(self):

        db = Database(self.new_username.text, self.new_passw.text, self.new_email.text)
        validity = db.add_user()
        if validity:
            Registration_successful_popup()
            App.get_running_app().root.current = "login"
            self.new_username.text = ""
            self.new_passw.text = ""
            self.new_email.text = ""
        else:
            Registration_unsuccessful_popup()

    def null_value_popup(self):
        show = Null_value()
        popupWindow = Popup(title="Alert!!", content=show, size_hint=(None, None), size=(400, 200))
        popupWindow.open()


class User_details(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
        self.title = 'App demo'
        return kv


if __name__ == "__main__":
    MyApp().run()
