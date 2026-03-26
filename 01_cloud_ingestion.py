!pip install pymysql sqlalchemy pandas

import pandas as pd

from sqlalchemy import create_engine, text



# ==========================================

# 1. CONFIGURACIÓN DE CONEXIÓN

# ==========================================

USER = 'avnadmin'

PASSWORD = ''

HOST = ''

PORT = ''

DB_NAME = 'riesgo_crediticio'



# String de conexión apuntando al certificado en tu Google Drive

connection_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?ssl_ca=/content/drive/MyDrive/PRUEBAS EN COLAB/ca.pem"

engine = create_engine(connection_string)



# ==========================================

# 2. LECTURA Y MUESTREO DE DATOS (DEV SAMPLE)

# ==========================================

print("Leyendo el archivo CSV completo desde Drive...")

df_application_full = pd.read_csv('/content/drive/MyDrive/PRUEBAS EN COLAB/application_train.csv')



print("Creando muestra de 20,000 filas para proteger el servidor gratuito...")

# Esto evita que Aiven colapse por falta de espacio en disco y binlogs (Error 1598)

df_application = df_application_full.sample(n=20000, random_state=42).copy()



# ==========================================

# 3. INGESTA A LA BASE DE DATOS CLOUD

# ==========================================

print("Iniciando conexión a Aiven MySQL...")



# Usamos un bloque "with" para mantener la conexión segura y en la misma sesión

with engine.begin() as conn:

    print("Paso 1: Pausando regla estricta de Aiven temporalmente...")

    conn.execute(text("SET SESSION sql_require_primary_key = 0;"))



    print("Paso 2: Creando la estructura de la tabla vacía...")

    # Mandamos solo la fila 0 para que Pandas cree las columnas en MySQL sin datos

    df_application.head(0).to_sql('raw_application_train', con=conn, if_exists='replace', index=False)



    print("Paso 3: Asignando la Primary Key (SK_ID_CURR)...")

    # Alteramos la tabla recién creada para cumplir con el estándar de la industria

    conn.execute(text("ALTER TABLE raw_application_train ADD PRIMARY KEY (SK_ID_CURR);"))



    print("Paso 4: Reactivando seguridad...")

    conn.execute(text("SET SESSION sql_require_primary_key = 1;"))



    print("Paso 5: Subiendo la muestra masiva (esto tomará unos segundos)...")

    # Usamos if_exists='append' para meter los datos en la tabla que ya tiene su PK

    df_application.to_sql('raw_application_train', con=conn, if_exists='append', index=False, chunksize=5000)



print("¡Éxito total! Tabla creada y datos cargados a la nube sin saturar el servidor.")
