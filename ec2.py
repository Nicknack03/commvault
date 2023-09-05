import boto3


region = 'us-east-1' 
ami_id = 'ami-0123456789abcdef0' 
instance_type = 't2.micro'

ec2 = boto3.client('ec2', region_name=region)


response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    MinCount=1,
    MaxCount=1,
    KeyName='your-key-pair-name',  
    SecurityGroupIds=['your-security-group-id'],  
    SubnetId='your-subnet-id'  
)


instance_id = response['Instances'][0]['InstanceId']


waiter = ec2.get_waiter('instance_running')
waiter.wait(InstanceIds=[instance_id])

ec2.associate_address(InstanceId=instance_id)

print(f"EC2 instance {instance_id} is running with a public IP address.")
