import pandas as pd
import os
from datetime import datetime


def create_logs(sample_size=10):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, '..', 'data', 'OnlineRetail.csv')
    print("CSV path:", csv_path)
    
    df = pd.read_csv(csv_path, encoding="ISO-8859-1")
    df_sample = df.sample(n=sample_size)

    name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Ruta absoluta de la carpeta logs
    logs_dir = os.path.join(script_dir, '..', 'logs')
    
    # Si la carpeta logs no existe, crearla:
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
        
    # Construye la ruta completa al archivo
    log_path = os.path.join(logs_dir, f'{name}.log')
    
    # Guardar como JSON
    df_sample.to_json(log_path, orient="records")




if __name__ == '__main__':
    sample_size=10
    create_logs(sample_size=sample_size)