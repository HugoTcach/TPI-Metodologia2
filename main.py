import json
import random

class GeneradorReportes:
    def imprimir_resumen(self, solicitudes):
        # Feature Envy: Accede directamente a las claves del diccionario ajeno
        print("--- REPORTE DE SOLICITUDES ---")
        for solicitud in solicitudes:
            if solicitud['estado'] != "RECHAZADA":
                print(f"ID: {solicitud['id']} | Alumno: {solicitud['nombre']} {solicitud['apellido']} | Estado: {solicitud['estado']}")

class GestorSolicitudes:
    # God Class: Maneja persistencia, validaciones, I/O de consola y reglas de negocio
    
    def registrar_solicitud(self, dni, nombre, apellido, email, tipo, descripcion, prioridad):
        # Long Method y Long Parameter List
        if len(dni) < 7:
            print("Error: DNI inválido.")
            return
        if "@" not in email:
            print("Error: Email inválido.")
            return
        if len(descripcion) > 500:
            print("Error: Descripción muy larga.")
            return
        
        # Magic Numbers (prioridad > 3)
        if prioridad > 3:
            print("Prioridad máxima excedida.")
            return
            
        nuevo_id = random.randint(1000, 9999)
        nueva_solicitud = {
            "id": nuevo_id,
            "dni": dni,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "tipo": tipo,
            "descripcion": descripcion,
            "prioridad": prioridad,
            "estado": "PENDIENTE", # Primitive Obsession
            "responsable": None
        }
        
        # Duplicated Code y Shotgun Surgery (hardcodeo de solicitudes_db.json)
        try:
            with open('solicitudes_db.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
            
        data.append(nueva_solicitud)
        
        with open('solicitudes_db.json', 'w') as file:
            json.dump(data, file, indent=4)
            
        print(f"Solicitud {nuevo_id} registrada con éxito.")

    def cambiar_estado(self, id_solicitud, nuevo_estado):
        # Duplicated Code
        try:
            with open('solicitudes_db.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
            
        encontrada = False
        for req in data:
            if req['id'] == id_solicitud:
                # Magic Strings
                if req['estado'] == "RECHAZADA":
                    print("No se puede revivir una solicitud rechazada.")
                    return
                req['estado'] = nuevo_estado
                encontrada = True
                break
                
        if encontrada:
            # Duplicated Code
            with open('solicitudes_db.json', 'w') as file:
                json.dump(data, file, indent=4)
            print("Estado actualizado.")
        else:
            print("Solicitud no encontrada.")

if __name__ == "__main__":
    gestor = GestorSolicitudes()
    gestor.registrar_solicitud("32111222", "Mateo", "Serafini", "mateo@test.com", "Equivalencia", "Solicito equivalencia MS1", 1)