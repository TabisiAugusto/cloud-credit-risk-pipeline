# End-to-End Cloud Credit Risk Data Pipeline 🌩️🏦

🌍 *[Read in English](#-english-version) | [Leer en Español](#-versión-en-español)*

---

## 🇬🇧 English Version

### 📌 Project Overview
This project is an end-to-end cloud data engineering and analytics pipeline designed to assess credit risk. It simulates a production-grade environment by orchestrating data ingestion, relational modeling, and secure cloud storage.

The core business objective is to provide a robust infrastructure for financial risk analysis, allowing stakeholders to evaluate default probabilities and portfolio health using structured, scalable data instead of static spreadsheets.

### 🧱 Architecture & Engineering Decisions
* **Cloud Infrastructure:** Processing orchestrated via Google Colab, directly connected to an **Aiven MySQL** cloud database server.
* **Security First:** Implemented SSL/TLS encryption (`ca.pem` certificates) to secure the connection between the execution environment and the cloud database, adhering to corporate data privacy standards.
* **Programmatic DDL & Modeling:** Database schema creation, Primary Keys, and relational constraints are fully orchestrated using DDL commands directly within Python scripts.
* **Resource Optimization (Dev/Prod):** Engineered a "Dev Sample" of 20,000 rows to test and optimize the ETL pipeline. This prevents free-tier server saturation and demonstrates a production-ready mindset for handling Big Data environments.

### 🛠 Tech Stack
* **Data Engineering:** Python (Pandas), SQL DDL orchestration
* **Cloud & Security:** Aiven MySQL, SSL/TLS Encryption
* **Analytics:** Financial Risk Assessment

### 📂 Repository Structure
*(Structure will be updated as scripts are uploaded)*

---

## 🇪🇸 Versión en Español

### 📌 Descripción del Proyecto
Este proyecto es un *pipeline* integral de ingeniería y análisis de datos en la nube diseñado para evaluar el riesgo crediticio. Simula un entorno de producción corporativo orquestando la ingesta de datos, el modelado relacional y el almacenamiento seguro en la nube.

El objetivo central de negocio es proporcionar una infraestructura robusta para el análisis de riesgos financieros, permitiendo a la dirección evaluar probabilidades de impago (*default*) y la salud de la cartera utilizando datos estructurados y escalables en lugar de hojas de cálculo estáticas.

### 🧱 Arquitectura y Decisiones de Ingeniería
* **Infraestructura Cloud:** Procesamiento orquestado a través de Google Colab, conectado directamente a un servidor de base de datos en la nube **Aiven MySQL**.
* **Seguridad de Datos:** Implementación de encriptación SSL/TLS (certificados `ca.pem`) para asegurar la conexión entre el entorno de ejecución y la base de datos, cumpliendo con los estándares de privacidad corporativos.
* **Modelado y DDL Programático:** La creación del esquema de la base de datos, las Claves Primarias y las restricciones relacionales se orquestan completamente mediante comandos DDL ejecutados desde scripts en Python.
* **Optimización de Recursos (Dev/Prod):** Diseño estratégico de un "Dev Sample" (muestra de desarrollo) de 20.000 filas para testear y optimizar el *pipeline* ETL. Esto evita la saturación del servidor y demuestra mentalidad de escalabilidad para entornos de Big Data.

### 🛠 Stack Tecnológico
* **Ingeniería de Datos:** Python (Pandas), orquestación SQL DDL
* **Nube y Seguridad:** Aiven MySQL, Encriptación SSL/TLS
* **Analítica:** Evaluación de Riesgo Financiero

### 📂 Estructura del Repositorio
*(La estructura se actualizará a medida que se suban los scripts)*
