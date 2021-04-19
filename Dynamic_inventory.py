import json

#Get inventory data from source.
def get_inventory_data():
    return {
        "database": {
            "hosts": "{target1}",
            "vars": {
                "ansible_ssh_pass": "admin",
                "ansible_ssh_host": "192.168.0.101"
            }
        },
        "web": {
            "hosts": "{target2}",
            "vars": {
                "ansible_ssh_pass": "admin"
                "ansible_ssh_host": "192.168.0.103"
            }
        }
    }

# Default main function
if __name__ == "__main__":
    inventory_data = get_inventory_data()
    print(json.dumps(inventory_data))
