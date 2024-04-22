# Azure Blob Storage

- Azure blob storage is a service that enables you to store massive amounts of unstructured data as bianry large objects or blobs in Cloud. Blobs are the efficient way to store the data files and our applicaiton can perform read and write operations by using Azure blob storage API.
- In an Azure storage account you store blobs in containers. Containers provide a convenient way of grouping related blobs.You control who can read and write blobs inside a container at the container level.

Blob storage provides three access tiers, which help to balance access latency and storage cost:

- **Hot Access Tier:** The Hot tier is the default. You use this tier for blobs that are accessed frequently.
- **Cool Access Tier:** The Cool tier has lower performance and incurs reduced storage charges compared to the Hot tier. Use the Cool tier for data that is accessed infrequently.
- **Archive Tier:** The Archive tier is intended for historical data that mustn't be lost, but is required only rarely. Blobs in the Archive tier are effectively stored in an offline state.
  Typical reading latency for the Hot and Cool tiers is a few milliseconds, but for the Archive tier, it can take hours for the data to become available.
  To retrieve a blob from the Archive tier, you must change the access tier to Hot or Cool. The blob will then be rehydrated. You can read the blob only when the rehydration process is complete.

You can create lifecycle management policies for blobs in a storage account to move the tier or to delete the blobs.
