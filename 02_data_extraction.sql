/*
=============================================================================
Paso 2: Extracción y Limpieza de Datos en SQL (Data Wrangling)
=============================================================================
Objetivo: Limpiar anomalías financieras, estandarizar formatos de fecha 
y preparar el dataset estructurado para su consumo en Tableu Public.
=============================================================================
*/

USE riesgo_crediticio;

-- Consulta limpia exportada para el modelo analítico
SELECT 
    SK_ID_CURR AS id_cliente,
    TARGET AS estado_riesgo,
    CODE_GENDER AS genero,
    FLAG_OWN_CAR AS tiene_auto,
    FLAG_OWN_REALTY AS tiene_propiedad,
    NAME_INCOME_TYPE AS tipo_ingreso,
    NAME_EDUCATION_TYPE AS nivel_educativo,
    NAME_FAMILY_STATUS AS estado_civil,
    
    -- Variables Financieras
    ROUND(AMT_INCOME_TOTAL, 2) AS ingreso_total,
    ROUND(AMT_CREDIT, 2) AS monto_credito,
    ROUND(AMT_ANNUITY, 2) AS cuota_anual,
    
    -- Convertimos días negativos a Años positivos
    ROUND(DAYS_BIRTH / -365, 0) AS edad_anios,
    
    -- Limpieza avanzada: Manejo de anomalía del sistema (365243 = nulo)
    CASE 
        WHEN DAYS_EMPLOYED = 365243 THEN NULL 
        ELSE ROUND(DAYS_EMPLOYED / -365, 1) 
    END AS antiguedad_laboral_anios

FROM raw_application_train;
