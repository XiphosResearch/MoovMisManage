# MoovMisManage
Moovbox Mismanagement Utilities

## Contents

./openvpn_keys: OpenVPN keys/certs extracted from the devices  
ca.crt  
dh1024.pem  
server.key  

###./ssh_keys: SSH keys (unique) extracted from devices.  
* ssh_host_dsa_key - /etc/ssh/ host dsa key.
* ssh_host_rsa_key - /etc/ssh/ host rsa key.
* ssh_key - wierd file named "ssh_key" in /etc/ that auths to two German boxes. See presentation.  

###./ssl_keys: SSL keys/certs extracted from the devices. Only the unique ones listed here :)  
* cacert.pem   
* moovbox.cert.pem   
* moovbox.key.3des.pem   
* server.pem

###./tools: Tools and such :)  
* moovbox.py - Remote Root Exploit leveraging Shellshock. Gives backconnect shell.   
* moovmanage_auth.py - Enable/Disable Auth on Moovmanage Web Interface leveraging the Shellshock exploit    
* moovmanage_extract_creds.py - Credentials extractor for parsing moovbox.settings databases  
