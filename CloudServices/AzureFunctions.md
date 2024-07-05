## Azure Functions

Azure Functions is a serverless solution that allowas you to write less code, maintain less infrastructure, and save on costs. Instead of worrying about deploying and maintaing the servers, the cloud infrastructure provides all the up-to-date resources needed to keep your applications running.

## Azure Functions support availiability Zones

- Availiability zones is only supported on Premium Plan.
- You cannot convert the existing function app to availiability zones.
- You must use ZRS fro your function app storage account otherwise it may show unexpected behavior during a zonal outage.
- Availability zone support isn't currently available for function apps on Consumption plans.

## What is a Cold Start in Azure Function Apps?

A cold start in function app occurs when latency is experienced when a function app is invoked after being idle for sometime. This latency is due to the time it takes to initialize the function's runtime environment and load the necessary application code and dependencies before the function can handle the incoming request.
