from marshmallow import Schema, fields, post_load, EXCLUDE

from .errors import PasswordlessProblemDetails
from .models import UserSummary, ListResponse, Alias, CredentialDescriptor, Credential, VerifiedUser, \
    RegisteredToken


class PasswordlessProblemDetailsSchema(Schema):
    type = fields.Str()
    title = fields.Str()
    status = fields.Int()
    detail = fields.Str(required=False)
    instance = fields.Str(required=False)
    error_code = fields.Str(required=False)
    errors = fields.Dict(fields.Str(), fields.List(fields.Str()), required=False)

    @post_load
    def make(self, data, **kwargs):
        return PasswordlessProblemDetails(**data)

    class Meta:
        unknown = EXCLUDE


class CreateAliasSchema(Schema):
    user_id = fields.Str(data_key='userId')
    aliases = fields.List(fields.Str())
    hashing = fields.Bool()

    class Meta:
        unknown = EXCLUDE


class AliasSchema(Schema):
    user_id = fields.Str(data_key='userId')
    alias = fields.Str()
    plaintext = fields.Str(allow_none=True)
    tenant = fields.Str()

    @post_load
    def make(self, data, **kwargs):
        return Alias(**data)

    class Meta:
        unknown = EXCLUDE


class AliasListResponseSchema(Schema):
    values = fields.List(fields.Nested(AliasSchema()))

    @post_load
    def make(self, data, **kwargs):
        return ListResponse(**data)

    class Meta:
        unknown = EXCLUDE


class UpdateAppsFeatureSchema(Schema):
    audit_logging_retention_period = fields.Int(data_key='auditLoggingRetentionPeriod')

    class Meta:
        unknown = EXCLUDE


class DeleteCredentialSchema(Schema):
    credential_id = fields.Str(data_key='credentialId')

    class Meta:
        unknown = EXCLUDE


class CredentialDescriptorSchema(Schema):
    type = fields.Str()
    id = fields.Str()
    transports = fields.List(fields.Str(), required=False)

    @post_load
    def make(self, data, **kwargs):
        return CredentialDescriptor(**data)

    class Meta:
        unknown = EXCLUDE


class CredentialSchema(Schema):
    descriptor = fields.Nested(CredentialDescriptorSchema())
    public_key = fields.Str(data_key='publicKey')
    user_handle = fields.Str(data_key='userHandle')
    signature_counter = fields.Int(data_key='signatureCounter')
    attestation_fmt = fields.Str(data_key='attestationFmt')
    created_at = fields.DateTime(data_key='createdAt')
    aa_guid = fields.Str(data_key='aaGuid')
    last_user_at = fields.DateTime(data_key='lastUsedAt')
    rp_id = fields.Str(data_key='rpid')
    origin = fields.Str()
    country = fields.Str()
    device = fields.Str()
    user_id = fields.Str(data_key='userId')

    @post_load
    def make(self, data, **kwargs):
        return Credential(**data)

    class Meta:
        unknown = EXCLUDE


class CredentialListResponseSchema(Schema):
    values = fields.List(fields.Nested(CredentialSchema()))

    @post_load
    def make(self, data, **kwargs):
        return ListResponse(**data)

    class Meta:
        unknown = EXCLUDE


class RegisterTokenSchema(Schema):
    user_id = fields.Str(data_key='userId')
    username = fields.Str()
    display_name = fields.Str(data_key='displayName')
    attestation = fields.Str()
    authenticator_type = fields.Str(data_key='authenticatorType')
    discoverable = fields.Bool()
    user_verification = fields.Str(data_key='userVerification')
    aliases = fields.List(fields.Str())
    alias_hashing = fields.Bool(data_key='aliasHashing')
    expires_at = fields.DateTime(data_key='expiresAt')

    class Meta:
        unknown = EXCLUDE


class RegisteredTokenSchema(Schema):
    token = fields.Str()

    @post_load
    def make(self, data, **kwargs):
        return RegisteredToken(**data)

    class Meta:
        unknown = EXCLUDE


class VerifySignInSchema(Schema):
    token = fields.Str()

    class Meta:
        unknown = EXCLUDE


class VerifiedUserSchema(Schema):
    success = fields.Bool()
    user_id = fields.Str(data_key='userId')
    timestamp = fields.DateTime()
    rp_id = fields.Str(data_key='rpid')
    origin = fields.Str()
    device = fields.Str()
    country = fields.Str()
    nickname = fields.Str()
    credential_id = fields.Str(data_key='credentialId')
    expires_at = fields.DateTime(data_key='expiresAt')
    token_id = fields.Str(data_key='tokenId')
    type = fields.Str()

    @post_load
    def make(self, data, **kwargs):
        return VerifiedUser(**data)

    class Meta:
        unknown = EXCLUDE


class UserSummarySchema(Schema):
    user_id = fields.Str(data_key='userId')
    alias_count = fields.Int(data_key='aliasCount')
    aliases = fields.List(fields.Str(allow_none=True), allow_none=True)
    credentials_count = fields.Int(data_key='credentialsCount')
    last_used_at = fields.DateTime(data_key='lastUsedAt')

    @post_load
    def make(self, data, **kwargs):
        return UserSummary(**data)

    class Meta:
        unknown = EXCLUDE


class UserSummaryListResponseSchema(Schema):
    values = fields.List(fields.Nested(UserSummarySchema()))

    @post_load
    def make(self, data, **kwargs):
        return ListResponse(**data)

    class Meta:
        unknown = EXCLUDE


class DeleteUserSchema(Schema):
    user_id = fields.Str(data_key='userId')
