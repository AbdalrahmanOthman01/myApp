from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.properties import NumericProperty
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
import os

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        buttons_layout = BoxLayout(size_hint=(1, 0.7), spacing=10)
        
        camera_button = Button(text="Open Camera")
        camera_button.bind(on_press=self.open_camera)
        buttons_layout.add_widget(camera_button)
        
        flash_button = ToggleButton(text="Flash Off")
        flash_button.bind(on_press=self.toggle_flash)
        buttons_layout.add_widget(flash_button)
        
        silent_button = ToggleButton(text="Silent Mode Off")
        silent_button.bind(on_press=self.toggle_silent_mode)
        buttons_layout.add_widget(silent_button)
        
        airplane_button = ToggleButton(text="Airplane Mode Off")
        airplane_button.bind(on_press=self.toggle_airplane_mode)
        buttons_layout.add_widget(airplane_button)
        
        dnd_button = ToggleButton(text="DND Off")
        dnd_button.bind(on_press=self.toggle_dnd_mode)
        buttons_layout.add_widget(dnd_button)
        
        launch_app_button = Button(text="Launch TikTok")
        launch_app_button.bind(on_press=self.launch_app)
        buttons_layout.add_widget(launch_app_button)
        
        layout.add_widget(buttons_layout)
        self.add_widget(layout)

    def open_camera(self, instance):
        self.manager.transition = NoTransition()
        self.manager.current = 'camera'

    def toggle_flash(self, instance):
        if instance.state == 'down':
            instance.text = "Flash On"
            # Add flashlight enabling logic
        else:
            instance.text = "Flash Off"
            # Add flashlight disabling logic

    def toggle_silent_mode(self, instance):
        if instance.state == 'down':
            instance.text = "Silent Mode On"
            # Add silent mode enabling logic
        else:
            instance.text = "Silent Mode Off"
            # Add silent mode disabling logic

    def toggle_airplane_mode(self, instance):
        if instance.state == 'down':
            instance.text = "Airplane Mode On"
            # Add airplane mode enabling logic
        else:
            instance.text = "Airplane Mode Off"
            # Add airplane mode disabling logic

    def toggle_dnd_mode(self, instance):
        if instance.state == 'down':
            instance.text = "DND On"
            # Add DND mode enabling logic
        else:
            instance.text = "DND Off"
            # Add DND mode disabling logic

    def launch_app(self, instance):
        # Replace 'tiktok' with any app package name you want to launch
        os.system('start WhatsApp Business')

class CameraScreen(Screen):
    zoom_level = NumericProperty(1.0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        self.scatter = Scatter(do_translation=False, do_rotation=False)
        
        self.camera = Camera(resolution=(640, 480), play=True)
        self.scatter.add_widget(self.camera)
        layout.add_widget(self.scatter)
        
        back_button = Button(text="Back", size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0})
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)
        
        self.slider = Slider(min=1, max=3, value=1, size_hint=(1, 0.1), pos_hint={'x': 0, 'y': 0.1})
        self.slider.bind(value=self.on_zoom)
        layout.add_widget(self.slider)
        
        self.add_widget(layout)

    def on_zoom(self, instance, value):
        self.zoom_level = value
        anim = Animation(scale=value, duration=0.2)
        anim.start(self.scatter)

    def go_back(self, instance):
        self.manager.transition = NoTransition()
        self.manager.current = 'main'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CameraScreen(name='camera'))
        return sm

if __name__ == '__main__':
    MyApp().run()
