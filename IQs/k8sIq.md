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

## 5. Explain Canary deployment model in k8s ?

## ✅ What is Canary Deployment in Kubernetes?

**Canary deployment** is a progressive delivery strategy where you **release a new version of your application to a small subset of users** first (like 10%) and **gradually increase the traffic**. This helps test stability in production without impacting all users.

- Safer than full rollout
- Easy rollback
- Real traffic validation

---

### 🧠 Interview Soundbite:

> "In Kubernetes, I implement canary deployments by running both old and new versions of the app with different labels. I use weighted traffic distribution using multiple services or tools like Istio, Linkerd, or NGINX Ingress to shift traffic gradually."

---

## 🧪 Basic Example without Service Mesh (using 2 Deployments + 2 Services)

We’ll simulate traffic splitting manually by using two services and controlling access (not true weighted routing but basic canary logic).

---

### 1️⃣ **Stable Deployment (v1)**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-stable
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: stable
  template:
    metadata:
      labels:
        app: myapp
        version: stable
    spec:
      containers:
      - name: app
        image: myapp:v1
        ports:
        - containerPort: 80
```

---

### 2️⃣ **Canary Deployment (v2)**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-canary
spec:
  replicas: 1
  selector:
    matchLabels:
      app: myapp
      version: canary
  template:
    metadata:
      labels:
        app: myapp
        version: canary
    spec:
      containers:
      - name: app
        image: myapp:v2
        ports:
        - containerPort: 80
```

---

### 3️⃣ **Service for Stable**

```
apiVersion: v1
kind: Service
metadata:
  name: app-stable-svc
spec:
  selector:
    app: myapp
    version: stable
  ports:
  - port: 80
    targetPort: 80
```

---

### 4️⃣ **Service for Canary**

```
apiVersion: v1
kind: Service
metadata:
  name: app-canary-svc
spec:
  selector:
    app: myapp
    version: canary
  ports:
  - port: 80
    targetPort: 80
```

---

### ⚙️ How Canary Traffic Works in This Setup

- Route **90% of traffic** to `app-stable-svc`
- Route **10% of traffic** to `app-canary-svc`
- You can control this via **DNS**, **Ingress rules**, or **API Gateway** (like NGINX or Istio)

---

## ✅ Advanced (True Canary) with Istio

If you want **real traffic splitting (e.g., 90/10)**, use **Istio’s VirtualService** like this:

```
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: myapp
spec:
  hosts:
  - myapp.example.com
  http:
  - route:
    - destination:
        host: myapp
        subset: stable
      weight: 90
    - destination:
        host: myapp
        subset: canary
      weight: 10
```

This lets Istio split traffic **evenly at the request level**, which is not possible with just Kubernetes Services alone.

---

## 🧼 Rollout Strategy

1. Start with 10% traffic to canary.
2. Monitor performance/logs/metrics.
3. Gradually increase to 50%, 100% if stable.
4. If issues, route 100% back to stable.

---
