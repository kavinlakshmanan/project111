

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.widget import Widget


class LoginPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background = Image(source='login.jpg', allow_stretch=False, keep_ratio=False, size_hint=(1, 1))
        self.register_input = TextInput(hint_text='Register Number',multiline=False)
        self.roll_input = TextInput(hint_text='Roll Number',multiline=False)
        self.signin_button = Button(text='Sign In', background_color='blue', bold=True)
        self.signin_button.bind(on_press=self.sign_in)
        self.roll_input.pos_hint = {"center_x": .5, "center_y": .5}
        self.register_input.size_hint = (0.6, 0.15)
        self.roll_input.size_hint = (0.6, 0.15)
        self.register_input.pos_hint = {"center_x": .5, "center_y": .5}
        self.signin_button.size_hint = (0.6, 0.15)
        self.signin_button.pos_hint = {"center_x": .5, "center_y": .5}
        self.empty_space = Label(size_hint_y=None, height=10)
        layout = BoxLayout(orientation='vertical', spacing=10)
        layout.add_widget(self.background)
        layout.add_widget(self.register_input)
        layout.add_widget(self.roll_input)
        layout.add_widget(self.signin_button)
        layout.add_widget(self.empty_space)
        self.add_widget(layout)

    def sign_in(self, instance):
        register_number = self.register_input.text
        roll_number = self.roll_input.text
        if register_number and roll_number:
            sm.current = 'main'


class MainPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=10)
        self.background = Image(source='login.jpg', allow_stretch=False, keep_ratio=False, size_hint=(1, 1))
        self.categories = Button(text='Quiz', bold=True,background_color='cyan')
        self.profile = Button(text='Profile', bold=True,background_color='cyan')
        self.notes = Button(text='Notes', bold=True,background_color='cyan')
        self.exit = Button(text='Back', bold=True,background_color=(0,0,0,0.2))
        self.exit.bind(on_release=self.quit)
        self.categories.bind(on_press=self.show_question)
        self.profile.bind(on_press=self.show_profile)
        self.notes.bind(on_press=self.show_notes)

        self.categories.pos_hint = {"center_x": .5, "center_y": .5}
        self.categories.size_hint = (0.6, 0.15)
        self.profile.size_hint = (0.6, 0.15)
        self.profile.pos_hint = {"center_x": .5, "center_y": .5}
        self.notes.size_hint = (0.6, 0.15)
        self.notes.pos_hint = {"center_x": .5, "center_y": .5}
        self.exit.size_hint = (0.6, 0.15)
        self.exit.pos_hint = {"center_x": .5, "center_y": .5}
        self.empty_space = Label(size_hint_y=None, height=10)



        layout.add_widget(self.background)
        layout.add_widget(Widget(size_hint_y=None))
        layout.add_widget(self.categories)
        layout.add_widget(self.profile)
        layout.add_widget(self.notes)

        layout.add_widget(self.exit)
        self.add_widget(layout)




    def quit(self, instance):
        # Go back to the login page
        sm.current = 'login'

    def show_question(self,insatnce):
        sm.current ='questions'

    def show_profile(self, instance):
        sm.current = 'profile'

    def show_notes(self, instance):
        sm.current = 'notes'


class ProfilePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)
        self.background = Image(source='Stu_Logo.jpg', allow_stretch=False, keep_ratio=False, size_hint=(1, 1))
        self.marks_label = Label(text='                 WELCOME     TO   \n   \n  DEPARTMENT    OF      MECHANICAL !', bold=True, font_size=20 )
        self.exit_button = Button(text='Back', bold=True, background_color=(0, 0, 0.2))
        self.exit_button.size_hint = (0.6, 0.15)
        self.exit_button.pos_hint = {"center_x": .5, "center_y": .5}
        self.marks_label.pos_hint = {"center_x": .5, "center_y": .5}
        self.exit_button.bind(on_release=self.quit)
        self.empty_space = Label(size_hint_y=None, height=10)

        layout.add_widget(self.background)
        layout.add_widget(self.marks_label)
        layout.add_widget(self.exit_button)
        layout.add_widget(self.empty_space)
        self.add_widget(layout)

    def quit(self, instance):
        # Go back to the main page
        sm.current = 'main'

class NotesPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)
        self.background = Image(source='doc.jpg', allow_stretch=False, keep_ratio=False, size_hint=(1, 1))
        self.pdf_viewer = Label(text='Subject Notes', bold=True, font_size=20)
        self.exit_button = Button(text='Back', bold=True, background_color=(0, 0, 0.2))
        self.exit_button.size_hint = (0.6, 0.15)
        self.exit_button.pos_hint = {"center_x": .5, "center_y": .5}
        self.exit_button.bind(on_release=self.quit)
        self.empty_space = Label(size_hint_y=None, height=10)


        layout.add_widget(self.background)
        layout.add_widget(self.pdf_viewer)
        layout.add_widget(self.exit_button)
        layout.add_widget(self.empty_space)
        self.add_widget(layout)

    def quit(self, instance):
        # Go back to the main page
        sm.current = 'main'


class QuestionsPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical',spacing=10)
        self.background = Image(source='login.jpg', allow_stretch=False, keep_ratio=False, size_hint=(1, 1))
        self.level1 = Button(text='DOM', bold=True, background_color='cyan')
        self.level2 = Button(text='DME', bold=True, background_color='cyan')
        self.level3= Button(text='HMT', bold=True, background_color='cyan')
        self.level4 = Button(text='FEA', bold=True, background_color='cyan')
        self.exit = Button(text='Back', bold=True,background_color=(0,0,0))
        self.level1.pos_hint = {"center_x": .5, "center_y": .5}
        self.level1.size_hint = (0.6, 0.15)
        self.level2.size_hint = (0.6, 0.15)
        self.level2.pos_hint = {"center_x": .5, "center_y": .5}
        self.level3.size_hint = (0.6, 0.15)
        self.level3.pos_hint = {"center_x": .5, "center_y": .5}
        self.level4.size_hint = (0.6, 0.15)
        self.level4.pos_hint = {"center_x": .5, "center_y": .5}
        self.exit.size_hint = (0.6, 0.15)
        self.exit.pos_hint = {"center_x": .5, "center_y": .5}
        self.empty_space = Label(size_hint_y=None, height=10)

        self.exit.bind(on_release=self.quit)
        self.level1.bind(on_press=self.show_level1)
        self.level2.bind(on_press=self.show_level1)
        self.level3.bind(on_press=self.show_level1)
        self.level4.bind(on_press=self.show_level1)


        layout.add_widget(self.background)
        layout.add_widget(self.level1)
        layout.add_widget(self.level2)
        layout.add_widget(self.level3)
        layout.add_widget(self.level4)
        layout.add_widget(self.exit)

        self.add_widget(layout)


    def quit(self, instance):
        # Go back to the login page
        sm.current = 'main'

    def show_level1(self, insatnce):
        sm.current = 'level1'

    def show_level2(self, insatnce):
        sm.current = 'level2'

    def show_level3(self, insatnce):
        sm.current = 'level3'

    def show_level4(self, insatnce):
        sm.current = 'level4'


class BeginnerPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)
        self.background = Image(source='login.jpg', allow_stretch=False, keep_ratio=False, size_hint=(1, 1))
        self.test1 = Button(text='Quiz - I', bold=True, background_color='cyan')
        self.test2 = Button(text='Quiz - II', bold=True, background_color='cyan')
        self.test3 = Button(text='Quiz - III', bold=True, background_color='cyan')
        self.test4 = Button(text='Quiz - IV', bold=True, background_color='cyan')
        self.test5 = Button(text='Quiz - V', bold=True, background_color='cyan')
        self.exit = Button(text='Back', bold=True, background_color=(0, 0, 0))
        self.test1.pos_hint = {"center_x": .5, "center_y": .5}
        self.test1.size_hint = (0.6, 0.15)
        self.test2.size_hint = (0.6, 0.15)
        self.test2.pos_hint = {"center_x": .5, "center_y": .5}
        self.test3.size_hint = (0.6, 0.15)
        self.test3.pos_hint = {"center_x": .5, "center_y": .5}
        self.test4.size_hint = (0.6, 0.15)
        self.test4.pos_hint = {"center_x": .5, "center_y": .5}
        self.test5.size_hint = (0.6, 0.15)
        self.test5.pos_hint = {"center_x": .5, "center_y": .5}
        self.exit.size_hint = (0.6, 0.15)
        self.exit.pos_hint = {"center_x": .5, "center_y": .5}
        self.empty_space = Label(size_hint_y=None, height=10)
        self.exit.bind(on_release=self.quit)


        layout.add_widget(self.background)
        layout.add_widget(self.test1)
        layout.add_widget(self.test2)
        layout.add_widget(self.test3)
        layout.add_widget(self.test4)
        layout.add_widget(self.test5)
        layout.add_widget(self.exit)

        self.add_widget(layout)

    def quit(self, instance):
        # Go back to the login page
        sm.current = 'questions'


class IntermediatePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)
        self.background = Image(source='login.jpg', allow_stretch=False, keep_ratio=False, size_hint=(1, 1))
        self.test1 = Button(text='Quiz - I', bold=True, background_color='cyan')
        self.test2 = Button(text='Quiz - II', bold=True, background_color='cyan')
        self.test3 = Button(text='Quiz - III', bold=True, background_color='cyan')
        self.test4 = Button(text='Quiz - IV', bold=True, background_color='cyan')
        self.test5 = Button(text='Quiz - V', bold=True, background_color='cyan')
        self.exit = Button(text='Back', bold=True, background_color=(0, 0, 0))
        self.test1.pos_hint = {"center_x": .5, "center_y": .5}
        self.test1.size_hint = (0.6, 0.15)
        self.test2.size_hint = (0.6, 0.15)
        self.test2.pos_hint = {"center_x": .5, "center_y": .5}
        self.test3.size_hint = (0.6, 0.15)
        self.test3.pos_hint = {"center_x": .5, "center_y": .5}
        self.test4.size_hint = (0.6, 0.15)
        self.test4.pos_hint = {"center_x": .5, "center_y": .5}
        self.test5.size_hint = (0.6, 0.15)
        self.test5.pos_hint = {"center_x": .5, "center_y": .5}
        self.exit.size_hint = (0.6, 0.15)
        self.exit.pos_hint = {"center_x": .5, "center_y": .5}
        self.empty_space = Label(size_hint_y=None, height=10)
        self.exit.bind(on_release=self.quit)


        layout.add_widget(self.background)
        layout.add_widget(self.test1)
        layout.add_widget(self.test2)
        layout.add_widget(self.test3)
        layout.add_widget(self.test4)
        layout.add_widget(self.test5)
        layout.add_widget(self.exit)

        self.add_widget(layout)

    def quit(self, instance):
        # Go back to the login page
        sm.current = 'questions'


class AdvancePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)
        self.background = Image(source='login.jpg', allow_stretch=False, keep_ratio=False, size_hint=(1, 1))
        self.test1 = Button(text='Quiz - I', bold=True, background_color='cyan')
        self.test2 = Button(text='Quiz - II', bold=True, background_color='cyan')
        self.test3 = Button(text='Quiz - III', bold=True, background_color='cyan')
        self.test4 = Button(text='Quiz - IV', bold=True, background_color='cyan')
        self.test5 = Button(text='Quiz - V', bold=True, background_color='cyan')
        self.exit = Button(text='Back', bold=True, background_color=(0, 0, 0))
        self.test1.pos_hint = {"center_x": .5, "center_y": .5}
        self.test1.size_hint = (0.6, 0.15)
        self.test2.size_hint = (0.6, 0.15)
        self.test2.pos_hint = {"center_x": .5, "center_y": .5}
        self.test3.size_hint = (0.6, 0.15)
        self.test3.pos_hint = {"center_x": .5, "center_y": .5}
        self.test4.size_hint = (0.6, 0.15)
        self.test4.pos_hint = {"center_x": .5, "center_y": .5}
        self.test5.size_hint = (0.6, 0.15)
        self.test5.pos_hint = {"center_x": .5, "center_y": .5}
        self.exit.size_hint = (0.6, 0.15)
        self.exit.pos_hint = {"center_x": .5, "center_y": .5}
        self.empty_space = Label(size_hint_y=None, height=10)
        self.exit.bind(on_release=self.quit)

        layout.add_widget(self.background)
        layout.add_widget(self.test1)
        layout.add_widget(self.test2)
        layout.add_widget(self.test3)
        layout.add_widget(self.test4)
        layout.add_widget(self.test5)
        layout.add_widget(self.exit)

        self.add_widget(layout)

    def quit(self, instance):
        # Go back to the login page
        sm.current = 'questions'


class ProPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)
        self.background = Image(source='login.jpg', allow_stretch=False, keep_ratio=False, size_hint=(1, 1))
        self.test1 = Button(text='Quiz - I', bold=True, background_color='cyan')
        self.test2 = Button(text='Quiz - II', bold=True, background_color='cyan')
        self.test3 = Button(text='Quiz - III', bold=True, background_color='cyan')
        self.test4 = Button(text='Quiz - IV', bold=True, background_color='cyan')
        self.test5 = Button(text='Quiz - V', bold=True, background_color='cyan')
        self.exit = Button(text='Back', bold=True, background_color=(0, 0, 0))
        self.test1.pos_hint = {"center_x": .5, "center_y": .5}
        self.test1.size_hint = (0.6, 0.15)
        self.test2.size_hint = (0.6, 0.15)
        self.test2.pos_hint = {"center_x": .5, "center_y": .5}
        self.test3.size_hint = (0.6, 0.15)
        self.test3.pos_hint = {"center_x": .5, "center_y": .5}
        self.test4.size_hint = (0.6, 0.15)
        self.test4.pos_hint = {"center_x": .5, "center_y": .5}
        self.test5.size_hint = (0.6, 0.15)
        self.test5.pos_hint = {"center_x": .5, "center_y": .5}
        self.exit.size_hint = (0.6, 0.15)
        self.exit.pos_hint = {"center_x": .5, "center_y": .5}
        self.empty_space = Label(size_hint_y=None, height=10)
        self.exit.bind(on_release=self.quit)

        layout.add_widget(self.background)
        layout.add_widget(self.test1)
        layout.add_widget(self.test2)
        layout.add_widget(self.test3)
        layout.add_widget(self.test4)
        layout.add_widget(self.test5)
        layout.add_widget(self.exit)

        self.add_widget(layout)

    def quit(self, instance):
        # Go back to the login page
        sm.current = 'questions'

sm = ScreenManager()
sm.add_widget(LoginPage(name='login'))
sm.add_widget(MainPage(name='main'))
sm.add_widget(QuestionsPage(name='questions'))
sm.add_widget(BeginnerPage(name='level1'))
sm.add_widget(IntermediatePage(name='level2'))
sm.add_widget(AdvancePage(name='level3'))
sm.add_widget(ProPage(name='level4'))
sm.add_widget(ProfilePage(name='profile'))
sm.add_widget(NotesPage(name='notes'))

class PECApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    PECApp().run()
