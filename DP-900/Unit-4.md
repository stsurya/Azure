# Relational Database services in Azure

Azure support multiple database services such as SQL Server, PostgresSQL, MySQL. All these services are managed by Azure by freeingup time to manage them.

Azure SQL is a collective term for a family of Microsoft SQL Server based database services in Azure. Azure SQL services include:

**1. SQL Server on Virtual Machine(VMs):**

- SQL Server is installed on Azure Virtual Machine. This is an IAAS solution which provides you the more flexibilty to manage all aspects of Operating system, database backups, updates, monitoring and other maintenance tasks.
- Best fit for lift and shift migrations without changes or minimal changes.
- SQL Server instances are installed on VM's can have multiple databases.

**2.Azure SQL Managed Instance:**

- This is a PAAS solution.
- Near 100% capability with SQL Server. Most on-premises databases can be migrated with minimal code changes.
- Each instance can have multiple databases.
- Fully automated updates and backups, less maintenance.
- use this option for lift and shift migrations, with minimal application changes.

**3.SQL Database**

- This is PAAS solution.
- You can create multipe databases within a single SQL server.
- This may not support most of the on-premises feature. This is fully automated backups, updates. Less maintenace.
- Use this option for new cloud solutions, or to migrate applications that have minimal instance-level dependencies.
