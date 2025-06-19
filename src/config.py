from dataclasses import dataclass


@dataclass
class Config:
    endpoint: str = "https://www.example.com"
    password: str = "NEVER INCLUDE PASSWORDS OR OTHER SENSITIVE DATA HERE"
