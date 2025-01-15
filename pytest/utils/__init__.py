from dataclasses import dataclass


@dataclass(frozen=True)
class AccountInfo:
    email: str
    password: str
    

ManagerAccount = AccountInfo(email="lingze_m@ip8value.com", password="lingze")
InventorAccount = AccountInfo(email="lingze_v@ip8value.com", password="123")
