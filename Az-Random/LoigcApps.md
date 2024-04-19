# Logic Apps

- Azure logic apps is a cloud service where you can create and run automated workflows with little to no code.
- By using Visual desginer and 1000+ pre-built operations we can design the workflow that integrates and manages the apps,data.
- A workflow is a series of steps to perform a task or business process. Each workflow will be having a trigger point, which is starting point of workflow. After the initial trigger, the remaining set of operations will be exectued one-by-one.
- The initial trigger can be anything something like an emain in inbox, or detecting a file in storage account.

Examples:

- Schedule and send email notifications using Office 365 when a specific event happens, exmaple when a new mail landed up in inbox.
- Route and process customer orders across on-premises systems and cloud services.
- Move uploaded files from an SFTP or FTP server to Azure Storage.
- Monitor tweets, analyze the sentiment, and create alerts or tasks for items that need review.

**Consumption Logic App** will only supports one workflow in multitenant
**Standard Logic App** will support multiple workflows in single tenant.

## Logic App Vs Function App

- Functions and logic apps are azure services that enables serverless workloads.
- Function apps are serverless compute service, whereas logic apps are serverless workflow integration platform.
- Both can be used to perform orchestrations. Orchestration means a bunch of functions in function apps or actions in azure logic apps to complete a task.
- We need to write code to build Functions, we can use GUI to build workgflows in logic apps.
- You can mix and match services when you build an orchestration, such as calling functions from logic app workflows and calling logic app workflows from functions.
