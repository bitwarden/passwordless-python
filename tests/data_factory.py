from dateutil import parser

from passwordless import (
    Alias,
    Credential,
    CredentialDescriptor,
    DeleteCredential,
    DeleteUser,
    PasswordlessOptions,
    PasswordlessProblemDetails,
    RegisteredToken,
    RegisterToken,
    SendMagicLinkRequest,
    SetAlias,
    UpdateAppsFeature,
    UserSummary,
    VerifiedUser,
    VerifySignIn,
)

USER_ID = "eb4dee07-2d05-404e-80ed-0f65d0c4e30e"
SECRET = "app:secret:34286d0b2cb24b8687d1639d20eb29fa"


def build_passwordless_options(url: str):
    return PasswordlessOptions(SECRET, url)


def build_passwordless_problem_details_invalid_token():
    return PasswordlessProblemDetails(
        type="https://docs.passwordless.dev/guide/errors.html#invalid_token",
        title="The token you sent was not correct. The token used for this "
        "endpoint should start with 'verify_'. Make sure you are not "
        "sending the wrong value. The value you sent started with 'x'",
        status=400,
        detail="Makes sure your request contains the expected a value for the "
        "token.",
        instance="/some/api",
        error_code="invalid_token",
    )


def build_set_alias():
    return SetAlias(USER_ID, ["TestUser1", "TestUser2"])


def build_alias_1():
    return Alias(
        user_id=USER_ID,
        alias="xCsgbuTXbvoIhdyD7B2QSKkhWip8Y2zMRVA20sj+ihA=",
        tenant="app",
    )


def build_alias_2():
    return Alias(
        user_id=USER_ID,
        alias="Yn3R4Gra0U7nr0vGEsHQVxHqpKZKgbchWQ1IoM8Snwk=",
        tenant="app",
    )


def build_update_apps_feature():
    return UpdateAppsFeature(12)


def build_delete_credential():
    return DeleteCredential("ZtmCjN6tOMM5X_KxfYApAHI-5n6C4KRy9YMeMqfNjj8")


def build_credential_1():
    return Credential(
        user_id=USER_ID,
        descriptor=CredentialDescriptor(
            type="public-key", id="ZtmCjN6tOMM5X_KxfYApAHI-5n6C4KRy9YMeMqfNjj8"
        ),
        public_key="pQECAyYgASFYIOsfC6kHh3pBohSGE6WwwGo8rJYG2lgmSbBfgtIq1gJzI"
        "lggr/6DYuFeATzcucHJ2ejCF2qWH7Z43yK4z/UYAV9YrY4=",
        user_handle="ZWI0ZGVlMDctMmQwNS00MDRlLTgwZWQtMGY2NWQwYzRlMzBl",
        signature_counter=2,
        attestation_fmt="none",
        created_at=parser.parse("2023-09-09T20:05:03.6059728Z"),
        aa_guid="00000000-0000-0000-0000-000000000000",
        last_user_at=parser.parse("2023-09-09T20:09:59.6593325Z"),
        origin="http://localhost:8080",
        country="PL",
        device="Chrome, Mac OS X 10",
        rp_id="rp_id",
    )


def build_credential_2():
    return Credential(
        user_id=USER_ID,
        descriptor=CredentialDescriptor(
            type="public-key", id="CYdwzAHqmUr85Dpei2kbWHs9xsBp1clzbG09VUcfnS0"
        ),
        public_key="pQECAyYgASFYIHSn0S/oH/sgZx12v37duci9gDkg0bB4f25h8p+6ecq2I"
        "lgg2RadGaGqyJpNtm9ETrg+Uinf5n8SdPZN0oibSWb6TDc=",
        user_handle="ODU5YTIyZTAtYmVmYS00ZWY0LWFjNDktNTRlZDkwYzFkZWIy",
        signature_counter=1,
        attestation_fmt="none",
        created_at=parser.parse("2023-09-09T21:18:00.1309909Z"),
        aa_guid="00000000-0000-0000-0000-000000000000",
        last_user_at=parser.parse("2023-09-09T21:32:50.2848782Z"),
        origin="http://localhost:8080",
        country="PL",
        device="Chrome, Mac OS X 10",
        rp_id="rp_id",
    )


def build_register_token():
    return RegisterToken(
        user_id=USER_ID,
        username="TestUser",
        attestation="none",
        authenticator_type="any",
        discoverable=True,
        user_verification="preferred",
        aliases=[],
        alias_hashing=True,
        expires_at=parser.parse("2023-09-09T20:07:02.365573Z"),
    )


def build_register_token_without_expires_at():
    return RegisterToken(
        user_id=USER_ID,
        username="TestUser",
        attestation="none",
        authenticator_type="any",
        discoverable=True,
        user_verification="preferred",
        aliases=[],
        alias_hashing=True,
    )


def build_registered_token():
    return RegisteredToken(
        "register_k8QgFOUhu_arMUbfi_93OZFdc6M39tPdmmNbx5xF"
        "ZlMUS_TEgdwAE9f_VyjOIGT80GbZJDAwMDAwMDAwLTAwMDAtM"
        "DAwMC0wMDAwLTAwMDAwMDAwMDAwMMDAwMDAwMDA2SRlYjRkZW"
        "UwNy0yZDA1LTQwNGUtODBlZC0wZjY1ZDBjNGUzMGXAqFRlc3R"
        "Vc2VypG5vbmWjYW55w6lwcmVmZXJyZWSQw84VNwZS"
    )


def build_verify_sign_in():
    return VerifySignIn(
        "verify_k8QgiPlgfMVr34FyFipBrkj6jBwKT9QifsFx-DSa1L3Yp"
        "_PE1NwAE9f_ppPH0GT80Y_ZJDBlZGQ2NWJjLTliOGQtNGIxYS1iM"
        "jA4LTIxYzZjOGYxYWQ5NK5wYXNza2V5X3NpZ25pbsDAwMDAwMDZJ"
        "GViNGRlZTA3LTJkMDUtNDA0ZS04MGVkLTBmNjVkMGM0ZTMwZdf_p"
        "pOx8GT80RepbG9jYWxob3N0tWh0dHA6Ly9sb2NhbGhvc3Q6ODA4M"
        "MOzQ2hyb21lLCBNYWMgT1MgWCAxMKJQTMDEIGbZgozerTjDOV_ys"
        "X2AKQByPuZ-guCkcvWDHjKnzY4_zhU3BlI"
    )


def build_verified_user():
    return VerifiedUser(
        success=True,
        user_id=USER_ID,
        timestamp=parser.parse("2023-09-09T20:09:59.698674300Z"),
        origin="http://localhost:8080",
        device="Chrome, Mac OS X 10",
        country="PL",
        credential_id="ZtmCjN6tOMM5X/KxfYApAHI+5n6C4KRy9YMeMqfNjj8=",
        expires_at=parser.parse("2023-09-09T20:11:59.698675700Z"),
        token_id="0edd65bc-9b8d-4b1a-b208-21c6c8f1ad94",
        type="passkey_signin",
        rp_id="rp_id",
        nickname="nickname",
    )


def build_user_summary_1():
    return UserSummary(
        user_id=USER_ID,
        alias_count=2,
        aliases=[None, None],
        credentials_count=1,
        last_used_at=parser.parse("2023-09-09T20:09:59.6593325Z"),
    )


def build_user_summary_2():
    return UserSummary(
        user_id="859a22e0-befa-4ef4-ac49-54ed90c1deb2",
        alias_count=1,
        aliases=["TestUser2"],
        credentials_count=1,
        last_used_at=parser.parse("2023-09-09T21:09:59.6593325Z"),
    )


def build_delete_user():
    return DeleteUser(USER_ID)

def build_send_magic_link_request_1():
    return SendMagicLinkRequest(
        email_address="support@passwordless.dev",
        url_template="https://www.example.com?token=$TOKEN",
        user_id="859a22e0-befa-4ef4-ac49-54ed90c1deb2",
    )

def build_send_magic_link_request_2():
    return SendMagicLinkRequest(
        email_address="support@passwordless.dev",
        url_template="https://www.example.com?token=$TOKEN",
        user_id="859a22e0-befa-4ef4-ac49-54ed90c1deb2",
        time_to_live=24
    )