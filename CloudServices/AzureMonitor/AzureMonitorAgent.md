## What's Azure Monitor Agent ?

- The purpose of Azure monitor agent is to collect logs from guest operating system and ingest them to log analytics workspace.

Before Azure monitor agent, there is another agent called Microsoft monitoring agent/log analytics agent which is deprecated now. 

challenege 1 - We need to use the worskapce ID and worksapce key in MMA, and this became a security concern, where as AMA uses managed Identity for Authentication.
challened 2 - Configuration is defined at workspace level. Each agent should have each workspace.

## Data Collection Rule(DCR)

- What type of data must be collected, either it's performance logs, secuirty logs, custom logs.
- How to transform the data ? - Data Transfromation should happen before the data ingestion, like deleteing few coulmns before isnerting to LAW.
- Where to send data ? - LAW

- Azure monitor Agent uses ETL(Extract Transform and Load) data ingestion pipeline