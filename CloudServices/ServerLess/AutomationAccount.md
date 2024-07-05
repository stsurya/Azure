## Azure Automation Account

Azure automation account is the compute service which is suitable in scripting scenarios to automate repeated tasks.
An Azure Automation Account can have multiple "RUNBOOKS" - which is the component that executes a piece of code.
Azure automation accounts were mainly used for solving repeated admin operations (onboarding a user, offboarding a user, adding tags to resources, etc.). You can have PowerShell modules or Python packages imported in your runbook to perform slightly complicated tasks that Logic Apps would struggle with.

## Pricing for Azure Automation

Process automation includes runbook jobs and watchers. Billing for jobs is based on the number of job run time minutes used in the month, and for watchers, it is on the number of hours used in a month.
