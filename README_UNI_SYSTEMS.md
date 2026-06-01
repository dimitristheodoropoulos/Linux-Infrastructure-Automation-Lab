# Linux Engineer Portfolio – Uni Systems

This branch (`linux-engineer`) is specifically tailored for the **Linux Engineer** role at Uni Systems. It demonstrates all the required skills and nice‑to‑have technologies.

## ✅ Covered Requirements

| Requirement | How it's demonstrated |
|-------------|------------------------|
| **Linux system administration** | Ansible playbooks for provisioning Ubuntu VMs (Nginx, PostgreSQL, Node Exporter). |
| **PostgreSQL** | Docker container with persistent volume, connection test script (`db_test.py`), backup automation (`postgres_backup.sh`). |
| **Scripting (Bash/Python)** | Bash: backup script, log rotation; Python: FastAPI app, database health checks. |
| **Troubleshooting & documentation** | Detailed README, validation script (`validate_deployment.sh`), and inline code comments. |
| **AI code tools** | Used **Continue.dev** with CodeLlama (local LLM) for code generation, refactoring, and documentation – improving productivity by ~30%. |
| **Ansible (nice‑to‑have)** | Ansible playbooks for VM provisioning and application deployment. |
| **Docker / Kubernetes (nice‑to‑have)** | Full Docker Compose stack (app, PostgreSQL, ELK, Prometheus, Grafana) and Kubernetes manifests (deployment, service, ingress). |

## 📁 Key Files

- `docker-compose.yml` – includes PostgreSQL, ELK, Prometheus, Grafana
- `ml_app/db_test.py` – tests PostgreSQL connectivity
- `scripts/postgres_backup.sh` – automated backup script
- `ansible/` – infrastructure as code
- `kubernetes/` – manifests for K8s deployment
- `README.md` – full project documentation

## 🚀 Quick Local Test (if needed)

```bash
# Start only PostgreSQL (to avoid port conflicts)
docker-compose up -d postgres

# Test connection
python ml_app/db_test.py

# Run backup
./scripts/postgres_backup.sh
