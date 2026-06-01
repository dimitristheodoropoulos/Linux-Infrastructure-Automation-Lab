# Advanced DevOps Infrastructure Components

This branch (`advanced-devops`) adds production‑grade infrastructure components:

- **Terraform** – Infrastructure as Code (Docker provider demo)
- **Ingress Controller (nginx)** – path‑based routing, TLS termination
- **Helm** – package manager for Kubernetes (chart included)
- **Istio** – service mesh (canary releases, mTLS, traffic splitting)

## How to use

| Component | Location | Commands |
|-----------|----------|----------|
| Terraform | `terraform/` | `cd terraform && terraform init && terraform apply` |
| Ingress | `kubernetes/ingress/` | `minikube addons enable ingress && kubectl apply -f ingress.yaml` |
| Helm | `kubernetes/ml-app-chart/` | `helm install ml-app ./ml-app-chart` |
| Istio | `istio/` | `./install.sh` (needs internet) |

## Link to this branch

[https://github.com/dimitristheodoropoulos/Linux-Infrastructure-Automation-Lab/tree/advanced-devops](https://github.com/dimitristheodoropoulos/Linux-Infrastructure-Automation-Lab/tree/advanced-devops)
