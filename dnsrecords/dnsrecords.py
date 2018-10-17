import os, errno
import dns.resolver
import string

domain = input("Domain ie: google, hotmail: ") +'.com'
dnsr = ['A', 'MX','TXT', 'NS']

try:
	os.mkdir('records/')
except OSError as e:
	if e.errno != errno.EEXIST:
		raise

for i in dnsr:
	recf = i+'.txt'
	file = open('records/'+recf, 'w')
	rquery = dns.resolver.query(domain, i)
	for x in rquery:
		print(x.to_text())
		file.write(x.to_text())
	file.close()

answers = dns.resolver.query('google.com', 'SOA')
print ('query qname:', answers.qname, ' num ans.', len(answers))
for rdata in answers:
    print (' serial: %s  tech: %s' % (rdata.serial, rdata.rname))
    print (' refresh: %s  retry: %s' % (rdata.refresh, rdata.retry))
    print (' expire: %s  minimum: %s' % (rdata.expire, rdata.minimum))
    print (' mname: %s' % (rdata.mname))
    print (' rname: %s' % (rdata.rname))