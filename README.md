# Dockerized Machine Learning API
---
## Project Structure

```
├── docker-compose.yml   # Docker Compose configuration for the services
├── init.sql             # SQL script to initialize the MySQL database
├── mlapi/               # The Flask API for handling requests
│   ├── Dockerfile       # Dockerfile for building the Flask API container
│   ├── requirements.txt # Python dependencies
│   ├── app.py           # Flask application
│   └── templates/       # HTML templates for rendering the UI
├── temperaturedata.csv   # Historical temperature data for training the model
```
---

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/affafghani98/Docker-ML-Deployment.git

   ```

2. **Navigate to the Project Directory**

   ```bash
   cd Docker-Machine-Learning-API
   ```

3. **Build and Start Services with Docker Compose**

   ```bash
   docker-compose up --build
   ```

---

## API Endpoints

- **POST /predict**: Receives historical temperature data and returns a prediction based on the trained machine learning model.
  
---

## Requirements

- Docker
- Docker Compose
- Python 3.x (inside the container)

---

## License

This project is licensed under the MIT License.
