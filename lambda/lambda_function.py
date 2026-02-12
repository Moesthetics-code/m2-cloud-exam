import boto3
import os

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    """
    Fonction Lambda pour stopper une instance EC2.
    L'Instance ID doit être fourni via variable d'environnement INSTANCE_ID.
    """
    
    instance_id = os.environ.get('INSTANCE_ID')
    
    if not instance_id:
        return {
            'statusCode': 400,
            'body': 'ERROR: INSTANCE_ID environment variable not set'
        }
    
    try:
        # Stopper l'instance
        response = ec2.stop_instances(InstanceIds=[instance_id])
        
        print(f" Instance {instance_id} arrêtée avec succès")
        print(f"État: {response['StoppingInstances'][0]['CurrentState']['Name']}")
        
        return {
            'statusCode': 200,
            'body': f"Instance {instance_id} stopped successfully",
            'response': response
        }
        
    except Exception as e:
        print(f" Erreur lors de l'arrêt de l'instance: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }