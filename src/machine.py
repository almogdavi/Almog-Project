from typing import Literal
from pydantic import BaseModel


class Computer(BaseModel):
    system: Literal["windows", "mac", "linux"]
    gpu: Literal["nvidia", "intel"]
    ram: Literal[4, 8, 12, 16, 32, 64]
    cpu: Literal[2, 4, 8, 10, 12]
  