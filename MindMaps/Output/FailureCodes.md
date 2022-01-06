# Failure Codes
## ID: 100001
### Meaning: 100001 AUTHMGR-5-FAIL Authorization failed for client
## ID: 100002
### Meaning: 100002 AUTHMGR-5-SECURITY_VIOLATION Security violation on the interface
## ID: 100003
### Meaning: 100003 AUTHMGR-5-UNAUTHORIZED Interface unauthorized
## ID: 100004
### Meaning: 100004 DOT1X-5-FAIL Authentication failed for client
## ID: 100005
### Meaning: 100005 MAB-5-FAIL Authentication failed for client
## ID: 100006
### Meaning: 100006 RADIUS-4-RADIUS_DEAD RADIUS server is not responding
## ID: 100007
### Meaning: 100007 EPM-6-POLICY_APP_FAILURE Interface ACL not configured
## ID: 100008
### Meaning: 100008 DOT1X_SWITCH-5-ERR_VLAN_NOT_FOUND Attempt to assign non-existent or shutdown VLAN to 802.1x port
## ID: 100009
### Meaning: 100009 WEBAUTH_FAIL
## ID: 10001
### Meaning: 10001 Internal error. Incorrect configuration version
## ID: 10002
### Meaning: 10002 Internal error: Failure to load appropriate service
## ID: 10003
### Meaning: 10003 Internal error: Administrator authentication received blank Administrator name
## ID: 10004
### Meaning: 10004 Internal error: Administrator authentication received blank Administrator password
## ID: 10006
### Meaning: 10006 Administrator authentication failed
## ID: 10007
### Meaning: 10007 Administrator authentication failed - DB Error
## ID: 11007
### Meaning: 11007 Could not locate Network Device or AAA Client
## ID: 11011
### Meaning: 11011 RADIUS listener failed to open
## ID: 11012
### Meaning: 11012 RADIUS packet contains invalid header
## ID: 11014
### Meaning: 11014 RADIUS packet contains invalid attribute(s)
## ID: 11021
### Meaning: 11021 RADIUS could not decipher password. packet missing necessary attributes
## ID: 11023
### Meaning: 11023 The requested dACL is not found. This is an unknown dACL name
## ID: 11024
### Meaning: 11024 The Access-Request for the requested dACL is missing a Message-Authenticator attribute. The request is rejected
## ID: 11025
### Meaning: 11025 The Access-Request for the requested dACL is missing a cisco-av-pair attribute with the value aaa:event=acl-download. The request is rejected
## ID: 11026
### Meaning: 11026 The requested dACL is not found
## ID: 11029
### Meaning: 11029 Unsupported RADIUS packet type
## ID: 11030
### Meaning: 11030 Pre-parsing of the RADIUS packet failed
## ID: 11031
### Meaning: 11031 RADIUS packet type is not a valid Request
## ID: 11033
### Meaning: 11033 Selected Service type is not Network Access
## ID: 11034
### Meaning: 11034 Process Host Lookup is disabled. (Service-Type = Call Check (10) cannot be applied)
## ID: 11035
### Meaning: 11035 The session associated with the requested dACL has timed out
## ID: 11036
### Meaning: 11036 The Message-Authenticator RADIUS attribute is invalid
## ID: 11037
### Meaning: 11037 Dropped accounting request received via unsupported port
## ID: 11038
### Meaning: 11038 RADIUS Accounting-Request header contains invalid Authenticator field
## ID: 11039
### Meaning: 11039 RADIUS authentication request rejected due to critical logging error
## ID: 11040
### Meaning: 11040 RADIUS accounting request dropped due to critical logging error
## ID: 11041
### Meaning: 11041 RADIUS PAP session timed out
## ID: 11051
### Meaning: 11051 RADIUS packet contains invalid state attribute
## ID: 11052
### Meaning: 11052 Authentication request dropped due to unsupported port number
## ID: 11053
### Meaning: 11053 Invalid attributes in outgoing radius packet - possibly some attributes exceeded their size limit
## ID: 11054
### Meaning: 11054 Request from a non-wireless device was dropped due to installed Wireless license
## ID: 11057
### Meaning: 11057 The Access-Request for the requested RADIUS is missing
## ID: 11103
### Meaning: 11103 RADIUS-Client encountered error during processing flow
## ID: 11106
### Meaning: 11106 Error in KeyWrap configuration
## ID: 11107
### Meaning: 11107 Required attributes for KeyWrap are missing
## ID: 11108
### Meaning: 11108 Missing required EapMessage attribute for KeyWrap
## ID: 11109
### Meaning: 11109 RADIUS request improperly contains both KeyWrap and MessageAuthenticator attributes
## ID: 11110
### Meaning: 11110 Request received from a KeyWrap enabled device. The TunnelPassword attribute is present in KeyWrap.
## ID: 11111
### Meaning: 11111 RADIUS request has been received with KeyWrap attributes. However, KeyWrap is not configured for the requesting device in ISE.
## ID: 11114
### Meaning: 11114 KeyWrap parameters on RADIUS request packet are not compatible with the earlier KeyWrap request in this session.
## ID: 11115
### Meaning: 11115 The AAA Client Message Authenticator Code Key does not match the configured ISE Server Message Authenticator Code Key.
## ID: 11200
### Meaning: 11200 Received invalid dynamic authorization request
## ID: 11205
### Meaning: 11205 Could not find Network Access Device
## ID: 11206
### Meaning: 11206 Could not find Client ISE Node
## ID: 11213
### Meaning: 11213 No response received from Network Access Device after sending a Dynamic Authorization request
## ID: 11214
### Meaning: 11214 An invalid response received from Network Access Device
## ID: 11215
### Meaning: 11215 No response has been received from Dynamic Authorization Client in ISE
## ID: 11216
### Meaning: 11216 The Internal Proxy PAC generation has failed
## ID: 11225
### Meaning: 11225 The dynamic authorization request was rejected due to a critical logging error
## ID: 11226
### Meaning: 11226 ISE Proxy Node, functioning as Dynamic Authorization Client, is deregistered from the deployment
## ID: 11227
### Meaning: 11227 ISE Proxy Node, functioning as Dynamic Authorization Client, is marked as inactive in the deployment
## ID: 11300
### Meaning: 11300 Could not locate TrustSec Device
## ID: 11302
### Meaning: 11302 Received Secure RADIUS request without a cts-pac-opaque cisco-av-pair attribute
## ID: 11303
### Meaning: 11303 Could not parse the cts-pac-opaque attribute
## ID: 11304
### Meaning: 11304 Could not retrieve requested Security Group Tag
## ID: 11305
### Meaning: 11305 Could not retrieve requested Security Group ACL
## ID: 11307
### Meaning: 11307 Incorrect RADIUS CHAP attribute
## ID: 11308
### Meaning: 11308 Incorrect RADIUS MS-CHAP v1 attribute
## ID: 11309
### Meaning: 11309 Incorrect RADIUS MS-CHAP v2 attribute
## ID: 11311
### Meaning: 11311 Failed to locate ACE of Security Group Access Control List
## ID: 11313
### Meaning: 11313 ISE detected that the Unknown SGT was provisioned to a network device or endpoint.
## ID: 11314
### Meaning: 11314 ISE detected a malformed  TrustSec PAC.
## ID: 11315
### Meaning: 11315 TrustSec environment data request failed
## ID: 11350
### Meaning: 11350 Detected proxy loop; dropping request
## ID: 11351
### Meaning: 11351 Failed to read RADIUS server sequence configuration; dropping request
## ID: 11352
### Meaning: 11352 Response Proxy-State attribute validation failed
## ID: 11353
### Meaning: 11353 No more external RADIUS servers; can't perform failover
## ID: 11354
### Meaning: 11354 Accounting request received but neither local nor remote accounting is configured
## ID: 11360
### Meaning: 11360 RADIUS server sequence failed to validate incoming request
## ID: 11368
### Meaning: 11368 Please review logs on the External RADIUS Server to determine the precise failure reason.
## ID: 11369
### Meaning: 11369 Proxy request  was rejected, as the external RADIUS server that handled previous related EAP messages is now down
## ID: 11400
### Meaning: 11400 EAP-MSCHAP password change not allowed by the Allowed Protocols
## ID: 11402
### Meaning: 11402 EAP-GTC password change not allowed by the Allowed Protocols
## ID: 11500
### Meaning: 11500 Invalid or unexpected EAP payload received
## ID: 11501
### Meaning: 11501 Invalid EAP payload
## ID: 11502
### Meaning: 11502 EAP packet contains invalid type
## ID: 11508
### Meaning: 11508 EAP-Response/Identity contains invalid identity data
## ID: 11509
### Meaning: 11509 Allowed Protocols does not allow any EAP protocols
## ID: 11510
### Meaning: 11510 Supplicant declined EAP method selected by Authentication Policy but did not propose another one; EAP negotiation failed
## ID: 11511
### Meaning: 11511 Extracted EAP-Response/NAK packet not requesting any EAP protocols; EAP-negotiation failed
## ID: 11512
### Meaning: 11512 Extracted EAP-Response/NAK packet requesting to use unsupported EAP protocol; EAP-negotiation failed
## ID: 11513
### Meaning: 11513 Extracted second EAP-Response/NAK in current EAP conversation; failed to negotiate EAP
## ID: 11514
### Meaning: 11514 Unexpectedly received empty TLS message; treating as a rejection by the client
## ID: 11515
### Meaning: 11515 Supplicant declined inner EAP method selected by Authentication Policy but did not proposed another one; inner EAP negotiation failed
## ID: 11516
### Meaning: 11516 Extracted EAP-Response/NAK packet not requesting any EAP protocols for inner EAP method; inner EAP-negotiation failed
## ID: 11517
### Meaning: 11517 Extracted EAP-Response/NAK packet requesting to use unsupported inner EAP protocol; inner EAP-negotiation failed
## ID: 11518
### Meaning: 11518 Extracted second EAP-Response/NAK in current inner EAP conversation; inner EAP-negotiation failed
## ID: 11523
### Meaning: 11523 Invalid or unexpected inner-EAP payload received
## ID: 11524
### Meaning: 11524 Invalid inner-EAP payload
## ID: 11545
### Meaning: 11545 Machine Authentication is disabled
## ID: 11553
### Meaning: 11553 Reject User Authorization PAC since its Initiator-ID does not match the Tunnel PAC Initiator-ID
## ID: 11566
### Meaning: 11566 TEAP inner method finished with failure
## ID: 11577
### Meaning: 11577 TEAP cryptobinding verification failed
## ID: 11578
### Meaning: 11578 Rejected PAC provisioning request because supplicant failed to adhere to protocol
## ID: 11579
### Meaning: 11579 No valid PAC requests on provisioning
## ID: 11580
### Meaning: 11580 Rejected PAC unexpectedly received during PAC-less mode of TEAP
## ID: 11588
### Meaning: 11588 Supplicant failed to adhere to protocol
## ID: 11590
### Meaning: 11590 Anonymous TLS renegotiation failed
## ID: 11593
### Meaning: 11593 TEAP provisioning failed. General error
## ID: 11594
### Meaning: 11594 Client certificate authentication failed
## ID: 11598
### Meaning: 11598 TEAP authentication failed
## ID: 11600
### Meaning: 11600 TEAP provisioning phase finished
## ID: 11601
### Meaning: 11601 TEAP failed SSL/TLS handshake because the client rejected the ISE local-certificate
## ID: 11602
### Meaning: 11602 TEAP failed SSL/TLS handshake after a client alert
## ID: 11604
### Meaning: 11604 PAC contains invalid Authority ID
## ID: 11605
### Meaning: 11605 PAC contains invalid PAC type
## ID: 11610
### Meaning: 11610 PAC contains invalid Authentication Tag
## ID: 11611
### Meaning: 11611 Failed to decrypt PAC
## ID: 11612
### Meaning: 11612 Failed to derive TEAP Master Key
## ID: 11613
### Meaning: 11613 Fallback on invalid PAC: no available additional cipher configured on server
## ID: 11614
### Meaning: 11614 Cannot perform more then one invalid PAC fallback
## ID: 11615
### Meaning: 11615 No cipher on client side for invalid PAC fallback
## ID: 11616
### Meaning: 11616 Neither anonymous nor authenticated provisioning allowed by Allowed Protocols
## ID: 11617
### Meaning: 11617 Client didn't provide suitable ciphers for anonymous PAC-provisioning
## ID: 11618
### Meaning: 11618 Client didn't provide suitable ciphers for authenticated PAC provisioning
## ID: 11619
### Meaning: 11619 Client didn't provide suitable ciphers for either anonymous or authenticated PAC-provisioning
## ID: 11625
### Meaning: 11625 No cipher for PAC-less TEAP authentication
## ID: 11626
### Meaning: 11626 Unexpectedly received empty TLS message during TEAP handshake; treating as a rejection by the client
## ID: 11631
### Meaning: 11631 TEAP channelbinding verification failed
## ID: 11633
### Meaning: 11633 Client requested TLSv1.1 that is not allowed
## ID: 11634
### Meaning: 11634 Client requested TLS of unknown version
## ID: 11635
### Meaning: 11635 Downgrading from EMSK to MSK is not allowed
## ID: 11638
### Meaning: 11638 Client sent Result TLV indicating failure
## ID: 11803
### Meaning: 11803 Failed to negotiate EAP because EAP-MSCHAP not allowed in the Allowed Protocols
## ID: 11809
### Meaning: 11809 Failed to negotiate EAP for inner method because EAP-MSCHAPv2 not allowed in the Allowed Protocols
## ID: 11813
### Meaning: 11813 EAP-MSCHAP authentication failed
## ID: 11815
### Meaning: 11815 Inner EAP-MSCHAP authentication failed
## ID: 11816
### Meaning: 11816 MSCHAP username doesn't match inner method EAP-Response/Identity
## ID: 11817
### Meaning: 11817 Received unexpected EAP-MSCHAP message
## ID: 11818
### Meaning: 11818 Failed to parse EAP-MSCHAP packet
## ID: 11819
### Meaning: 11819 Received EAP-MSCHAP packet with invalid argument
## ID: 11821
### Meaning: 11821 EAP-MSCHAP password change attempt failed
## ID: 11823
### Meaning: 11823 EAP-MSCHAP authentication attempt failed
## ID: 11825
### Meaning: 11825 MSCHAP inner method username is missing
## ID: 12003
### Meaning: 12003 Failed to negotiate EAP because EAP-MD5 not allowed in the Allowed Protocols
## ID: 12006
### Meaning: 12006 EAP-MD5 authentication failed
## ID: 12007
### Meaning: 12007 Internal error - invalid EAP-MD5 state
## ID: 12008
### Meaning: 12008 Failed to parse EAP-MD5 packet
## ID: 12103
### Meaning: 12103 Failed to negotiate EAP because EAP-FAST not allowed in the Allowed Protocols
## ID: 12108
### Meaning: 12108 EAP-FAST authentication failed
## ID: 12109
### Meaning: 12109 EAP-FAST provisioning phase finished
## ID: 12111
### Meaning: 12111 PAC contains invalid Authority ID
## ID: 12112
### Meaning: 12112 PAC contains invalid PAC type
## ID: 12114
### Meaning: 12114 PAC contains invalid Authentication Tag
## ID: 12116
### Meaning: 12116 Client sent Result TLV indicating failure
## ID: 12117
### Meaning: 12117 EAP-FAST inner method finished with failure
## ID: 12118
### Meaning: 12118 EAP-FAST cryptobinding verification failed
## ID: 12120
### Meaning: 12120 Neither anonymous nor authenticated provisioning allowed by Allowed Protocols
## ID: 12121
### Meaning: 12121 Client didn't provide suitable ciphers for anonymous PAC-provisioning
## ID: 12122
### Meaning: 12122 Client didn't provide suitable ciphers for authenticated PAC provisioning
## ID: 12123
### Meaning: 12123 Client didn't provide suitable ciphers for either anonymous or authenticated PAC-provisioning
## ID: 12129
### Meaning: 12129 EAP-FAST provisioning failed. General error
## ID: 12130
### Meaning: 12130 Failed to decrypt PAC
## ID: 12134
### Meaning: 12134 Failed to update seed key
## ID: 12140
### Meaning: 12140 Anonymous TLS renegotiation failed
## ID: 12141
### Meaning: 12141 Failed to find Legacy Master Key
## ID: 12142
### Meaning: 12142 Legacy Master Key expired
## ID: 12143
### Meaning: 12143 Failed to derive EAP-FAST Master Key
## ID: 12144
### Meaning: 12144 Fallback on invalid PAC: no available additional cipher configured on server
## ID: 12145
### Meaning: 12145 Cannot perform more then one invalid PAC fallback
## ID: 12146
### Meaning: 12146 No cipher on client side for invalid PAC fallback
## ID: 12147
### Meaning: 12147 Machine Authentication is disabled
## ID: 12150
### Meaning: 12150 Prepared RADIUS Access-Reject after successful in-band PAC provisioning
## ID: 12152
### Meaning: 12152 Rejected PAC provisioning request because supplicant failed to adhere to protocol
## ID: 12153
### Meaning: 12153 EAP-FAST failed SSL/TLS handshake because the client rejected the ISE local-certificate
## ID: 12154
### Meaning: 12154 EAP-FAST failed SSL/TLS handshake after a client alert
## ID: 12177
### Meaning: 12177 No cipher for PAC-less EAP-FAST authentication
## ID: 12178
### Meaning: 12178 Rejected PAC unexpectedly received during PAC-less mode of EAP-FAST
## ID: 12229
### Meaning: 12229 No valid PAC requests on provisioning
## ID: 12235
### Meaning: 12235 Unexpectedly received empty TLS message during EAP-FAST handshake; treating as a rejection by the client
## ID: 12303
### Meaning: 12303 Failed to negotiate EAP because PEAP not allowed in the Allowed Protocols
## ID: 12307
### Meaning: 12307 PEAP authentication failed
## ID: 12308
### Meaning: 12308 Client sent Result TLV indicating failure
## ID: 12309
### Meaning: 12309 PEAP handshake failed
## ID: 12315
### Meaning: 12315 PEAP inner method finished with failure
## ID: 12316
### Meaning: 12316 PEAP version negotiation failed
## ID: 12320
### Meaning: 12320 Client failed to acknowledge receipt of success or failure result
## ID: 12321
### Meaning: 12321 PEAP failed SSL/TLS handshake because the client rejected the ISE local-certificate
## ID: 12322
### Meaning: 12322 PEAP failed SSL/TLS handshake after a client alert
## ID: 12323
### Meaning: 12323 PEAP cryptobinding verification failed
## ID: 12503
### Meaning: 12503 Failed to negotiate EAP because EAP-TLS not enabled in Allowed Protocols
## ID: 12507
### Meaning: 12507 EAP-TLS authentication failed
## ID: 12508
### Meaning: 12508 EAP-TLS handshake failed
## ID: 12511
### Meaning: 12511 Unexpectedly received TLS alert message; treating as a rejection by the client
## ID: 12512
### Meaning: 12512 Treat the unexpected TLS acknowledge message as a rejection from the client
## ID: 12513
### Meaning: 12513 Could not establish the EAP TLS SSL session
## ID: 12514
### Meaning: 12514 EAP-TLS failed SSL/TLS handshake because of an unknown CA in the client certificates chain
## ID: 12515
### Meaning: 12515 EAP-TLS failed SSL/TLS handshake because of an expired CRL associated with a CA in the client certificates chain
## ID: 12516
### Meaning: 12516 EAP-TLS failed SSL/TLS handshake because of an expired certificate in the client certificates chain
## ID: 12517
### Meaning: 12517 EAP-TLS failed SSL/TLS handshake because of a revoked certificate in the client certificate chain
## ID: 12518
### Meaning: 12518 EAP-TLS failed SSL/TLS handshake because of a bad certificate in the client certificate chain
## ID: 12519
### Meaning: 12519 EAP-TLS failed SSL/TLS handshake because of an unsupported certificate in the client certificate chain
## ID: 12520
### Meaning: 12520 EAP-TLS failed SSL/TLS handshake because the client rejected the ISE local-certificate
## ID: 12521
### Meaning: 12521 EAP-TLS failed SSL/TLS handshake after a client alert
## ID: 12525
### Meaning: 12525 Failed to negotiate EAP for inner method because EAP-TLS not allowed in the Allowed Protocols
## ID: 12529
### Meaning: 12529 Inner EAP-TLS authentication failed
## ID: 12530
### Meaning: 12530 EAP-TLS failed SSL/TLS handshake because of the client certificate is not yet valid
## ID: 12532
### Meaning: 12532 Failed to update seed key
## ID: 12535
### Meaning: 12535 The EAP-TLS session ticket received from supplicant is expired
## ID: 12536
### Meaning: 12536 Failed to verify the EAP-TLS session ticket received from supplicant.
## ID: 12537
### Meaning: 12537 The EAP-TLS session ticket identity does not match the EAP identity
## ID: 12538
### Meaning: 12538 The EAP-TLS session ticket received from supplicant contains an invalid authentication code
## ID: 12539
### Meaning: 12539 Failed to decrypt the EAP-TLS session ticket received from supplicant
## ID: 12543
### Meaning: 12543 Cannot generate a new session ticket
## ID: 12544
### Meaning: 12544 The EAP-TLS session ticket contains invalid Authority ID
## ID: 12555
### Meaning: 12555 OCSP status of user certificate is revoked
## ID: 12557
### Meaning: 12557 User Auth failed because OCSP status is unknown
## ID: 12603
### Meaning: 12603 Failed to negotiate EAP because EAP-GTC not allowed in the Allowed Protocols
## ID: 12609
### Meaning: 12609 Failed to negotiate EAP for inner method because EAP-GTC not allowed in the Allowed Protocols
## ID: 12613
### Meaning: 12613 EAP-GTC authentication failed
## ID: 12615
### Meaning: 12615 Inner EAP-GTC authentication failed
## ID: 12616
### Meaning: 12616 GTC username doesn't match inner method EAP-Response/Identity
## ID: 12617
### Meaning: 12617 Internal error: invalid EAP-GTC state
## ID: 12618
### Meaning: 12618 Failed to parse EAP-GTC packet
## ID: 12619
### Meaning: 12619 Received EAP-GTC packet with invalid argument
## ID: 12621
### Meaning: 12621 EAP-GTC password change attempt failed
## ID: 12623
### Meaning: 12623 EAP-GTC authentication attempt failed
## ID: 12628
### Meaning: 12628 Invalid operation performed
## ID: 12653
### Meaning: 12653 Failed to negotiate EAP for inner method because EAP-GTC denied for anonymous PAC provisioning
## ID: 12703
### Meaning: 12703 Failed to negotiate EAP because LEAP not allowed in the Allowed Protocols
## ID: 12706
### Meaning: 12706 LEAP authentication failed; Finishing protocol
## ID: 12707
### Meaning: 12707 LEAP authentication error; Finishing protocol
## ID: 12708
### Meaning: 12708 LEAP packet validation failed
## ID: 12709
### Meaning: 12709 LEAP packet parsing failed
## ID: 12710
### Meaning: 12710 LEAP internal error: Invalid state
## ID: 12711
### Meaning: 12711 LEAP internal error: LEAP challenge not created
## ID: 12712
### Meaning: 12712 LEAP internal error: LEAP challenge-response and session-key not created
## ID: 12750
### Meaning: 12750 Failed to negotiate EAP for inner method because EAP-MSCHAP not allowed under PEAP configuration in the Allowed Protocols
## ID: 12751
### Meaning: 12751 Failed to negotiate EAP for inner method because EAP-MSCHAP not allowed under EAP-FAST configuration in the Allowed Protocols
## ID: 12752
### Meaning: 12752 Failed to negotiate EAP for inner method because EAP-TLS not allowed under PEAP configuration in the Allowed Protocols
## ID: 12753
### Meaning: 12753 Failed to negotiate EAP for inner method because EAP-TLS not allowed under EAP-FAST configuration in the Allowed Protocols
## ID: 12754
### Meaning: 12754 Failed to negotiate EAP for inner method because EAP-GTC not allowed under PEAP configuration in the Allowed Protocols
## ID: 12755
### Meaning: 12755 Failed to negotiate EAP for inner method because EAP-GTC not allowed under EAP-FAST configuration in the Allowed Protocols
## ID: 12759
### Meaning: 12759 Failed to negotiate EAP because TEAP not allowed in the Allowed Protocols
## ID: 12760
### Meaning: 12760 Failed to negotiate EAP for inner method because EAP-MSCHAP not allowed under TEAP configuration in the Allowed Protocols
## ID: 12761
### Meaning: 12761 Failed to negotiate EAP for inner method because EAP-TLS not allowed under TEAP configuration in the Allowed Protocols
## ID: 12762
### Meaning: 12762 Failed to negotiate EAP for inner method because EAP-GTC not allowed under TEAP configuration in the Allowed Protocols
## ID: 12818
### Meaning: 12818 Expected TLS acknowledge for last alert but received another message
## ID: 12819
### Meaning: 12819 Expected TLS acknowledge for handshake succeeded but received another message
## ID: 12831
### Meaning: 12831 Unable to download CRL
## ID: 12850
### Meaning: 12850 Received NAK TLV. Client rejected the conversation
## ID: 12851
### Meaning: 12851 Received unexpected EAP NAK message. Client rejected the conversation
## ID: 12852
### Meaning: 12852 Cryptographic processing of received buffer failed
## ID: 12854
### Meaning: 12854 Cannot authenticate because password was not present or was empty
## ID: 12857
### Meaning: 12857 Client certificate authentication failed
## ID: 12915
### Meaning: 12915 PEAP version negotiation failed
## ID: 12916
### Meaning: 12916 Expected TLS acknowledge for TLS fragment but received another message
## ID: 12917
### Meaning: 12917 Expected TLS acknowledge for PEAPv1 protected termination but received another message
## ID: 12918
### Meaning: 12918 Supplicant sent unmatched EAP Response packet identifier
## ID: 12919
### Meaning: 12919 Supplicant sent unmatched inner EAP Response packet identifier
## ID: 12920
### Meaning: 12920 Supplicant stopped responding to ISE after sending it the first TEAP message
## ID: 12921
### Meaning: 12921 Supplicant stopped responding to ISE during TEAP tunnel establishment
## ID: 12928
### Meaning: 12928 Supplicant stopped responding to ISE during TEAP protected termination
## ID: 12929
### Meaning: 12929 NAS sends RADIUS accounting update messages too frequently
## ID: 12930
### Meaning: 12930 Supplicant stopped responding to ISE after sending it the first PEAP message
## ID: 12931
### Meaning: 12931 Supplicant stopped responding to ISE after sending it the first EAP-TLS message
## ID: 12932
### Meaning: 12932 Supplicant stopped responding to ISE after sending it the first EAP-FAST message
## ID: 12933
### Meaning: 12933 Supplicant stopped responding to ISE during EAP-FAST tunnel establishment
## ID: 12934
### Meaning: 12934 Supplicant stopped responding to ISE during PEAP tunnel establishment
## ID: 12935
### Meaning: 12935 Supplicant stopped responding to ISE during EAP-TLS certificate exchange
## ID: 12936
### Meaning: 12936 Supplicant stopped responding to ISE after sending it inner EAP Identity Request
## ID: 12937
### Meaning: 12937 Supplicant stopped responding to ISE after sending it the first inner EAP-MSCHAPv2 message
## ID: 12938
### Meaning: 12938 Supplicant stopped responding to ISE after sending it the first inner EAP-GTC message
## ID: 12939
### Meaning: 12939 Supplicant stopped responding to ISE after sending it the first inner EAP-TLS message
## ID: 12940
### Meaning: 12940 Supplicant stopped responding to ISE during conducting inner EAP-MSCHAPv2 method
## ID: 12941
### Meaning: 12941 Supplicant stopped responding to ISE during conducting inner EAP-GTC method
## ID: 12942
### Meaning: 12942 Supplicant stopped responding to ISE during conducting inner EAP-TLS method
## ID: 12943
### Meaning: 12943 Supplicant stopped responding to ISE during PEAPv0 protected termination
## ID: 12944
### Meaning: 12944 Supplicant stopped responding to ISE during PEAPv1 protected termination
## ID: 12945
### Meaning: 12945 Supplicant stopped responding to ISE during EAP-FAST protected termination
## ID: 12946
### Meaning: 12946 Supplicant stopped responding to ISE during LEAP
## ID: 12947
### Meaning: 12947 Supplicant stopped responding to ISE during EAP-MD5
## ID: 12948
### Meaning: 12948 Supplicant sent unexpected unencrypted TLS handshake message instead of TLS application data in PEAP protocol
## ID: 12949
### Meaning: 12949 Supplicant sent malformed PEAP message - wrong block cioher padding
## ID: 12950
### Meaning: 12950 Supplicant sent malformed PEAP message - bad record MAC
## ID: 12951
### Meaning: 12951 Unexpected renegotiation received. Renegotiation is not supported in PEAP
## ID: 12952
### Meaning: 12952 Received EAP packet from the middle of conversation but the conversation was not started on this PSN
## ID: 12953
### Meaning: 12953 Received EAP packet from the middle of conversation that contains a session on this PSN that does not exist
## ID: 12954
### Meaning: 12954 CRL signature check failed
## ID: 12955
### Meaning: 12955 RADIUS request that contains EAP message must contain MessageAuthenticator attribute
## ID: 12956
### Meaning: 12956 Client certificate validation failed due to name constraints permitted subtree violation
## ID: 12957
### Meaning: 12957 Client certificate validation failed due to name constraints excluded subtree violation
## ID: 12958
### Meaning: 12958 Client certificate validation failed due to min or max name constraints values violation
## ID: 12959
### Meaning: 12959 Client certificate validation failed due to unsupported name constraint type
## ID: 12960
### Meaning: 12960 Client certificate validation failed due to bad or unsupported name constraint syntax
## ID: 12961
### Meaning: 12961 Client certificate validation failed due to bad or unsupported name syntax of the constraint
## ID: 12962
### Meaning: 12962 Reject User Authorization PAC since its Initiator-ID does not match the Tunnel PAC Initiator-ID
## ID: 12963
### Meaning: 12963 Received malformed EAP Payload TLV
## ID: 12968
### Meaning: 12968 Client didn't provide suitable ciphers
## ID: 12970
### Meaning: 12970 EAP-TTLS inner method finished with failure
## ID: 12972
### Meaning: 12972 EAP-TTLS failed SSL/TLS handshake because the client rejected the ISE local-certificate
## ID: 12973
### Meaning: 12973 EAP-TTLS failed SSL/TLS handshake after a client alert
## ID: 12974
### Meaning: 12974 EAP-TTLS handshake failed
## ID: 12976
### Meaning: 12976 EAP-TTLS authentication failed
## ID: 12980
### Meaning: 12980 Failed to negotiate EAP because EAP-TTLS not allowed in the Allowed Protocols
## ID: 12981
### Meaning: 12981 Supplicant stopped responding to ISE during EAP-TTLS tunnel establishment
## ID: 12982
### Meaning: 12982 Supplicant stopped responding to ISE during EAP-TTLS plain inner MSCHAPv2 authentication flow
## ID: 12984
### Meaning: 12984 Unexpected renegotiation received. Renegotiation is not supported in EAP_TTLS
## ID: 12986
### Meaning: 12986 Client requested TLSv1.0 or TLSv1.1 that is not allowed
## ID: 12990
### Meaning: 12990 No valid OCSP server URLs found in the AIA extension of client certificate
## ID: 12993
### Meaning: 12993 User Auth failed because OCSP is unreachable
## ID: 12994
### Meaning: 12994 EAP-TTLS inner method CHAP is not allowed in Allowed Protocols
## ID: 12995
### Meaning: 12995 EAP-TTLS inner method MSCHAPv1 is not allowed in Allowed Protocols
## ID: 12996
### Meaning: 12996 EAP-TTLS inner method MSCHAPv2 is not allowed in Allowed Protocols
## ID: 12997
### Meaning: 12997 EAP-TTLS inner method PAP is not allowed in Allowed Protocols
## ID: 12998
### Meaning: 12998 Failed to negotiate EAP for inner method because EAP-MD5 not allowed under EAP-TTLS configuration in the Allowed Protocols
## ID: 13023
### Meaning: 13023 Command matched a Deny-Always rule
## ID: 13025
### Meaning: 13025 Command failed to match a Permit rule
## ID: 13036
### Meaning: 13036 Selected Shell Profile is DenyAccess
## ID: 13037
### Meaning: 13037 Shell Profile Privilege Level not configured correctly
## ID: 13051
### Meaning: 13051 Size of data fieid is small.
## ID: 13052
### Meaning: 13052 Size of data fieid is small.
## ID: 13061
### Meaning: 13061 Accounting request received but neither local nor remote accounting is configured.
## ID: 13076
### Meaning: 13076 No command set for selected rule
## ID: 15001
### Meaning: 15001 Adapter must contain at least one value
## ID: 15002
### Meaning: 15002 Configured operator failed to match the value type
## ID: 15003
### Meaning: 15003 Incorrect database configuration
## ID: 15007
### Meaning: 15007 Policy result type did not match expected result
## ID: 15010
### Meaning: 15010 Identity policy is not configured
## ID: 15015
### Meaning: 15015 Could not find ID Store
## ID: 15019
### Meaning: 15019 Could not find selected Authorization Profiles
## ID: 15020
### Meaning: 15020 Could not find selected Shell Profiles
## ID: 15021
### Meaning: 15021 Could not find selected Command Set
## ID: 15022
### Meaning: 15022 Could not find selected Access Service
## ID: 15024
### Meaning: 15024 PAP is not allowed
## ID: 15039
### Meaning: 15039 Rejected per authorization profile
## ID: 15045
### Meaning: 15045 CHAP is not allowed
## ID: 15046
### Meaning: 15046 MS-CHAP v1 is disabled under allowed protocols.
## ID: 15047
### Meaning: 15047 MS-CHAP v2 is disabled under allowed protocols.
## ID: 15056
### Meaning: 15056 IP Address for interface selected in portal settings is undefined
## ID: 22000
### Meaning: 22000 Authentication resulted in internal error
## ID: 22003
### Meaning: 22003 Missing attribute for authentication
## ID: 22004
### Meaning: 22004 Wrong password
## ID: 22005
### Meaning: 22005 Could not get shell profile object
## ID: 22007
### Meaning: 22007 Username attribute is not present in the authentication request
## ID: 22008
### Meaning: 22008 Changing enable password is not allowed
## ID: 22017
### Meaning: 22017 Selected Identity Source is DenyAccess
## ID: 22020
### Meaning: 22020 Configuration error: identity source blank
## ID: 22021
### Meaning: 22021 Configuration error: authentication IDStores list blank
## ID: 22022
### Meaning: 22022 Error in setting fail open options
## ID: 22040
### Meaning: 22040 Wrong password or invalid shared secret
## ID: 22041
### Meaning: 22041 User not found in Internal Identity Store
## ID: 22044
### Meaning: 22044 Identity policy result is configured for certificate based authentication methods but received password based
## ID: 22045
### Meaning: 22045 Identity policy result is configured for password based authentication methods but received certificate based authentication request
## ID: 22047
### Meaning: 22047 User name attribute is missing in client certificate
## ID: 22048
### Meaning: 22048 Client certificate binary is missing
## ID: 22049
### Meaning: 22049 Binary comparison of certificates failed
## ID: 22052
### Meaning: 22052 Authentication IDStore empty after completing authentication
## ID: 22055
### Meaning: 22055 Failed to find expected Principal Username X509 Attribute in user's certificate
## ID: 22056
### Meaning: 22056 Subject not found in the applicable identity store(s)
## ID: 22063
### Meaning: 22063 Wrong password
## ID: 22064
### Meaning: 22064 Authentication method is not supported by any applicable identity store(s)
## ID: 22065
### Meaning: 22065 Guest session limit could not be enforced as MnT node not reachable
## ID: 22066
### Meaning: 22066 Guest session limit is active; removing older guest sessions
## ID: 22067
### Meaning: 22067 Guest session limit response is missing relevant information in order to remove old guest sessions
## ID: 22069
### Meaning: 22069 AD account search attribute is missing in client certificate
## ID: 22074
### Meaning: 22074 This Protocol is disabled in FIPS mode.
## ID: 22089
### Meaning: 22089 New user session not permitted. Max sessions user limit has been reached
## ID: 22091
### Meaning: 22091 Authentication failed. User account is disabled due to excessive failed authentication attempts at global level
## ID: 22096
### Meaning: 22096 Max session policy is not available for Proxy
## ID: 22097
### Meaning: 22097 New user session not permitted. Max sessions group limit has been reached
## ID: 22098
### Meaning: 22098 New user session not permitted. Max sessions user in group limit has been reached
## ID: 24001
### Meaning: 24001 Cannot establish connection with LDAP server
## ID: 24002
### Meaning: 24002 Cannot bind connection with administrator credentials
## ID: 24003
### Meaning: 24003 Cannot bind connection with anonymous credentials
## ID: 24006
### Meaning: 24006 User search ended with an error
## ID: 24007
### Meaning: 24007 Host search ended with an error
## ID: 24008
### Meaning: 24008 User not found in LDAP Server
## ID: 24009
### Meaning: 24009 Host not found in LDAP Server
## ID: 24010
### Meaning: 24010 Ambiguous user
## ID: 24011
### Meaning: 24011 Ambiguous host
## ID: 24018
### Meaning: 24018 Cannot retrieve user's certificate
## ID: 24019
### Meaning: 24019 LDAP connection error was encountered
## ID: 24020
### Meaning: 24020 User authentication against the LDAP Server failed
## ID: 24021
### Meaning: 24021 User authentication ended with an error
## ID: 24027
### Meaning: 24027 Groups search ended with an error
## ID: 24030
### Meaning: 24030 SSL connection error was encountered
## ID: 24050
### Meaning: 24050 Cannot authenticate with LDAP Identity Store because password was not present or was empty
## ID: 24051
### Meaning: 24051 Secure LDAP failed SSL handshake because of an unknown CA in the certificates chain
## ID: 24052
### Meaning: 24052 Secure LDAP connection reconnect due to OCSP found revoked certificate
## ID: 24053
### Meaning: 24053 Secure LDAP connection reconnect due to CRL found revoked certificate
## ID: 24056
### Meaning: 24056 User authentication against LDAP server detected that user password has expired and there are no more grace authentications
## ID: 24057
### Meaning: 24057 User authentication against LDAP server detected that the password failure limit has been reached and the account is locked
## ID: 24058
### Meaning: 24058 LDAP server does not support password modify extended operation (RFC 3062)
## ID: 24059
### Meaning: 24059 User password change ended with an error
## ID: 24064
### Meaning: 24064 The user doesn't have sufficient rights to change password
## ID: 24065
### Meaning: 24065 The new password does not conform to LDAP password policy
## ID: 24067
### Meaning: 24067 The password change is not enabled on LDAP Identity Store configuration page
## ID: 24202
### Meaning: 24202 Internal ID Store could not connect to the database
## ID: 24203
### Meaning: 24203 User need to change password
## ID: 24205
### Meaning: 24205 Could not change password to new password
## ID: 24206
### Meaning: 24206 User disabled
## ID: 24207
### Meaning: 24207 Host disabled
## ID: 24216
### Meaning: 24216 The user is not found in the internal users identity store
## ID: 24217
### Meaning: 24217 The host is not found in the internal endpoints identity store
## ID: 24218
### Meaning: 24218 The TrustSec device is not defined under Network Devices and AAA Clients in ISE
## ID: 24219
### Meaning: 24219 User account suspended
## ID: 24300
### Meaning: 24300 No domain controller available
## ID: 24301
### Meaning: 24301 No writable domain controller available
## ID: 24302
### Meaning: 24302 No global catalog available
## ID: 24305
### Meaning: 24305 Failover threshold has been exceeded
## ID: 24306
### Meaning: 24306 No DNS server available
## ID: 24307
### Meaning: 24307 DNS server returned error
## ID: 24322
### Meaning: 24322 Identity resolution detected no matching account
## ID: 24331
### Meaning: 24331 Lookup SID By Name request failed
## ID: 24333
### Meaning: 24333 Lookup Object By SID request failed
## ID: 24338
### Meaning: 24338 Authentication Ticket (TGT) request failed
## ID: 24340
### Meaning: 24340 Service Ticket request failed
## ID: 24342
### Meaning: 24342 Service Ticket validation failed
## ID: 24344
### Meaning: 24344 RPC Logon request failed
## ID: 24346
### Meaning: 24346 RPC Change Password request failed
## ID: 24347
### Meaning: 24347 Account disabled
## ID: 24348
### Meaning: 24348 Account locked
## ID: 24349
### Meaning: 24349 Account expired
## ID: 24350
### Meaning: 24350 Password expired
## ID: 24351
### Meaning: 24351 Account validation succeeded
## ID: 24352
### Meaning: 24352 Identity resolution failed
## ID: 24356
### Meaning: 24356 LDAP fetch failed
## ID: 24370
### Meaning: 24370 User credentials have been revoked.
## ID: 24371
### Meaning: 24371 The ISE machine account does not have the required privileges to fetch groups.
## ID: 24401
### Meaning: 24401 Could not establish connection with ISE Active Directory agent
## ID: 24403
### Meaning: 24403 User authentication against Active Directory failed
## ID: 24404
### Meaning: 24404 Active Directory operation failed because of an invalid input parameter
## ID: 24405
### Meaning: 24405 Active Directory operation failed because of a timeout error
## ID: 24406
### Meaning: 24406 User authentication against Active Directory failed since user has invalid credentials
## ID: 24407
### Meaning: 24407 User authentication against Active Directory failed since user is required to change his password
## ID: 24408
### Meaning: 24408 User authentication against Active Directory failed since user has entered the wrong password
## ID: 24409
### Meaning: 24409 User authentication against Active Directory failed since the user's account is disabled
## ID: 24410
### Meaning: 24410 User authentication against Active Directory failed since user is considered to be in restricted logon hours
## ID: 24411
### Meaning: 24411 Change password against Active Directory failed since user has a non-compliant password
## ID: 24412
### Meaning: 24412 User not found in Active Directory
## ID: 24413
### Meaning: 24413 User's domain is not recognized by Active Directory
## ID: 24414
### Meaning: 24414 User authentication against Active Directory failed since the user's account has expired
## ID: 24415
### Meaning: 24415 User authentication against Active Directory failed since user's account is locked out
## ID: 24417
### Meaning: 24417 User's Groups retrieval from Active Directory failed
## ID: 24418
### Meaning: 24418 Machine authentication against Active Directory failed since it is disabled in configuration
## ID: 24419
### Meaning: 24419 User's Attributes retrieval from Active Directory failed
## ID: 24421
### Meaning: 24421 Change password against Active Directory failed since it is disabled in configuration
## ID: 24426
### Meaning: 24426 User change password against Active Directory failed
## ID: 24427
### Meaning: 24427 Access to Active Directory failed
## ID: 24428
### Meaning: 24428 Connection related error has occurred in either LRPC, LDAP or KERBEROS
## ID: 24429
### Meaning: 24429 Could not establish connection with Active Directory
## ID: 24436
### Meaning: 24436 Machine Lookup in Active Directory failed
## ID: 24437
### Meaning: 24437 Machine not found in Active Directory
## ID: 24438
### Meaning: 24438 Found multiple occurrences of the machine in Active Directory
## ID: 24440
### Meaning: 24440 Machine primary group name does not exist in Active Directory
## ID: 24441
### Meaning: 24441 ISE machine account is not permitted to log on
## ID: 24442
### Meaning: 24442 User-related object retrieval operation from Active Directory has failed
## ID: 24444
### Meaning: 24444 Active Directory operation has failed because of an unspecified error in the ISE
## ID: 24446
### Meaning: 24446 Active Directory domain controller is unreachable
## ID: 24447
### Meaning: 24447 ISE appliance machine account in Active Directory is disabled, deleted or reset
## ID: 24448
### Meaning: 24448 User object retrieval from Active Directory failed because of a timeout error
## ID: 24449
### Meaning: 24449 User's Groups retrieval from Active Directory failed because of  a timeout error
## ID: 24450
### Meaning: 24450 User's Attributes retrieval from Active Directory failed because of a timeout error
## ID: 24451
### Meaning: 24451 Machine object retrieval from Active Directory failed because of a timeout error
## ID: 24452
### Meaning: 24452 Machine primary group retrieval from Active Directory failed because of a timeout error
## ID: 24453
### Meaning: 24453 Machine Attributes retrieval from Active Directory failed because of a timeout error
## ID: 24454
### Meaning: 24454 User authentication against Active Directory failed because of a timeout error
## ID: 24455
### Meaning: 24455 Change password against Active Directory failed because of a timeout error
## ID: 24460
### Meaning: 24460 There are multiple occurrences of the user name in the Active directory
## ID: 24461
### Meaning: 24461 Could not locate the user in the Active directory using User Lookup
## ID: 24462
### Meaning: 24462 The ISE Active Directory module does not have sufficient memory
## ID: 24463
### Meaning: 24463 Internal error in the ISE Active Directory
## ID: 24464
### Meaning: 24464 The Active Directory does not have the required privileges
## ID: 24465
### Meaning: 24465 ISE is not joined to an Active Directory Domain Controller
## ID: 24466
### Meaning: 24466 ISE Active Directory agent is down
## ID: 24467
### Meaning: 24467 Could not retrieve the specified object
## ID: 24468
### Meaning: 24468 Failed to retrieve the user certificate from Active Directory
## ID: 24480
### Meaning: 24480 The machine-related object retrieval operation from Active Directory has failed
## ID: 24481
### Meaning: 24481 The machine's attribute retrieval from Active Directory has failed
## ID: 24483
### Meaning: 24483 Failed to retrieve the machine certificate from Active Directory
## ID: 24484
### Meaning: 24484 Machine authentication against Active Directory has failed because the machine's password has expired
## ID: 24485
### Meaning: 24485 Machine authentication against Active Directory has failed because of wrong password
## ID: 24486
### Meaning: 24486 Machine authentication against Active Directory has failed because the machine's account is disabled
## ID: 24487
### Meaning: 24487 Machine authentication against Active Directory failed since machine is considered to be in restricted logon hours
## ID: 24488
### Meaning: 24488 The machine's domain is not recognized by Active Directory
## ID: 24489
### Meaning: 24489 Machine authentication against Active Directory has failed because the machine's account has expired
## ID: 24490
### Meaning: 24490 Machine authentication against Active Directory has failed because the machine's account is locked out
## ID: 24491
### Meaning: 24491 Machine authentication against Active Directory has failed because the machine has invalid credentials
## ID: 24492
### Meaning: 24492 Machine authentication against Active Directory has failed
## ID: 24493
### Meaning: 24493 ISE has problems communicating with Active Directory using its machine credentials
## ID: 24494
### Meaning: 24494 Active Directory DNS servers are not available
## ID: 24495
### Meaning: 24495 Active Directory servers are not available
## ID: 24496
### Meaning: 24496 Authentication rejected due to a white or black list restriction
## ID: 24497
### Meaning: 24497 Selected Active Directory Scope is empty
## ID: 24498
### Meaning: 24498 Resolve identity exceeded time limit
## ID: 24503
### Meaning: 24503 Cannot establish a session with the RSA SecurID Server
## ID: 24504
### Meaning: 24504 The lock user request has failed
## ID: 24508
### Meaning: 24508 User authentication failed
## ID: 24511
### Meaning: 24511 Check passcode operation against RSA SecurID Server resulted in error
## ID: 24512
### Meaning: 24512 Next tokencode operation in RSA SecurID Server resulted in error
## ID: 24513
### Meaning: 24513 Set New PIN operation in RSA SecurID Server resulted in error
## ID: 24514
### Meaning: 24514 Next tokencode operation in RSA SecurID Server failed
## ID: 24515
### Meaning: 24515 Set New PIN operation in RSA SecurID Server failed
## ID: 24518
### Meaning: 24518 User canceled New PIN operation; User authentication against RSA SecurIDServer failed
## ID: 24519
### Meaning: 24519 User entered invalid PIN; PIN must only contain alpha-numeric characters
## ID: 24520
### Meaning: 24520 User entered invalid PIN; PIN must only contain numeric characters
## ID: 24521
### Meaning: 24521 User entered PIN with invalid length
## ID: 24522
### Meaning: 24522 PIN Accepted. Wait for the token code to change, then reauthenticate using the new passcode.
## ID: 24533
### Meaning: 24533 User reentered a different PIN
## ID: 24547
### Meaning: 24547 RSA request timeout expired. RSA authentication session cancelled
## ID: 24551
### Meaning: 24551 RSA request is declined, because RSA agent initialization has failed
## ID: 24552
### Meaning: 24552 Reject response from the RSA server is considered as User not found
## ID: 24556
### Meaning: 24556 User record was not found in the cache
## ID: 24557
### Meaning: 24557 An error occurred while searching for user records in the cache
## ID: 24558
### Meaning: 24558 User cache is not enabled in the RSA identity store configuration
## ID: 24563
### Meaning: 24563 An error occurred while searching for user record in the Passcode cache
## ID: 24564
### Meaning: 24564 Passcode cache is not enabled in the RSA identity store configuration
## ID: 24565
### Meaning: 24565 Authentication passed via Passcode cache
## ID: 24608
### Meaning: 24608 RADIUS token identity store failed due to wrong input
## ID: 24611
### Meaning: 24611 RADIUS token server configuration error
## ID: 24613
### Meaning: 24613 Authentication against the RADIUS token server failed
## ID: 24616
### Meaning: 24616 RADIUS token identity store received timeout error
## ID: 24617
### Meaning: 24617 RADIUS token identity store received external error
## ID: 24618
### Meaning: 24618 RADIUS token identity store received unknown error
## ID: 24626
### Meaning: 24626 User record not found in the cache
## ID: 24627
### Meaning: 24627 An error occurred while searching for user records in the cache
## ID: 24628
### Meaning: 24628 User cache not enabled in the RADIUS token identity store configuration
## ID: 24630
### Meaning: 24630 Failed to get Server IP by name
## ID: 24633
### Meaning: 24633 The user is not found in the internal guests identity store
## ID: 24637
### Meaning: 24637 An error occurred while searching for user record in the Passcode cache
## ID: 24638
### Meaning: 24638 Passcode cache is not enabled in the RADIUS token identity store configuration
## ID: 24639
### Meaning: 24639 Authentication passed via Passcode cache
## ID: 24701
### Meaning: 24701 Identity resolution by certificate failed
## ID: 24702
### Meaning: 24702 Identity resolution by certificate found no matching account
## ID: 24703
### Meaning: 24703 Identity resolution by certificate found ambiguous accounts
## ID: 24704
### Meaning: 24704 Authentication failed because identity credentials are ambiguous
## ID: 24705
### Meaning: 24705 Authentication failed because ISE server is not joined to required domains
## ID: 24706
### Meaning: 24706 Authentication failed because NTLM was blocked
## ID: 24707
### Meaning: 24707 Authentication failed because all identity names have been rejected
## ID: 24708
### Meaning: 24708 User not found in Active Directory. Some authentication domains were not available
## ID: 24709
### Meaning: 24709 Host not found in Active Directory. Some authentication domains were not available
## ID: 24710
### Meaning: 24710 Identity resolution is configured to drop request if required domain is not available
## ID: 24711
### Meaning: 24711 Domain controller cannot pass request through the trust path to the account domain
## ID: 24712
### Meaning: 24712 Authentication failed because domain trust is restricted
## ID: 24717
### Meaning: 24717 Active Directory Kerberos ticket authentication failed
## ID: 24718
### Meaning: 24718 Active Directory Kerberos ticket expired
## ID: 24719
### Meaning: 24719 Active Directory Kerberos ticket authentication failed because of the ISE account password mismatch, integrity check failure or expired ticket
## ID: 24801
### Meaning: 24801 Unable to decode SAML request
## ID: 24802
### Meaning: 24802 Unknown SAML attribute value type assertion used for 'username'
## ID: 24803
### Meaning: 24803 Unable to find 'username' attribute assertion
## ID: 24804
### Meaning: 24804 SAML message intended destination (required by binding) was not present
## ID: 24805
### Meaning: 24805 SAML message intended destination endpoint did not match recipient endpoint
## ID: 24806
### Meaning: 24806 SAML IdentityProvider Certificate is not valid
## ID: 24807
### Meaning: 24807 SAML IdentityProvider Certificate was not checked
## ID: 24808
### Meaning: 24808 SAML IdentityProvider Certificate is expired
## ID: 24809
### Meaning: 24809 SAML IdentityProvider Certificate is revoked
## ID: 24810
### Meaning: 24810 SAML IdentityProvider CA Certificate is not valid
## ID: 24811
### Meaning: 24811 The request could not be performed due to an error on the part of the requester
## ID: 24812
### Meaning: 24812 The request could not be performed due to an error on the part of the SAML responder or SAML authority
## ID: 24813
### Meaning: 24813 The SAML responder could not process the request because the version of the request message was incorrect
## ID: 24814
### Meaning: 24814 The responding provider was unable to successfully authenticate the principal
## ID: 24815
### Meaning: 24815 Unexpected or invalid content was encountered within a saml:Attribute or saml:AttributeValue element
## ID: 24816
### Meaning: 24816 The SAML responder or SAML authority is able to process the request but has chosen not to respond.
## ID: 24817
### Meaning: 24817 The SAML responder or SAML authority does not support the request
## ID: 24818
### Meaning: 24818 The SAML responder cannot properly fulfil the request using the protocol binding specified in the request
## ID: 24819
### Meaning: 24819 Failed to retrieve signing certificate from the SAML response
## ID: 24820
### Meaning: 24820 Assertion does not contain Issuer
## ID: 24821
### Meaning: 24821 Assertion does not contain authentication statement
## ID: 24822
### Meaning: 24822 Assertion does not contain audience restriction conditions
## ID: 24823
### Meaning: 24823 Assertion does not contain matching service provider identifier in the audience restriction conditions
## ID: 24824
### Meaning: 24824 Subject confirmation does not contain subject confirmation data
## ID: 24825
### Meaning: 24825 The response must contain single assertion
## ID: 24826
### Meaning: 24826 Recipient does not match assertion consumption URL
## ID: 24827
### Meaning: 24827 Subject confirmation data does not contain NotOnOrAfter
## ID: 24828
### Meaning: 24828 Assertion is expired
## ID: 24829
### Meaning: 24829 Subject confirmation data IP address does not match end user IP address
## ID: 24830
### Meaning: 24830 Subject confirmation data does not contain InResponseTo
## ID: 24831
### Meaning: 24831 The InResponseTo does not match the original request id
## ID: 24832
### Meaning: 24832 Issuer format is not equal to urn:oasis:names:tc:SAML:2.0:nameid-format:entity
## ID: 24833
### Meaning: 24833 Issuer does not match Identity Provider ID
## ID: 24834
### Meaning: 24834 Assertion does not contain subject
## ID: 24835
### Meaning: 24835 Assertion does not contain subject confirmation
## ID: 24836
### Meaning: 24836 Assertion does not contain bearer subject confirmation
## ID: 24837
### Meaning: 24837 The signed response does not contain a Destination
## ID: 24838
### Meaning: 24838 The Destination on the response does not match the assertion consumer URL
## ID: 24839
### Meaning: 24839 The response does not contain assertion
## ID: 24840
### Meaning: 24840 The response signature is invalid
## ID: 24841
### Meaning: 24841 Response signature did not validate against the IdP signature certificate
## ID: 24842
### Meaning: 24842 The assertion signature on the response is invalid
## ID: 24843
### Meaning: 24843 Assertion signature is not not validated against the IdP signature certificate
## ID: 24844
### Meaning: 24844 Neither SAML response nor assertion are signed
## ID: 24845
### Meaning: 24845 SAML response can contain only one signing certificate
## ID: 24846
### Meaning: 24846 Several certificates are configured on IdP,however can not determine certificate for signature
## ID: 24847
### Meaning: 24847 Certificate is invalid
## ID: 24848
### Meaning: 24848 Failed to get signing certificate from IdP configuration
## ID: 24851
### Meaning: 24851 Connection to external ODBC database failed
## ID: 24857
### Meaning: 24857 Failed processing external ODBC database stored procedure results in a returned recordset
## ID: 24858
### Meaning: 24858 Failed processing external ODBC database stored procedure results in a returned output parameters
## ID: 24859
### Meaning: 24859 Failed calling external ODBC database stored procedure
## ID: 24860
### Meaning: 24860 ODBC database indicated plain text password authentication failure
## ID: 24864
### Meaning: 24864 ODBC database indicated fetching plain text password failure
## ID: 24868
### Meaning: 24868 ODBC database indicated user lookup failure
## ID: 24877
### Meaning: 24877 Subject formats persistent or transient are not supported as Identity Attribute
## ID: 24879
### Meaning: 24879 Identity provider metadata is not set
## ID: 24880
### Meaning: 24880 ODBC operation failed due to timeout elapsed
## ID: 24890
### Meaning: 24890 Social Login operation failed
## ID: 24900
### Meaning: 24900 Loading LDAP ID Store failed because of an unknown or missing CA for primary or secondary connection
## ID: 24901
### Meaning: 24901 Loading ID Store Sequence failed because of missing or corrupted ID Store
## ID: 25001
### Meaning: 25001 AD: ISE account password update failed.
## ID: 25003
### Meaning: 25003 AD: Machine TGT refresh failed.
## ID: 25010
### Meaning: 25010 Trusted domains discovery failed
## ID: 25016
### Meaning: 25016 DNS SRV query failed
## ID: 25018
### Meaning: 25018 DC discovery failed
## ID: 25020
### Meaning: 25020 KDC discovery failed
## ID: 25022
### Meaning: 25022 GC discovery failed
## ID: 25024
### Meaning: 25024 LDAP connect to domain controller failed
## ID: 25026
### Meaning: 25026 LDAP connect to global catalog failed
## ID: 25028
### Meaning: 25028 RPC connect to domain controller failed
## ID: 25030
### Meaning: 25030 KDC connect to domain controller failed
## ID: 25031
### Meaning: 25031 AD Provider failed to start
## ID: 25034
### Meaning: 25034 DNS A/AAAA query failed
## ID: 25044
### Meaning: 25044 Communication to domain failed
## ID: 25045
### Meaning: 25045 Configured nameserver is not responsive within timeout period. Server is either busy or unreachable.
## ID: 25046
### Meaning: 25046 Joined domain is unavailable
## ID: 25047
### Meaning: 25047 Authentication domain is unavailable
## ID: 25048
### Meaning: 25048 Active-Directory forest is unavailable
## ID: 25057
### Meaning: 25057 The ISE machine account does not have the required privileges to fetch groups.
## ID: 25058
### Meaning: 25058 ISE is not joined to an Active Directory Domain Controller
## ID: 25102
### Meaning: 25102 Connection to external REST database failed
## ID: 25106
### Meaning: 25106 REST ID Store server indicated plain text password authentication failure
## ID: 25111
### Meaning: 25111 Failed to set user groups in session cache
## ID: 25112
### Meaning: 25112 REST database indicated plain text password authentication failure
## ID: 31102
### Meaning: 31102 Applying configuration changes failed
## ID: 31104
### Meaning: 31104 Start up configuration load failed
## ID: 31106
### Meaning: 31106 Configuration management could not translate configuration change. Runtime configuration changes will not take effect
## ID: 31108
### Meaning: 31108 Cold configuration restart failed
## ID: 32006
### Meaning: 32006 Could not log to critical logger
## ID: 32016
### Meaning: 32016 System reached low disk space limit
## ID: 32700
### Meaning: 32700 Failover mode caused by an internal error. Configuration changes may not take effect
## ID: 33205
### Meaning: 33205 General PI error
## ID: 33300
### Meaning: 33300 General GUI error
## ID: 33500
### Meaning: 33500 Could not initialize EAP-TLS
## ID: 33501
### Meaning: 33501 Could not initialize EAP-FAST
## ID: 33502
### Meaning: 33502 Could not initialize PEAP
## ID: 33503
### Meaning: 33503 A blank CTL was configured for EAP-TLS
## ID: 33504
### Meaning: 33504 CTL initialization failed
## ID: 33505
### Meaning: 33505 Could not initialize EAP-TLS server-certificate
## ID: 33506
### Meaning: 33506 Could not initialize EAP-FAST server-certificate
## ID: 33507
### Meaning: 33507 Could not initialize PEAP server-certificate
## ID: 33508
### Meaning: 33508 Could not initialize the complete EAP-TLS server-certificate chain
## ID: 33509
### Meaning: 33509 PEAP failed to completely initialize the server-certificate chain
## ID: 33510
### Meaning: 33510 Could not initialize the complete EAP-FAST server-certificate chain
## ID: 33511
### Meaning: 33511 Could not initialize TEAP server-certificate
## ID: 33512
### Meaning: 33512 Could not initialize the complete TEAP server-certificate chain
## ID: 33513
### Meaning: 33513 Could not initialize TEAP
## ID: 33518
### Meaning: 33518 No cipher for full handshake TEAP authentication
## ID: 34157
### Meaning: 34157 Could not initialize EAP-TTLS
## ID: 34158
### Meaning: 34158 Could not initialize EAP-TTLS server-certificate
## ID: 34161
### Meaning: 34161 LDAPS connection establishment failed with SSL error
## ID: 34162
### Meaning: 34162 LDAPS connection terminated with SSL error
## ID: 34163
### Meaning: 34163 LDAPS connection establishment failed with non-SSL error
## ID: 34164
### Meaning: 34164 LDAPS connection terminated with non-SSL error
## ID: 35010
### Meaning: 35010 License is set to expire soon
## ID: 35011
### Meaning: 35011 License expired
## ID: 35012
### Meaning: 35012 Device count exceeded for base license
## ID: 35013
### Meaning: 35013 License deletion failed
## ID: 35014
### Meaning: 35014 License create failed
## ID: 35015
### Meaning: 35015 License update failed
## ID: 41015
### Meaning: 41015 Could not run
## ID: 41021
### Meaning: 41021 Could not update ISE Node Object
## ID: 41022
### Meaning: 41022 An error occurred while collecting NodeInfo
## ID: 41023
### Meaning: 41023 An error occurred while collecting replication status
## ID: 41024
### Meaning: 41024 Error loading NodeInfo
## ID: 41025
### Meaning: 41025 NodeInfo file contains incomplete information
## ID: 41026
### Meaning: 41026 Management config directory could not be created
## ID: 41027
### Meaning: 41027 NodeInfo file could not be created
## ID: 41031
### Meaning: 41031 Registering Secondary Hostname already exists in Primary database
## ID: 41032
### Meaning: 41032 Register failed since Secondary MAC address already exists in the Primary database
## ID: 41045
### Meaning: 41045 Failure. Specified replacement keyword is associated with a registered instance
## ID: 41064
### Meaning: 41064 The deployment Log Collector cannot be deregistered
## ID: 51005
### Meaning: 51005 Administrator authentication failed. Administrator account is disabled
## ID: 51007
### Meaning: 51007 Authentication failed. Account is disabled due to password expiration
## ID: 51008
### Meaning: 51008 Administrator authentication failed. Account is disabled due to excessive failed authentication attempts
## ID: 5238
### Meaning: 5238 Endpoint authentication problem was fixed
## ID: 5239
### Meaning: 5239 NAS problem was fixed
## ID: 5411
### Meaning: 5411 Supplicant stopped responding to ISE
## ID: 5417
### Meaning: 5417 Dynamic Authorization failed
## ID: 5434
### Meaning: 5434 Endpoint conducted several failed authentications of the same scenario
## ID: 5435
### Meaning: 5435 NAS conducted several failed authentications of the same scenario
## ID: 5436
### Meaning: 5436 RADIUS packet already in the process
## ID: 5437
### Meaning: 5437 Duplicate RADIUS packet for existing session but with different RADIUS parameters
## ID: 5438
### Meaning: 5438 RADIUS packet contains session on this PSN that does not exist
## ID: 5439
### Meaning: 5439 RADIUS packet contains session not started on this PSN
## ID: 5440
### Meaning: 5440 Endpoint abandoned EAP session and started new
## ID: 5441
### Meaning: 5441 Endpoint started new session while the packet of previous session is being processed. Dropping new session.
## ID: 5442
### Meaning: 5442 RADIUS request dropped due to system overload
## ID: 5443
### Meaning: 5443 RADIUS request dropped due to reaching EAP sessions limit
## ID: 5449
### Meaning: 5449 Endpoint failed authentication of the same scenario several times and was rejected
## ID: 60200
### Meaning: 60200 An IP-SGT mapping has failed deploying
## ID: 60202
### Meaning: 60202 IP-SGT deployment to TrustSec device failed
## ID: 60227
### Meaning: 60227 Failed to perform a CoA termination
## ID: 60234
### Meaning: 60234 The SXP connection has been disconnected
## ID: 60236
### Meaning: 60236 SXP connection failed
## ID: 60238
### Meaning: 60238 SXP binding failed
## ID: 60239
### Meaning: 60239 SXP binding conflict has occurred
## ID: 60459
### Meaning: 60459 SXP binding binding not propagated because binding threshold has been reached
## ID: 61074
### Meaning: 61074 Node went out of sync due to expired system certificate
## ID: 86009
### Meaning: 86009 Guest user is not found
## ID: 86010
### Meaning: 86010 Guest user authentication failed
## ID: 86011
### Meaning: 86011 Guest user is not enabled
## ID: 86012
### Meaning: 86012 User declined Access-Use Policy
## ID: 86013
### Meaning: 86013 Portal not found
## ID: 86014
### Meaning: 86014 User is suspended
## ID: 86015
### Meaning: 86015 Invalid Password Change
## ID: 86016
### Meaning: 86016 Guest Timeout Exceeded
## ID: 86017
### Meaning: 86017 Session Missing
## ID: 86018
### Meaning: 86018 Guest Change of Authorization Failed
## ID: 86019
### Meaning: 86019 Guest User restricted
## ID: 86020
### Meaning: 86020 Guest Unknown Error
## ID: 86023
### Meaning: 86023 Device Registration Web Authentication AUP Declined
## ID: 86025
### Meaning: 86025 Device Registration Web Authentication Portal Endpoint Creation Failed
## ID: 86026
### Meaning: 86026 Device Registration Web Authentication Portal CoA Termination Failed
## ID: 86029
### Meaning: 86029 Failed to perform a CoA termination
## ID: 88001
### Meaning: 88001 Failed to added a device (endpoint)
## ID: 88003
### Meaning: 88003 Failed to modify the device (endpoint)
## ID: 88005
### Meaning: 88005 Failed to delete the device (endpoint)
## ID: 88007
### Meaning: 88007 Failed to blacklist the device (endpoint)
## ID: 88009
### Meaning: 88009 Failed to reinstate the device (endpoint)
## ID: 88011
### Meaning: 88011 Failed to register/provision the device (endpoint)
## ID: 88013
### Meaning: 88013 Failed to perform a CoA termination
## ID: 88015
### Meaning: 88015 Failed to perform a CoA re-authentication
## ID: 89003
### Meaning: 89003 Failed to connect to MDM server
## ID: 89004
### Meaning: 89004 MDM server API version mismatch
## ID: 89005
### Meaning: 89005 MDM server response error
## ID: 91020
### Meaning: 91020 Active Directory dialin access denied for user.
## ID: 91050
### Meaning: 91050 RADIUS DTLS: TLS handshake failed because of an unknown CA in the certificates chain
## ID: 91051
### Meaning: 91051 RADIUS DTLS: TLS handshake failed because of a bad certificate in the certificate chain
## ID: 91052
### Meaning: 91052 RADIUS DTLS: TLS handshake failed because decryption error
## ID: 91053
### Meaning: 91053 RADIUS DTLS: TLS handshake failed because certificate has expired
## ID: 91054
### Meaning: 91054 RADIUS DTLS: TLS handshake failed because unknown certificate
## ID: 91056
### Meaning: 91056 RADIUS DTLS: TLS handshake failed because of unsupported protocol version
## ID: 91057
### Meaning: 91057 RADIUS DTLS CoA: TLS handshake failed because of an unknown CA in the certificates chain
## ID: 91058
### Meaning: 91058 RADIUS DTLS CoA: TLS handshake failed because of a bad certificate in the certificate chain
## ID: 91059
### Meaning: 91059 RADIUS DTLS CoA: TLS handshake failed because decryption error
## ID: 91060
### Meaning: 91060 RADIUS DTLS CoA: TLS handshake failed because certificate has expired
## ID: 91061
### Meaning: 91061 RADIUS DTLS CoA: TLS handshake failed because unknown certificate
## ID: 91062
### Meaning: 91062 RADIUS DTLS CoA: TLS handshake failed because of unsupported protocol version
## ID: 91063
### Meaning: 91063 RADIUS DTLS CoA: Client Certificate in not found in System certificates list
## ID: 91064
### Meaning: 91064 RADIUS DTLS connection disconnect due to OCSP found revoked certificate
## ID: 91065
### Meaning: 91065 RADIUS DTLS connection disconnect due to CRL found revoked certificate
## ID: 91066
### Meaning: 91066 RADIUS DTLS connection disconnect because of the client certificate is not yet valid
## ID: 91067
### Meaning: 91067 RADIUS DTLS CoA connection disconnect due to OCSP found revoked certificate
## ID: 91068
### Meaning: 91068 RADIUS DTLS CoA connection disconnect due to CRL found revoked certificate
## ID: 91069
### Meaning: 91069 RADIUS DTLS CoA connection disconnect because of the server certificate is not yet valid
## ID: 91076
### Meaning: 91076 RADIUS DTLS: OCSP status of user certificate is revoked
## ID: 91078
### Meaning: 91078 RADIUS DTLS: Handshake failed because OCSP status is unknown
## ID: 91080
### Meaning: 91080 RADIUS DTLS: Internal error occurred during communication with the OCSP server
## ID: 91081
### Meaning: 91081 RADIUS DTLS: OCSP server URL is invalid
## ID: 91082
### Meaning: 91082 RADIUS DTLS: Connection to OCSP server failed
## ID: 91084
### Meaning: 91084 RADIUS DTLS: OCSP server returned an error
## ID: 91085
### Meaning: 91085 RADIUS DTLS: OCSP server did not provide the required nonce in response
## ID: 91087
### Meaning: 91087 RADIUS DTLS: OCSP server response time verification failed
## ID: 91088
### Meaning: 91088 RADIUS DTLS: OCSP server response signature verification failed
## ID: 91097
### Meaning: 91097 RADIUS DTLS: No valid OCSP server URLs found in the AIA extension of client certificate
## ID: 91100
### Meaning: 91100 RADIUS DTLS: Handshake failed because OCSP is unreachable
## ID: 91102
### Meaning: 91102 RADIUS DTLS: client Identity check failed
## ID: 91107
### Meaning: 91107 RADIUS DTLS: TLS handshake failed because of client hello verification failed