import os
from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    core,
)


class LambdaCognitoAadOidcAuthStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Ensure the Cognito ARN is set
        cognito_arn = os.environ.get('COGNITO_ARN')
        if cognito_arn is None:
            raise ValueError(
                'An environment variable for COGNITO_ARN is required')

        # Deploy Lambda
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='hello.handler',
        )

        # create the API gateway
        api = apigw.RestApi(
            self,
            'HelloHandler2',
            rest_api_name="LCAOA_Demo",
            description="Demo of lambda, cognito, Azure AD and OpenId auth"
        )

        # configure the Authorizer
        auth = apigw.CfnAuthorizer(
            scope=self,
            id='cognito_authorizer',
            rest_api_id=api.rest_api_id,
            name='MyAuth',
            type='COGNITO_USER_POOLS',
            identity_source='method.request.header.Authorization',
            provider_arns=[
                cognito_arn
            ]
        )
        resource = api.root.add_resource("endpoint")
        lambda_integration = apigw.LambdaIntegration(
            my_lambda, proxy=True)
        method = resource.add_method("GET", lambda_integration)
        method_resource = method.node.find_child('Resource')
        method_resource.add_property_override(
            'AuthorizationType', 'COGNITO_USER_POOLS')
        method_resource.add_property_override(
            'AuthorizerId', {"Ref": auth.logical_id})
