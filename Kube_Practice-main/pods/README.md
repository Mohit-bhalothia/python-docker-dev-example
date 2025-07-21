### Kubectl and Pods

1. `kubectl get nodes`  
   List all nodes in the Kubernetes cluster.
2. `kubectl run nginx --image=nginx -n nginx`  
   Create a pod named nginx in the nginx namespace.
3. `kubectl describe pod nginx -n nginx`  
   Display detailed information about the nginx pod.
