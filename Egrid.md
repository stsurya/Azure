## Difference between Azure Event Grid System topics and Custom topics ?

### System topics

Represent one or more events published by Azure services, such as Azure Storage and Azure Event Hubs. For example, a system topic may represent all blob events or only blob created and blob deleted events published for a specific storage account. System topics do not have endpoints or access keys for publishing events.

### Custom topics

Are used with third-party applications. They are self-standing resources that expose their own endpoint to which events are published.
