import json
import boto3

def lambda_handler(event, context):
    # Exemplo de log do evento (quando um arquivo é carregado no S3)
    print("Evento recebido:", json.dumps(event, indent=2))
    return {
        'statusCode': 200,
        'body': json.dumps('Função Lambda executada com sucesso!')
    }
