# 🚀 NASA Astronomy Picture of the Day ETL Pipeline

## 📋 Project Overview
A robust ETL pipeline leveraging Apache Airflow to fetch, process, and store NASA's Astronomy Picture of the Day data using Docker, PostgreSQL, and the NASA API.

## 🛠️ Tech Stack
- Apache Airflow
- PostgreSQL
- Docker
- NASA Astronomy API
- Astro CLI

## ✨ Key Features
- Automated daily NASA API data extraction
- Containerized development environment
- Efficient data transformation
- Persistent PostgreSQL storage
- Comprehensive workflow management

## 🏗️ Architecture Diagram
```
NASA API → Airflow (Extract) → Transform → PostgreSQL (Load)
```

## 🔍 Pipeline Components

### 1. Extract
- `SimpleHttpOperator` for NASA API data fetching
- Retrieves daily astronomy picture details
- Manages API authentication

### 2. Transform
- Airflow TaskFlow API with `@task` decorator
- Extracts key information:
  - Date
  - Title
  - Explanation
  - Image URL

### 3. Load
- `PostgresHook` for database interactions
- Automatic table creation
- Data insertion into PostgreSQL

## 🖼️ Project Screenshots

### Airflow Admin Connection Setup
![Airflow Admin Setup](https://github.com/user-attachments/assets/d0d8a0e0-b91c-436c-929a-bd647a2c050a)

### PostgreSQL Database View
![PostgreSQL Database](https://github.com/user-attachments/assets/ea04680d-8239-4f5a-ac21-7b1b58d68f42)

## 🚀 Local Development Setup

### Prerequisites
- Docker Desktop
- Python 3.8+
- Astro CLI

### Installation Steps
```bash
# Install Astro CLI
winget install -e --id Astronomer.Astro

# Clone repository
git clone <repository-url>
cd nasa-astronomy-etl

# Install dependencies
pip install -r requirements.txt

# Start Docker Desktop
# Initialize Airflow
astro dev start
```

## 🔧 Airflow Configuration
1. Open Airflow Web UI
2. Navigate to Admin → Connections
3. Configure connections:
   - NASA API Connection
   - PostgreSQL Database Connection

### Connection Details

#### NASA API Connection
- Type: HTTP
- Host: `https://api.nasa.gov`
- Extra: Include API key

#### PostgreSQL Connection
- Type: Postgres
- Host: `postgres container name`
- Schema: `postgres`
- Login: `postgres`
- Password: `postgres`
- Port: `5432`

## ☁️ Cloud Deployment with AWS

### RDS Database Setup
1. Create AWS RDS PostgreSQL instance
2. Allow public access
3. Configure security group (Port 5432)

### Astronomer Deployment
```bash
# Login to Astronomer
astro login

# Create workspace and deployment
astro deploy --dag
```

## 🖼️ Cloud Deployment Screenshots

### AWS RDS Database
![Amazon RDS](https://github.com/user-attachments/assets/a32d8010-8cbd-4337-9558-7370e96fc0b2)

### Astronomer Dashboard
![Astronomer DAG 1](https://github.com/user-attachments/assets/79536d17-77dc-455a-8024-2966beedf0d3)

### Astronomer Airflow UI
![Astronomer DAG](https://github.com/user-attachments/assets/67080298-3d1f-45f3-bfef-dbaec54723dd)

### DBeaver AWS Database Table View
![DBeaver Table AWS](https://github.com/user-attachments/assets/eb4095c7-b78d-4385-ad81-7c5f75a744a0)

## 🌟 Benefits
- Reproducible environment
- Isolated services
- Scalable architecture
- Easy deployment
- Comprehensive logging

## 🤝 Contributing
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Create Pull Request

## 🔗 Resources
- [Apache Airflow Docs](https://airflow.apache.org/docs/)
- [NASA API Docs](https://api.nasa.gov/)
- [Docker Docs](https://docs.docker.com/)

---
*Powered by Airflow, Docker, NASA API*
