import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class CreateAlias:
    user_id: str
    aliases: List[str]
    hashing: bool = True


@dataclass
class UserSummary:
    user_id: str
    alias_count: int
    aliases: List[str]
    credentials_count: int
    last_used_at: datetime.datetime


@dataclass
class Alias:
    user_id: str
    alias: str
    plaintext: str
    tenant: str


@dataclass
class ListResponse:
    values: List[UserSummary | Alias]

@dataclass
class UpdateAppsFeature:
    audit_logging_retention_period: int
