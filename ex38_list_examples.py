#list examples
#1.List of clients
#2.List of employees on payroll
#3.List of days in a week
#4.List of months in a year
#5.List of genes in a gene sequence
#6.List of amino acids in a peptide
#7.List of members in a sports team
#8.List of suppliers to a manufacturing operation
#9.List of customer complaints
#10.List of stored items

na_base=['Adenine','Thymine','Guanine','Cytosine','Uracil']
for i in range(len(na_base)):
    print(f"The base no: {i+1} is {na_base[i]}.")
na_base.append('CRISPR base 1')
print(na_base)
print(' '.join(na_base))
