### KeyVault Secrets references in FunctionApps, LogicApps, WebApps

```
@Microsoft.KeyVault(SecretUri=https://<KeyVaultName>.vault.azure.net/secrets/PasswordName)
```

### Managed Identity to connect between storage account and function app. In function app configs you need to give Endpoints of storage account.

### Grant Databse access to Azure AD

```
az sql server ad-admin create --resource-group $(ResourceGroupName) --server-name $(server-name) --display-name ADMIN --object-id $(az ad user list --filter "userPrincipalName eq '$(userPrincipalName)'" --query [].id --output tsv)
```

### Grant SQL Database access to user-assigned MI

**Authentication type:** Active Directory - Password
**Below SQL Script need to be run on the database**

```
CREATE USER [$(<User-Managed-Identity>)] FROM EXTERNAL PROVIDER
ALTER ROLE db_datareader ADD MEMBER [$(<User-Managed-Identity>)]
ALTER ROLE db_datawriter ADD MEMBER [$(<User-Managed-Identity>)]

ALTER ROLE db_ddladmin ADD MEMBER [$(<User-Managed-Identity>)]

Grant view any column master key definition to [$(<User-Managed-Identity>)]
Grant view any column encryption key definition to [$(<User-Managed-Identity>)]
```

**Below SQL Script is to check the access of USer Assigned MI on Database**

```
SELECT r.name role_principal_name, m.name AS member_principal_name

FROM sys.database_role_members rm

JOIN sys.database_principals r

    ON rm.role_principal_id = r.principal_id

JOIN sys.database_principals m

    ON rm.member_principal_id = m.principal_id

where m.name = '<User-Assigned-MI>'
```

### Creating CMK and CEK Subscriber keys in Databsae

```
# Define your Key Vault and SQL Server details
$KeyVaultName = "$(keyVaultName)"
$KeyVaultKeyName = "$(keyName)"
$ServerName = "sqldb-uks-$(env)-db.database.windows.net"
$DatabaseName = "$(SqlDBName)"
$SqlServerAdminUser = "$(adminuser)"
$SqlServerAdminPassword = "$(dbPassword)"

# Connect to Azure Key Vault
$KeyVaultKey = Get-AzKeyVaultKey -VaultName $KeyVaultName -Name $KeyVaultKeyName

# Connect to your SQL Server
$ConnectionString = "Server=$ServerName;Database=$DatabaseName;User Id=$SqlServerAdminUser;Password=$SqlServerAdminPassword;MultipleActiveResultSets=true;"

# Import the SQL Server module
Import-Module "SqlServer"

# Establish a connection to the database
$Database = Get-SqlDatabase -ConnectionString $ConnectionString

# Create column master key settings for your Key Vault key
$KeyVaultKeyURL = $KeyVaultKey.Key.Kid
$CMKSettings = New-SqlAzureKeyVaultColumnMasterKeySettings -KeyURL $KeyVaultKeyURL

# Obtain an access token for the Key Vault
$KeyVaultAccessToken = (Get-AzAccessToken -ResourceUrl https://vault.azure.net).Token

# Create or open the column master key in the database
$CMKName = "CMK_Subscriber"
try {
    $ExistingCMK = Get-SqlColumnMasterKey -Name $CMKName -InputObject $Database
    Write-Host "Column Master Key already exists."
} catch {
    $NewCMK = New-SqlColumnMasterKey -Name $CMKName -InputObject $Database -ColumnMasterKeySettings $CMKSettings
    Write-Host "Column Master Key created."
}

# Generate a column encryption key and bind it to the column master key
$CEKName = "CEK_Subscriber"
$CEK = New-SqlColumnEncryptionKey -Name $CEKName -InputObject $Database -ColumnMasterKey $CMKName -KeyVaultAccessToken $KeyVaultAccessToken
Write-Host "Column Encryption Key created and bound to Column Master Key."
```

**To switch to the subscription on Azure CloudShell**
`az account set --subscription c56e18b5–23ce-4d2c-ac8c-35d3c9bc7e0f` (use your own subscription id)

**Powershell script to get the PrimaryConnectionString of Eventhub Namespace of RootManageSharedAccessKey**

```
$eventhubConnString = (Get-AzEventHubKey -ResourceGroupName rg-uks-dev-core -NamespaceName ehubns-uks-dev-trafficdata -AuthorizationRuleName RootManageSharedAccessKey).PrimaryConnectionString
```

### To keep the stages manual in azure devops YAML pipeline.

```
condition: eq(variables['Build.Reason'], 'Manual')
```

### Fetching the IP of Microsoft-Hosted Agents

```
$IP= Invoke-RestMethod http://ipinfo.io/json | Select -exp ip
$IP
```
