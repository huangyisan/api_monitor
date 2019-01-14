from api.alerts_summary_hosts import Ambari
from zabbix_handler.call_zabbix_sender import zabbix_sender

def main():
    platform = 'pacdn_hadoop'
    url = "http://10.1.11.31:8080/api/v1/clusters/"
    username = 'admin'
    password = 'admin'
    querystring = {"fields":"Clusters/total_hosts,alerts_summary_hosts","minimal_response":"true"}

    value_file = 'value_file'

    ambari = Ambari(platform, url=url, username=username, password=password, querystring=querystring)

    response_json = ambari.get_alerts_summary()

    zabbix_sender(valuefile=value_file,message=response_json)

if __name__ == '__main__':
    main()


