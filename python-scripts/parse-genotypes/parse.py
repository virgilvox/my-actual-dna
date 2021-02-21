from snps import SNPs
s = SNPs("../../genome.txt")

print(s.source)
print(s.count)

df = s.snps
print(df.columns.values)
for index, row in df.iterrows():
    print(row['genotype'])
    