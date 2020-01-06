from aws_cdk import (
    core,
    aws_ec2 as ec2
)

class VPC(core.Stack):

    def __init__(
        self, 
        scope: core.Construct,
        id: str,
        **kwargs) -> None:
        super().__init__(scope, id, **kwargs
    )
            vpc = ec2.Vpc(
            self, 'Vpc',
            # cidr=config['cidr_block'],
            cidr='10.0.0.0/16',
            max_azs=99,
            subnet_configuration = [ 
                { 
                    cidrMask: 24,
                    name: ‘ingress’,
                    subnetType: SubnetType.PUBLIC,
                },
                { 
                    cidrMask: 24,
                    name: ‘application’,
                    subnetType: SubnetType.PRIVATE 
                },
                { 
                    cidrMask: 28, 
                    name: ‘rds’, 
                    subnetType: SubnetType.ISOLATED
                } 
            ]
        )

