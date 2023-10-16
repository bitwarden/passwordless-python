from dataclasses import dataclass, field
from typing import Dict, List, Optional


def passwordless_problem_details_errors_factory() -> (
    Optional[Dict[str, List[str]]]
):
    return dict()


@dataclass
class PasswordlessProblemDetails:
    """Problem details for Passwordless Api.

    See Passwordless Docs Errors:
    https://docs.passwordless.dev/guide/errors.html#problem-details
    """

    type: str
    title: str
    status: int
    detail: Optional[str] = None
    instance: Optional[str] = None
    error_code: Optional[str] = None
    errors: Optional[Dict[str, List[str]]] = field(
        default_factory=passwordless_problem_details_errors_factory
    )


class PasswordlessError(Exception):
    """Thrown when Passwordless API returns an error during the
    `PasswordlessClient` method execution.

    Access the problem details with `problem_details` field.
    """

    def __init__(self, problem_details: PasswordlessProblemDetails):
        self.problem_details = problem_details

    def __str__(self) -> str:
        return self.problem_details.__str__()
