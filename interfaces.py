import psutil, socket, json

payload = []

def get_ip_addresses(family):
    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == family:
                yield (interface, snic.address, snic.netmask)

ipv4s = list(get_ip_addresses(socket.AF_INET))

#print (json.dumps(ipv4s))
print("{\n\t\"Interfaces\":[")

i = 0
for i in range(len(ipv4s)) :
  print ("\t\t{")
  print ("\t\t\t\"Interface\":" + "\"" + ipv4s[i][0] + "\",")
  print ("\t\t\t\"Address\":" + "\"" + ipv4s[i][1] + "\"," )
  print ("\t\t\t\"Netmask\":" + "\"" + ipv4s[i][2] + "\"" )
  print ("\t\t}",end="")
  i += 1
  if ( i < len(ipv4s) ) :
    print(",")
  else:
    print("\n")
  

print("\t]")
print("}")
