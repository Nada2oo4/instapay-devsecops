# DevOps/DevSecOps Engineer Role Documentation: Instapay DevSecOps

## Overview
As the DevOps/DevSecOps Engineer for the **Instapay** project, my primary responsibility was to design and implement a secure, automated, and observable lifecycle for a fintech application. The project serves as a demonstration-grade platform, integrating security into every stage of the development process—from code commit to deployment. My focus was on establishing a "Shift Left" security culture, ensuring that vulnerabilities are identified and remediated early in the pipeline.

## Design & Implementation
The system architecture was designed with security and scalability as core principles:
- **Containerization**: The application is fully containerized using Docker. I implemented security best practices by using `python:3.11-slim` as a base image to reduce the attack surface and enforced a **non-root user** (`appuser`) for running the application.
- **Infrastructure as Code (IaC)**: I provided **Terraform** scripts to provision AWS resources (EC2) and **Kubernetes** manifests for container orchestration, ensuring consistent and reproducible environments.
- **Observability**: **Prometheus** was integrated to monitor application metrics. I configured a custom `/metrics` endpoint in the Flask backend using `prometheus_client` and set up a Prometheus instance to scrape these metrics, enabling real-time monitoring of request latency and status codes.
- **Database Security**: MongoDB is used for transaction storage, with connection strings managed via environment variables to avoid hardcoding credentials.

## CI/CD Pipelines
I engineered a multi-tiered CI/CD strategy using GitHub Actions to automate testing, security scanning, and deployment:
- **Continuous Integration (CI)**: Automated on every push to `main`, this pipeline runs unit tests, performs SAST and SCA, and verifies the Docker build.
- **Continuous Deployment (CD)**: Automates the build and push of Docker images to a registry and handles deployment to Kubernetes clusters using `kubectl`.
- **Scheduled Scans**: Implemented weekly dependency scans to detect new vulnerabilities in third-party libraries over time.

## Security Measures
Security is not a checkbox but a continuous process integrated into the pipeline:
- **SAST (Static Application Security Testing)**: Integrated **Bandit** to scan Python source code for common security issues like hardcoded passwords or insecure function calls.
- **SCA (Software Composition Analysis)**: Utilized **pip-audit** to check project dependencies against known vulnerability databases (CVEs).
- **Secret Scanning**: Implemented **Gitleaks** to prevent sensitive information (API keys, tokens) from being committed to the repository.
- **DAST (Dynamic Application Security Testing)**: Integrated **OWASP ZAP** into the pipeline to perform baseline security scans on the running application, identifying issues like missing security headers.
- **Hardening**: Applied `nosec` markers in code where specific security checks were intentionally bypassed for demo purposes, while maintaining overall security integrity.

## Testing
A comprehensive testing strategy was implemented to ensure both functional and security requirements are met:
- **Unit Testing**: Developed a suite of tests using **pytest** to validate core API functionality, such as health checks and authentication.
- **Local Environment Testing**: Provided a `docker-compose.yml` file to allow developers to spin up the entire stack (Backend, MongoDB, Prometheus) locally for integration testing.
- **Automated Pipeline Testing**: Every PR and push triggers the full test suite and security scans, ensuring no regressions or security flaws are introduced.

## Lessons Learned
- **Shift Left works**: Integrating tools like Bandit and pip-audit early in the CI process significantly reduces the cost and effort of fixing security bugs.
- **Automation is Key**: Manually running security scans is error-prone. Automating them in GitHub Actions ensures 100% compliance.
- **Observability is Security**: Monitoring metrics through Prometheus helps in detecting anomalies that could indicate a security breach or a performance bottleneck.
- **Documentation Matters**: Clear documentation for both developers and operators is essential for maintaining a secure DevSecOps culture.

---
**Project Repository**: [https://github.com/Nada2oo4/instapay-devsecops](https://github.com/Nada2oo4/instapay-devsecops)
**Role**: DevOps/DevSecOps Engineer
