import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

# Inicialize o Firebase fora das classes do Kivy para garantir que está feito uma vez
cred = credentials.Certificate('C:/Users/sofia/Downloads/noble-might-399221-firebase-adminsdk-blpau-93e21293d0.json') 
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://noble-might-399221-default-rtdb.firebaseio.com/'  
})


class Tela_Login(Screen):
    def __init__(self, **kwargs):
        super(Tela_Login, self).__init__(**kwargs)
        layout_main = FloatLayout()
        self.orientation= "vertical"
        self.padding= [50, 20]
        self.spacing= 10

        Window.clearcolor= (0, 0, 0.1, 2)

        l_login = Label(
            text="L O G I N", 
            size_hint=(.2, .1),
            pos=(325, 390),
            font_size= 20,
            color = [1,1,1,1],
            halign = ('center')
        )

        layout_main.add_widget(l_login)

        l_login1 = Label(
            text="E M A I L", 
            size_hint=(.2, .1),
            pos=(325, 340),
            font_size= 15,
            color = [1,1,1,1],
            halign = ('center')
        )
        layout_main.add_widget(l_login1)

        self.input = TextInput(
            multiline= False,
            size_hint=(0.4, 0.09),
            pos=(250, 300),
            hint_text='Digite o email aqui...',
            padding_y=(15)
        )
    
        layout_main.add_widget(self.input)

        l_login2 = Label(
            text="S E N H A", 
            size_hint=(.2, .1),
            pos=(325, 250),
            font_size= 15,
            color = [1,1,1,1],
            halign = ('center')
        )
        layout_main.add_widget(l_login2)

        self.input2 = TextInput(
            multiline= False,
            size_hint=(0.4, 0.09),
            pos=(250, 210),
            hint_text='Digite a senha aqui...',
            padding_y=(15)
        )
    
        layout_main.add_widget(self.input2)

        botaoL = Button(
                text="E N T R A R",
                pos_hint={'x': 0.4, 'y':0.27},
                halign=('center'),
                size_hint=(0.2, 0.045),
                font_size=(15),
                on_release=self.login
            )
        
        layout_main.add_widget(botaoL)

        botaoC = Button(
                text="CA D A S T R A R",
                pos_hint={'x': 0.4, 'y':0.20},
                halign=('center'),
                size_hint=(0.2, 0.045),
                font_size=(15),
                on_release=self.cadastrar
            )
        layout_main.add_widget(botaoC)

        self.add_widget(layout_main)

    def login(self, instance):
        email = self.input.text
        senha = self.input2.text
        ref = db.reference('login')
        users = ref.get()

        for user in users.values():
            if user['email'] == email and user['senha'] == senha:
                print("Login feito com sucesso")
                return
        print("Login não encontrado")

    def cadastrar(self, instance):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'cadastro'

class Tela_Cadastro(Screen):
    def __init__(self, **kwargs):
        super(Tela_Cadastro, self).__init__(**kwargs)
        layout_main = FloatLayout()
        self.orientation= "vertical"
        self.padding= [50, 20]
        self.spacing= 10

        Window.clearcolor= (0, 0, 0.1, 2)

        l_login = Label(
            text="C A D A S T R O", 
            size_hint=(.2, .1),
            pos=(325, 390),
            font_size= 20,
            color = [1,1,1,1],
            halign = ('center')
        )

        layout_main.add_widget(l_login)

        l_login1 = Label(
            text="E M A I L", 
            size_hint=(.2, .1),
            pos=(325, 340),
            font_size= 15,
            color = [1,1,1,1],
            halign = ('center')
        )
        layout_main.add_widget(l_login1)

        self.input = TextInput(
            multiline= False,
            size_hint=(0.4, 0.09),
            pos=(250, 300),
            hint_text='Digite o email aqui...',
            padding_y=(15)
        )
    
        layout_main.add_widget(self.input)

        l_login2 = Label(
            text="S E N H A", 
            size_hint=(.2, .1),
            pos=(325, 250),
            font_size= 15,
            color = [1,1,1,1],
            halign = ('center')
        )
        layout_main.add_widget(l_login2)

        self.input2 = TextInput(
            multiline= False,
            size_hint=(0.4, 0.09),
            pos=(250, 210),
            hint_text='Digite a senha aqui...',
            padding_y=(15)
        )
    
        layout_main.add_widget(self.input2)

        botaoC2 = Button(
                text="CA D A S T R A R",
                pos_hint={'x': 0.4, 'y':0.27},
                halign=('center'),
                size_hint=(0.2, 0.045),
                font_size=(15),
                on_release=self.cadastrar
            )

        layout_main.add_widget(botaoC2)
        
        self.add_widget(layout_main)
    
    def cadastrar(self, instance):
        email = self.input.text
        senha = self.input2.text
        if email and senha:
            ref = db.reference('login')
            ref.push({
                'email': email,
                'senha': senha
            })
            print('Usuário cadastrado com sucesso!')
            self.manager.transition = SlideTransition(direction="right")
            self.manager.current = 'login'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Tela_Login(name='login'))
        sm.add_widget(Tela_Cadastro(name='cadastro'))
        return sm

if __name__ == '__main__':
    MyApp().run()
