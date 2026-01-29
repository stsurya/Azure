## What's DCR ?

- DCR is basicually a configuration, which lets the azure monitor agent know, what type of data must be captured and forwarded to data ingestion pipeline, then are there any transformaiton which must be applied before the data gets ingested to the workspace and where exactly the data must be ingested, precisely speaking to which table of worksapce.

- DCR's can be created for windows, linux and other pllatforms as well where you might use data ingestion API of log analytics workspace.

- Data Collection rule only be applied to Azure VM or Azure Arc-enabled servers, which means that you must onboard your on-prem, aws, GCP virtual machines to Azure Arc before you can deploy Azure Monitor Agent.

## Which Platform ?

- Windows
    - Performance logs.
    - Windows events.
- Linux
    - Performance logs.
    - Syslog
- All
    - IIS
    - Custom Text
    - Custom JSON.

- Whenever any resource is added to data collection rule, Azure monitor agent is installed automatically.

## Required Permissions

Monitoring Contributor
Virtual Machine Contributor
Azure Connected Machine Resource Adminstrator
- Deploy agent extensions to Azure Arc enabled servers.

- To deploy Azure Monitor Agent from azure portal, you've to create DCR and then associate the resource with the DCR.
- Azure monitor agent will be installed automatically in the form of extension.