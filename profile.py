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

# Lists for the nodes
nodeList = []
linkList = []

for x in range(1,4):
     # Add a XenVM node to the request.
     node = request.XenVM("node"+str(x))
     # Use Centos
     node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
     # Request private IP addresses for everyone.
     iface = node.addInterface("if1")
     iface.component_id = "eth1"
     iface.addAddress(pg.IPv4Address("192.168.1."+str(x), "255.255.255.0"))
     # Request a public IP address for node1
     if (x == 1):
          node.routable_control_ip = "true"
     # Install and execute a script that is contained in the repository.
     node.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))
     nodeList.append(node)
     # Print the RSpec to the enclosing page.
     pc.printRequestRSpec(request)

for i in range(1,4):
     for j in range(1,4):
          if (i!=j):
               linkList.append(request.Link(members = [nodeList(i),nodeList(j)]))
