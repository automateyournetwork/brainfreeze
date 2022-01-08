import requests
import json
import xmltodict

# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))
brainfreeze_template = env.get_template('BrainFreeze.j2')

# -------------------------
# Headers
# -------------------------
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

ise = "10.10.20.70:9060"
mnt = "10.10.20.70:443"

# -------------------------
# Allowed Protocols
# -------------------------

allowedProtocols_template = env.get_template('allowedProtocols.j2')
allowedProtocols = requests.request("GET", f"https://{ ise }/ers/config/allowedprotocols", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
allowedProtocolsJSON = allowedProtocols.json()

# -------------------------
# Details Per Protocol Group
# -------------------------

allowedProtocolsDetails = []
for href in allowedProtocolsJSON['SearchResult']['resources']:
    allowedProtocolHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    allowedProtocolHrefJSON = allowedProtocolHref.json()
    allowedProtocolsDetails.append(allowedProtocolHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = allowedProtocols_template.render(allowedProtocolsDetails = allowedProtocolsDetails)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Allowed_Protocols.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Admin Users
# -------------------------

adminUsers_template = env.get_template('adminUsers.j2')
adminUsers = requests.request("GET", f"https://{ ise }/ers/config/adminuser", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
adminUsersJSON = adminUsers.json()

# -------------------------
# Details Per Admin User
# -------------------------

adminUsersDetails = []
for href in adminUsersJSON['SearchResult']['resources']:
    adminUserHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    adminUserHrefJSON = adminUserHref.json()
    adminUsersDetails.append(adminUserHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = adminUsers_template.render(adminUsersDetails = adminUsersDetails)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Administrators.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Active Directory
# -------------------------

activeDirectory_template = env.get_template('activeDirectory.j2')
activeDirectoryAll = requests.request("GET", f"https://{ ise }/ers/config/activedirectory", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
activeDirectoryAllJSON = activeDirectoryAll.json()

# -------------------------
# Details Per Active Directory
# -------------------------

activeDirectory = []
for href in activeDirectoryAllJSON['SearchResult']['resources']:
    activeDirectoryHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    activeDirectoryJSON = activeDirectoryHref.json()
    activeDirectory.append(activeDirectoryJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = activeDirectory_template.render(activeDirectory = activeDirectory)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Active_Directory.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Authorization Profile
# -------------------------

authorizationProfile_template = env.get_template('authorizationProfiles.j2')
authorizationProfileAll = requests.request("GET", f"https://{ ise }/ers/config/authorizationprofile", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
authorizationProfileAllJSON = authorizationProfileAll.json()

# -------------------------
# Details Per Authorization User
# -------------------------

authorizationProfile = []
for href in authorizationProfileAllJSON['SearchResult']['resources']:
    authorizationProfileHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    authorizationProfileJSON = authorizationProfileHref.json()
    authorizationProfile.append(authorizationProfileJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = authorizationProfile_template.render(authorizationProfile = authorizationProfile)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Active_Directory.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# DACLs
# -------------------------

dacl_template = env.get_template('dacls.j2')
daclAll = requests.request("GET", f"https://{ ise }/ers/config/downloadableacl", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
daclAllJSON = daclAll.json()

# -------------------------
# Details Per DACL
# -------------------------

dacl = []
for href in daclAllJSON['SearchResult']['resources']:
    daclHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    daclHrefJSON = daclHref.json()
    dacl.append(daclHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = dacl_template.render(dacl = dacl)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Downloadable_ACLs.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Endpoints
# -------------------------

endpoint_template = env.get_template('endpoints.j2')
endpointAll = requests.request("GET", f"https://{ ise }/ers/config/endpoint", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
endpointAllJSON = endpointAll.json()

# -------------------------
# Details Per Endpoint
# -------------------------

endpoint = []
for href in endpointAllJSON['SearchResult']['resources']:
    endpointHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    endpointHrefJSON = endpointHref.json()
    endpoint.append(endpointHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = endpoint_template.render(endpoint = endpoint)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Endpoints.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Endpoint Groups
# -------------------------

endpointGroup_template = env.get_template('endpointGroups.j2')
endpointGroupsAll = requests.request("GET", f"https://{ ise }/ers/config/endpointgroup", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
endpointGroupsAllJSON = endpointGroupsAll.json()

# -------------------------
# Details Per Endpoint Group
# -------------------------

endpointGroup = []
for href in endpointGroupsAllJSON['SearchResult']['resources']:
    endpointGroupHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    endpointGroupHrefJSON = endpointGroupHref.json()
    endpointGroup.append(endpointGroupHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = endpointGroup_template.render(endpointGroup = endpointGroup)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Endpoint_Groups.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Identity Groups
# -------------------------

identityGroup_template = env.get_template('identityGroups.j2')
identityGroupsAll = requests.request("GET", f"https://{ ise }/ers/config/identitygroup", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
identityGroupsAllJSON = identityGroupsAll.json()

# -------------------------
# Details Per Identity Group
# -------------------------

identityGroup = []
for href in identityGroupsAllJSON['SearchResult']['resources']:
    identityGroupHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    identityGroupHrefJSON = identityGroupHref.json()
    identityGroup.append(identityGroupHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = identityGroup_template.render(identityGroup = identityGroup)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Identity_Groups.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Identity Store Sequence
# -------------------------

idStoreSequence_template = env.get_template('identityStoreSequence.j2')
idStoreSequenceAll = requests.request("GET", f"https://{ ise }/ers/config/idstoresequence", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
idStoreSequenceAllJSON = idStoreSequenceAll.json()

# -------------------------
# Details Per Identity Store Sequence
# -------------------------

identityStoreSequence = []
for href in idStoreSequenceAllJSON['SearchResult']['resources']:
    identityStoreHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    identityStoreHrefJSON = identityStoreHref.json()
    identityStoreSequence.append(identityStoreHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = idStoreSequence_template.render(identityStoreSequence = identityStoreSequence)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Identity_Store_Sequence.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Internal Users
# -------------------------

internalUser_template = env.get_template('internalUsers.j2')
internalUserAll = requests.request("GET", f"https://{ ise }/ers/config/internaluser", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
internalUserAllJSON = internalUserAll.json()

# -------------------------
# Details Per Internal User
# -------------------------

internalUser = []
for href in internalUserAllJSON['SearchResult']['resources']:
    internalUserHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    internalUserHrefJSON = internalUserHref.json()
    internalUser.append(internalUserHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = internalUser_template.render(internalUser = internalUser)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Internal_Users.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Network Devices 
# -------------------------

networkDevices_template = env.get_template('networkDevices.j2')
networkDeviceAll = requests.request("GET", f"https://{ ise }/ers/config/networkdevice", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
networkDeviceAllJSON = networkDeviceAll.json()

# -------------------------
# Details Per Network Device
# -------------------------

networkDevice = []
for href in networkDeviceAllJSON['SearchResult']['resources']:
    networkDeviceHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    networkDeviceHrefJSON = networkDeviceHref.json()
    networkDevice.append(networkDeviceHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = networkDevices_template.render(networkDevice = networkDevice)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Network_Devices.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Network Device Groups
# -------------------------

networkDeviceGroups_template = env.get_template('networkDeviceGroups.j2')
networkDeviceGroupAll = requests.request("GET", f"https://{ ise }/ers/config/networkdevicegroup", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
networkDeviceGroupAllJSON = networkDeviceGroupAll.json()

# -------------------------
# Details Per Network Device Group
# -------------------------

networkDeviceGroup = []
for href in networkDeviceGroupAllJSON['SearchResult']['resources']:
    networkDeviceGroupHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    networkDeviceGroupHrefJSON = networkDeviceGroupHref.json()
    networkDeviceGroup.append(networkDeviceGroupHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = networkDeviceGroups_template.render(networkDeviceGroup = networkDeviceGroup)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Network_Device_Groups.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Nodes
# -------------------------

nodes_template = env.get_template('nodes.j2')
nodeAll = requests.request("GET", f"https://{ ise }/ers/config/node", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
nodeAllJSON = nodeAll.json()

# -------------------------
# Details Per Node
# -------------------------

node = []
for href in nodeAllJSON['SearchResult']['resources']:
    nodeHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    nodeHrefJSON = nodeHref.json()
    node.append(nodeHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = nodes_template.render(node = node)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Nodes.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Portals
# -------------------------

portals_template = env.get_template('portals.j2')
portalAll = requests.request("GET", f"https://{ ise }/ers/config/portal", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
portalAllJSON = portalAll.json()

# -------------------------
# Details Per Portal
# -------------------------

portal = []
for href in portalAllJSON['SearchResult']['resources']:
    portalHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    portalHrefJSON = portalHref.json()
    portal.append(portalHrefJSON)

# -------------------------
# Profiler Profiles
# -------------------------

profiles_template = env.get_template('profiles.j2')
profilerAll = requests.request("GET", f"https://{ ise }/ers/config/profilerprofile", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
profilerAllJSON = profilerAll.json()

# -------------------------
# Details Per Profiler Profile
# -------------------------

profiler = []
for href in profilerAllJSON['SearchResult']['resources']:
    profilerHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    profilerHrefJSON = profilerHref.json()
    profiler.append(profilerHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = profiles_template.render(profiler = profiler)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Profiles.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Deployment Info
# -------------------------

deployment_template = env.get_template('deploymentInfo.j2')
deploymentInfo = requests.request("GET", f"https://{ ise }/ers/config/deploymentinfo/getAllInfo", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
deploymentInfoJSON = deploymentInfo.json()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = deployment_template.render(deploymentInfoJSON = deploymentInfoJSON['ERSDeploymentInfo'])

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Deployment_Info.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# SGTs
# -------------------------

sgt_template = env.get_template('sgts.j2')
sgtAll = requests.request("GET", f"https://{ ise }/ers/config/sgt", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
sgtAllJSON = sgtAll.json()

# -------------------------
# Details Per SGT
# -------------------------

sgt = []
for href in sgtAllJSON['SearchResult']['resources']:
    sgtHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    sgtHrefJSON = sgtHref.json()
    sgt.append(sgtHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = sgt_template.render(sgt = sgt)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Secure_Group_Tags.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# SGT ACLs
# -------------------------

sgtACL_template = env.get_template('sgt_acls.j2')
sgtACLAll = requests.request("GET", f"https://{ ise }/ers/config/sgacl", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
sgtACLAllJSON = sgtACLAll.json()

# -------------------------
# Details Per SGT ACL
# -------------------------

sgtacl = []
for href in sgtACLAllJSON['SearchResult']['resources']:
    sgtACLHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    sgtACLHrefJSON = sgtACLHref.json()
    sgtacl.append(sgtACLHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = sgtACL_template.render(sgtacl = sgtacl)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Secure_Group_Tag_ACLs.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Self-Registration Portals
# -------------------------

selfRegPortalAll = requests.request("GET", f"https://{ ise }/ers/config/selfregportal", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
selfRegPortalAllJSON = selfRegPortalAll.json()

# -------------------------
# Details Per Self Reg Portal
# -------------------------

selfRegPortal = []
for href in selfRegPortalAllJSON['SearchResult']['resources']:
    selfRegPortalHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    selfRegPortalHrefJSON = selfRegPortalHref.json()
    selfRegPortal.append(selfRegPortalHrefJSON)

# -------------------------
# Sponsor Groups
# -------------------------

sponsorGroups_template = env.get_template('sponsorGroups.j2')
sponsorGroupAll = requests.request("GET", f"https://{ ise }/ers/config/sponsorgroup", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
sponsorGroupAllJSON = sponsorGroupAll.json()

# -------------------------
# Details Per Sponsor Group
# -------------------------

sponsorGroup = []
for href in sponsorGroupAllJSON['SearchResult']['resources']:
    sponsorGroupHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    sponsorGroupHrefJSON = sponsorGroupHref.json()
    sponsorGroup.append(sponsorGroupHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = sponsorGroups_template.render(sponsorGroup = sponsorGroup)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Sponsor_Groups.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Sponsor Portal
# -------------------------

sponsorPortalAll = requests.request("GET", f"https://{ ise }/ers/config/sponsorportal", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
sponsorPortalAllJSON = sponsorPortalAll.json()

# -------------------------
# Details Per Sponsor Portal
# -------------------------

sponsorPortal = []
for href in sponsorPortalAllJSON['SearchResult']['resources']:
    sponsorPortalHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    sponsorPortalHrefJSON = sponsorPortalHref.json()
    sponsorPortal.append(sponsorPortalHrefJSON)

# -------------------------
# Sponsored Guest Portal
# -------------------------

sponsorGuestPortalAll = requests.request("GET", f"https://{ ise }/ers/config/sponsoredguestportal", headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
sponsorGuestPortalAllJSON = sponsorGuestPortalAll.json()

# -------------------------
# Details Per Sponsored Guest Portal
# -------------------------

sponsorGuestPortal = []
for href in sponsorGuestPortalAllJSON['SearchResult']['resources']:
    sponsorGuestPortalHref = requests.request("GET", href['link']['href'], headers=headers, auth=('admin', 'C1sco12345!'), verify=False)
    sponsorGuestPortalHrefJSON = sponsorGuestPortalHref.json()
    sponsorGuestPortal.append(sponsorGuestPortalHrefJSON)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = portals_template.render(
    portal = portal,
    selfRegPortal = selfRegPortal,
    sponsorPortal = sponsorPortal,
    sponsorGuestPortal = sponsorGuestPortal
    )

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Portals.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# MnT Active Session Count
# -------------------------

sessionCounts_template = env.get_template('sessionCounts.j2')
activeSessionCount = requests.request("GET", f"https://{ mnt }/admin/API/mnt/Session/ActiveCount", auth=('admin', 'C1sco12345!'), verify=False)
xmlParse = xmltodict.parse(activeSessionCount.text)
activeSessionCountJSON = json.loads(json.dumps(xmlParse))

# -------------------------
# MnT Posture
# -------------------------

postureCount = requests.request("GET", f"https://{ mnt }/admin/API/mnt/Session/PostureCount", auth=('admin', 'C1sco12345!'), verify=False)
xmlParse = xmltodict.parse(postureCount.text)
postureCountJSON = json.loads(json.dumps(xmlParse))

# -------------------------
# MnT Active Session Count
# -------------------------

profilerCount = requests.request("GET", f"https://{ mnt }/admin/API/mnt/Session/ProfilerCount", auth=('admin', 'C1sco12345!'), verify=False)
xmlParse = xmltodict.parse(profilerCount.text)
profilerCountJSON = json.loads(json.dumps(xmlParse))

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = sessionCounts_template.render(
    activeSessionCount = activeSessionCountJSON,
    postureCount = postureCountJSON,
    profilerCount = profilerCountJSON
    )

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Session_Count.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# MnT ISE Version
# -------------------------

version_template = env.get_template('version.j2')
version = requests.request("GET", f"https://{ mnt }/admin/API/mnt/Version", auth=('admin', 'C1sco12345!'), verify=False)
xmlParse = xmltodict.parse(version.text)
versionJSON = json.loads(json.dumps(xmlParse))

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = version_template.render(version = versionJSON)

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/Version.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# MnT Failure Codes
# -------------------------

failureCodes_template = env.get_template('failureCodes.j2')
failureCodes = requests.request("GET", f"https://{ mnt }/admin/API/mnt/FailureReasons", auth=('admin', 'C1sco12345!'), verify=False)
xmlParse = xmltodict.parse(failureCodes.text)
failureCodesJSON = json.loads(json.dumps(xmlParse))

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = failureCodes_template.render(failureCodes = failureCodesJSON['failureReasonList'])

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/FailureCodes.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = brainfreeze_template.render(
    ISE = ise,
    allowedProtocolsDetails = allowedProtocolsDetails,
    adminUsersDetails = adminUsersDetails,
    activeDirectory = activeDirectory,
    authorizationProfile = authorizationProfile,
    dacl = dacl,
    endpoint = endpoint,
    endpointGroup = endpointGroup,
    identityGroup = identityGroup,
    identityStoreSequence = identityStoreSequence,
    internalUser = internalUser,
    networkDevice = networkDevice,
    networkDeviceGroup = networkDeviceGroup,
    node = node,
    portal = portal,
    profiler = profiler,
    deploymentInfoJSON = deploymentInfoJSON['ERSDeploymentInfo'],
    sgt = sgt,
    sgtacl = sgtacl,
    selfRegPortal = selfRegPortal,
    sponsorGroup = sponsorGroup,
    sponsorPortal = sponsorPortal,
    sponsorGuestPortal = sponsorGuestPortal,
    activeSessionCount = activeSessionCountJSON,
    postureCount = postureCountJSON,
    profilerCount = profilerCountJSON,
    version = versionJSON,
    failureCodes = failureCodesJSON['failureReasonList']
    )

# -------------------------
# Save the markdown file
# -------------------------

with open("Output/BrainFreeze.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()