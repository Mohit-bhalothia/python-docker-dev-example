### Deployments

1. `kubectl apply -f deployment.yml`  
   Deploy a workload defined in `deployment.yml`.
2. `kubectl scale deployment nginx-deployment --replicas=3 -n nginx`  
   Scale the deployment to 3 replicas.
