from dataclasses import dataclass
from typing import Optional

@dataclass
class Product:
   name: str
   price: float
   id: Optional[int] = None
   bar_code: Optional[str] = None

@dataclass
class Lot:
   product_id: int
   quant: int
   date_valid: str
   id: Optional[int] = None
   location: str = "LOJA"
   status: str = "NORMAL"
   price: Optional[float] = None # Reservado para ativação futura em preço de Lote

@dataclass
class LotEntity:
   lot_id: int
   product_name: str
   product_id: int
   quant: int
   price: int
   date_valid: str
   location: str = "LOJA"
   status: str = "NORMAL"