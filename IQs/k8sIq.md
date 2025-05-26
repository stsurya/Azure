## 1. What is Service Mesh ?

- A Service Mesh is a dedicated infrastructure layer that facilitates secure, fast and reliable communicaiton between services.
- A Service mesh is typically implemented by using sidecar proxy alongside the each microservice container, intercepting and managing the network.
- Popular service mesh implementation includes istio, Consul, Linkerd
  **Problems solved by service mesh:**
  - Advance traffic management: It allows fine-grained traffic control using routing rules. You need to do canary deployments, blue-green deployments, or A/B testing.
  - You want zero-trust security where all communication is encrypted and services are authenticated. It enables automatic mTLS (mutual TLS) between services without changing application code.
  - You want insight into service communication, like latency, request count, and distributed tracing.

## 2. What are sidecar containers ?

- A SideCar container is the secondary container inside the same pod, which are commonly used for logging, networking and traffic-management purposes without modifying the application code.
