from snps import SNPs
import musicalbeeps
import math

player = musicalbeeps.Player(volume = 0.3, mute_output = False)

s = SNPs("../../genome.txt")
df = s.snps

for index, row in df.iterrows():
    print(row['genotype'])
    if type(row['genotype']) == str:
        for c in row['genotype']:
            if c == 'T':
                c = 'B'
            player.play_note(c, 0.1)
