from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class PasswordlessProblemDetails:
    type: str
    title: str
    status: int
    detail: Optional[str] = None
    instance: Optional[str] = None
    error_code = Optional[None]
    errors: Optional[Dict[str, List[str]]] = field(default_factory=dict)


class PasswordlessError(Exception):
    def __init__(self, problem_details):
        self.problem_details = problem_details

    def __str__(self):
        return self.problem_details.__str__()
