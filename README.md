# Informe final: MinIO y su integración con Python

[Documentación de proyecto](https://docs.google.com/document/d/1-lpK4JAgmZegJdbopkq33DryTwFPGCSc-gsIHQPAVrI/edit)

## ¿Qué es MinIO?

> MinIO es un servidor de almacenamiento de objetos de código abierto diseñado para proporcionar almacenamiento escalable y de alto rendimiento. Compatible con la API de almacenamiento de objetos S3 de AWS, MinIO se utiliza comúnmente para construir sistemas de almacenamiento en la nube y aplicaciones de big data. Su diseño modular y su enfoque en la escalabilidad lo hacen ideal para entornos que manejan grandes volúmenes de datos.

## ¿Qué buscamos lograr con este script de Python?

Como parte de nuestra investigación acerca de MinIO para la materia 'Laboratorio de Sistemas Operativos y redes', implementamos un script utilizando el lenguaje Python para proporcionar a aquellos que deseen experimentar el uso de una herramienta de código abierto como MinIO puedan lograrlo.

El uso es sencillo, cuenta con una consola interactiva con inputs númericos que permite realizar acciones como por ejemplo:
- Creación de Buckets de objetos
- Eliminación de Buckets
- Listado de Buckets
- Agregado de objetos a un Bucket dado
- Eliminación de objetos de un Bucket
- Listado de objetos almacenados en un Bucket

## Pasos para su ejecución

Para la ejecución de este script, principalmente necesitaremos realizar el proceso de instalación de forma local de MinIO.


Para esto, podemos dirigirnos al enlace a la documentación desarrollada y luego observar el paso de 'Proceso de Instalación' donde se detalla una guía de como alcanzar a preparar el ambiente local para su ejecución en el SO Linux.


Si desea experimentarlo en otro SO puede observar la [página oficial](https://min.io/) que brinda información detallada.

Una vez MinIO descargado e instalado debemos descargar el script (clonar el repositorio si prefiere)

```
git clone git@github.com:nicolasdemaio/minio-integration-labo.git
```

Adicionalmente, requerirá la ejecución de los siguientes comandos:

```
sudo apt-get update 
sudo apt-get install python3-pip
sudo pip3 install minio
chmod +x minioApp.py
```

Para ejecutar el script, simplemente nos situamos sobre el directorio donde descargamos el mismo y ejecutamos:

```
python3 minioApp.py
```


