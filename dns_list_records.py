import json
import urllib

v_username = "your_name"
v_token = "your_token"
v_url_getdomain='https://'+v_username+":"+v_token+"@api.name.com/v4/domains"

print v_url_getdomain;

v_domainlist=[]
v_domaindic={}

request = urllib.urlopen(v_url_getdomain)
data = json.loads(request.read())
# get domain_name list from name.com

f = open('dns.txt', 'w')

for i in data['domains']:
    print  i['domainName']

    v_url_getrecord='https://'+v_username+":"+v_token+"@api.name.com/v4/domains/"+i['domainName']+"/records"
    print v_url_getrecord
    request = urllib.urlopen(v_url_getrecord)
    data_rec = json.loads(request.read())
    # get domain records by domain_name from name.com

    try:
        for j in data_rec['records']:
            #print j['fqdn'],j['answer']
            f.write(j['fqdn']+" " +j['answer']+"\n")

    except:
        # if domain_name don't contain records will trigger exception
        print  i['domainName']+": read failed"
        f.write(i['domainName']+": read failed\n")

f.close()