# 🛒 Retail Sales Batch ETL Pipeline

### End-to-End Data Engineering Project | Python • PostgreSQL • Apache Airflow • Docker

Automated batch ETL pipeline that ingests daily retail sales transaction files, validates and transforms records, loads a PostgreSQL data warehouse using a Star Schema design, generates business KPIs, and orchestrates the entire workflow using Apache Airflow.

---

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![Apache Airflow](https://img.shields.io/badge/Apache_Airflow-Orchestration-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![ETL](https://img.shields.io/badge/Data_Engineering-ETL-green)

---

## 🚀 Key Highlights

✔ Incremental Data Loading

✔ Star Schema Data Warehouse

✔ Apache Airflow Orchestration

✔ Dockerized Infrastructure

✔ Automated KPI Generation

✔ Data Quality Validation

✔ Production-Style ETL Design

---

## 🎯 Business Problem

An e-commerce company receives daily sales transaction files from multiple regional stores.

Manual processing creates delays, inconsistent reporting, and limited visibility into business performance. The organization requires a centralized and automated solution that can ingest sales data, perform validation and transformation, store historical records, and generate business insights for reporting and decision-making.

This project addresses these requirements by building a fully automated Retail Sales Batch ETL Pipeline.

---

## 🏗️ Solution Architecture

<img width="1690" height="740" alt="Retail-Sales-Batch-ETL arch" src="https://github.com/user-attachments/assets/93b075de-1c75-4ef5-be07-af45b9f9249d" />

---

## 🔄 End-to-End Workflow

```text
Raw CSV Files
        ↓
Data Validation
        ↓
Data Transformation
        ↓
Incremental Loading
        ↓
PostgreSQL Data Warehouse
        ↓
KPI Generation
        ↓
Data Quality Checks
        ↓
Apache Airflow Orchestration
```

---

## 💡 Why This Project?

This project was designed to simulate a real-world retail analytics platform and demonstrate core Data Engineering concepts commonly used in production environments.

The solution focuses on:

* Building scalable ETL pipelines
* Designing analytical data warehouses
* Implementing incremental data processing
* Automating workflows with Airflow
* Containerizing applications using Docker
* Applying data quality and validation checks
* Generating business-ready KPIs

---

## 🛠️ Technology Stack

| Component                | Technology     |
| ------------------------ | -------------- |
| Programming Language     | Python         |
| Workflow Orchestration   | Apache Airflow |
| Data Warehouse           | PostgreSQL     |
| Containerization         | Docker         |
| Data Processing          | Pandas         |
| Database Connectivity    | SQLAlchemy     |
| Configuration Management | YAML           |
| Analytics                | SQL            |

---

## ⭐ Data Warehouse Design

The warehouse follows a Star Schema design commonly used in enterprise analytics platforms.

```text
                    dim_customer
                          |
                          |
dim_product ---- fact_sales ---- dim_store
                          |
                          |
                       dim_date
```

### Fact Table

#### fact_sales

| Column         |
| -------------- |
| sale_id        |
| customer_id    |
| product_id     |
| store_id       |
| date_id        |
| quantity       |
| unit_price     |
| total_amount   |
| load_timestamp |

### Dimension Tables

#### dim_customer

| Column      |
| ----------- |
| customer_id |

#### dim_product

| Column     |
| ---------- |
| product_id |

#### dim_store

| Column   |
| -------- |
| store_id |
| region   |

#### dim_date

| Column  |
| ------- |
| date_id |
| year    |
| month   |
| day     |
| quarter |

---

## ⚙️ Engineering Features

### Incremental Loading

The pipeline processes only new files during each execution.

A tracking mechanism prevents duplicate ingestion by maintaining a processed files registry.

---

### Data Validation

Automated quality checks include:

* Null Value Detection
* Duplicate Record Detection
* Invalid Date Validation
* Negative Quantity Detection
* Negative Price Detection

---

### Data Transformation

Transformation logic includes:

* Date Standardization
* Business Metric Derivation
* Total Sales Calculation
* Invalid Record Removal
* Audit Timestamp Generation

---

### Workflow Orchestration

Apache Airflow manages:

* Scheduling
* Task Dependencies
* Retry Logic
* Monitoring
* Failure Handling

---

### Dockerized Deployment

The complete solution runs inside Docker containers, ensuring:

* Consistent Environments
* Easy Deployment
* Reproducibility
* Simplified Setup

---

## 📊 KPI Generation

The pipeline automatically generates business metrics including:

### Revenue Metrics

* Total Revenue
* Daily Revenue Trend

### Product Analysis

* Top Selling Products
* Product Revenue Contribution

### Regional Analysis

* Revenue by Region
* Sales Distribution

### Payment Analysis

* Payment Method Distribution

---

## ✅ Data Quality Checks

The pipeline includes automated quality validation after data loading.

Checks include:

* Fact Table Row Count Validation
* Null Customer Validation
* Negative Sales Detection
* Warehouse Load Verification
* KPI Generation Validation

---

## 🌬️ Apache Airflow DAG

The workflow is orchestrated through Apache Airflow.

### DAG Flow

```text
check_new_files
        ↓
extract_transform_load
        ↓
generate_kpis
        ↓
quality_checks
```

### Airflow Features

* Daily Scheduling
* Dependency Management
* Retry Mechanism
* Monitoring Dashboard
* Failure Visibility
* Execution Logs

---

## 📸 Project Screenshots

### Airflow DAG

<img width="1466" height="582" alt="airflow_dag_graph" src="https://github.com/user-attachments/assets/3e4764c4-fbb4-436e-9876-38c16dce0d65" />

---

### Successful Pipeline Execution

<img width="1866" height="721" alt="airflow_success_run" src="https://github.com/user-attachments/assets/4dac0113-a991-4821-8858-a6ec31740058" />


---

### PostgreSQL Data Warehouse

<img width="1500" height="967" alt="postgres_dwh_tables1" src="https://github.com/user-attachments/assets/7c3b93b6-6b44-4e9f-9560-a622ae7972ef" />

<img width="1025" height="417" alt="postgres_dwh_tables2" src="https://github.com/user-attachments/assets/5c77aa0c-70ed-4f02-ac7f-e703726bbbab" />

<img width="1032" height="407" alt="postgres_dwh_tables3" src="https://github.com/user-attachments/assets/106846e4-0d9b-4ef1-a695-027841d434b9" />


---

### KPI Results

<img width="1072" height="721" alt="kpi_results" src="https://github.com/user-attachments/assets/c830c0fa-6c87-42e2-a6e5-7950aabcc784" />

---

### Docker Containers

<img width="1462" height="170" alt="docker_containers" src="https://github.com/user-attachments/assets/71d8a22c-d16b-44b4-acd6-c1e91d5ff476" />

---

## 📂 Project Structure

```text
retail-sales-etl/

├── airflow/
│   ├── dags/
│   ├── logs/
│   └── plugins/
│
├── architecture/
│   └── architecture.png
│
├── data/
│   └── raw_csv/
│
├── etl/
│   ├── check_files.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── validations.py
│   ├── generate_kpis.py
│   ├── quality_checks.py
│   └── run_pipeline.py
│
├── screenshots/
│
├── sql/
│   ├── schema.sql
│   └── kpi_queries.sql
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── config.yaml
└── README.md
```

---

## 📈 Skills Demonstrated

This project demonstrates hands-on experience with:

* ETL Pipeline Development
* Python Data Engineering
* PostgreSQL Data Warehousing
* Star Schema Modeling
* Apache Airflow DAG Development
* Docker Containerization
* Incremental Data Loading
* KPI Reporting
* Data Validation Frameworks
* Workflow Automation
* SQL Analytics
* Production-Oriented Data Engineering

---

## 🚀 Future Enhancements

Potential improvements include:

* Slowly Changing Dimensions (SCD Type 2)
* Power BI Dashboard Integration
* Cloud Deployment (AWS / Azure)
* CI/CD Automation
* Automated Unit Testing
* Data Observability Layer
* Data Lineage Tracking
* Alerting & Monitoring Frameworks

---

## 👨‍💻 Author

**Abhinav Anand**

Data Engineering Portfolio Project

Built to demonstrate modern ETL development, data warehousing, orchestration, and analytics engineering best practices.
