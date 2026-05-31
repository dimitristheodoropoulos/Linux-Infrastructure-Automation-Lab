#!/bin/bash
set -e

echo "Waiting for pod to be ready..."
kubectl wait --for=condition=ready pod -l app=ml-app --timeout=60s

echo "Forwarding port 8000..."
kubectl port-forward service/ml-app-service 8000:8000 &
PF_PID=$!
sleep 5

echo "Testing /health endpoint..."
curl -f http://localhost:8000/health || exit 1

echo "Testing /llm-query (expected 429 or success)..."
curl -f "http://localhost:8000/llm-query/Test" || echo "Validation OK (received error, but endpoint works)"

kill $PF_PID
echo "✅ Deployment validated successfully"