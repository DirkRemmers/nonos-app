from re import S
import streamlit as st
from collections import defaultdict
import random
from streamlit_tags import st_tags
import json

@st.experimental_memo()
def maak_artikelen_dict():
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
        'kers':{}, 
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

def voeg_nieuw_ingredient_toe():
    # laadt de data
    with open('data.json', 'r') as fp:
        data = json.load(fp)

    if st.session_state['nieuw ingredient'] not in data['ingredienten'] and st.session_state['nieuw ingredient'] != "":
        oude_ingredienten_lijst = data['ingredienten'].copy()
        nieuwe_ingredienten_lijst = sorted(oude_ingredienten_lijst + [str.lower(st.session_state['nieuw ingredient'])])
        data['ingredienten'] = nieuwe_ingredienten_lijst
        with open('data.json', 'w') as fp:
            json.dump(data, fp)
    
    st.session_state['nieuw ingredient'] = ""

def voeg_nieuw_unit_toe():
    # laadt de data
    with open('data.json', 'r') as fp:
        data = json.load(fp)

    if st.session_state['nieuw unit'] not in data['units'] and st.session_state['nieuw unit'] != "":
        oude_unit_lijst = data['units'].copy()
        nieuwe_unit_lijst = oude_unit_lijst + [str.lower(st.session_state['nieuw unit'])]
        data['units'] = nieuwe_unit_lijst
        with open('data.json', 'w') as fp:
            json.dump(data, fp)
    
    st.session_state['nieuw unit'] = ""

def sla_nieuw_recept_op():
    # laadt de data
    with open('data.json', 'r') as fp:
        data = json.load(fp)

    if st.session_state['recept titel'] not in data['recepten'].keys():
        data['recepten'][st.session_state['recept titel']] = st.session_state['nieuw_recept_dict']
        # store ev"appeltaart": {"aantal personen": 8, "ingredienten": {"appels": {"hoeveelheid": 2, "unit": "stuks"}}}, "test": {"aantal personen": 2, "ingredienten": {"appels": {"hoeveelheid": 3, "unit": "g"}}}entual new data
        with open('data.json', 'w') as fp:
            json.dump(data, fp)
        st.success("Het recept is toegevoegd!")

    st.session_state['recept titel'] = ""
    for key in st.session_state.keys():
        if key != 'recept titel':
            del st.session_state[key]

def sla_recept_aanpassing_op():
    # laadt de data
    with open('data.json', 'r') as fp:
        data = json.load(fp)

    data['recepten'][st.session_state['recept titel']] = st.session_state['aangezpast_recept_dict']
    with open('data.json', 'w') as fp:
        json.dump(data, fp)
    st.success("Het recept is aangepast!")

    st.session_state['recept titel'] = ""
    for key in st.session_state.keys():
        if key != 'recept titel':
            del st.session_state[key]

# define the main layout of the plotter
st.set_page_config(page_title="Nono's app", page_icon='nono_logo.jpeg', layout = 'wide')
cols = st.columns(2)
cols[0].image('nono_logo.jpeg', width = 200)
cols[1].title("Nono's app")

# kies een modus
# mode = st.selectbox('Wat wil je doen?', ['Browse recepten', 'Randomize de vitrine', 'Voeg recepten toe'])
mode = st.sidebar.radio('Wat wil je doen?', ['Randomize de vitrine', 'Recept invoeren', 'Recept aanpassen', 'Download de data'])

# mode specifieke functies
if mode == 'Randomize de vitrine':
    artikelen_dict = maak_artikelen_dict()
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


elif mode == 'Recept invoeren':
    # vul de titel van dit recept in
    st.text_input('Hoe heet het recept dat je wilt toevoegen?', key = 'recept titel')

    # laadt de data
    with open('data.json', 'r') as fp:
        data = json.load(fp)

    # waarschuw dat dit recept er al in staat
    if st.session_state['recept titel'] in data['recepten'].keys():
        st.warning(f'{st.session_state["recept titel"]} staat al in de receptenlijst, als je dit wil aanpassen, selecteer de optie "recept aanpassen".')
        st.stop()

    if st.session_state['recept titel'] != '':

        with st.expander('Voeg de ingredienten toe.', expanded = True):

            # geef aan voor hoeveel personen dit recept is
            aantal_personen = st.number_input('Voor hoeveel personen is dit recept?', min_value = 0, max_value = 100, step = 1)

            # selecteer alle nodige ingredienten
            beschikbare_ingredienten_lijst = data['ingredienten'].copy()

            if 'ingredienten selectie' not in st.session_state.keys():
                st.session_state['ingredienten selectie'] = []

            kolommen = st.columns(2)
            nieuw_ingredient = kolommen[1].text_input("Voeg een nieuw soort ingredient in", key = 'nieuw ingredient')
            nieuw_ingredient_toevoegen = kolommen[1].button("Voeg toe.", on_click = voeg_nieuw_ingredient_toe, key = "ingredient toevoegen")
            ingredienten_selectie = kolommen[0].multiselect("Selecteer de ingredienten", data['ingredienten'], default = st.session_state['ingredienten selectie'])
            if ingredienten_selectie != st.session_state['ingredienten selectie']:
                st.session_state['ingredienten selectie'] = ingredienten_selectie.copy()
                st.experimental_rerun()
                
            beschikbare_units_lijst = data['units']

            # vul de hoeveelheden en units in per ingredient
            cols = st.columns(2)
            st.session_state['nieuw_recept_dict'] = {}
            st.session_state['nieuw_recept_dict']['aantal personen'] = aantal_personen
            st.session_state['nieuw_recept_dict']['ingredienten'] = {}
            for ingredient in ingredienten_selectie:
                st.session_state['nieuw_recept_dict']['ingredienten'][ingredient] = {}
                st.session_state['nieuw_recept_dict']['ingredienten'][ingredient]['hoeveelheid'] = cols[0].number_input(f'Hoeveel van {ingredient} heb je nodig?', key = f'{ingredient}_hoeveelheid', min_value = 0)
                st.session_state['nieuw_recept_dict']['ingredienten'][ingredient]['unit'] = cols[1].selectbox('Selecteer ', beschikbare_units_lijst, key = f'{ingredient}_unit')

        if all([x['hoeveelheid'] != 0 for x in st.session_state['nieuw_recept_dict']['ingredienten'].values()]) and aantal_personen > 0 and len(ingredienten_selectie) > 0:
            if st.button("Klik hier om het recept in te voeren.", on_click = sla_nieuw_recept_op):
                st.experimental_rerun()

        units_expander = st.expander("Voeg units toe", expanded = False)
        with units_expander:    
            nieuw_unit = st.text_input("Voeg een nieuwe unit in", key = 'nieuw unit')
            nieuw_unit_toevoegen = st.button("Voeg toe.", on_click = voeg_nieuw_unit_toe, key = "unit toevoegen")


elif mode == 'Recept aanpassen':
    # laadt de data
    with open('data.json', 'r') as fp:
        data = json.load(fp)

    # selecteer het recept wat je wilt aanpassen
    beschikbare_recepten_lijst = sorted(list(data['recepten'].keys()))
    recept_selectie = st.selectbox("Kies het recept dat je wilt aanpassen", [''] + beschikbare_recepten_lijst, key = 'recept titel')

    if recept_selectie != '':

        with st.expander('Voeg de ingredienten toe.', expanded = True):
            # geef aan voor hoeveel personen dit recept is
            aantal_personen = st.number_input("Voor hoeveel personen is dit recept?", min_value = 1, max_value=100, step = 1, value = data['recepten'][recept_selectie]['aantal personen'])

            # selecteer alle nodige ingredienten
            beschikbare_ingredienten_lijst = data['ingredienten'].copy()

            if 'ingredienten selectie' not in st.session_state:
                st.session_state['ingredienten selectie'] = list(data['recepten'][recept_selectie]['ingredienten'].keys())

            kolommen = st.columns(2)
            nieuw_ingredient = kolommen[1].text_input("Voeg een nieuw soort ingredient in", key = 'nieuw ingredient')
            nieuw_ingredient_toevoegen = kolommen[1].button("Voeg toe.", on_click = voeg_nieuw_ingredient_toe, key = "ingredient toevoegen")
            ingredienten_selectie = kolommen[0].multiselect("Selecteer de ingredienten", data['ingredienten'], default = st.session_state['ingredienten selectie'])
            if ingredienten_selectie != st.session_state['ingredienten selectie']:
                st.session_state['ingredienten selectie'] = ingredienten_selectie.copy()
                st.experimental_rerun()
                
            beschikbare_units_lijst = data['units']

            # vul de hoeveelheden en units in per ingredient
            cols = st.columns(2)
            st.session_state['aangepast_recept_dict'] = {}
            st.session_state['aangepast_recept_dict']['aantal personen'] = aantal_personen
            st.session_state['aangepast_recept_dict']['ingredienten'] = {}
            for ingredient in ingredienten_selectie:
                st.session_state['aangepast_recept_dict']['ingredienten'][ingredient] = {}
                if ingredient in data['recepten'][recept_selectie]['ingredienten'].keys():
                    value = data['recepten'][recept_selectie]['ingredienten'][ingredient]['hoeveelheid']
                else: 
                    value = 0
                st.session_state['aangepast_recept_dict']['ingredienten'][ingredient]['hoeveelheid'] = cols[0].number_input(f'Hoeveel van {ingredient} heb je nodig?', value = value, key = f'{ingredient}_hoeveelheid', min_value = 0)
                aangepaste_unit_lijst = beschikbare_units_lijst.copy()
                if ingredient in data['recepten'][recept_selectie]['ingredienten'].keys():
                    aangepaste_unit_lijst.insert(0, aangepaste_unit_lijst.pop(aangepaste_unit_lijst.index(data['recepten'][recept_selectie]['ingredienten'][ingredient]['unit'])))
                st.session_state['aangepast_recept_dict']['ingredienten'][ingredient]['unit'] = cols[1].selectbox('Selecteer ', aangepaste_unit_lijst, key = f'{ingredient}_unit')

        if all([x['hoeveelheid'] != 0 for x in st.session_state['aangepast_recept_dict']['ingredienten'].values()]) and aantal_personen > 0 and len(ingredienten_selectie) > 0:
            if st.button("Klik hier om het recept in te voeren.", on_click = sla_recept_aanpassing_op):
                st.experimental_rerun()

        units_expander = st.expander("Voeg units toe", expanded = False)
        with units_expander:    
            nieuw_unit = st.text_input("Voeg een nieuwe unit in", key = 'nieuw unit')
            nieuw_unit_toevoegen = st.button("Voeg toe.", on_click = voeg_nieuw_unit_toe, key = "unit toevoegen")


elif mode == 'Download de data':

    # laadt de data
    with open('data.json', 'r') as fp:
        data = json.load(fp)

    json_string = json.dumps(data)

    st.download_button(
        label="Download JSON",
        file_name="data.json",
        mime="application/json",
        data=json_string,
    )