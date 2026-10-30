import random
from modelos import SolicitudRequest, Solicitud, EstadoSolicitud
from repositorio import RepositorioJSON

class EstadoInvalidoError(Exception):
    pass

class SolicitudService:
    def __init__(self, repositorio: RepositorioJSON):
        self.repositorio = repositorio

    def registrar_solicitud(self, datos: SolicitudRequest) -> int:
        self._validar_datos_estudiante(datos)
        self._validar_reglas_negocio(datos)
        
        nuevo_id = self._generar_nuevo_id()
        nueva_solicitud = Solicitud(nuevo_id, datos)
        
        self.repositorio.guardar(nueva_solicitud.to_dict())
        return nuevo_id

    def _validar_datos_estudiante(self, datos: SolicitudRequest):
        if len(datos.dni) < 7:
            raise ValueError("DNI inválido.")
        if "@" not in datos.email:
            raise ValueError("Email inválido.")

    def _validar_reglas_negocio(self, datos: SolicitudRequest):
        if len(datos.descripcion) > 500:
            raise ValueError("Descripción muy larga.")
        if datos.prioridad > 3:
            raise ValueError("Prioridad máxima excedida.")

    def _generar_nuevo_id(self) -> int:
        return random.randint(1000, 9999)

    def cambiar_estado(self, id_solicitud: int, nuevo_estado: EstadoSolicitud):
        data = self.repositorio.obtener_todas()
        encontrada = False
        for req in data:
            if req['id'] == id_solicitud:
                if req['estado'] == EstadoSolicitud.RECHAZADA.value:
                    raise EstadoInvalidoError("No se puede revivir una solicitud rechazada.")
                req['estado'] = nuevo_estado.value
                self.repositorio.guardar(req)
                encontrada = True
                break
        
        if not encontrada:
            raise ValueError("Solicitud no encontrada.")