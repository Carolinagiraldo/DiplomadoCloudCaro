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
     
    
   #opcion3      
#crear funcion para insertar elemento en tabla de dynamodb
def insertar_elemento_tabla(nombre_tabla, id, nombre, apellido):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    table.put_item(
        Item={
            'id': id,
            'nombre': nombre,
            'apellido': apellido
        }
    )
    print("Elemento insertado exitosamente")
 #opcion 4   
#leer los elementos de una tabla de dynamodb
def leer_elementos_tabla(nombre_tabla):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    response = table.scan()
    items = response['Items']
    for item in items:
        print(item)

#eliminar elementos de una tabla de dynamondb
def eliminar_elemento_tabla(nombre_tabla, id):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    table.delete_item(
        Key={
            'id': id
        }
    )
    print("Elemento eliminado exitosamente")
    
#reconocer celebridad en imagen
def reconocer_celebridad_imagen(imagen):
    rekognition = boto3.client('rekognition')
    response = rekognition.recognize_celebrities(Image={'Bytes': imagen})
    for celebrity in response['CelebrityFaces']:
        print(response['celebrityFaces'][0]['Name'])
        
        
opcion = 1 

while opcion != 0:
    print("ingrese la opcion que desea")
    print("1. listar tabla de dynamobd de la cuenta")
    print("2. crear nueva tabla")
    print("3. insertar elemento en tabla")
    print("4. leer elementos de tabla")
    print("5. eliminar elemento de tabla")
    print("6. reconocer celebridad en imagen")
    print("0. salir")
    opcion = int(input())
    
    if opcion == 1:
        listar_tablas()
    elif opcion == 2:
        nombre_tabla = input("Ingrese el nombre de la tabla: ")
        crear_tabla_dynamodb(nombre_tabla)
    elif opcion == 3:
        nombre_tabla = input("Ingrese el nombre de la tabla: ")
        id = input("Ingrese el id: ")
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        insertar_elemento_tabla(nombre_tabla, id, nombre, apellido)  
    elif opcion == 4:
        nombre_tabla = input("ingrese el nombre ")
        leer_elementos_tabla(nombre_tabla)   
    elif opcion == 5:
        nombre_tabla = input("ingrese el nombre de la tabla")
        id = input("ingrese el id del elementos ")
        eliminar_elemento_tabla(nombre_tabla, id)   
    elif opcion == 6:
       #convertir imagen a bytes
        with open('imagen.jpg', 'rb') as f:     #para insertar la imagen solo en imagen.jpg pongo el nombre de la mia.
            imagen = f.read()
            reconocer_celebridad_imagen(imagen)
    elif opcion == 0:
        print("hasta luego")
    else:
        print("Opcion no valida")
        

