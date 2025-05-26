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

## 3. How to save costs on k8s ?

- Right sizing the resources: I define accurate CPU and memory requests/limits for pods based on historical usage.
- Cluster and Pod Autoscaling: I enable the Cluster Autoscaler to automatically scale node pools based on demand, and configure the Horizontal Pod Autoscaler (HPA) and Vertical Pod Autoscaler (VPA) to dynamically adjust workloads based on metrics.
- use spot instances.
- Idle reasource cleanup like unused PVC's or namespaces..
- Schedule based scalings.
- Cost monitoring tools like azure adivisor and optimize based on metrics.

## 4. Expalin Blue-Green Deployment in k8s ?

Certainly, Surya! Here's an **interview-ready explanation** of **Blue-Green Deployment** in Kubernetes, followed by a **practical -based example** 👇

---

### ✅ **What is Blue-Green Deployment in Kubernetes?**

**Blue-Green Deployment** is a release strategy where you run **two environments**—one **live (blue)** and one **idle (green)**—to deploy new versions of an application with **zero downtime and easy rollback**.

- **Blue** = current stable version serving traffic
- **Green** = new version deployed in parallel
- Once verified, traffic is switched to green by updating the service selector.

---

### 🎯 **When to Use It**

- You need **zero-downtime deployments**
- Rollback needs to be **instant and safe**
- Useful for **mission-critical services**

---

### 📄 **Kubernetes Blue-Green Deployment Example**

Let’s assume you're deploying a web app.

---

#### 1. **Blue Deployment (existing)**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-blue
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
      version: blue
  template:
    metadata:
      labels:
        app: web
        version: blue
    spec:
      containers:
      - name: web
        image: myapp:v1
        ports:
        - containerPort: 80
```

---

#### 2. **Green Deployment (new version)**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-green
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
      version: green
  template:
    metadata:
      labels:
        app: web
        version: green
    spec:
      containers:
      - name: web
        image: myapp:v2
        ports:
        - containerPort: 80
```

---

#### 3. **Service (Traffic switch happens here)**

```
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web
    version: blue  # <-- Initially points to blue
  ports:
  - port: 80
    targetPort: 80
```

---

### 🔄 **To Switch from Blue to Green**

Just patch or update the service selector:

```
spec:
  selector:
    app: web
    version: green
```

You can use `kubectl patch`:

```bash
kubectl patch service web-service -p '{"spec":{"selector":{"app":"web","version":"green"}}}'
```

---

### ✅ **Rollback**

If something goes wrong, revert the selector back to `version: blue`.

---

### 🧠 **Interview Soundbite**:

> “In Kubernetes, I implement blue-green deployments by maintaining two deployments with different labels (e.g., `version: blue` and `version: green`). I switch traffic by updating the service selector. This ensures zero downtime and easy rollback, making it ideal for production releases.”

---
