from prefect import flow

from datetime import datetime

from src import create_df

# Definimos las variables de tiempo
fecha = datetime.now()
hora = int(str(fecha).replace('-', '').replace(':', '').replace(' ', '')[8:14])

@flow(log_prints=True)
def hello_world():
    '''
    Función principal que encapsula nuestro flujo (flow) de trabajo
    '''
    
    # Ejecutamos uno de nuestros modulos para crear y guardar un csv
    create_df.run(hora)

if __name__ == '__main__':
    # Ejecutamos nuestro flujo
    hello_world.serve(
        name='hello_prefect', # Definimos el nombre con el que se hara el seguimiento del flujo
        tags=["testing", 'onboarding'], # Agregamos las respectivas etiquetas
        interval=30 # Especificamos cada cuantos segundos queremos que nuestra tarea se relance
    )