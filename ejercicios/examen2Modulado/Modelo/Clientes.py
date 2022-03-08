
from dataclasses import dataclass

@dataclass
class Clientes:
    numero_cliente: int
    nome_cliente: str
    apellido_cliente: str
    telefono: int
    direccion: str
    cidade: str
    provinciaEstado: str
    codigo_postal: int
    pais: str
    axente_comercial: str
