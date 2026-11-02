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
   price: float
   date_valid: str
   location: str = "LOJA"
   status: str = "NORMAL"

   def __str__(self) -> str:
     """Define como a entidade se transforma em texto para a tabela."""
     return f"{self.lot_id:<6} | {self.product_name:<50} | {self.product_id:<8} | {self.quant:<6} | R${self.price:<6.2f} | {self.date_valid:<10}"