#!/usr/bin/env python3

from aws_cdk import core

from test.test_stack import TestStack


app = core.App()
TestStack(app, "test", env={'region': 'us-west-2'})

app.synth()
