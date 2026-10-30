import json
import os

class RepositorioJSON:
    def __init__(self, archivo: str = 'solicitudes_db.json'):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            self._guardar_todo([])

    def _leer_todo(self):
        with open(self.archivo, 'r') as file:
            return json.load(file)

    def _guardar_todo(self, data):
        with open(self.archivo, 'w') as file:
            json.dump(data, file, indent=4)

    def guardar(self, solicitud_dict):
        data = self._leer_todo()
        for i, req in enumerate(data):
            if req['id'] == solicitud_dict['id']:
                data[i] = solicitud_dict
                self._guardar_todo(data)
                return
        data.append(solicitud_dict)
        self._guardar_todo(data)

    def obtener_todas(self):
        return self._leer_todo()