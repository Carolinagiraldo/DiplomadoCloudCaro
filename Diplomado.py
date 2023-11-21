import boto3

print("SI")

    
#crear funcion para listar tablas de dynamobd
def listar_tablas():
    dynamodb = boto3.resource('dynamodb')
    for table in dynamodb.tables.all():
        print(table.name)
        
#crear funcion para crear tabla de dynamodb con capacidad para bajo demanda
def crear_tabla_dynamodb(nombre_tabla):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName=nombre_tabla,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST',
        
    )
    print("Tabla creada exitosamente")
     
        
opcion = 1 

while opcion != 0:
    print("ingrese la opcion que desea")
    print("1. listar tabla de dynamobd de la cuenta")
    print("2. crear nueva tabla")
    print("0. salir")
    opcion = int(input())
    
    if opcion == 1:
        listar_tablas()
    elif opcion == 2:
        nombre_tabla = input("Ingrese el nombre de la tabla: ")
        crear_tabla_dynamodb(nombre_tabla)
    elif opcion == 0:
        print("hasta luego")
    else:
        print("Opcion no valida")
        

