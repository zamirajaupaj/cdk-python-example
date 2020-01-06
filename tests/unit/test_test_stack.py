import json
import pytest

from aws_cdk import core
from test.test_stack import TestStack


def get_template():
    app = core.App()
    TestStack(app, "test")
    return json.dumps(app.synth().get_stack("test").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
