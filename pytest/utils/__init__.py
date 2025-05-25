from dataclasses import dataclass


@dataclass(frozen=True)
class AccountInfo:
    email: str
    password: str
    

