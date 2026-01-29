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

C:\WindowsAzure\Resources\AMADataStore.ExchangeServer\mcs\configchunks - The json file is stored in this location which is DCR.

## Custom logs ingestion

- In DCR by using Xpath queries you can send the required logs to the LAW.
- Goto Event Viewer on Windows server, select and DNS Server or any other event enable the required logs like Critical, Warning, Verbose, Error, Information.
-  Click on XML, pick the XML and paste on notepad, remove the tags, pick the only line in DNS Server*![System[(Level=1 or Level=2 or Level=3)]]
- Goto Azure portal, DCR and psate it in the Xpath query and they'll autmatically reflect in your VM as well, and LAW will start collecting the logs as well.