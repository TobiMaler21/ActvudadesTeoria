import csv
import PySimpleGUI as sg
import json 


def Goku (ruta,key):
        """ Recibe como parametro la ruta del archivo, y una key.
            Abre el archivo que esta en la ruta y lo convierte en una lsita de diccionarios.
            Luego los ordena de mayor a menor seguna la key y devuelve la lista ordenada"""    
        arch = open(ruta,'r',encoding = 'utf8')
        data = list(csv.DictReader(arch))
        lista_de_nombres = (sorted(data, key = lambda data: data[key], reverse= True)[:20])
        return lista_de_nombres

def save_nombres (data, key):
        lista = list(map(lambda x: x[key], data))
        with open("file.json", "w") as file:
            json.dump(lista,file, indent=4, ensure_ascii=False)
        
run():
        layout = [[sg.Text('Elija que informacion quiere ver')],
                  [sg.Button(button_text="Top 20 titulos de Netflix con mejor calificacion")],
                  [sg.Button(button_text="Top 10 Apps de Appstore con mejor calificacion")],
                  [sg.Cancel()]]


        window = sg.Window('Activivdad por Python +', layout)

        while True:
            event, values = window.read()
            if event == 'Aplicaciones de Appstore':
                data = Goku('./appstore_games.csv','Average User Rating')
                save_nombres(data,'Name')

            elif event == 'Titulos de Netflix':
                data = Goku('./netflix_titles.csv','rating')
                save_nombres(data,'title')
            elif event == None or 'Cancel':
                break
