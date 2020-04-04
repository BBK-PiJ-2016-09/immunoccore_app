## Genes app

Basic app to store genes

It runs on sqlite by default, to change it to postgres go to immunocore/immunocore/settings.py and uncomment the postgres
section, user is docker pwd is docker database is docker.
I include the sqlite file so you can see a couple of uploaded genes if you run it locally.


### Installation:
To run it locally 
````
virtualenv immunocore_env -p python3.7
source immunocore_env/bin/activate
cd immunocore

# install the packages
python setup.py install

# migrations
python manage.py makemigrations
python manage.py migrate

# start the server
python manage.py runserver

````

You can now access a home page in http://localhost:8000/immunocore_app

### Adding new genes:
Go to: http://localhost:8000/admin click on GENES + add and enter the required values
````e.g. {
    "name": "TTN",
    "sequence": "TGCAGTCGAANGGAGCANCCTTGNCTGAGGTTTCGGCC AAATGATAGGAATGCTTAGTGGCGGACTGGTGAGTAACGCGTGAGGAACCTACCTTCCAG AGGGGGACAACAGTTGGAAACGACTGCTAATACCGCATGACGCATGACCGGGGCATCCCG GGCATGTCAAAGATTTTATCGCTGGAAGATGGCCTCGCGTCTGATTAGCTAGATGGTGGG GTAACGGCCCACCATGGCGACGATCAGTAGCCGGACTGAGAGGTTGACCGGCCACATTGG GACTGAGATACGGCCCAGACTCCTACGGGAGGCAGCAGTGGGGAATATTGGGCAATGGAC GCAAGTCTGACCCAGCAACGCCGCGTGAAGGAAGAAGGCTTTCGGGTTGTAAACTTCTTT TGTCAGGGAAGAGTAGAAGACGGTACCTGACGAATAAGCCACGGCTAACTACGTGCCAGC AGCCGCGGTAATACGTAGGTGGCAAGCGTTGTCCGGATTTACTGGGTGTAAAGGGCGTGC AGCCGGGCCGGCAAGTCAGATGTGAAATCTGGAGGCTTAACCTCCAAACTGCATTTGAAA CTGTAGGTCTTGAGTACCGGAGAGGTTATCGGAATTCCTTGTGTAGCGGTGAAATGCGTA GATATAAGGAAGAACACCAGTGGCGAAGGCGGATAACTGGNCGGCNACTGACGGTGAGGC GCGAAAGCGTGGGGAGCAAACAGGANTAGATACCCTGGNAGTCCACGCTGTAAACGATGG NNACTAGGTGTGCGGGGACTGACCCCCTGCGTGCCNCANTTAACACAATAANTATCCCAC CTGGGGNNTANNATCGCAAGGNTGAAACTC",
    "comments": "The TTN gene provides instructions for making a very large protein called titin. This protein plays an important role in muscles the body uses for movement (skeletal muscles) and in heart (cardiac) muscle.",
}
````

### Viewing your genes:
http://127.0.0.1:8000/immunocore_app/genes/
Each gene is shown in a card, if you are using the local version with preuploaded genes, try:
http://127.0.0.1:8000/immunocore_app/gene_router/1/ This is the api endpoint for the gene entity, you can modify the 
values here, changing the content section and invoking PATCH

### Running on docker:
Change the settings.py to support postgres (uncomment DATABASES postgres section and comment the sqlite section)
build a postgres image and redirect its port to your local postgres port

````
# Run postgres publishing port 5432 
docker run -d postgres -p 5432:5432 --env POSTGRES_PASSWORD=docker \
    --env POSTGRES_USER=docker --env POSTGRES_DB=docker postgres

# Build the image for the app 
docker build -t immunocore_app <DIRECTORY_WHERE_DOCKERFILE_LIVES>
docker run -d immunocore_app 
````

### Running on docker swarm
This will give you a load balancer and separate services in a network, just execute the docker-swarm.sh script


### Command line access
Only basic requests access: e.g. if you are using the default sqlite db

To rename a gene
````
import requests
gene_1 = requests.get('http://127.0.0.1:8000/immunocore_app/gene_router/1/').json()     
gene_1['name'] = 'modified_name_for_testing'
requests.patch('http://127.0.0.1:8000/immunocore_app/gene_router/1/', json=gene_1)
````

You can also use the core api package included with Django, but I am not familiar with this, you can see how it works in immunocore_app/client.py
