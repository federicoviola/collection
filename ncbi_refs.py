from Bio import Entrez

pmid = "21994945"

# tell NCBI who I am
Entrez.email = 'zaking@ucsd.edu'

# get details for pmid
print Entrez.efetch(db="pubmed", id=pmid).read()

# find articles in pmc that cite this PMID
Entrez.read(Entrez.elink(dbfrom="pubmed", db="pmc", LinkName="pubmed_pmc_refs", from_uid=pmid))

# get references
r = Entrez.read(Entrez.elink(dbfrom="pubmed", db="pubmed", LinkName="pubmed_pubmed_refs", from_uid=pmid))

print r[0]['LinkSetDb'][0]['Link'].__len__()
