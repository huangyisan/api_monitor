import os
import platform


hostname = platform.node()

def zabbix_sender(valuefile, message):
    f = open('./{0}'.format(valuefile), 'w+')
    for k,v in message.items():
        f.write("{0} {1} {2}\n".format(hostname, k, v))
    f.close()
    os.system('/usr/bin/zabbix_sender -vv -z 10.1.18.1 -i ./value_file')

