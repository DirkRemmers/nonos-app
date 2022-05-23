import streamlit as st
from collections import defaultdict
import random

@st.experimental_memo()
def maak_recepten_dicts():
    # dit wordt een lange dict met beschrijvingen van alle recepten. Key beschrijft het artikel en de soort (bijvoorbeeld: tartelette - pecan karamel) 

    recepten_dict = {}

    # monchou taarten - monchou kers
    recepten_dict['monchou taarten - kers'] = {}
    recepten_dict['monchou taarten - kers']['ingredienten'] = {
        'bastogne koeken': {'hoeveelheid': 200, 'unit': 'g'},
        'monchou': {'hoeveelheid': 200, 'unit': 'g'},
        'witte basterdsuiker': {'hoeveelheid': 100, 'unit': 'g'},
        'vanille suiker': {'hoeveelheid': 2, 'unit': 'zakje'},
        'slagroom': {'hoeveelheid': 250, 'unit': 'mL'},
        'klopvast': {'hoeveelheid': 1, 'unit': 'zakje'},
        'kersenvlaaifruit': {'hoeveelheid': 1, 'unit': 'blik'},
    }
    recepten_dict['monchou taarten - kers']['bereiding'] = [ 
    '1: Maal de Bastogne koeken fijn en smelt de boter. Zorg ervoor dat de boter niet bruin wordt.',
    '2: Mix de Bastognekruimels en de boter en schep het mengsel in de springvorm.',
    '3: Druk het mengsel aan met de bolle kant van een eetlepel.',
    '4: ',
    ]

    return recepten_dict

@st.experimental_memo()
def maak_artikelen_dict(recepten_dict):
    artikelen = defaultdict()
    # tartelletjes
    artikelen['tartelette'] = {}
    artikelen['tartelette']['soorten'] = {
        'pecan karamel': {},
        'lemon meringue':{}, 
        'millionare shortbread':{}, 
        'snicker':{}, 
        'passievrucht meringue':{}, 
        'rood fruit':{}
        }
    artikelen['tartelette']['prijs'] = 3.75
    artikelen['tartelette']['max hoeveelheid per soort'] = 12
    artikelen['tartelette']['max soorten'] = 2

    # brownie
    artikelen['brownie'] = {}
    artikelen['brownie']['soorten'] = {
        'brownie':{}, 
        'blondie':{}, 
        'oreo':{}, 
        'stroopwafel':{}, 
        'blondie pecan':{}, 
        'blondie macadamia':{}, 
        'rood fruit':{}, 
        'pindakaas':{}
        }
    artikelen['brownie']['prijs'] = 3.00
    artikelen['brownie']['max hoeveelheid per soort'] = 16
    artikelen['brownie']['max soorten'] = 1

    # koeken
    artikelen['koeken'] = {}
    artikelen['koeken']['soorten'] = {
        'macadamia wit':{}, 
        'chocolade':{}, 
        'm&m':{}, 
        'pecan chocolade':{}, 
        'cranberry':{}, 
        'fondantkoeken':{}, 
        'oatmeal':{}, 
        'nutella':{}, 
        'bueno':{}, 
        'red velvet':{}
        }
    artikelen['koeken']['prijs'] = 2.00
    artikelen['koeken']['max hoeveelheid per soort'] = 10
    artikelen['koeken']['max soorten'] = 2

    # cake
    artikelen['cake'] = {}
    artikelen['cake']['soorten'] = {
        'bramen':{}, 
        'chocolade':{}, 
        'normaal':{}, 
        'blauwe bes':{}, 
        'wortel':{}, 
        'courgette':{}, 
        'citroen maanzaad':{}
        }
    artikelen['cake']['prijs'] = 2.50 # per plakje
    artikelen['cake']['max hoeveelheid per soort'] = 10 # plakken = 1 cake
    artikelen['cake']['max soorten'] = 1

    # macarons
    artikelen['macarons'] = {}
    artikelen['macarons']['soorten'] = {
        'citroen':{}, 
        'witte chocolade':{}, 
        'chocolade':{}, 
        'passievrucht':{}, 
        'framboos':{}, 
        'mokka':{}, 
        'speculaas':{}, 
        'appel':{}, 
        'aardbei':{}, 
        'mango':{}
        }
    artikelen['macarons']['prijs'] = 1.50
    artikelen['macarons']['max hoeveelheid per soort'] = 30
    artikelen['macarons']['max soorten'] = 3

    # fudge
    artikelen['fudge'] = {}
    artikelen['fudge']['soorten'] = {
        'ferrero':{}, 
        'oreo':{}, 
        'witte chocolade framboos':{}, 
        'ruby pistache':{}, 
        'karamel':{}, 
        'pecan zeezout':{}, 
        'puur':{}
        }
    artikelen['fudge']['prijs'] = 1.50
    artikelen['fudge']['max hoeveelheid per soort'] = 16
    artikelen['fudge']['max soorten'] = 1

    # cupcake
    artikelen['cupcake'] = {}
    artikelen['cupcake']['soorten'] = {
        'vanille':{}, 
        'witte chocolade':{}, 
        'chocolade':{}, 
        'blauwe bes':{}, 
        'bramen':{}, 
        'citroen maanzaad':{}, 
        'wortel':{}, 
        'nutella':{}
        }
    artikelen['cupcake']['prijs'] = 3.00
    artikelen['cupcake']['max hoeveelheid per soort'] = 12
    artikelen['cupcake']['max soorten'] = 1

    # niet fruit taarten
    artikelen['niet fruit taarten'] = {}
    artikelen['niet fruit taarten']['soorten'] = {
        'carrotcake':{}, 
        'cheesecake':{}, 
        'chocolade karamel':{}, 
        'chocolade maracuja':{}, 
        'chocolade mousse':{}, 
        'chocolade taart':{}, 
        'framboos chocolade':{}, 
        'mokka':{}, 'nutella schuimtaart':{}, 
        'oreo':{}, 
        'red velvet':{}, 
        'tiramisu':{}, 
        'vegan carrotcake':{}
        }
    artikelen['niet fruit taarten']['prijs'] = 4.00
    artikelen['niet fruit taarten']['max hoeveelheid per soort'] = 10
    artikelen['niet fruit taarten']['max soorten'] = 1

    # fruit taarten
    artikelen['fruit taarten'] = {}
    artikelen['fruit taarten']['soorten'] = {
        'annanas bavarois':{}, 
        'biscuit banaan':{}, 
        'biscuit lemomcurd aardbei':{}, 
        'bosvruchten yoghurt':{}, 
        'citroen meringue':{}, 
        'limoncello tiramisu':{}, 
        'pavlova':{}, 
        'slagroom rood fruit':{}
        }
    artikelen['fruit taarten']['prijs'] = 4.00
    artikelen['fruit taarten']['max hoeveelheid per soort'] = 10
    artikelen['fruit taarten']['max soorten'] = 1
    
    # monchou taarten
    artikelen['monchou taarten'] = {}
    artikelen['monchou taarten']['soorten'] = {
        'aardbei':{}, 
        'citroen':{}, 
        'kers':recepten_dict['monchou taarten - kers'], 
        'kokos limoen':{}, 
        'oreo':{}
        }
    artikelen['monchou taarten']['prijs'] = 3.50
    artikelen['monchou taarten']['max hoeveelheid per soort'] = 8
    artikelen['monchou taarten']['max soorten'] = 1

    # appeltaart
    artikelen['appeltaart'] = {}
    artikelen['appeltaart']['soorten'] = {
        'appeltaart1':{},
        'appeltaart2': {},
        }
    artikelen['appeltaart']['prijs'] = 3.50
    artikelen['appeltaart']['max hoeveelheid per soort'] = 8
    artikelen['appeltaart']['max soorten'] = 2

    return artikelen

# don't cache!
def randomize_artikelen(artikelen_dict, vorige_vitrine_dict= False):
    # selecteer artikelen
    gekozen_artikelen_dict = {}
    totale_waarde = 0
    for soort in artikelen_dict.keys():
        if soort != 'appeltaart':
            # get artikel informatie
            artikel_info = artikelen_dict[soort]

            # kies een aantal artikelen
            gekozen_artikelen = random.sample(artikel_info['soorten'].keys(), artikel_info['max soorten'])

            # voeg ze toe aan de gekozen_artikel_dict
            gekozen_artikelen_dict[soort] = {}
            gekozen_artikelen_dict[soort]['soorten'] = {}
            for gekozen_artikel in gekozen_artikelen:
                gekozen_artikelen_dict[soort]['soorten'][gekozen_artikel] = artikel_info['soorten'][gekozen_artikel]

            # voeg de prijs per artikel toe
            gekozen_artikelen_dict[soort]['prijs'] = artikel_info['prijs']
            gekozen_artikelen_dict[soort]['hoeveelheid per artikel'] = artikel_info['max hoeveelheid per soort']

    return gekozen_artikelen_dict

def maak_vitrine_zin(soort, gekozen_artikelen_dict):
    # maak een zin om te presenteren
    gekozen_artikelen_lijst = gekozen_artikelen_dict[soort]['soorten'].keys()
    n_gekozen_artikelen = len(gekozen_artikelen_lijst)
    for n, artikel in enumerate(gekozen_artikelen_lijst):
        # begin van de zin
        if n == 0:
            gekozen_artikelen_text = f"**_{artikel}_**"
        # eind van de zin
        elif n == n_gekozen_artikelen-1:
            gekozen_artikelen_text = f"{gekozen_artikelen_text} en **_{artikel}_**"
        # midden in de zin
        else:
            gekozen_artikelen_text = f"{gekozen_artikelen_text}, **_{artikel}_**"

# define the main layout of the plotter
st.set_page_config(page_title="Nono's vitrine randomizer!", page_icon='nono_logo.jpeg', layout = 'wide')
cols = st.columns(2)
cols[0].image('nono_logo.jpeg', width = 200)
cols[1].title("Nono's vitrine randomizer!")

# maak alle recepten en organizeer deze
recepten_dict = maak_recepten_dicts()
artikelen_dict = maak_artikelen_dict(recepten_dict)

# kies een modus
# mode = st.selectbox('Wat wil je doen?', ['Browse recepten', 'Randomize de vitrine', 'Voeg recepten toe'])
mode = st.selectbox('Wat wil je doen?', ['Randomize de vitrine'])

# mode specifieke functies
if mode == 'Randomize de vitrine':
    # kies een random set aan artikelen
    if st.button('Wat ga ik deze week maken?'):
        gekozen_artikelen_dict = randomize_artikelen(artikelen_dict)
        for soort in gekozen_artikelen_dict.keys():
            
            # maak een zin om te presenteren
            gekozen_artikelen_lijst = gekozen_artikelen_dict[soort]['soorten'].keys()
            n_gekozen_artikelen = len(gekozen_artikelen_lijst)
            for n, artikel in enumerate(gekozen_artikelen_lijst):
                # begin van de zin
                if n == 0:
                    gekozen_artikelen_text = f"**_{artikel}_**"
                # eind van de zin
                elif n == n_gekozen_artikelen-1:
                    gekozen_artikelen_text = f"{gekozen_artikelen_text} en **_{artikel}_**"
                # midden in de zin
                else:
                    gekozen_artikelen_text = f"{gekozen_artikelen_text}, **_{artikel}_**"

            st.markdown(f"Als {soort} gaan we de {gekozen_artikelen_text} soort(en) maken.")

