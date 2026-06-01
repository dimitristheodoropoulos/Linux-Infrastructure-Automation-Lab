# Terraform Demo

This folder demonstrates Infrastructure as Code using Terraform (Docker provider).  
In a real production environment, this would provision cloud resources or a Kubernetes cluster.

## Usage

```bash
cd terraform
terraform init
terraform plan
terraform apply -auto-approve
terraform destroy -auto-approve
