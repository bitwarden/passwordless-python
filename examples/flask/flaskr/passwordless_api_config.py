from dataclasses import dataclass


@dataclass
class PasswordlessApiConfig:
    url: str
    key: str
    secret: str
