# coding=utf-8
from ipwhois import IPWhois
import socket

def sitebilgilerinibul(site):
    ip     = socket.gethostbyname(site)
    obje   = IPWhois(ip)
    obj    = obje.lookup_whois()
    eposta = obj["nets"][0]['emails']
    desc  = obj["nets"][0]['description']
    print  "Site\t: ", site, "\n"
    print "IP adresi\t: ", ip
    print  "\nAçıklama\t: ", desc
    print "\nEmails\t: \n"
    print  email

if __name__ == "__main__":
    site = "website_name"
    sitebilgilerinibul(site)
