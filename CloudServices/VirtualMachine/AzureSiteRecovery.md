## Azure Site Recovery

As an organization, you need to adopt a business continuity and disaster recovery (BCDR) strategy that keeps your data safe, and your apps and workloads online, when planned and unplanned outages occur.

Azure Recovery Services contributes to your BCDR strategy:

- Site Recovery service: Site Recovery helps ensure business continuity by keeping business apps and workloads running during outages. Site Recovery replicates workloads running on physical and virtual machines (VMs) from a primary site to a secondary location. When an outage occurs at your primary site, you fail over to a secondary location, and access apps from there. After the primary location is running again, you can fail back to it.
- Backup service: The Azure Backup service keeps your data safe and recoverable.
- Site Recovery contributes to your **business continuity and disaster recovery (BCDR) strategy**, by orchestrating and automating replication of Azure VMs between regions,

**Key Differences b/w Availability Zones and ASR:**

- Scope of Protection: AZs protect against failures within a region, while ASR provides protection against regional disasters.
- Data Replication: AZs use synchronous replication within the same region, while ASR typically uses asynchronous replication across regions.
- Use Cases: AZs are used for high availability and low-latency failover within a region. ASR is used for comprehensive disaster recovery planning and compliance across regions.

Azure Site Recovery is billed based on number of instances protected. Every instance that is protected with Azure Site Recovery is free for the first 31 days.
