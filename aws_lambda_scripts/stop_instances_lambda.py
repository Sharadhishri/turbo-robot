import boto3

client = boto3.client('ec2')

def stop_ec2_handler(event, context):
   response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:name',
            'Values': [
                'expensive-ec2',
            ]
        },
    ]
   )
   
   for reservation in response["Reservations"]:
      for instance in reservation["Instances"]:
         instance_id = [instance['InstanceId']]
         client.stop_instances(InstanceIds=instance_id)     
         print(instance_id,  ' stopped')
         
   return "Completed."         
