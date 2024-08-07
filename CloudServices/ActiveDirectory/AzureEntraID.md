## Azure Entra ID

- Microsoft Entra ID is a multi-tenant **cloud-based identity and access management solution** for the resources that exist in the cloud.
- For **IT Admins**, Azure AD provides an affordable, easy to use solution to give employees and business partners Single Sign-On(SSO) access to thousands of Cloud SaaS Applications like Office365, Dropbox and Concur.
- For **Application Developers**, Azure AD let's you focus on building your application by making it fast, simple to integrate with a world class indentity management solution used by millions of organizations around the world.
- Organizations can use Azure AD to improve employee productivity, streamline IT processes and improve security for adopting various cloud services. Employess can access online applications by using single account.
- Azure AD is highly scalable and highly available by design. Therefore, organization do not have to maintain related infrastructure or worry about disaster recovery. Running out of 28 data centers around the world with automated failover, you'll have the comfort of knowing that azure ad is highly reliable even if a data center goes down, copies of your directory are stored in atleast two more regionally dispersed data centers and available for instant access.
- Many applications based on .Net, Java, PHP and e.t.c can use industry standard protocols such as Securtiy Assertion MarkUp Language(SAML) 2.o, and Open ID Connect to integrate the identity management provided by Azure AD into the application logic. Through the support of OAuth 2.o, developers can develop the mobile and web applications that integrate with Microsoft's Identity Platform for cloud authentication and access management.
- Azure AD provides access to its content via **Rest-Based Graph API**, rather than by LDAP on which Active directory relies.

## you can use azure ad to:

- Provide an identity management solution.
- Manage usres and groups.
- Enable federation b/w organisations.
- Identify irregular sing-in activity.
- configure SSO to cloud based SaaS applications like Office365, DropBox e.t.c
- Configure access to the on-prem applications.
- Configure Multi-factor authentication.
- Extend existing on-prem Active Directory implementations Azure AD.

## Azure AD Editions:

### Free:

- User and Group Management.
- Self-Service password change for cloud users.
- Synchronize with on-prem directories.
- Get Single Sign-On access across Office365 and thousands of other SaaS applications.
- End-users are entitled to get single sign-on access for upto 10 applications.

### Basic edition:

It extends free edition capabilties. Aditionally, this edition has a Microsoft high availabilty service level agreement(SLA) uptime of 99.9%. It supports cost reducing features like

- Group-based access management.
- Self-service password reset for cloud users.
- Company Branding(Logon Pages/Access Panel Customizaition)

### Premium P1 edition:

- It supports Multi-Factor Authentication.
- Self-Service Identity and Management Solution.
- Advanced reports for security and usage information.
- Dynamic groups and self-service group management.
- Self-Service password reset with password write-back for on-premises.

### Premium P2 edition:

- All Premium P1 features.
- some other advanced features.

## Managing Active Directories

Directories provide a simple and logical way of grouping identities.

A directory can consist of the following three types of Identites:

- Users added manually to the directory(cloud only Identities)
- Users synced from existing Active Directory installaitons(On-Prem).
- Third party accounts

### Access control in azure starts from a billing perspective.

- The actual owner of an azure account - is the Account Administrator(AA)
- Subscritpion are a container for billing, but they also act as a security boundary. Your Azure subscription has a trust relationship with Azure AD, which means that it trusts the directory to authenticate users, serivces and devices.
- Multiple subscriptions can trust the same directory, but each subscription trust only one directory.
- You can have your own custom domain name for your AD and company branding as well.

## Creating a Domain Controller and Join Azure Virtual Machines to a domain

- Create a new VM to be used as a Domain Controller and DNS Server.
- Change the private IP to static: VM -> Networking -> Click on NIC -> IP Configurations -> IPConfig1 -> Private IP Address Settings.
- Virtual Network -> Select the Vnet -> DNS Servers -> Select Custom and provide static IP of VM from previous step.
- Promtoe the VM as Active Directory Domain Controller.<br>
  a) RDP to VM.<br>
  b) Server Manager -> Dashboard -> Add Roles and Features -> Next -> Next.<br>
  c) Check Active Directory Domain Service and DNS -> Next -> Next -> .... -> Finish.<br>
  d) From Notification in Server Manager Window(Top Right) -> Click on Promote this server to a Domain Controller.<br>
  e) Select Add a new forest -> Next -> Enter a name for the new domain -> Next, Provide DSRM Password -> Next -> Finish.<br>
  f) Server Manager -> Tools -> DNS -> Right Click on Server -> Properties -> Forwardes -> Edit -> Delete existing IP -> OK.<br>

- Create a new VM and join the Domain Controller (Optional)<br>
  a) RDP to VM.<br>
  b) Server Manager -> local server -> Workgroup -> change -> Domain Name = mydemodomain.local, Provide admin u/p -> Your machine has now joined the domain -> Restart the Machine.

## Azure AD Connect Express Installation Walkthrough

- Azure portal -> Active Directory -> Users and Groups -> All users -> + New User -> Username = "abcd@\*.com", Directory Role = Global Admin.
- Remote login to VM (Primary Domain Controller).
- Server Manager -> Local Server -> IE Enhanced Security Configuration = Off
- Add few Users to its Active Directory Users and Groups.
- Download Azure AD Connect. Navigate to and double-click on AzureADConnect.msi.
- On the Welcome screen, select the box agreeing to the licensing terms and click Continue.
- On the Express settings screen, click Use express settings.
- On the Connect to Azure AD screen, enter the credentials of the Global Admin account you created earlier for your Azure AD. Click Next.
- On the Connect to AD DS screen, enter the username and password for an enterprise admin account. you can enter the domain part in either NetBios or FQDN format, i.e., FABRIKAM\administrator or fabrikam.com\administrator. Click Next.
- The Azure AD sign-in configuration page will only show if you did not complete verify your domains.
- On the Ready to configure screen, click install<br>

  1. Optionally on the Ready to configure page, you can unselect the Start synchronization process as soon as configuration completes checkbox. You should unselect this checkbox if you want to do additional configuration, such as filterting. If you unselect this option, the wizard configures sync but leave the scheduler disabled. It does not run unitl you enable it manullay by rerunning the installation wizard.<br>
  2. If you have Exchange in your on-premisse Active Directory, then you also have an option to enable Exchange Hybrid deployment. enable this option if you plan to have Exhange mailboxes both in the cloud and on-premises at the same time.<br>

- After the installation has completed, sign off and sign in again before you use Synchronization Service Manager or Synchronization Rule Editor.

**To disable Azure AD sync using Powershell**
Execure the below powershell script (use global amdin account)

```
# Specify credential for azure ad connect
$Msolcred = Get-credential

# Connect to azure ad
Connect-MsolService -Credential $Msolcred
# Disable Azure AD sync / Dir Sync
Set-MsolDirSyncEnabled -EnableDirSync $false
# confirm AD Connect / Dir Sync disabled
(Get-msolCompanyInformation).DirectorySynchronizationEnabled

```
