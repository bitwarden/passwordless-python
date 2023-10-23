"""The official Bitwarden Passwordless.dev Python library for Python
3+."""

__version__ = "0.0.1"

from .client import PasswordlessClient, PasswordlessClientBuilder
from .config import PasswordlessOptions
from .errors import PasswordlessError, PasswordlessProblemDetails
from .models import (
    Alias,
    Credential,
    CredentialDescriptor,
    DeleteCredential,
    DeleteUser,
    RegisteredToken,
    RegisterToken,
    SetAlias,
    UpdateAppsFeature,
    UserSummary,
    VerifiedUser,
    VerifySignIn,
)
from .serialization import (
    AliasSchema,
    CredentialDescriptorSchema,
    CredentialSchema,
    DeleteCredentialSchema,
    DeleteUserSchema,
    PasswordlessProblemDetailsSchema,
    RegisteredTokenSchema,
    RegisterTokenSchema,
    SetAliasSchema,
    UpdateAppsFeatureSchema,
    UserSummarySchema,
    VerifiedUserSchema,
    VerifySignInSchema,
)
