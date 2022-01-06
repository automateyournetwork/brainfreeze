# Portals
## Sponsor Portal (default)
### ID: 40963c00-2e02-11e8-ba71-005056872c7f
### Description: Default portal used by sponsors to create and manage accounts for authorized visitors to securely access the network
### Allow Sponsor To Change Own Password: False
### Guest User Field List
#### First name
##### Data Type: TEXT
##### Required: False
##### Dictionary Label Key: ui_first_name_label
##### Custom Type: False
#### Last name
##### Data Type: TEXT
##### Required: False
##### Dictionary Label Key: ui_last_name_label
##### Custom Type: False
#### Email address
##### Data Type: EMAIL
##### Required: False
##### Dictionary Label Key: ui_email_address_label
##### Custom Type: False
#### Mobile number
##### Data Type: PHONE
##### Required: False
##### Dictionary Label Key: ui_phone_number_label
##### Custom Type: False
#### Use Mobile number as username
##### Data Type: CHECK
##### Required: False
##### Dictionary Label Key: ui_use_mobile_number_as_username_label
##### Custom Type: False
#### Company
##### Data Type: TEXT
##### Required: False
##### Dictionary Label Key: ui_company_label
##### Custom Type: False
#### SMS Service Provider
##### Data Type: DROPDOWN
##### Required: False
##### Dictionary Label Key: ui_sms_provider_label
##### Custom Type: False
#### Person being visited
##### Data Type: EMAIL
##### Required: False
##### Dictionary Label Key: ui_person_visited_label
##### Custom Type: False
#### Reason for visit
##### Data Type: TEXT
##### Required: False
##### Dictionary Label Key: ui_reason_visit_label
##### Custom Type: False
### Portal Type: SPONSOR
## Self-Registered Guest Portal (default)
### ID: 404e0f70-2e02-11e8-ba71-005056872c7f
### Description: Guests may create their own accounts and be assigned a username and password, or use their social login to access the network
### Allow Sponsor To Change Own Password: 
### Guest User Field List
### Portal Type: GUEST
## Sponsored Guest Portal (default)
### ID: 401e25d0-2e02-11e8-ba71-005056872c7f
### Description: Sponsors create guest accounts, and guests access the network using their assigned username and password
### Allow Sponsor To Change Own Password: 
### Guest User Field List
### Portal Type: GUEST
## Hotspot Guest Portal (default)
### ID: 3fab66d0-2e02-11e8-ba71-005056872c7f
### Description: Guests do not require username and password credentials to access the network, but you can optionally require an access code
### Allow Sponsor To Change Own Password: 
### Guest User Field List
### Portal Type: GUEST
## Self-Registration
### Self-Registered Guest Portal (default)
#### ID: 404e0f70-2e02-11e8-ba71-005056872c7f
#### Description: Guests may create their own accounts and be assigned a username and password, or use their social login to access the network
#### Portal Type: SELFREGGUEST
#### [Portal Test URL](https://10.10.20.70:8443/portal/PortalSetup.action?portal=404e0f70-2e02-11e8-ba71-005056872c7f)
#### HTTPS Port: 8443
#### Allowed Interface
#### Cetificate Group Tag: Default Portal Certificate Group
#### Authentication Method: 92e50f80-8c01-11e6-996c-525400b48521
#### Assigned Guest Type For Employee: Contractor (default)
#### Language
##### Display Language: USEBROWSERLOCALE
##### Fallback Language: English
##### Always Used Language: English
#### Require Access Code: False
#### Rate Limit
##### Max Failed Attempts Before Rate Limit: 5
##### Time Between Logins During Rate Limit: 2
#### Include AUP: False
#### Permissions
##### Allowed Guest To Create Accounts: True
##### Allowed Forgot Password: True
##### Allowed Guest to Change Password: False
##### Allowed Alternate Guest Portal: False
#### Assign Guest to Guest Type: Daily (default)
#### Account Validity Duration: 1
#### Required Registration Code: False
#### Required Fields
##### Username Required: False
##### First Name Required: False
##### Last Name Required: False
##### E-Mail Required: False
##### Phone Number Required: False
##### Company Required: False
##### Location Required: False
##### Selectable Location: San Jose
##### SMS Provider Required: False
##### Selectable SMS Provider: Global Default
##### Person Being Visited: False
##### Reason for Visit: False
#### Include AUP: False
#### Require AUP Acceptance: False
#### Guest Email
##### Enable Guest E-Mail Whitelist: False
##### Guest E-Mail Blacklist: False
#### Require Guest Approval: False
#### Auto Login
##### Auto Login Self Wait: False
##### Auto Login Period: 5
#### Grace Access
##### Allow Grace Access: False
##### Grace Access Expire Interval: 10
##### Grace Account Expire Notification: False
#### POST Registration Redirect: SELFREGISTRATIONSUCCESS
#### Credential Notification
##### E-Mail: False
##### SMS: False
#### Link Time Units: DAYS
#### Authenticate Sponsors Using Portal List: False
#### Sponsor Portal List
### Success
#### Include
##### Username: True
##### Password: True
##### First Name: True
##### Last Name: True
##### E-Mail: True
##### Phone Number: True
##### Company: True
##### Location: True
##### SMS Provider: True
##### Person Being Visited: True
##### Reason for Visit: True
##### AUP: False
#### Allow
##### Guest Send Self Using Print: False
##### Guest Send Self Using E-Mail: False
##### Guest Send Self Using SMS: False
##### Guest Login From Self Registration Page: False
#### Acceptable Use Policy
##### AUP On Page: False
##### AUP Acceptance: False
##### AUP Scrolling: False
### Acceptable Use Policy
#### Include: True
#### Require Scrolling: False
#### Display Frequency: FIRSTLOGIN
### Guest Settings
#### Allow Password Change At First Login: False
#### Auto Register Guest Devices: True
#### Allow Guest To Register Devices: False
### Bring Your Own Device
#### Welcome Settings
##### Enable BYOD: False
##### Enable Guest Access: False
##### Require MDM: False
#### AUP
##### Include: False
##### Display: ONPAGE
##### Require Acceptance: False
##### Require Scrolling: False
#### Registration Settings
##### Show Device ID: False
##### Endpoint Identity Group ID: aa13bb40-8bff-11e6-996c-525400b48521
#### Success Settings
##### Redirect: AUTHSUCCESSPAGE
### Post Login
#### Include Banner: True
#### Success Redirect: AUTHSUCCESSPAGE
### Support Information Include
#### Support Info Page: False
#### MAC Address: True
#### IP Address: True
#### Browser User Agent: True
#### Policy Server: True
#### Failure Code: True
#### Empty Field: HIDE
### Customizations
#### Portal Theme
##### Default Blue theme
##### ID: 9eb421c0-8c01-11e6-996c-525400b48521
#### Language: English
#### Banner Title: Guest Portal
#### Contact: Contact Support
#### Footer: 
## Sponsor
### Sponsor Portal (default)
#### ID: 40963c00-2e02-11e8-ba71-005056872c7f
#### Description: Default portal used by sponsors to create and manage accounts for authorized visitors to securely access the network
#### Portal Type: SPONSOR
#### [Test URL](https://10.10.20.70:8445/sponsorportal/PortalSetup.action?portal=40963c00-2e02-11e8-ba71-005056872c7f)
#### Portal Settings
##### HTTPS Port: 8445
##### Allowed Interface: ['eth0', 'bond0']
##### Allowed Interface: ['eth0', 'bond0']
##### Certificate Group Tage: Default Portal Certificate Group
##### Authentication Method: 92faba60-8c01-11e6-996c-525400b48521
##### Idle Timeout: 10
##### Display Language: USEBROWSERLOCALE
##### Fallback Language: English
##### Always Used Language: Italian
#### Login Page
##### Max Failed Attempts Before Rate Limit: 5
##### Time Between Logins During Rate Limit: 2
##### Include AUP: False
##### Require AUP Scrolling: False
#### Acceptable Use Policy
##### Include: True
##### Require Scrolling: False
##### Display Frequency: FIRSTLOGIN
#### Sponsor Change Password
##### Allow Sponsor to Change Password: False
#### Post Login Banner
##### Include POST Access: False
#### Support Info
##### Support Page: False
##### MAC Address: True
##### IP Address: True
##### Browser User Agent: True
##### Policy Server: True
##### Failure Code: True
##### Empty Field Display: HIDE
### Customizations
#### Portal Theme
##### Name: Default Blue theme
##### ID: 9eb421c0-8c01-11e6-996c-525400b48521
#### Language: English
#### Banner Title: Sponsor Portal
#### Contact Text: Contact Support
#### Footer Element: 
## Sponsored Guest
### Sponsored Guest Portal (default)
#### ID: 401e25d0-2e02-11e8-ba71-005056872c7f
#### Description: Sponsors create guest accounts, and guests access the network using their assigned username and password
#### Portal Type: SPONSOREDGUEST
#### [Test URL](https://10.10.20.70:8443/portal/PortalSetup.action?portal=401e25d0-2e02-11e8-ba71-005056872c7f)
#### Portal Settings
##### HTTPS Port: 8443
##### Interface: eth0
##### Interface: bond0
##### Certificate Group Tag: Default Portal Certificate Group
##### Authentication Method: 92e50f80-8c01-11e6-996c-525400b48521
##### Assigned Guest Type For Employee: Contractor (default)
##### Display Language: USEBROWSERLOCALE
##### Fallback Language: English
##### Always Used Language: English
#### Login Page Settings
##### Required Access Code: False
##### Max Failed Attempts Before Rate Limit: 5
##### Time Between Logins During Rate Limit: 2
##### Include AUP: False
##### Allowed Guest to Create Accounts: False
##### Allowed Forgot Password: True
##### Allowed Guest to Change Password: False
##### Allowed Alternative Guest Portal: False
#### Acceptable Use Policy
##### Include: True
##### Require Scrolling: False
##### Display Frequency: FIRSTLOGIN
#### Guest Change Password
##### Allow Password Change at First Login: False
#### Device Registration
##### Auto Register Guest Devices: True
##### Allow Guest to Register Devices: False
#### Bring Your Own Device
##### Enable: False
##### Enable Guest Access: False
##### Require MDM: False
##### Include AUP: False
##### AUP Display: ONPAGE
##### Require AUP Acceptance: False
##### Require Scrolling: False
##### Show Device ID: False
##### Endpoint Identity Group ID: aa13bb40-8bff-11e6-996c-525400b48521
##### Success Redirect: AUTHSUCCESSPAGE
#### Post Login Banner
##### Include Post Access Banner: True
#### Authentication Success
##### Success Redirect: AUTHSUCCESSPAGE
#### Support Information
##### Support Info Page: False
##### MAC Address: True
##### IP Address: True
##### Browser User Agent: True
##### Policy Server: True
##### Failure Code: True
##### Empty Field: HIDE
#### Customizations
##### Portal Theme Name: Default Blue theme
##### Portal Theme ID: 9eb421c0-8c01-11e6-996c-525400b48521
##### Portal Language: English
##### Banner Title: Guest Portal
##### Contact Text: Contact Support
##### Footer: 