"""This is part 2 of Assignment 2 for CSC496.

Instructions:
Cheer when this works. 
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add a raw PC to the request.
#node = request.RawPC("node")

# Add a XenVM node to the request.
node = request.XenVM("node")

# Use Centos
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"

# Request a public IP address
node.routable_control_ip = "true"

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
