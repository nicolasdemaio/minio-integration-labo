import os
from minio import Minio
from minio.error import S3Error

# Configura las credenciales y la URL del servidor MinIO
minio_client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="password",
    secure=False
)
current_directory = os.getcwd()

def create_bucket():
    bucket_name = input("Ingrese el nombre del bucket a crear: ")
    try:
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' creado correctamente.")
        else:
            print(f"El bucket '{bucket_name}' ya existe.")
    except S3Error as e:
        print(f"Error al crear el bucket '{bucket_name}'")

def upload_file():
    bucket_name = input("Ingrese el nombre del bucket: ")
    file_directory = current_directory
    file_to_upload = input("Ingrese el nombre del archivo a subir: ")
    file_name = input("Ingrese el nombre del archivo en MinIO: ")

    try:
        minio_client.fput_object(bucket_name, file_name, file_directory + '/' + file_to_upload)
        print(f"Archivo '{file_name}' subido correctamente desde '{file_directory}'.")
    except S3Error as e:
        print(f"Error al subir el archivo: {e}")

def download_file():
    bucket_name = input("Ingrese el nombre del bucket: ")
    file_directory = current_directory
    file_to_upload = input("Ingrese el nombre del archivo a descargar: ")
    file_name = input("Ingrese el nombre del archivo en MinIO que desea descargar: ")

    try:
        minio_client.fget_object(bucket_name, file_name, file_directory + '/' + file_to_upload)
        print(f"Archivo '{file_name}' descargado correctamente en '{file_directory}'.")
    except S3Error as e:
        print(f"Error al descargar el archivo: {e}")

def list_objects():
    bucket_name = input("Ingrese el nombre del bucket: ")
    try:
        objects = minio_client.list_objects(bucket_name, recursive=True)
        print("Objetos en el bucket:")
        for obj in objects:
            print(obj.object_name)
    except S3Error as e:
        print(f"Error al listar los objetos del '{bucket_name}': {e}")

def list_buckets():
    try:
        buckets = minio_client.list_buckets()
        print("Buckets disponibles:")
        for bt in buckets:
            print(bt.name)
    except S3Error as e:
        print(f"Error al listar los buckets: {e}")

def delete_bucket():
    bucket_name = input("Ingrese el nombre del bucket a eliminar: ")
    try:
        objects = minio_client.list_objects(bucket_name, recursive=True)
        for obj in objects:
            minio_client.remove_object(bucket_name, obj.object_name)
            print(f"Objeto '{obj.object_name}' eliminado correctamente.")

        minio_client.remove_bucket(bucket_name)
        print(f"Bucket '{bucket_name}' eliminado correctamente.")
    except S3Error as e:
        print(f"Error al borrar el bucket")

def main_menu():
    while True:
        print("\nMenú:")
        print("1. Crear Bucket")
        print("2. Subir Archivo")
        print("3. Descargar Archivo")
        print("4. Listar Objetos en el Bucket")
        print("5. Listar Buckets")
        print("6. Borrar Bucket")
        print("0. Salir")

        choice = input("Ingrese el número de la opción que desea realizar: ")

        if choice == "1":
            create_bucket()
        elif choice == "2":
            upload_file()
        elif choice == "3":
            download_file()
        elif choice == "4":
            list_objects()
        elif choice == "5":
            list_buckets()
        elif choice == "6":
            delete_bucket()
        elif choice == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main_menu()

