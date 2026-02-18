API + Worker Kubernetes Setup Guide

 setup using:

Docker

Kubernetes (Minikube)

Prometheus

Grafana

Horizontal Pod Autoscaler (HPA)

Prerequisites

Make sure the following tools are installed:

-Docker

- Minikube

- kubectl

- Helm

1. Install Docker
- curl -fsSL https://get.docker.com | sh
docker --version

2. Install Minikube
- curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

- minikube start --driver=docker


Verify cluster:

- kubectl get nodes

3. Create Namespaces (Environment Isolation)
- kubectl create namespace dev
- kubectl create namespace uat
- kubectl create namespace prod

4. Deploy Redis
- kubectl apply -f redis-deployment.yml -n <namespace>
- kubectl apply -f redis-service.yml -n <namespace>
- kubectl apply -f redis-exporter.yml -n <namespace>


Example:

kubectl apply -f redis-deployment.yml -n dev

5. Enable Horizontal Pod Autoscaler (HPA)

Enable metrics server in Minikube:

- minikube addons enable metrics-server


Verify:

- kubectl get pods -n kube-system

6. Install Prometheus and Grafana
Install Helm
- curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

Add Prometheus Helm Repository
- helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
- helm repo update

Install kube-prometheus-stack
- helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace

7. Access Grafana

Get Grafana admin password:

- kubectl get secret prometheus-grafana \
  -n monitoring \
  -o jsonpath="{.data.admin-password}" | base64 --decode


Port forward:

- kubectl port-forward svc/prometheus-grafana 3000:80 -n monitoring


Open in browser:

http://localhost:3000

Monitoring Strategy

Monitor the following metrics:

- Error rate

- Latency (P95 / P99)

- CPU usage

- Memory usage

- Pod restarts

Handling API Crash During Peak Hour

To reduce downtime:

- Use liveness probe:
Automatically restarts crashed containers.

- Use readiness probe:
Stops traffic to unhealthy pods.

- Enable HPA:
Scale pods automatically during peak load.

- Use LoadBalancer or Ingress:
Distribute traffic properly.

Handling Bad Deployment

Monitor system behavior after deployment:

- Error rate spike

- Latency spike

- CPU or memory spike

- Pod crash loops

- Rollback Deployment

If deployment causes issues:

- kubectl rollout undo deployment/api -n <namespace>


Example:

- kubectl rollout undo deployment/api -n prod


Check rollout history:

- kubectl rollout history deployment/api -n prod