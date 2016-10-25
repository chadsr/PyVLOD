from rdflib import Namespace, XSD
import os

DATA_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))) + '/data/parltrack/'

DATA_OUTPUT = DATA_DIR + 'parltrack.trig'
DATA_MEP = DATA_DIR + 'meps.json'
DATA_VOTES = DATA_DIR + 'votes.json'
DATA_DOSSIER = DATA_DIR + 'dossiers.json'

DICT_MEPS = DATA_DIR + 'dict_meps.json'
DICT_PARTIES = DATA_DIR + 'dict_parties.json'

# Number of elements to mine
MEP_LIMIT = None
DOSSIER_LIMIT = None
VOTES_LIMIT = None

DATABASE = 'http://localhost:5820/#/databases/votes/'
NAMESPACE = DATABASE

ont = 'http://votes.examples.com/ontology/'
ONT = Namespace(ont)
PREFIX = ''

DOSSIER_TYPE = 'Legislative proposal published'

# eo = 'http://www.w3.org/2003/01/geo/wgs84_pos#'
# GEO = Namespace(geo)

dbo = 'http://dbpedia.org/ontology/'
DBO = Namespace(dbo)
dbr = 'http://dbpedia.org/resource/'
DBR = Namespace(dbr)
dbp = 'http://dbpedia.org/property/'
DBP = Namespace(dbp)

foaf = 'http://xmlns.com/foaf/0.1/'
FOAF = Namespace(foaf)

DOSSIER = ONT['Bill']
DOSSIER_TITLE = ONT['bill_text']
PROCESSED_BY = ONT['processedBy']

ABSTAINS = ONT['abstains']
VOTES_FOR = ONT['votesYay']
VOTES_AGAINST = ONT['votesNay']
VOTES_IN = ONT['votesIn']

MEMBER_OF = ONT['memberOf']

GENDER = DBO['gender']
MALE = DBR['Male']
FEMALE = DBR['Female']
EUROPEAN_PARLIAMENT = DBR['European_Parliament']
POLITICAL_PARTY = DBO['PoliticalParty']
POLITICAL_PARTY_IN_LEGISLATURE = DBO['politicalPartyInLegislature']

FULL_NAME = FOAF['name']
BIRTH_DATE = DBO['birthDate']
BIRTH_PLACE = DBO['birthPlace']
DEATH_DATE = DBO['deathDate']

URI = XSD['anyURI']
STRING = XSD['string']
DATE = XSD['date']