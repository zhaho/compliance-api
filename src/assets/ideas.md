# Services/{hostname}/Contracts
hostname
services: [{servicename: telegraf, port: 9126},{servicename: node_exporter, port: 9100}]

# Services
servicename telegraf|node_exporter|windows_exporter
host_id 1,2,3,4,5
port 9126|9100|9186

# Hosts
image linux/oracle/windows
type    app/data

# Backup
host_id
type