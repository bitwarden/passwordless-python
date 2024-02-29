"""The official Bitwarden Passwordless.dev Python library for Python
3+."""

__version__ = "0.1.1"

from .client import PasswordlessClient, PasswordlessClientBuilder
from .config import PasswordlessOptions
from .errors import PasswordlessError, PasswordlessProblemDetails
from .models import (
    Alias,
    Credential,
    CredentialDescriptor,
    DeleteCredential,
    DeleteUser,
    GenerateAuthenticationTokenOptions,
    GeneratedAuthenticationToken,
    RegisteredToken,
    RegisterToken,
    SendMagicLinkOptions,
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
    GenerateAuthenticationTokenOptionsSchema,
    GeneratedAuthenticationTokenSchema,
    PasswordlessProblemDetailsSchema,
    RegisteredTokenSchema,
    RegisterTokenSchema,
    SendMagicLinkOptionsSchema,
    SetAliasSchema,
    UpdateAppsFeatureSchema,
    UserSummarySchema,
    VerifiedUserSchema,
    VerifySignInSchema,
)
