# InstaPay DevSecOps Project

> A secure, demo-ready payment system built for university-level DevSecOps and security modules.  
> This project demonstrates best practices in secure development, CI/CD automation, security scanning, and containerized deployment.

---

## Table of Contents

- [Overview](#overview)
- [DevSecOps Workflow](#devsecops-workflow)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [API Reference](#api-reference)
- [Security Pipeline](#security-pipeline)
- [Project Structure](#project-structure)

---

## Overview

InstaPay is a demonstration-grade fintech application designed to showcase a complete DevSecOps lifecycle. It integrates security tooling directly into the development and deployment pipeline, ensuring that security is treated as a first-class concern rather than an afterthought.

---

## DevSecOps Workflow

```
[Code Commit]
      |
      v
[GitHub Actions CI/CD]
      |
      |-- [SAST: Bandit]         Static code analysis for Python security flaws
      |-- [SCA: pip-audit]       Dependency vulnerability scanning
      |-- [Tests: pytest]        Functional test suite
      |-- [Docker Build]         Container image verification
      |
      v
[Deployment / Monitoring]
```

Every push to `main` triggers this full pipeline automatically.

---

## Features

### Backend
- **Flask** (Python) with **JWT-based authentication**
- **MongoDB** for secure transaction storage

### Monitoring
- **Prometheus** for real-time metrics and observability

### Security Controls
- Non-root Docker user for container safety
- **SAST** via [Bandit](https://github.com/PyCQA/bandit) — static analysis for Python
- **SCA** via [pip-audit](https://github.com/pypa/pip-audit) — dependency vulnerability detection
- **CI/CD** with GitHub Actions — automated on every push to `main`

### Infrastructure and Deployment
- **Docker Compose** for local deployment
- **Kubernetes** manifests (demo-ready)
- **Terraform** scripts (demo-ready)

---

## Prerequisites

| Requirement | Notes |
|---|---|
| Docker | Required for local deployment |
| Docker Compose | Required for local deployment |
| Kubernetes | Optional — for infrastructure demos |
| Terraform | Optional — for infrastructure demos |

---

## Quick Start

Clone the repository and spin up the full stack locally:

```bash
git clone https://github.com/<your-username>/instapay.git
cd instapay
docker compose up --build
```

Once running, the following services are available:

| Service | URL |
|---|---|
| Health Check | http://localhost:5000/health |
| Metrics (Prometheus format) | http://localhost:5000/metrics |
| Prometheus Dashboard | http://localhost:9090 |

---

## API Reference

### POST `/login` — Authenticate and Retrieve JWT

**Request**

```json
{
  "username": "admin",
  "password": "password"
}
```

**Response**

```json
{
  "token": "<jwt_token>"
}
```

---

### POST `/pay` — Make a Payment (Protected)

**Headers**

```
Authorization: Bearer <token>
```

**Request**

```json
{
  "amount": 100,
  "recipient": "bob"
}
```

**Response**

```json
{
  "status": "success",
  "transaction_id": "<id>"
}
```

---

## Security Pipeline

The CI/CD pipeline is defined in `.github/workflows/ci.yml` and runs on every push to `main`.

| Stage | Tool | Purpose |
|---|---|---|
| Dependency Scan (SCA) | pip-audit | Detects known CVEs in Python dependencies |
| Static Analysis (SAST) | Bandit | Scans source code for security anti-patterns |
| Functional Tests | pytest | Validates application behavior |
| Container Build | Docker | Verifies image builds and containerization |

All stages must pass before a build is considered successful.

---

## Project Structure

```
instapay/
├── backend/              Flask application, Dockerfile, and requirements
├── monitoring/           Prometheus configuration
├── k8s/                  Kubernetes deployment manifests (demo)
├── terraform/            Sample infrastructure-as-code scripts (demo)
└── .github/
    └── workflows/
        └── ci.yml        GitHub Actions CI/CD pipeline definition
```

---

## Highlights

- Fully automated DevSecOps workflow covering SAST, SCA, testing, and build verification
- Secure containerized deployment with non-root execution enforced at the Docker level
- Clean separation between application, monitoring, and infrastructure concerns
- Extensible design — ready to be adapted for real-world CI/CD and security practices

---

> Built as part of a university DevSecOps module. For educational and demonstration purposes.
