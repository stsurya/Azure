## OSI Model

OSI model breaks down the communication b/w two computers into seven layers. These layers are helpful for Identifying network issues.

[!Image missing](./Images/OSI.png)

Whether it's the one person who can't get his laptop on the internet or website down for thousands of users. This model can help us to narrow down where the problem is and if we're able to figure it out then lot of unnecsaary work can be avoided.

7. Application Layer

This is the only layer that directly interacts with data from the user. Software applications like web browsers and email clients rely on the application layer to intiate communicaitons. This layer includes protocols like HTTPS and SMTP which enables the email communications.

6. Presentation layer

- Presentation layer is primarily responsible for preparing the data so that it can be used by the application layer and also responsible for Encryption and compressing the data.
- This layer is responsible for adding encryption on the sender's end as well as decoding the encryption on receivers end.
- Finally it is also responsible for compressing the data before sending it to layer 5 to increase the speed and efficiency by minimizing the amount of data will be transfered.

5. Session layer
