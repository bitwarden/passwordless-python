from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")
STR_OR_NONE = TypeVar("STR_OR_NONE", str, None)


@dataclass
class SetAlias:
    user_id: str
    aliases: List[str]
    hashing: bool = True


@dataclass
class Alias:
    user_id: str
    alias: str
    tenant: str
    plaintext: Optional[str] = None


@dataclass
class ListResponse(Generic[T]):
    values: List[T]


@dataclass
class UpdateAppsFeature:
    audit_logging_retention_period: int


@dataclass
class DeleteCredential:
    credential_id: str


@dataclass
class CredentialDescriptor:
    type: str
    """Base64 encoded credential descriptor id."""
    id: str
    transports: Optional[List[str]] = None


@dataclass
class Credential:
    descriptor: CredentialDescriptor
    """Base64 encoded public key."""
    public_key: str
    """Base64 encoded user handle."""
    user_handle: str
    signature_counter: int
    attestation_fmt: str
    created_at: datetime
    aa_guid: str
    last_user_at: datetime
    rp_id: str
    origin: str
    country: str
    device: str
    user_id: str


@dataclass
class RegisterToken:
    user_id: str
    username: str
    display_name: Optional[str] = None
    attestation: str = "none"
    authenticator_type: str = "any"
    discoverable: bool = True
    user_verification: str = "preferred"
    aliases: List[str] = field(default_factory=list)
    alias_hashing: bool = True
    expires_at: datetime = field(
        default_factory=lambda: datetime.utcnow() + timedelta(minutes=2)
    )


@dataclass
class RegisteredToken:
    token: str


@dataclass
class VerifySignIn:
    token: str


@dataclass
class VerifiedUser:
    success: bool
    user_id: str
    timestamp: datetime
    origin: str
    device: str
    country: str
    nickname: str
    """Base64 encoded credential id."""
    credential_id: str
    expires_at: datetime
    token_id: str
    type: str
    rp_id: Optional[str] = None


@dataclass
class UserSummary(Generic[STR_OR_NONE]):
    user_id: str
    alias_count: int
    aliases: List[STR_OR_NONE]
    credentials_count: int
    last_used_at: datetime


@dataclass
class DeleteUser:
    user_id: str


@dataclass
class SendMagicLinkOptions:
    email_address: str
    url_template: str
    user_id: str
    time_to_live: Optional[int] = None


@dataclass
class GenerateAuthenticationTokenOptions:
    user_id: str
    time_to_live: Optional[int] = None


@dataclass
class GeneratedAuthenticationToken:
    token: str
