#!/usr/bin/env python3

from aws_cdk import core

from lambda_cognito_aad_oidc_auth.lambda_cognito_aad_oidc_auth_stack import LambdaCognitoAadOidcAuthStack


app = core.App()
LambdaCognitoAadOidcAuthStack(app, "lambda-cognito-aad-oidc-auth")

app.synth()
