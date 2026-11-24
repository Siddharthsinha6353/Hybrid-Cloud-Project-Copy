# Hybrid Cloud Web Application using Docker, Kubernetes and Redis

**Student:** Siddharth Sinha | **Roll No.:** 2410030257  
**IILM University, Greater Noida | Section:** 3CSE2  
**Submitted to:** Mr. Rohit Kumar

## Overview
A small Flask web application stores a visit counter in Redis. The same application image is used in Docker Compose and Kubernetes. Kubernetes manifests include two web replicas, resource requests/limits, readiness checks and an HPA configuration (minimum 2, maximum 6, target CPU 50%).

## Local run
1. Install Docker Engine/Desktop with Docker Compose.
2. Run `docker compose up --build`.
3. Open `http://localhost:5000`.
4. In another terminal run `python load_test.py`.
5. Stop using `docker compose down`.

## Kubernetes run
Use a local Kubernetes cluster such as Minikube or kind for the private-cluster simulation. Build or load the container image into the cluster. Apply `kubectl apply -f k8s/private/`. Check `kubectl get pods,svc,hpa`. Delete one web pod to test self-healing: `kubectl delete pod <pod-name>`. Enable Metrics Server before expecting CPU-based HPA measurements.

## Hybrid-cloud simulation
The `k8s/public-simulated/` folder is a second, separate Kubernetes environment. Deploy the same app there after making the image available. This is a simulated second environment, not a real public-cloud account or a managed global failover service.

## GitHub
Profile: https://github.com/SiddharthSinha6353  
Repository URL provided: https://github.com/  
Replace this placeholder with the exact repository URL after creating the repository.

## Evidence
Add your own screenshots for Compose, running pods, readiness, pod recreation, HPA under load, second-cluster deployment and failover. Record actual measurements; do not use invented results.
