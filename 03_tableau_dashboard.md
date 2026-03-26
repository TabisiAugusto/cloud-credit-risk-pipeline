# Step 3: Credit Risk Dashboard (Tableau Public) 📊

🌍 *[Read in English](#-english-version) | [Leer en Español](#-versión-en-español)*

---

## 🇬🇧 English Version

### 📌 Overview
The final layer of this data pipeline is the visual analytics dashboard, built and deployed in **Tableau Public**. It consumes the clean, transformed data from our SQL views to provide actionable insights into the credit portfolio's risk distribution.

### 🔗 Interactive Dashboard
* **[View Live Dashboard on Tableau Public](https://public.tableau.com/app/profile/augusto.tabisi/viz/Credit_Risk_Analysis_Dashboard/CreditRiskAnalysisDashboard)**

### 📈 Key Business Questions Answered
* **Demographic Risk (Education):** How does the client's educational background impact the probability of default?
* **Lifecycle & Age Risk:** Which age groups represent the highest exposure to default risk for the bank's portfolio?
* **Financial Exposure:** Is there a direct correlation between high financial leverage (Credit Amount vs. Total Income) and default likelihood?

### 🛠 Visual & Analytical Techniques
* **Calculated Fields:** Custom logic applied to group quantitative variables (e.g., age and income bins) for clearer categorical analysis.
* **Interactive Filters:** Enabled drill-down capabilities by gender, property ownership, and income type to isolate specific risk segments.
* **Data Storytelling:** Strategic use of color palettes to highlight high-risk segments without overwhelming the stakeholder.

---

## 🇪🇸 Versión en Español

### 📌 Resumen
La capa final de este *pipeline* de datos es el *dashboard* de analítica visual, desarrollado y desplegado en **Tableau Public**. Consume los datos limpios y transformados desde nuestras consultas SQL para proporcionar *insights* accionables sobre la distribución del riesgo en la cartera de créditos.

### 🔗 Dashboard Interactivo
* **[Ver Dashboard Interactivo en Tableau Public](https://public.tableau.com/app/profile/augusto.tabisi/viz/Credit_Risk_Analysis_Dashboard/CreditRiskAnalysisDashboard)**

### 📈 Preguntas de Negocio Respondidas
* **Riesgo Demográfico (Educación):** ¿Cómo impacta el nivel educativo del cliente en la probabilidad de caer en morosidad?
* **Riesgo por Ciclo de Vida (Edad):** ¿Qué grupos etarios representan la mayor exposición al riesgo de impago para la cartera del banco?
* **Exposición Financiera:** ¿Existe una correlación directa entre un alto apalancamiento financiero (Monto del Crédito vs. Ingresos) y la probabilidad de *default*?

### 🛠 Técnicas Analíticas y Visuales
* **Campos Calculados:** Lógica personalizada aplicada para agrupar variables cuantitativas (ej., rangos de edad e ingresos) para un análisis categórico más claro.
* **Filtros Interactivos:** Capacidad de exploración profunda (*drill-down*) por género, propiedad y tipo de ingreso para aislar segmentos de riesgo específicos.
* **Data Storytelling:** Uso estratégico de paletas de colores para resaltar los segmentos de alto riesgo sin saturar visualmente al usuario.
