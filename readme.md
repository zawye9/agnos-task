Prerequisites
 - docker 
 - minikube

 Install docker
  curl -fsSL https://get.docker.com | sh
  docker --version
 Install miniKube
  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start --driver=docker

Create the Namespace for Envrionment 
 kubectl create namespace dev
 kubectl create namespace uat
 kubectl create namespace prod
 Deploy Redis
 k apply -f redis-deployment.yml -n {namespace}
 k apply -f redis-service.yml -n {namespace}
 k apply -f redis-exporter.yml -n {namespace}

For HPA 
 enble metrics server
  minikube addons enable metrics-server

Install Prometheus  (with Helm)
 install helm 
  curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
  add helm repo
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm repo update
install Prometheus
  helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace
install Grafana 
  kubectl get secret prometheus-grafana \
  -n monitoring \
  -o jsonpath="{.data.admin-password}" | base64 --decode
kubectl port-forward svc/prometheus-grafana 3000:80 -n monitoring
--------------------------------------------------------------------------
Handling API crash in peak hour
liveness probe to restart crash container
readiness probe to stop sending the request to crash pod
setup HPA and setup loadbalancer
-----------------------------------------------------------------------
For Bad deployment
Monitoring using Grafana and prometheus 
base on these metrics
error rate 
latency spike
cpu/memory spike 
and roll out to the stable deployment
kubectl rollout undo deployment/api -n {namespace}


