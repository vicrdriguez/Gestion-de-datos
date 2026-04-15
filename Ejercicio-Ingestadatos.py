import pandas as pd
import logging
import os
from datetime import datetime

# 1. Configuración de Logging (Trazabilidad)
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=f"{LOG_DIR}/proceso_extraccion.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'

    
)

def extraer_datos(ruta_archivo):
    inicio_time = datetime.now()
    logging.info("--- Inicio del proceso de obtención de datos ---")
    
    try:
    
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"No se encontró el archivo en: {ruta_archivo}")

        df = pd.read_csv(ruta_archivo)
        
     
        num_registros = len(df)
        logging.info(f"exito: Se han procesado {num_registros} registros correctamente.")
        
       
        
        print(f"Proceso finalizado. Registros: {num_registros}")
        
    except Exception as e:
        logging.error(f"Error durante la ejecución: {str(e)}")
        print(f"Hubo un error. Revisa los logs en la carpeta /{LOG_DIR}")
    
    finally:
        duracion = datetime.now() - inicio_time
        logging.info(f"Tiempo total de ejecución: {duracion}")
        logging.info("--- Fin del proceso ---\n")
        

if __name__ == "__main__":
    
    PATH_CSV = "abandono_escolar_dataset.csv"
    extraer_datos(PATH_CSV)