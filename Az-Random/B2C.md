# What is Azure B2C ?

- Azure B2C is a cloud identity management service that enables you to customize and control how your customers want to sign in, sing up and edit their profiles to use you application.
- Customers can use their social, enterprise or other local accounts to get single-sign on access to you application and API's
- It’s capable of supporting millions of users and billions of authentications per day. It takes care of the scaling, denial of service attacks, password spray, brute-force attacks.

## The primary resources you work with in an Azure AD B2C tenant are:

- **Directory:** This is where Azure AD B2C stores user credentials, profile data and application registrations.
- **Application registrations:** You can register your web, mobile, and native applications with Azure AD B2C to enable identity management. You can also register any APIs you want to protect with Azure AD B2C.
- **User flow and custom policies:** These are used to create identity experiences for your applications with built-in user flows and custom policies

1. **User flows:** help you quickly enable common identity tasks like sign-up, sign-in, and profile editing
2. **Custom policies:** let you build complex identity workflows unique to your organization, customers, employees, partners, and citizens

- **Sign-in options** - Azure AD B2C offers various sign-up and sign-in options for users of your applications:

Username, email, and phone sign-in - You can configure your Azure AD B2C local accounts to allow sign up and sign in with a username, email address, phone number, or a combination of methods.

Social identity providers - You can federate with social providers like Facebook, LinkedIn, or Twitter.

External identity providers - You can also federate with standard identity protocols like OAuth 2.0, OpenID Connect, and more.
