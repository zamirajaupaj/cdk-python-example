#!/usr/bin/env python3

from aws_cdk import core

from cdk_python_example.cdk_python_example_stack import CdkPythonExampleStack
from cdk-python-example.network.vpc import VPC


app = core.App()
CdkPythonExampleStack(app, "cdk-python-example")

app.synth()
