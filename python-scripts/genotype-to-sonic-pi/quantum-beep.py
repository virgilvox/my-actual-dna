from snps import SNPs
from pythonosc import udp_client
import time

oscclient = udp_client.SimpleUDPClient("127.0.0.1", 4560) # port Sonic Pi is listening on

s = SNPs("../../genome.txt")
df = s.snps

for index, row in df.iterrows():
    print(row['genotype'])
    if type(row['genotype']) == str:
        note = []
        for c in row['genotype']:
            if c == 'T':
                c = 2
            if c == 'A':
                c = 1
            if c == 'G':
                c = 0
            if c == 'C':
                c = 3
            
            # note.append(c)
            
            oscclient.send_message("/lounging/dna", c)
            time.sleep(0.01)

