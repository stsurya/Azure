## Azure SQL Database

Azure SQL Database is fully managed, cloud-based relational database service offered by Azure. It allows us to create, scale and manage databases without managing the underlying infrastructure.

### Purchasing Models

There are two purchasing models in SQL

**i) vCore-based purchasing model:**

- Choose the exact resources you need (like CPU, memory, and storage).
- Pay only for what you use.

**ii) DTU-based purchasing model:**

- Get a bundle of resources (compute, memory, and I/O) in three tiers (Basic, Standard, Premium).
- Each tier has different levels of resources (like CPU, memory, and storage).
- Can add more storage if needed.

### Service Tiers

The vCore-based purchasing model provides three service tiers: **General Purpose** is for common workloads, **Business Critical** is for high-performance apps, and **Hyperscale** is for flexible and scalable business workloads.

The DTU-based purchasing model offers two tiers Standard tier and Premium tier. Standard tier is for common workloads. It offers budget-oriented balanced compute and storage options. Premium tier if for OLTP applications with high transaction rates and low latency I/O requirements. It offers the highest resilience to failures by using several isolated replicas.

## Compute tiers

The vCore-based purchasing model provides two different compute tiers for Azure SQL Database - the provisioned compute tier, and the serverless compute tier. The DTU-based purchasing model provides just the provisioned compute tier.

**Provisioned compute tier:** provides a specific amount of compute resource that is continuously provisioned independent of workload activity, and bills for the amount of compute provisioned at a fixed price per hour.
**Serverless compute tier:** automatically scales compute resources based on workload activity and bills for the amount of compute used, per second. The serverless compute tier is generally available in the General Purpose service tier and in the Hyperscale service tier.

## 1. SQL Server on Virtual Machine(VMs):

- SQL Server is installed on Azure Virtual Machine. This is an IAAS solution which provides you the more flexibilty to manage all aspects of Operating system, database backups, updates, monitoring and other maintenance tasks.
- Best fit for lift and shift migrations without changes or minimal changes.
- SQL Server instances are installed on VM's can have multiple databases.

# 2.Azure SQL Managed Instance:

- This is a PAAS solution.
- Near 100% capability with SQL Server. Most on-premises databases can be migrated with minimal code changes.
- Each instance can have multiple databases.
- Fully automated updates and backups, less maintenance.
- Use this option for lift and shift migrations, with minimal application changes.
