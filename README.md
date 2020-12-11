
# Lambda, Cognito, Azure AD, OpenId Connect Demo

This project offers a demo of how to leverage the following tools for API and web app authentication:
 - AWS Lambda
 - AWS Cognito
 - Azure Active Directory 
 - OpenId Connect

The Lambda is developed in Python and deployed via the AWS CDK.

# CDK

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

# Prerequisits 
You will need to create your Cognito User Pool and configure the federation to Azure AD.  I recommend the following article to help you:
https://dev.to/danielbayerlein/how-to-use-azure-ad-b2c-as-idp-for-amazon-cognito-28nj

You will need to define the Cognito ARN (replace with your ARN)
```bash
export COGNITO_ARN='arn:aws:cognito-idp:us-east-1:123456789:userpool/us-east-1_abc123'

