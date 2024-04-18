### KeyVault Secrets references in FunctionApps, LogicApps, WebApps

@Microsoft.KeyVault(SecretUri=https://<KeyVaultName>.vault.azure.net/secrets/PasswordName)

### Managed Identity to connect between storage account and function app. In function app configs you need to give Endpoints of storage account.

### Grant Databse access to Azure AD

```
az sql server ad-admin create --resource-group $(ResourceGroupName) --server-name $(server-name) --display-name ADMIN --object-id $(az ad user list --filter "userPrincipalName eq '$(userPrincipalName)'" --query [].id --output tsv)
```

### Grant SQL Database access to user-assigned MI

**Authentication type:** Active Directory - Password
Belwo SQL Script need to be run on the database

```
CREATE USER [$(<User-Managed-Identity>)] FROM EXTERNAL PROVIDER
ALTER ROLE db_datareader ADD MEMBER [$(<User-Managed-Identity>)]
ALTER ROLE db_datawriter ADD MEMBER [$(<User-Managed-Identity>)]

ALTER ROLE db_ddladmin ADD MEMBER [$(<User-Managed-Identity>)]

Grant view any column master key definition to [$(<User-Managed-Identity>)]
Grant view any column encryption key definition to [$(<User-Managed-Identity>)]
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
