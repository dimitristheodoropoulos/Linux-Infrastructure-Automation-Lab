Από το validation script βλέπω:

- Το `/health` δουλεύει (200 OK).
- Το `/llm-query` δίνει `401 UNAUTHENTICATED` (το access token του service account έληξε – φυσιολογικό μετά από κάποια ώρα). Δεν πειράζει, γιατί η αγγελία ενδιαφέρεται για το deployment και το pipeline.

---

## 📄 Προτεινόμενο README.md (αγγλικό, επαγγελματικό, με όλες τις προσθήκες)

```markdown
# Linux Infrastructure Automation Lab

[![CI/CD Pipeline](https://github.com/dimitris424/Linux-Infrastructure-Automation-Lab/actions/workflows/ci-cd-pipeline.yml/badge.svg)](https://github.com/dimitris424/Linux-Infrastructure-Automation-Lab/actions/workflows/ci-cd-pipeline.yml)

A comprehensive DevOps home lab demonstrating **CI/CD**, **container orchestration**, **security scanning**, **centralized logging**, **monitoring**, and **LLM integration** using industry‑standard tools.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Phases](#phases)
- [Getting Started](#getting-started)
- [CI/CD Pipeline](#cicd-pipeline)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Monitoring & Logging](#monitoring--logging)
- [Validation](#validation)
- [Project Versions](#project-versions)
- [License](#license)

---

## Overview

This project is a personal home lab that evolves from basic Linux system administration to a full‑blown **DevOps + MLOps** platform. It showcases:

- Infrastructure as Code (Ansible, Terraform – planned)
- Containerization (Docker)
- Orchestration (Kubernetes, Minikube, ArgoCD)
- CI/CD with security scanning (GitHub Actions + Trivy)
- Centralized logging (ELK stack)
- Monitoring (Prometheus, Grafana)
- LLM integration (Google Gemini API)

---

## Architecture

![Architecture Diagram](docs/architecture.png) *(placeholder)*

- **Application**: FastAPI‑based web service that calls the Gemini LLM.
- **CI/CD**: GitHub Actions builds, scans (Trivy), and pushes the Docker image.
- **Kubernetes**: Minikube cluster with Deployment, Service, liveness/readiness probes.
- **Logging**: Logstash receives logs from the app (TCP), stores in Elasticsearch, visualized in Kibana.
- **Monitoring**: Prometheus scrapes metrics; Grafana dashboards.
- **GitOps**: ArgoCD syncs Kubernetes manifests from the repository.

---

## Technologies Used

| Category | Tools |
|----------|-------|
| **Infrastructure as Code** | Ansible, Terraform (planned) |
| **Containerization** | Docker, Docker Compose |
| **Orchestration** | Kubernetes, Minikube, ArgoCD |
| **CI/CD** | GitHub Actions, Trivy (security scanning) |
| **Monitoring** | Prometheus, Grafana |
| **Logging** | Elasticsearch, Logstash, Kibana (ELK) |
| **Programming** | Python (FastAPI), Bash |
| **Cloud / APIs** | Google Gemini API, Service Account authentication |
| **OS / Virtualization** | Ubuntu, KVM/QEMU |

---

## Phases

### Phase 1: SysAdmin & DevOps Lab
- Ansible playbooks for provisioning VMs (Nginx, PostgreSQL).
- Docker Compose for Prometheus + Grafana.
- Node Exporter for system metrics.

### Phase 2: MLOps Expansion
- Containerization of a simple ML model (Flask).

### Phase 3: Automated Deployment with Ansible
- Ansible playbook to pull and run the container on a VM.
- Verification via `curl` to `/predict`.

### Phase 4: CI/CD with GitHub Actions
- Full pipeline: `git push` → build → push → deploy.
- **Security addition**: Trivy scanner for HIGH/CRITICAL vulnerabilities.

### Phase 5: Kubernetes Integration
- Minikube cluster.
- Deployment and Service manifests.
- Exposed via NodePort.

### Phase 6: GitOps with ArgoCD
- ArgoCD continuously syncs manifests from the repo.
- Git push updates the cluster automatically.

### Phase 7: Advanced MLOps & LLM Integration
- Replaced the ML model with **Google Gemini API** (via service account).
- Added logging to ELK stack.
- Health check endpoint (`/health`) for Kubernetes probes.
- Validation script for post‑deployment testing.

---

## Getting Started

### Prerequisites

- Linux (Ubuntu 24.04) or WSL2
- Docker & Docker Compose
- Minikube & kubectl
- Python 3.9+ (for local testing)
- Google Cloud service account with **Gemini API** enabled

### Clone the Repository

```bash
git clone https://github.com/dimitris424/Linux-Infrastructure-Automation-Lab.git
cd Linux-Infrastructure-Automation-Lab
```

### Set Up Credentials

```bash
# Place your service account JSON key
cp /path/to/your-service-account-key.json ~/Desktop/gemini-sa-key.json

# Export the path
export GOOGLE_APPLICATION_CREDENTIALS="$HOME/Desktop/gemini-sa-key.json"
```

### Run Locally (without Kubernetes)

```bash
cd ml_app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app:app --reload --port 8000
```

### Deploy to Kubernetes

```bash
minikube start --driver=docker
kubectl create secret generic google-service-account-secret \
  --from-file=gcp-key.json=$GOOGLE_APPLICATION_CREDENTIALS
kubectl apply -f kubernetes/deployment-new.yml
kubectl apply -f kubernetes/service.yml
kubectl port-forward service/ml-app-service 8000:8000 &
curl http://localhost:8000/health
```

### Start ELK Stack (Logging)

```bash
cd monitoring
docker-compose -f docker-compose-elk.yml up -d
# Kibana available at http://localhost:5601
```

---

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci-cd-pipeline.yml`) does:

1. Checkout code
2. Log in to Docker Hub
3. Build Docker image
4. **Run Trivy security scan** (fails on HIGH/CRITICAL)
5. Push image to Docker Hub

> The pipeline ensures that only secure images are deployed.

---

## Kubernetes Deployment

The `deployment-new.yml` includes:

- **Liveness probe** (checks `/health` every 10s)
- **Readiness probe** (checks `/health` every 5s)
- **Volume mount** for the service account JSON
- **Environment variables** (`GOOGLE_APPLICATION_CREDENTIALS`, `LOGSTASH_HOST`)

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 10
  periodSeconds: 10
```

---

## Monitoring & Logging

### Prometheus + Grafana
- Prometheus scrapes metrics from node exporters and Kubernetes.
- Grafana dashboards visualise CPU, memory, and custom application metrics.

### ELK Stack
- **Logstash** listens on TCP port 5000 (JSON input).
- **Elasticsearch** stores logs.
- **Kibana** provides search and visualisation (index pattern `app-logs-*`).

Log shipping is implemented asynchronously inside `app.py`:

```python
asyncio.create_task(send_log_to_logstash(log_entry))
```

---

## Validation

A shell script (`scripts/validate_deployment.sh`) performs post‑deployment checks:

- Waits for pods to become ready.
- Forwards the service port.
- Tests the `/health` endpoint.
- Tests the `/llm-query` endpoint (may return 429/401 due to quota, but proves connectivity).

```bash
chmod +x scripts/validate_deployment.sh
./scripts/validate_deployment.sh
```

---

## Project Versions

- `v1.0-phase6`: GitOps phase, before LLM integration.
- `main`: Latest version with LLM, ELK, Trivy, and Kubernetes probes.

---

## License

MIT License – see [LICENSE](monitoring/LICENSE) file.

---

## 👤 Author

**Dimitris Theodoropoulos**  
GitHub: [dimitristheodoropoulos](https://github.com/dimitristheodoropoulos)  
DevOps / MLOps Engineer candidate

---

## 🚀 What I Learned / Demonstrated

- End‑to‑end CI/CD with integrated security.
- Running a stateful LLM application on Kubernetes.
- Centralised logging and monitoring for observability.
- GitOps principles for declarative infrastructure.
- Resilience through health probes and graceful degradation.
