from api.alerts_summary_hosts import Ambari
from zabbix_handler.call_zabbix_sender import zabbix_sender

def main():
    platform = 'pacdn_hadoop'
    url = "http://10.1.11.31:8080/api/v1/clusters/"
    username = 'admin'
    password = 'admin'
    querystring = {"fields":"Clusters/total_hosts,alerts_summary_hosts","minimal_response":"true"}

    promfile = '/app/local/node_exporter/collect/ambari.prom'
    # promfile = 'ambari.prom'
    value_file = 'value_file'

    ambari = Ambari(platform, url=url, username=username, password=password, querystring=querystring)

    response_json = ambari.get_alerts_summary()
    CRITICAL = response_json.get("CRITICAL",'0')
    OK = response_json.get("OK",'0')
    UNKNOWN = response_json.get("UNKNOWN",'0')
    WARNING = response_json.get("WARNING",'0')

    content = ['# HELP ambari status check ambari status.\n','# TYPE hardware_status counter\n','ambari_status_CRITICAL{{status="CRITICAL"}} {0}\n'.format(CRITICAL), \
               'ambari_status_OK{{status="OK"}} {0}\n'.format(OK),'ambari_status_UNKNOWN{{status="UNKNOWN"}} {0}\n'.format(UNKNOWN),'ambari_status_WARNING{{status="WARNING"}} {0}'.format(WARNING) ]

    f = open(promfile,'w+')
    f.writelines(content)
    f.close()

    try:
        zabbix_sender(valuefile=value_file,message=response_json)
    except Exception:
        pass

if __name__ == '__main__':
    main()


