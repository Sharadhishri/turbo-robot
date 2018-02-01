import boto3

client = boto3.client('ec2')

def terminate_ec2_handler(event, context):
   response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:name',
            'Values': [
                'unused-instances',
            ]
        },
    ]
   )
   
   for reservation in response["Reservations"]:
      for instance in reservation["Instances"]:
         instance_id = [instance['InstanceId']]
         client.terminate_instances(InstanceIds=instance_id)     
         print(instance_id,  ' terminated')
         
   return "Completed." 
