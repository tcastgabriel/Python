import PySimpleGUI as sg

#Layout
sg.theme('Topanga')
Layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#Janela
Janela = sg.Window('Tela de Login', Layout)
#Ler os eventos
while True:
    eventos, valores = Janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Gabriel' and valores['senha'] == '123456789':
            print('Wellcome my friend')