import pyrax
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("servername", help="Prefix for server name(s)")
parser.add_argument("-c", "--count", help="Number of instances to create", default=1)
args = parser.parse_args()

print "Server prefix: " + args.servername
print "Number of instances: " + str(args.count)

# Using credentials file
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cs = pyrax.cloudservers
print cs.servers.list()
