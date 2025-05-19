# ✅ **DevOps & Cloud Security Interview Notes – By Surya Teja Chatrathi**

---

### 1. ❓ What is **Immutable Infrastructure**?

> Immutable infrastructure is a model where servers or components are **never modified after deployment**. Any change requires replacing the whole resource (e.g., create new VM/image).
>
> This ensures **consistency, repeatability, and reduced configuration drift**.

🟢 **Example**: Instead of patching a live VM, you build a new VM image using Packer and deploy it via Terraform.

---

### 2. 🔁 **Mutable vs Immutable Infrastructure (with Benefit)**

| Type          | Description                                | Example                       | Benefit                                       |
| ------------- | ------------------------------------------ | ----------------------------- | --------------------------------------------- |
| **Mutable**   | You can SSH into the VM and make changes.  | Manually installing packages. | Quick changes but prone to drift/errors.      |
| **Immutable** | VMs or containers are recreated on change. | Replacing VM with new image   | Stable, version-controlled, consistent infra. |

🎯 **Benefit of Immutable**: Predictable deployments and easier rollback.

---

### 3. 🔄 **RTO vs RPO** in Disaster Recovery

| Term    | Full Form                | Meaning                                            |
| ------- | ------------------------ | -------------------------------------------------- |
| **RTO** | Recovery Time Objective  | How fast you can recover after a failure.          |
| **RPO** | Recovery Point Objective | How much **data loss** (in time) you can tolerate. |

🧠 **Example**:
If RPO = 15 mins, max data loss = 15 mins.
If RTO = 2 hrs, system must be back within 2 hrs.

---

### 4. 💥 What is **Chaos Engineering**?

> Chaos Engineering is the practice of **intentionally injecting faults or failures** into systems to test their **resilience and recovery behavior**.

🧪 **Example**: Using tools like Chaos Monkey to randomly kill VMs in production to ensure auto-scaling works.

---

### 5. 👨‍💻 Who is a **Chaos Engineer**?

> A Chaos Engineer designs and executes experiments that simulate **real-world failures** to validate the reliability and robustness of systems.

---

### 6. 🔄 What is **GitOps**?

> GitOps is a DevOps practice where **Git is the source of truth** for both **application and infrastructure configurations**. Changes are made via **pull requests**, then automatically applied by CI/CD tools.

🛠️ **Tools**: ArgoCD, Flux

📌 **Example**: Change a Kubernetes deployment YAML in Git → Flux/ArgoCD detects and applies it automatically.

---

### 7. 🕵️ **Threat vs Vulnerability**

| Term              | Meaning                        | Example                     |
| ----------------- | ------------------------------ | --------------------------- |
| **Threat**        | Potential danger               | Hacker, malware             |
| **Vulnerability** | Weakness that can be exploited | Unpatched server, open port |

📌 **Example**:

- Threat = Attacker
- Vulnerability = Open RDP port
- Risk = Brute force login attempt via RDP

---

### 8. 🔐 What is **Zero Trust Security**?

> Zero Trust is a security model that says **“never trust, always verify”**—whether the user or device is inside or outside the network.

🎯 **Principles**:

- Verify explicitly (MFA, device posture, location)
- Least privilege access
- Assume breach

🧰 **Azure Example**:

- Use Azure AD + Conditional Access
- Managed Identity for resource access
- Private Endpoints for secure networking

---

### 9. 🔐 Zero Trust in Azure and CI/CD

🟦 **Azure Example**:

- Function App uses Managed Identity to access Key Vault
- Private Endpoints used for Key Vault & SQL
- Conditional Access to restrict admin access

🧪 **CI/CD Example**:

- Use Service Connections with RBAC
- Secrets stored in Azure Key Vault
- Validate deployments with security scans

---

### 10. 🌐 What is **DDoS (Distributed Denial of Service)?**

> A DDoS attack floods a service or network with **massive traffic** from many sources (botnet) to make it **unavailable**.

🎯 **Protection Strategies**:

- Azure DDoS Protection
- Web Application Firewall (WAF)
- Rate limiting & traffic filtering
- CDN for traffic absorption

---

### 11. How to prevent DDoS Attack ?

To prevent DDoS attacks, I use Azure DDoS Protection for automatic mitigation, Application Gateway with WAF for Layer 7 filtering, and implement rate limiting at API level. I also use private endpoints to restrict exposure, monitor traffic using Sentinel, and ensure the system is resilient with auto-scaling and CDN support.

---

Absolutely, Surya! Below are **interview-ready answers** for both your questions: **Cost Optimization Techniques** and **SLA vs. SLO vs. SLI**—tailored for your 3 years of DevOps experience.

---

## **12: What are some cost optimization techniques you’ve used in your projects?**

> In my projects, I actively implemented several cost optimization strategies to reduce unnecessary cloud spend while maintaining performance and security.
>
> - **Rightsizing resources:** I used Azure Advisor and Azure Monitor to analyze underutilized VMs, databases, and App Services, then downsized them accordingly. For example, we identified a set of VMs running at less than 10% CPU and moved them to lower SKUs.
> - **Auto-shutdown for Dev/Test VMs:** I configured automation accounts to shut down non-production VMs after working hours, saving significant compute costs.
> - **Azure Reservations and Hybrid Benefit:** For consistent workloads like production databases and VMs, we purchased reserved instances and applied Azure Hybrid Benefit to leverage on-prem licenses.
> - **Storage tiering and cleanup:** I used lifecycle management rules to move infrequently accessed blob data to Cool or Archive tiers, and periodically cleaned up unused snapshots and disks.
> - **Using a single App Gateway with path-based routing:** This reduced the number of instances and saved us about \$300/month.
> - **Self-hosted agents in Azure DevOps:** Instead of using Microsoft-hosted agents (which are billed per minute), I deployed and maintained self-hosted agents on existing infrastructure to avoid additional costs.
> - **Monitoring and budgeting:** I set up Azure Cost Management alerts and dashboards to track spending, and proactively addressed any spikes.
>
> Overall, my approach combines proactive monitoring, automation, and smart architecture decisions to ensure cost-effective cloud usage.

---

## **13: What is the difference between SLA, SLO, and SLI?**

> SLA, SLO, and SLI are related but serve different purposes in defining and maintaining service reliability:
>
> - **SLA (Service Level Agreement)** is a formal, contractual agreement between a service provider and a customer. It defines the minimum acceptable level of service and often includes financial penalties if not met. For example, Azure guarantees 99.95% uptime for VMs in an availability set.
>
> - **SLO (Service Level Objective)** is an internal performance target that the engineering or DevOps team aims to meet. It’s not legally binding but helps guide reliability goals. For instance, we might set an internal objective that 99.9% of API calls should respond in under 200ms.
>
> - **SLI (Service Level Indicator)** is the actual measured metric that reflects service performance. It's what we use to evaluate if we are meeting our SLOs. Examples include availability percentage, latency, or error rate.
>
> In short:
>
> - SLA is the **promise** to the customer.
> - SLO is the **goal** for internal teams.
> - SLI is the **measurement** we track to check performance.

---
