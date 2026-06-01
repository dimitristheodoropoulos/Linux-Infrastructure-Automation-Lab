# Ingress Configuration

Enable nginx ingress in Minikube:
```bash
minikube addons enable ingress
kubectl apply -f ingress.yaml
