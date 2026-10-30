from modelos import SolicitudRequest, EstadoSolicitud, Solicitud
from repositorio import RepositorioJSON
from servicio import SolicitudService, EstadoInvalidoError

class InterfazConsola:
    def __init__(self):
        self.repositorio = RepositorioJSON()
        self.servicio = SolicitudService(self.repositorio)

    def ejecutar_alta(self):
        print("--- ALTA DE SOLICITUD ---")
        try:
            datos = SolicitudRequest(
                dni="32111222",
                nombre="Mateo",
                apellido="Serafini",
                email="mateo@test.com",
                tipo="Equivalencia",
                descripcion="Solicito equivalencia MS1",
                prioridad=1
            )
            nuevo_id = self.servicio.registrar_solicitud(datos)
            print(f"Solicitud {nuevo_id} registrada con éxito.")
        except ValueError as e:
            print(f"Error de validación: {e}")

    def imprimir_reporte(self):
        print("--- REPORTE DE SOLICITUDES ---")
        data = self.repositorio.obtener_todas()
        for req_dict in data:
            req_datos = SolicitudRequest(
                req_dict['dni'], req_dict['nombre'], req_dict['apellido'], 
                req_dict['email'], req_dict['tipo'], req_dict['descripcion'], req_dict['prioridad']
            )
            solicitud = Solicitud(req_dict['id'], req_datos, EstadoSolicitud(req_dict['estado']))
            print(solicitud.obtener_resumen())

if __name__ == "__main__":
    app = InterfazConsola()
    app.ejecutar_alta()
    app.imprimir_reporte()