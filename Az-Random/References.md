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

### Creating CMK and CEK Subscriber keys in Database

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
`az account set --subscription 6de23055-fc3a-4da6-a2de-fd4239c22fa7` (use your own subscription id)

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

### Fetching the Function app function URL in Azure.

```
$FunctionAppName = "<FuncApp Name>"
$GroupName = "<resource grp name>"
$Id = (Get-AzFunctionApp -ResourceGroupName $GroupName -Name $FunctionAppName).Id
$url = (Get-AzWebApp -ResourceGroupName $GroupName -Name $FunctionAppName).EnabledHostNames[0]
$Code = (Invoke-AzResourceAction -ResourceId "$Id/functions/<functionname>" -Action listkeys -Force).default

$FuncURL = "https://$url/api/<functionname>?code=$Code"
```

### Powershell to Fetch access key of event grid

```
(Get-AzEventGridTopicKey -ResourceGroup <ResourceGroup> -Name <EventGridName>).key1
```

### Powershell to Fetch System Assigned Identity of Azure resource.

```
(Get-AzADServicePrincipal -DisplayName '<ResourceName>').Id
```

### Powershell to fetch SAS token for storage account

```
$account_key = (Get-AzStorageAccountKey -ResourceGroupName $resourceGroupName -Name $StorageAccountName)[0].Value
$context = New-AzStorageContext -StorageAccountName $StorageAccountName -StorageAccountKey $account_key
$CommonStorageAccSASToken = New-AzStorageAccountSASToken -Service Blob,File,Table,Queue -ResourceType Service,Container,Object -Permission "racwlup" -Context $context -ExpiryTime 2024-08-22
```

### Powershell to fetch connection string of storage account

```
$storageAccountKeys = Get-AzStorageAccountKey -ResourceGroupName $resourceGroupName -AccountName $StorageAccountName
$storageAccountKey = $storageAccountKeys[0].Value
$CommonStorageAccConnectionString = "DefaultEndpointsProtocol=https;AccountName=$StorageAccountName;AccountKey=$storageAccountKey;EndpointSuffix=core.windows.net"
```

# Compare two KeyVaults and will create an excel

```
$keyVaults = @('<KeyVaultName01>', '<KeyVaultName02>')

$hashTable = $null
$hashTable = @{}
$resourceKey = ''

foreach($keyVaultName in $keyVaults)
{
    Write-Host 'Getting secrets from keyvault: ' $keyVaultName

    $secrets = Get-AzKeyVaultSecret -VaultName $keyVaultName

    foreach($secret in $secrets)
    {
        $secretName = $secret.Name

        if($hashTable.ContainsKey($secretName) -eq $false)
        {
            Write-Host 'Adding new secret to model'


            $azureResource = New-Object -TypeName psobject
            $azureResource | Add-Member -MemberType NoteProperty -Name 'Secret' -Value $secretName

            foreach($v in $keyVaults)
            {
                $azureResource | Add-Member -MemberType NoteProperty -Name $v -Value ''
            }

            $hashTable.add($secretName, $azureResource)

            Write-Host 'New Resource added: ' $secretName
        }


        $azureResource = $hashTable[$secretName]
        $azureResource.$keyVaultName = 'YES'
    }
}


$hashTable.GetEnumerator() | sort name
$resourceList = [System.Collections.ArrayList]::new();
foreach($val in $hashTable.Values)
{
    $resourceList.Add($val)
}

$resourceList | Export-Csv -Path C:\Temp\KeyVaultSecretMatrix.csv
```

### Powershell script to update the chrome on microsoft hosted agents to latest version.

```
# Below line is to get the current version of Chrome.
$chromeVersion = ((Get-Item "C:\Program Files\Google\Chrome\Application\chrome.exe").VersionInfo).ProductVersion

Write-Host "Current version before=" $chromeVersion

$theurl = "http://dl.google.com/edgedl/chrome/install/GoogleChromeStandaloneEnterprise64.msi"

mkdir c:\tmp

$output = "c:\tmp\chrome.msi"

Invoke-WebRequest -Uri $theurl -OutFile $output -ErrorAction SilentlyContinue

msiexec /q /i c:\tmp\chrome.msi

start-sleep -Seconds 300 # sleep for 5 mins just to allow updates to be processed

Remove-Item -Path c:\tmp\chrome.msi –Force
```

### checking the connection b/w function app and redis cache

`tcpping rc-uks-<env>-SubscriberPortal.redis.cache.windows.net:6380`

### How to hide terminal path while using PowerShell?

`function prompt {"PS >"}`

```
function prompt {
    "$(Split-Path -Leaf $PWD)> "
}
```

### How to increase the C drive of Windows VM in Azure ?

1. Increase the OS disk on Azure portal for the VM.
2. Login to the VM and
   **Open Disk Management:**

- You can do this by right-clicking on the Start menu and selecting Disk Management, or by typing diskmgmt.msc in the Run dialog.
- In Disk Management, you should see the C: drive with its original size (127 GB) and unallocated space representing the additional disk space you added.
- Right-click on the C: drive and select Extend Volume.
- Follow the wizard to extend the C: drive to use the unallocated space, which will increase the partition size up to the full 256 GB.

### How to remove the long path of WSL on vs code ?

1. nano ~/.bashrc
2. check for variable PS1=
3. Simplify the path to only show the current directory: Replace \w with \W, which shows only the current directory name instead of the full path.
   The modified code looks like below:

```
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\W\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \W\a\]$PS1"
    ;;
*)
    ;;
esac

```

4. Apply the changes `source ~/.bashrc`

**To check whether azure windows vm in connected to Entra ID or not**

`dsregcmd /status`

Or

In Entra ID, click on device and check the device name.

To connect to RDP VM -

`az network bastion rdp --name <Bastion-name> --resource-group "<ResourceGroupName>" --target-resource-id "<Resource ID>" --auth-type AAD`
