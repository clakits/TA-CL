import common

#csv_file="dns.csv"
#json_file="dns.json"

csv_file="/Users/clakits/Documents/Healthsouth/sensors012317-2.csv"
json_file="/Users/clakits/Documents/Healthsouth/sensors012317.json"
header_row =["cpu_quota_mode", "is_internal", "updated_at", "deleted_at", "last_registration_req_at", "uuid", "platform",
                  "data_plane_disabled", "auto_upgrade_opt_out", "health", "last_config_fetch_at",
                  "client_ip", "last_software_update_at", "description", "sw_upgrade_successful", "cpu_quota_us", "mac",
                  "current_sw_version", "vrf_id", "decommissioned", "config_updated_at", "created_at", "host_name",
                   "enable_pid_lookup", "_id"]
common.json2csv_file(json_file, csv_file, header_row)