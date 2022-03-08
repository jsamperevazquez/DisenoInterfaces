from dataclasses import dataclass
from datetime import date

@dataclass
class Ventas:
    numero_albaran: int
    data_albaran: date
    data_entrega: date
    numero_cliente: int