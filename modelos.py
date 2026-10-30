from enum import Enum
from dataclasses import dataclass

class EstadoSolicitud(Enum):
    PENDIENTE = "PENDIENTE"
    EN_PROCESO = "EN_PROCESO"
    RESUELTA = "RESUELTA"
    RECHAZADA = "RECHAZADA"

@dataclass
class SolicitudRequest:
    dni: str
    nombre: str
    apellido: str
    email: str
    tipo: str
    descripcion: str
    prioridad: int

class Solicitud:
    def __init__(self, id_solicitud: int, request: SolicitudRequest, estado: EstadoSolicitud = EstadoSolicitud.PENDIENTE):
        self.id = id_solicitud
        self.request = request
        self.estado = estado

    def obtener_resumen(self) -> str:
        return f"ID: {self.id} | Alumno: {self.request.nombre} {self.request.apellido} | Estado: {self.estado.value}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "dni": self.request.dni,
            "nombre": self.request.nombre,
            "apellido": self.request.apellido,
            "email": self.request.email,
            "tipo": self.request.tipo,
            "descripcion": self.request.descripcion,
            "prioridad": self.request.prioridad,
            "estado": self.estado.value
        }