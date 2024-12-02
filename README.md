# 🚀 NASA Astronomy Picture of the Day ETL Pipeline

## 📋 Project Overview

A robust ETL (Extract, Transform, Load) pipeline that leverages Apache Airflow to fetch, process, and store NASA's Astronomy Picture of the Day data using Docker, PostgreSQL, and the NASA API.

## 🛠️ Tech Stack
- Apache Airflow
- PostgreSQL
- Docker
- NASA Astronomy API
- Astro CLI

## ✨ Key Features
- Automated daily data extraction from NASA API
- Containerized development environment
- Efficient data transformation
- Persistent storage in PostgreSQL
- Comprehensive workflow management

## 🏗️ Architecture Diagram
```
NASA API → Airflow (Extract) → Transform → PostgreSQL (Load)
```

## 🔍 Pipeline Components

### 1. Extract
- Uses `SimpleHttpOperator` to fetch data from NASA API
- Retrieves daily astronomy picture details
- Handles API authentication and request management

### 2. Transform
- Utilizes Airflow's TaskFlow API with `@task` decorator
- Extracts critical information:
  - Date
  - Title
  - Explanation
  - Image URL

### 3. Load
- Implements `PostgresHook` for database interactions
- Automatically creates table if not exists
- Inserts transformed data into PostgreSQL

## 🖼️ Project Screenshots

### Airflow Admin Connection Setup
![Airflow Admin Setup](https://github.com/user-attachments/assets/d0d8a0e0-b91c-436c-929a-bd647a2c050a)

### PostgreSQL Database View
![PostgreSQL Database](https://github.com/user-attachments/assets/ea04680d-8239-4f5a-ac21-7b1b58d68f42)

## 🚀 Getting Started

### Prerequisites
- Docker Desktop
- Python 3.8+
- Astro CLI

### Installation Steps
1. Install Astro CLI
```bash
winget install -e --id Astronomer.Astro
```

2. Clone the repository
```bash
git clone <repository-url>
cd nasa-astronomy-etl
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Start Docker Desktop

5. Initialize Airflow
```bash
astro dev start
```

### Airflow Configuration
1. Open Airflow Web UI
2. Navigate to Admin → Connections
3. Configure two connections:
   - NASA API Connection
   - PostgreSQL Database Connection

## 🔧 Configuration Details

### NASA API Connection
- Conn Type: HTTP
- Host: `https://api.nasa.gov`
- Extra: Include API key

### PostgreSQL Connection
- Conn Type: Postgres
- Host: `paste complete name of postgress container running under the astro docker images`
- Schema: `postgres`
- Login: `postgres`
- Password: `postgres`
- Port: `5432`

## 📦 Docker Services
- Airflow Webserver
- Airflow Scheduler
- PostgreSQL Database
- Redis (Optional message broker)

## 🌟 Benefits
- Reproducible environment
- Isolated services
- Scalable architecture
- Easy deployment
- Comprehensive logging

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## 📄 License
[Specify your license - e.g., MIT]

## 🔗 Additional Resources
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [NASA API Documentation](https://api.nasa.gov/)
- [Docker Documentation](https://docs.docker.com/)

---
*Powered by Airflow, Docker, and NASA's Open API*
