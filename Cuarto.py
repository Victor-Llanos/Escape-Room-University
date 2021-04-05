import requests

api = requests.get("https://api-escapamet.vercel.app")

class Cuarto:
    def __init__(self,cuarto):
        self.cuarto = api.json()[cuarto]         #clase usada unicamente para enviar a las hijas su ubicacion y su nombre
        self.name = api.json()[cuarto]["name"]
