# Vault configuration file

ui = false
disable_mlock = false
log_format = "standard"

# Use node fqdn to advertise the leader in HA mode
# api_addr = "https://fqdn:8200"

listener "tcp" {
  address     = "127.0.0.1:8200"
  # scheme      = "https"

  # tls_ca_file = "/etc/vault/ca.crt"
  # tls_cert_file = "/etc/vault/vault.crt"
  # tls_key_file  = "/etc/vault/vault.key"
}

# storage "consul" {
#   token = "CHANGEME"
#   address = "127.0.0.1:8500"
#   path    = "vault/"
# }

# storage "etcd" {
#   # address is a comma separated list of the etcd nodes"
#   address = "https://127.0.0.1:2379"
#   etcd_api = "v3"
#   # ha_enabled = "true"
#   path = "/vault"
#   username = ""
#   password = ""
#   # tls_ca_file = "/etc/vault/ca.crt"
#   # tls_cert_file = "/etc/vault/vault.crt"
#   # tls_key_file  = "/etc/vault/vault.key"
# }

