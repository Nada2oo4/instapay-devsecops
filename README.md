# InstaPay DevSecOps Project

This is a complete, demo-ready DevSecOps project for a university security module. It features a secure payment system (InstaPay) with a focus on simple deployment, security scanning, and monitoring.

## Features
- **Backend:** Flask (Python) with JWT Authentication
- **Database:** MongoDB for transaction storage
- **Monitoring:** Prometheus for real-time metrics
- **Security:** 
  - Non-root Docker user
  - SAST (Bandit)
  - SCA (pip-audit)
  - CI/CD with GitHub Actions
- **Infrastructure:** Docker Compose, K8s (demo), Terraform (demo)

## Prerequisites
- Docker and Docker Compose

## Quick Start (Run Locally)

To start the entire system, run:

```bash
docker compose up --build
```

## URLs to Demo

Once the system is running,  can access:

- **Health Check:** [http://localhost:5000/health](http://localhost:5000/health)
- **Metrics (Prometheus format):** [http://localhost:5000/metrics](http://localhost:5000/metrics)
- **Prometheus Dashboard:** [http://localhost:9090](http://localhost:9090)

## API Endpoints

### 1. Login (Get JWT)
**POST** `/login`
```json
{
    "username": "admin",
    "password": "password"
}
```

### 2. Make a Payment (Protected)
**POST** `/pay`
**Headers:** `Authorization: Bearer <token>`
```json
{
    "amount": 100,
    "recipient": "bob"
}
```

## Security Pipeline (CI/CD)

The project includes a GitHub Actions workflow in `.github/workflows/devsecops.yml` that performs:
1. **SCA:** Scans dependencies for known vulnerabilities using `pip-audit`.
2. **SAST:** Scans source code for security flaws using `Bandit`.
3. **Tests:** Runs basic functional tests using `pytest`.
4. **Build:** Verifies the Docker image builds correctly.

## Project Structure
- `backend/`: Flask application, Dockerfile, and requirements.
- `monitoring/`: Prometheus configuration.
- `k8s/`: Sample Kubernetes deployment manifests.
- `terraform/`: Sample infrastructure code.
- `.github/`: CI/CD pipeline definitions.
