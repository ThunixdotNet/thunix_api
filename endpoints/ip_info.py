from flask_restful import Resource
import psutil

class Ip_Info(Resource):
    def get_ip_addresses(self, family):
        ip_addresses = []
        for interface, snics in psutil.net_if_addrs().items():
            for snic in snics:
                if snic.family == family:
                    ip_addresses.append(
                        {
                            # We use caps against convention here to make it easier to append
                            # into the JSON payload
                            "Interface": interface,
                            "Address": snic.address,
                            "Netmask": snic.netmask
                        }
                    )
        return ip_addresses
    
    def get(self):
        ipv4 = self.get_ip_addresses(socket.AF_INET)
        
        payload = [
            {
                "Interfaces": []
            }
        ]
        for addr in ipv4:
            payload[0]["Interfaces"].append(addr)
    
        return payload
