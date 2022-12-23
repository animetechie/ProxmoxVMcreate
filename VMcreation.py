import requests

# Set the API endpoint URL
api_endpoint = "https://proxmox_server/api2/json/nodes/proxmox/qemu"

# Set the authentication credentials
auth = ("root@pam", "secret")

# Set the VM configuration
vm_config = {
    "vmid": 100,  # set the VM ID
    "name": "vm1",  # set the VM name
    "sockets": 1,  # set the number of CPU sockets
    "cores": 1,  # set the number of CPU cores per socket
    "memory": 1024,  # set the amount of RAM in MB
    "ostype": "l26",  # set the operating system type
    "ide2": "local:iso/ubuntu-20.04.1-live-server-amd64.iso,media=cdrom",  # set the ISO image for the installation media
    "boot": "cd",  # set the boot order
    "net0": "virtio=52:54:00:12:34:56,bridge=vmbr0",  # set the network configuration
}

# Send a POST request to create the VM
response = requests.post(api_endpoint, auth=auth, json=vm_config)

# Check if the request was successful
if response.status_code == 200:
    print("VM created successfully")
else:
    print("Error creating VM: {}".format(response.json()["message"]))
