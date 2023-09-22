import logging

from marshmallow import Schema, fields, post_load

from src.passwordless.errors import PasswordlessProblemDetails
from src.passwordless.models import UserSummary, ListResponse


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


class CreateAliasSchema(Schema):
    user_id = fields.Str(data_key='userId')
    aliases = fields.List(fields.Str())
    hashing = fields.Bool()


class UserSummarySchema(Schema):
    user_id = fields.Str(data_key='userId')
    alias_count = fields.Int(data_key='aliasCount')
    aliases = fields.List(fields.Str(allow_none=True), allow_none=True)
    credentials_count = fields.Int(data_key='credentialsCount')
    last_used_at = fields.DateTime(data_key='lastUsedAt')

    @post_load
    def make(self, data, **kwargs):
        return UserSummary(**data)


class UserSummaryListResponseSchema(Schema):
    values = fields.List(fields.Nested(UserSummarySchema()))

    @post_load
    def make(self, data, **kwargs):
        return ListResponse(**data)


class AliasSchema(Schema):
    user_id = fields.Str(data_key='userId')
    alias = fields.Str()
    plaintext = fields.Str(allow_none=True)
    tenant = fields.Str()


class AliasListResponseSchema(Schema):
    values = fields.List(fields.Nested(AliasSchema()))

    @post_load
    def make(self, data, **kwargs):
        return ListResponse(**data)


class UpdateAppsFeatureSchema(Schema):
    audit_logging_retention_period = fields.Int(data_key='auditLoggingRetentionPeriod')
