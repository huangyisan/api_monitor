from api.alerts_summary_hosts import Ambari

platform = 'pacdn_hadoop'
url = "http://10.1.11.31:8080/api/v1/clusters/"
username = 'admin'
password = 'admin'
querystring = {"fields":"Clusters/total_hosts,alerts_summary_hosts","minimal_response":"true"}

ambari = Ambari(platform, url=url, username=username, password=password, querystring=querystring)

response_json = ambari.get_alerts_summary()