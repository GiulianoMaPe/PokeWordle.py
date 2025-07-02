import re
import customtkinter as ctk
import random
from PIL import Image
import os
import sys
from collections import Counter

if getattr(sys, 'frozen', False):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.abspath(".")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

primera_gen = {"bulbasaur": 9, "ivysaur": 7, "venusaur": 8, "charmander": 10, "charmeleon": 10, "charizard": 9, "squirtle": 8, "wartortle": 9, "blastoise": 9, "caterpie": 8, "metapod": 7,
               "butterfree": 10, "weedle": 6, "kakuna": 6, "beedrill": 8, "pidgey": 6, "pidgeotto": 9, "pidgeot": 7, "rattata": 7, "raticate": 8, "spearow": 7, "fearow": 6, "ekans": 5,
               "arbok": 5, "pikachu": 7, "raichu": 6, "sandshrew": 9, "sandslash": 9, "nidoran-f": 9, "nidorina": 8, "nidoqueen": 9, "nidoran-m": 9, "nidorino": 8, "nidoking": 8,
               "clefairy": 8, "clefable": 8, "vulpix": 6, "ninetales": 9, "jigglypuff": 10, "wigglytuff": 10, "zubat": 5, "golbat": 6, "oddish": 6, "gloom": 5, "vileplume": 9, "paras": 5,
               "parasect": 8, "venonat": 7, "venomoth": 8, "diglett": 7, "dugtrio": 7, "meowth": 6, "persian": 7, "psyduck": 7, "golduck": 7, "mankey": 6, "primeape": 8, "growlithe": 9,
               "arcanine": 8, "poliwag": 7, "poliwhirl": 9, "poliwrath": 9, "abra": 4, "kadabra": 7, "alakazam": 8, "machop": 6, "machoke": 7, "machamp": 7, "bellsprout": 10,
               "weepinbell": 10, "victreebel": 10, "tentacool": 9, "tentacruel": 10, "geodude": 7, "graveler": 8, "golem": 5, "ponyta": 6, "rapidash": 8, "slowpoke": 8, "slowbro": 7,
               "magnemite": 9, "magneton": 8, "farfetchd": 9, "doduo": 5, "dodrio": 6, "seel": 4, "dewgong": 7, "grimer": 6, "muk": 3, "shellder": 8, "cloyster": 8, "gastly": 6,
               "haunter": 7, "gengar": 6, "onix": 4, "drowzee": 7, "hypno": 5, "krabby": 6, "kingler": 7, "voltorb": 7, "electrode": 9, "exeggcute": 9, "exeggutor": 9, "cubone": 6,
               "marowak": 7, "hitmonlee": 9, "hitmonchan": 10, "lickitung": 9, "koffing": 7, "weezing": 7, "rhyhorn": 7, "rhydon": 6, "chansey": 7, "tangela": 7, "kangaskhan": 10,
               "horsea": 6, "seadra": 6, "goldeen": 7, "seaking": 7, "staryu": 6, "starmie": 7, "mr-mime": 7, "scyther": 7, "jynx": 4, "electabuzz": 10, "magmar": 6, "pinsir": 6,
               "tauros": 6, "magikarp": 8, "gyarados": 8, "lapras": 6, "ditto": 5, "eevee": 5, "vaporeon": 8, "jolteon": 7, "flareon": 7, "porygon": 7, "omanyte": 7, "omastar": 7,
               "kabuto": 6, "kabutops": 8, "aerodactyl": 10, "snorlax": 7, "articuno": 8, "zapdos": 6, "moltres": 7, "dratini": 7, "dragonair": 9, "dragonite": 9, "mewtwo": 6, "mew": 3}
segunda_gen = {"chikorita": 9, "bayleef": 7, "meganium": 8, "cyndaquil": 9, "quilava": 7, "typhlosion": 10, "totodile": 8, "croconaw": 8, "feraligatr": 10, "sentret": 7, "furret": 6,
               "hoothoot": 8, "noctowl": 7, "ledyba": 6, "ledian": 6, "spinarak": 8, "ariados": 7, "crobat": 6, "chinchou": 8, "lanturn": 7, "pichu": 5, "cleffa": 6, "igglybuff": 9,
               "togepi": 6, "togetic": 7, "natu": 4, "xatu": 4, "mareep": 6, "flaaffy": 7, "ampharos": 8, "bellossom": 9, "marill": 6, "azumarill": 9, "sudowoodo": 9, "politoed": 8,
               "hoppip": 6, "skiploom": 8, "jumpluff": 8, "aipom": 5, "sunkern": 7, "sunflora": 8, "yanma": 5, "wooper": 6, "quagsire": 8, "espeon": 6, "umbreon": 7, "murkrow": 7,
               "slowking": 8, "misdreavus": 10, "unown": 5, "wobbuffet": 9, "girafarig": 9, "pineco": 6, "forretress": 10, "dunsparce": 9, "gligar": 6, "steelix": 7, "snubbull": 8,
               "granbull": 8, "qwilfish": 8, "scizor": 6, "shuckle": 7, "heracross": 9, "sneasel": 7, "teddiursa": 9, "ursaring": 8, "slugma": 6, "magcargo": 8, "swinub": 6,
               "piloswine": 9, "corsola": 7, "remoraid": 8, "octillery": 9, "delibird": 8, "mantine": 7, "skarmory": 8, "houndour": 8, "houndoom": 8, "kingdra": 7, "phanpy": 6,
               "donphan": 7, "porygon2": 8, "stantler": 8, "smeargle": 8, "tyrogue": 7, "hitmontop": 9, "smoochum": 8, "elekid": 6, "magby": 5, "miltank": 7, "blissey": 7,
               "raikou": 6, "entei": 5, "suicune": 7, "larvitar": 8, "pupitar": 7, "tyranitar": 9, "lugia": 5, "ho-oh": 5, "celebi": 6}
tercera_gen = {"treecko": 7, "grovyle": 7, "sceptile": 8, "torchic": 7, "combusken": 9, "blaziken": 8, "mudkip": 6, "marshtomp": 9, "swampert": 8, "poochyena": 9, "mightyena": 9,
               "zigzagoon": 9, "linoone": 7, "wurmple": 7, "silcoon": 7, "beautifly": 9, "cascoon": 7, "dustox": 6, "lotad": 5, "lombre": 6, "ludicolo": 8, "seedot": 6, "nuzleaf": 7,
               "shiftry": 7, "taillow": 7, "swellow": 7, "wingull": 7, "pelipper": 8, "ralts": 5, "kirlia": 6, "gardevoir": 9, "surskit": 7, "masquerain": 10, "shroomish": 9, "breloom": 7,
               "slakoth": 7, "vigoroth": 8, "slaking": 7, "nincada": 7, "ninjask": 7, "shedinja": 8, "whismur": 7, "loudred": 7, "exploud": 7, "makuhita": 8, "hariyama": 8, "azurill": 7,
               "nosepass": 8, "skitty": 6, "delcatty": 8, "sableye": 7, "mawile": 6, "aron": 4, "lairon": 6, "aggron": 6, "meditite": 8, "medicham": 8, "electrike": 9, "manectric": 9,
               "plusle": 6, "minun": 5, "volbeat": 7, "illumise": 8, "roselia": 7, "gulpin": 6, "swalot": 6, "carvanha": 8, "sharpedo": 8, "wailmer": 7, "wailord": 7, "numel": 5,
               "camerupt": 8, "torkoal": 7, "spoink": 6, "grumpig": 7, "spinda": 6, "trapinch": 8, "vibrava": 7, "flygon": 6, "cacnea": 6, "cacturne": 8, "swablu": 6, "altaria": 7,
               "zangoose": 8, "seviper": 7, "lunatone": 8, "solrock": 7, "barboach": 8, "whiscash": 8, "corphish": 8, "crawdaunt": 9, "baltoy": 6, "claydol": 7, "lileep": 6, "cradily": 7,
               "anorith": 7, "armaldo": 7, "feebas": 6, "milotic": 7, "castform": 8, "kecleon": 7, "shuppet": 7, "banette": 7, "duskull": 7, "dusclops": 8, "tropius": 7, "chimecho": 8,
               "absol": 5, "wynaut": 6, "snorunt": 7, "glalie": 6, "spheal": 6, "sealeo": 6, "walrein": 7, "clamperl": 8, "huntail": 7, "gorebyss": 8, "relicanth": 9, "luvdisc": 7,
               "bagon": 5, "shelgon": 7, "salamence": 9, "beldum": 6, "metang": 6, "metagross": 9, "regirock": 8, "regice": 6, "registeel": 9, "latias": 6, "latios": 6, "kyogre": 6,
               "groudon": 7, "rayquaza": 8, "jirachi": 7, "deoxys": 6}
cuarta_gen = {"turtwig": 7, "grotle": 6, "torterra": 8, "chimchar": 8, "monferno": 8, "infernape": 9, "piplup": 6, "prinplup": 8, "empoleon": 8, "starly": 6, "staravia": 8, "staraptor": 9,
              "bidoof": 6, "bibarel": 7, "kricketot": 9, "kricketune": 10, "shinx": 5, "luxio": 5, "luxray": 6, "budew": 5, "roserade": 8, "cranidos": 8, "rampardos": 9, "shieldon": 8,
              "bastiodon": 9, "burmy": 5, "wormadam": 8, "mothim": 6, "combee": 6, "vespiquen": 9, "pachirisu": 9, "buizel": 6, "floatzel": 8, "cherubi": 7, "cherrim": 7, "shellos": 7,
              "gastrodon": 9, "ambipom": 7, "drifloon": 8, "drifblim": 8, "buneary": 7, "lopunny": 7, "mismagius": 9, "honchkrow": 9, "glameow": 7, "purugly": 7, "chingling": 9,
              "stunky": 6, "skuntank": 8, "bronzor": 7, "bronzong": 8, "bonsly": 6, "mime-jr": 7, "happiny": 7, "chatot": 6, "spiritomb": 9, "gible": 5, "gabite": 6, "garchomp": 8,
              "munchlax": 8, "riolu": 5, "lucario": 7, "hippopotas": 10, "hippowdon": 9, "skorupi": 7, "drapion": 7, "croagunk": 8, "toxicroak": 9, "carnivine": 9, "finneon": 7,
              "lumineon": 8, "mantyke": 7, "snover": 6, "abomasnow": 9, "weavile": 7, "magnezone": 9, "lickilicky": 10, "rhyperior": 9, "tangrowth": 9, "electivire": 10, "magmortar": 9,
              "togekiss": 8, "yanmega": 7, "leafeon": 7, "glaceon": 7, "gliscor": 7, "mamoswine": 9, "porygon-z": 9, "gallade": 7, "probopass": 9, "dusknoir": 8, "froslass": 8, "rotom": 5,
              "uxie": 4, "mesprit": 7, "azelf": 5, "dialga": 6, "palkia": 6, "heatran": 7, "regigigas": 9, "giratina": 8, "cresselia": 9, "phione": 6, "manaphy": 7, "darkrai": 7,
              "shaymin": 7, "arceus": 6}
quinta_gen = {"victini": 7, "snivy": 5, "servine": 7, "serperior": 9, "tepig": 5, "pignite": 7, "emboar": 6, "oshawott": 8, "dewott": 6, "samurott": 8, "patrat": 6, "watchog": 7,
              "lillipup": 8, "herdier": 7, "stoutland": 9, "purrloin": 8, "liepard": 7, "pansage": 7, "simisage": 8, "pansear": 7, "simisear": 8, "panpour": 7, "simipour": 8,
              "munna": 5, "musharna": 8, "pidove": 6, "tranquill": 9, "unfezant": 8, "blitzle": 7, "zebstrika": 9, "roggenrola": 10, "boldore": 7, "gigalith": 8, "woobat": 6,
              "swoobat": 7, "drilbur": 7, "excadrill": 9, "audino": 6, "timburr": 7, "gurdurr": 7, "conkeldurr": 10, "tympole": 7, "palpitoad": 9, "seismitoad": 10, "throh": 5,
              "sawk": 4, "sewaddle": 8, "swadloon": 8, "leavanny": 8, "venipede": 8, "whirlipede": 10, "scolipede": 9, "cottonee": 8, "whimsicott": 10, "petilil": 7, "lilligant": 9,
              "basculin": 8, "sandile": 7, "krokorok": 8, "krookodile": 10, "darumaka": 8, "darmanitan": 10, "maractus": 8, "dwebble": 7, "crustle": 7, "scraggy": 7, "scrafty": 7,
              "sigilyph": 8, "yamask": 6, "cofagrigus": 10, "tirtouga": 8, "carracosta": 10, "archen": 6, "archeops": 8, "trubbish": 8, "garbodor": 8, "zorua": 5, "zoroark": 7,
              "minccino": 8, "cinccino": 8, "gothita": 7, "gothorita": 9, "gothitelle": 10, "solosis": 7, "duosion": 7, "reuniclus": 9, "ducklett": 8, "swanna": 6, "vanillite": 9,
              "vanillish": 9, "vanilluxe": 9, "deerling": 8, "sawsbuck": 8, "emolga": 6, "karrablast": 10, "escavalier": 10, "foongus": 7, "amoonguss": 9, "frillish": 8, "jellicent": 9,
              "alomomola": 9, "joltik": 6, "galvantula": 10, "ferroseed": 9, "ferrothorn": 10, "klink": 5, "klang": 5, "klinklang": 9, "tynamo": 6, "eelektrik": 9, "eelektross": 10,
              "elgyem": 6, "beheeyem": 8, "litwick": 7, "lampent": 7, "chandelure": 10, "axew": 4, "fraxure": 7, "haxorus": 7, "cubchoo": 7, "beartic": 7, "cryogonal": 9, "shelmet": 7,
              "accelgor": 8, "stunfisk": 8, "mienfoo": 7, "mienshao": 8, "druddigon": 9, "golett": 6, "golurk": 6, "pawniard": 8, "bisharp": 7, "bouffalant": 10, "rufflet": 7,
              "braviary": 8, "vullaby": 7, "mandibuzz": 9, "heatmor": 7, "durant": 6, "deino": 5, "zweilous": 8, "hydreigon": 9, "larvesta": 8, "volcarona": 9, "cobalion": 8,
              "terrakion": 9, "virizion": 8, "tornadus": 8, "thundurus": 9, "reshiram": 8, "zekrom": 6, "landorus": 8, "kyurem": 6, "keldeo": 6, "meloetta": 8, "genesect": 8}
sexta_gen = {"chespin": 7, "quilladin": 9, "chesnaught": 10, "fennekin": 8, "braixen": 7, "delphox": 7, "froakie": 7, "frogadier": 9, "greninja": 8, "bunnelby": 8, "diggersby": 9,
             "fletchling": 10, "fletchinder": 11, "talonflame": 10, "scatterbug": 10, "spewpa": 6, "vivillon": 8, "litleo": 6, "pyroar": 6, "flabebe": 7, "floette": 7, "florges": 7,
             "skiddo": 6, "gogoat": 6, "pancham": 7, "pangoro": 7, "furfrou": 7, "espurr": 6, "meowstic": 8, "honedge": 7, "doublade": 8, "aegislash": 9, "spritzee": 8, "aromatisse": 10,
             "swirlix": 7, "slurpuff": 8, "inkay": 5, "malamar": 7, "binacle": 7, "barbaracle": 10, "skrelp": 6, "dragalge": 8, "clauncher": 9, "clawitzer": 9, "helioptile": 10,
             "heliolisk": 9, "tyrunt": 6, "tyrantrum": 9, "amaura": 6, "aurorus": 7, "sylveon": 7, "hawlucha": 8, "dedenne": 7, "carbink": 7, "goomy": 5, "sliggoo": 7, "goodra": 6,
             "klefki": 6, "phantump": 8, "trevenant": 9, "pumpkaboo": 9, "gourgeist": 9, "bergmite": 8, "avalugg": 7, "noibat": 6, "noivern": 7, "xerneas": 7, "yveltal": 7,
             "zygarde": 7, "diancie": 7, "hoopa": 5, "volcanion": 9}
septima_gen = {"rowlet": 6, "dartrix": 7, "decidueye": 9, "litten": 6, "torracat": 8, "incineroar": 10, "popplio": 7, "brionne": 7, "primarina": 9, "pikipek": 7, "trumbeak": 8,
             "toucannon": 9, "yungoos": 7, "gumshoos": 8, "grubbin": 7, "charjabug": 9, "vikavolt": 8, "crabrawler": 10, "crabominable": 12, "oricorio": 8, "cutiefly": 8, "ribombee": 8,
             "rockruff": 8, "lycanroc": 8, "wishiwashi": 10, "mareanie": 8, "toxapex": 7, "mudbray": 7, "mudsdale": 8, "dewpider": 8, "araquanid": 9, "fomantis": 8, "lurantis": 8,
             "morelull": 8, "shiinotic": 9, "salandit": 8, "salazzle": 8, "stufful": 7, "bewear": 6, "bounsweet": 9, "steenee": 7, "tsareena": 8, "comfey": 6, "oranguru": 8, "passimian": 9,
             "wimpod": 6, "golisopod": 9, "sandygast": 9, "palossand": 9, "pyukumuku": 9, "type-null": 9, "silvally": 8, "minior": 6, "komala": 6, "turtonator": 10, "togedemaru": 10,
             "mimikyu": 7, "bruxish": 7, "drampa": 6, "dhelmise": 8, "jangmo-o": 8, "hakamo-o": 8, "kommo-o": 7, "tapu-koko": 9, "tapu-lele": 9, "tapu-bulu": 9, "tapu-fini": 9,
             "cosmog": 6, "cosmoem": 7, "solgaleo": 8, "lunala": 6, "nihilego": 8, "buzzwole": 8, "pheromosa": 9, "xurkitree": 9, "celesteela": 10, "kartana": 7, "guzzlord": 8,
             "necrozma": 8, "magearna": 8, "marshadow": 9, "poipole": 7, "naganadel": 9, "stakataka": 9, "blacephalon": 11, "zeraora": 7, "meltan": 6, "melmetal": 8}
octava_gen = {"grookey": 7, "thwackey": 8, "rillaboom": 9, "scorbunny": 9, "raboot": 6, "cinderace": 9, "sobble": 6, "drizzile": 8, "inteleon": 8, "skwovet": 7, "greedent": 8,
              "rookidee": 8, "corvisquire": 11, "corviknight": 11, "blipbug": 7, "dottler": 7, "orbeetle": 8, "nickit": 6, "thievul": 7, "gossifleur": 10, "eldegoss": 8,
              "wooloo": 6, "dubwool": 7, "chewtle": 7, "drednaw": 7, "yamper": 6, "boltund": 7, "rolycoly": 8, "carkol": 6, "coalossal": 9, "applin": 6, "flapple": 7, "appletun": 8,
              "silicobra": 9, "sandaconda": 10, "cramorant": 9, "arrokuda": 8, "barraskewda": 11, "toxel": 5, "toxtricity": 10, "sizzlipede": 10, "centiskorch": 11, "clobbopus": 9,
              "grapploct": 9, "sinistea": 8, "polteageist": 11, "hatenna": 7, "hattrem": 7, "hatterene": 9, "impidimp": 8, "morgrem": 7, "grimmsnarl": 10, "obstagoon": 9, "perrserker": 10,
              "cursola": 7, "sirfetchd": 9, "mr-rime": 7, "runerigus": 9, "milcery": 7, "alcremie": 8, "falinks": 7, "pincurchin": 10, "snom": 4, "frosmoth": 8, "stonjourner": 11,
              "eiscue": 6, "indeedee": 8, "morpeko": 7, "cufant": 6, "copperajah": 10, "dracozolt": 9, "arctozolt": 9, "dracovish": 9, "arctovish": 9, "duraludon": 9, "dreepy": 6,
              "drakloak": 8, "dragapult": 9, "zacian": 6, "zamazenta": 9, "eternatus": 9, "kubfu": 5, "urshifu": 7, "zarude": 6, "regieleki": 9, "regidrago": 9, "glastrier": 9,
              "spectrier": 9, "calyrex": 7, "wyrdeer": 7, "kleavor": 7, "ursaluna": 8, "basculegion": 11, "sneasler": 8, "overqwil": 8, "enamorus": 8}
novena_gen = {"sprigatito": 10, "floragato": 9, "meowscarada": 11, "fuecoco": 7, "crocalor": 8, "skeledirge": 10, "quaxly": 6, "quaxwell": 8, "quaquaval": 9, "lechonk": 7,
              "oinkologne": 10, "tarountula": 10, "spidops": 7, "nymble": 6, "lokix": 5, "pawmi": 5, "pawmo": 5, "pawmot": 6, "tandemaus": 9, "maushold": 8, "fidough": 7,
              "dachsbun": 8, "smoliv": 6, "dolliv": 6, "arboliva": 8, "squawkabilly": 12, "nacli": 5, "naclstack": 9, "garganacl": 9, "charcadet": 9, "armarouge": 9, "ceruledge": 9,
              "tadbulb": 7, "bellibolt": 9, "wattrel": 7, "kilowattrel": 11, "maschiff": 8, "mabosstiff": 10, "shroodle": 8, "grafaiai": 8, "bramblin": 8, "brambleghast": 12,
              "toedscool": 9, "toedscruel": 10, "klawf": 5, "capsakid": 8, "scovillain": 10, "rellor": 6, "rabsca": 6, "flittle": 7, "espathra": 8, "tinkatink": 9, "tinkatuff": 9,
              "tinkaton": 8, "wiglett": 7, "wugtrio": 7, "bombirdier": 10, "finizen": 7, "palafin-zero": 12, "varoom": 6, "revavroom": 9, "cyclizar": 8, "orthworm": 8, "glimmet": 7,
              "glimmora": 8, "greavard": 8, "houndstone": 10, "flamigo": 7, "cetoddle": 8, "cetitan": 7, "veluza": 6, "dondozo": 7, "tatsugiri": 9, "annihilape": 10, "clodsire": 8,
              "farigiraf": 9, "dudunsparce": 11, "kingambit": 9, "great-tusk": 10, "scream-tail": 11, "brute-bonnet": 12, "flutter-mane": 12, "slither-wing": 12, "sandy-shocks": 12,
              "iron-treads": 11, "iron-bundle": 11, "iron-hands": 10, "iron-jugulis": 12, "iron-moth": 9, "iron-thorns": 11, "frigibax": 8, "arctibax": 8, "baxcalibur": 10,
              "gimmighoul": 10, "gholdengo": 9, "wo-chien": 8, "chien-pao": 9, "ting-lu": 7, "chi-yu": 6, "roaring-moon": 12, "iron-valiant": 12, "koraidon": 8, "miraidon": 8,
              "walking-wake": 12, "iron-leaves": 11, "dipplin": 7, "poltchageist": 12, "sinistcha": 9, "okidogi": 7, "munkidori": 9, "fezandipiti": 11, "ogerpon": 7, "archaludon": 10,
              "hydrapple": 9, "gouging-fire": 12, "raging-bolt": 11, "iron-boulder": 12, "iron-crown": 10, "terapagos": 9, "pecharunt": 9}

pokewordle = {}
pokewordle.update(primera_gen)
pokewordle.update(segunda_gen)
pokewordle.update(tercera_gen)
pokewordle.update(cuarta_gen)
pokewordle.update(quinta_gen)
pokewordle.update(sexta_gen)
pokewordle.update(septima_gen)
pokewordle.update(octava_gen)
pokewordle.update(novena_gen)

MAX_ATTEMPTS = 6
facil = range(3, 6)
media = range(6, 9)
dificil = range(9, 13)

def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
    ventana.lift()
    ventana.focus_force()
    ventana.grab_set()

def iniciar_juego(nombre_pokemon, longitud):
    app = ctk.CTk()
    app.title("Pokewordle")
    app.iconbitmap(os.path.join(BASE_PATH, "Textures", "icono.ico"))
    centrar_ventana(app, 700, 600)

    secret_word = nombre_pokemon.lower()
    attempt = 0
    entries_grid = []

    def on_key(event, row_index, col_index):
        widget = event.widget
        value = widget.get()

        if event.keysym == "BackSpace":
            if not value and col_index > 0:
                entries_grid[row_index][col_index - 1].focus()
            return

        if len(value) > 1:
            widget.delete(1, ctk.END)
        elif len(value) == 1 and col_index + 1 < longitud:
            entries_grid[row_index][col_index + 1].focus()

    def check_attempt():
        nonlocal attempt

        def mostrar_ventana_final(ganaste):
            popup = ctk.CTkToplevel(app)
            popup.title("Fin del Juego")
            popup.iconbitmap(os.path.join(BASE_PATH, "Textures", "icono.ico"))
            centrar_ventana(popup, 320, 320)
            popup.resizable(False, False)

            ruta_img = os.path.join(BASE_PATH, "Textures")
            try:
                if ganaste:
                    img_resultado = ctk.CTkImage(Image.open(os.path.join(ruta_img, "ganaste.png")), size=(220, 220))
                    ctk.CTkLabel(popup, image=img_resultado, text="").pack(pady=10)
                else:
                    img_resultado = ctk.CTkImage(Image.open(os.path.join(ruta_img, "perdiste.png")), size=(220, 220))
                    ctk.CTkLabel(popup, image=img_resultado, text="").pack(pady=10)
            except:
                ctk.CTkLabel(popup, text="¡Ganaste!" if ganaste else "Perdiste", font=ctk.CTkFont(size=18)).pack(pady=10)

            try:
                icono_reiniciar = ctk.CTkImage(Image.open(os.path.join(ruta_img, "volver_jugar.png")), size=(40, 40))
                icono_menu = ctk.CTkImage(Image.open(os.path.join(ruta_img, "volver_inicio.png")), size=(40, 40))
            except:
                icono_reiniciar = None
                icono_menu = None

            def volver_a_jugar():
                popup.destroy()
                app.destroy()
                seleccionar_regiones()

            def ir_menu():
                popup.destroy()
                app.destroy()
                mostrar_menu()

            botones = ctk.CTkFrame(popup, fg_color="transparent")
            botones.pack(pady=20)

            ctk.CTkButton(botones, image=icono_reiniciar, width=60, height=60, corner_radius=30, text="", fg_color="#1e90ff", hover_color="#4682b4", command=volver_a_jugar).pack(side="left", padx=20)
            ctk.CTkButton(botones, image=icono_menu, width=60, height=60, corner_radius=30, text="", fg_color="#ff6347", hover_color="#cd5c5c", command=ir_menu).pack(side="left", padx=20)

        guess = ""
        row_entries = entries_grid[attempt]

        for entry in row_entries:
            entry.configure(state="disabled")
            letter = entry.get().lower()
            if not letter or len(letter) != 1:
                status_label.configure(text="Completa todas las letras.")
                for e in row_entries:
                    e.configure(state="normal")
                return
            guess += letter

        secret_counter = Counter(secret_word)
        resultado_colores = [""] * longitud

        for i in range(longitud):
            if guess[i] == secret_word[i]:
                resultado_colores[i] = "green"
                secret_counter[guess[i]] -= 1

        for i in range(longitud):
            if resultado_colores[i] == "":
                letra = guess[i]
                if letra in secret_counter and secret_counter[letra] > 0:
                    resultado_colores[i] = "gold"
                    secret_counter[letra] -= 1
                else:
                    resultado_colores[i] = "gray"

        def colorear_letras(i=0):
            nonlocal attempt
            if i < longitud:
                row_entries[i].configure(fg_color=resultado_colores[i], text_color="white")
                app.after(200, lambda: colorear_letras(i + 1))
            else:
                if guess == secret_word:
                    status_label.configure(text="¡Correcto! Has adivinado el Pokémon.")
                    mostrar_ventana_final(True)
                else:
                    attempt += 1
                    if attempt >= MAX_ATTEMPTS:
                        status_label.configure(text=f"Era: {secret_word.upper()}. Jalaste Matemática Discreta.")
                        mostrar_ventana_final(False)
                    else:
                        for cell in entries_grid[attempt]:
                            cell.configure(state="normal")
                        entries_grid[attempt][0].focus()

        colorear_letras()

    ctk.CTkLabel(app, text="Adivina el Pokémon", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=15)
    grid_frame = ctk.CTkFrame(app)
    grid_frame.pack(pady=10)

    for i in range(MAX_ATTEMPTS):
        row = []
        for j in range(longitud):
            entry = ctk.CTkEntry(grid_frame, width=50, height=50, justify="center", font=ctk.CTkFont(size=20, weight="bold"))
            entry.grid(row=i, column=j, padx=5, pady=5)
            entry.configure(state="disabled")
            entry.bind("<KeyRelease>", lambda event, r=i, c=j: on_key(event, r, c))
            row.append(entry)
        entries_grid.append(row)

    for cell in entries_grid[0]:
        cell.configure(state="normal")
    entries_grid[0][0].focus()

    status_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
    status_label.pack(pady=10)
    ctk.CTkButton(app, text="Probar", command=check_attempt).pack(pady=10)
    ctk.CTkButton(app, text="Volver", fg_color="red", command=lambda: (app.destroy(), seleccionar_regiones())).pack(pady=10)

    app.mainloop()

def obtener_pokemon_por_generacion(generacion, rango_longitud):
    gens = [primera_gen, segunda_gen, tercera_gen, cuarta_gen,
            quinta_gen, sexta_gen, septima_gen, octava_gen, novena_gen]
    dic = gens[generacion - 1] if 1 <= generacion <= 9 else pokewordle
    filtrados = {nombre: long for nombre, long in dic.items() if long in rango_longitud}
    if not filtrados:
        raise ValueError("No hay Pokémon con esa longitud en esta generación.")
    nombre = random.choice(list(filtrados.keys()))
    return nombre, filtrados[nombre]

def elegir_dificultad(generacion):
    ventana = ctk.CTk()
    ventana.title("Dificultad")
    ventana.iconbitmap(os.path.join(BASE_PATH, "Textures", "icono.ico"))
    centrar_ventana(ventana, 300, 300)

    ctk.CTkLabel(ventana, text="Elije Dificultad", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=20)

    def lanzar_juego(rango):
        try:
            nombre, longitud = obtener_pokemon_por_generacion(generacion, rango)
            ventana.destroy()
            iniciar_juego(nombre, longitud)
        except ValueError:
            ctk.CTkMessagebox(title="Error", message="No hay Pokémon con esa dificultad en esta región.")

    ctk.CTkButton(ventana, text="Fácil", command=lambda: lanzar_juego(facil)).pack(pady=10)
    ctk.CTkButton(ventana, text="Media", command=lambda: lanzar_juego(media)).pack(pady=10)
    ctk.CTkButton(ventana, text="Difícil", command=lambda: lanzar_juego(dificil)).pack(pady=10)
    ctk.CTkButton(ventana, text="Volver", fg_color="red", command=lambda: (ventana.destroy(), seleccionar_regiones())).pack(pady=10)

    ventana.mainloop()

def seleccionar_regiones():
    ventana = ctk.CTk()
    ventana.title("Regiones")
    ventana.iconbitmap(os.path.join(BASE_PATH, "Textures", "icono.ico"))
    centrar_ventana(ventana, 300, 420)

    ctk.CTkLabel(ventana, text="Elije Regiones para Jugar", font=ctk.CTkFont(size=18)).pack(pady=20)
    seleccion = []

    def confirmar():
        for idx, var in enumerate(seleccion):
            if var.get():
                generacion_elegida = idx + 1 # Generación 1 a 9
                ventana.destroy()
                elegir_dificultad(generacion_elegida)
                return
        ctk.CTkMessagebox(title="Error", message="Debes seleccionar al menos una región")

    frame = ctk.CTkFrame(ventana)
    frame.pack()

    for i in range(1, 10):
        var = ctk.BooleanVar()
        cb = ctk.CTkCheckBox(frame, text=f"Región {i}", variable=var)
        cb.pack(anchor="w")
        seleccion.append(var)

    ctk.CTkButton(ventana, text="OK", command=confirmar).pack(pady=20)
    ctk.CTkButton(ventana, text="Volver", fg_color="red", command=lambda: (ventana.destroy(), mostrar_menu())).pack(pady=10)

    ventana.mainloop()

"""
def seleccionar_modo():
    ventana = ctk.CTk()
    ventana.title("Nuevo o Cargar")
    ventana.iconbitmap(os.path.join(BASE_PATH, "Textures", "icono.ico"))
    centrar_ventana(ventana, 300, 250)

    ctk.CTkLabel(ventana, text="Modo de Juego", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)
    ctk.CTkButton(ventana, text="Nuevo", command=lambda: (ventana.destroy(), seleccionar_regiones())).pack(pady=10)
    ctk.CTkButton(ventana, text="Cargar", command=lambda: ctk.CTkMessagebox(title="Cargar", message="Función aún no implementada")).pack(pady=10)
    ctk.CTkButton(ventana, text="Volver", fg_color="red", command=lambda: (ventana.destroy(), mostrar_menu())).pack(pady=10)

    ventana.mainloop()
"""

def iniciar_busqueda():
    ventana = ctk.CTk()
    ventana.title("Buscar por patrón")
    ventana.iconbitmap(os.path.join(BASE_PATH, "Textures", "icono.ico"))
    centrar_ventana(ventana, 300, 380)

    ctk.CTkLabel(ventana, text="Selecciona la cantidad de letras", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=15)

    grid_frame = ctk.CTkFrame(ventana)
    grid_frame.pack(pady=10)

    def seleccionar_longitud(n):
        ventana.destroy()
        ingresar_patron(n)

    fila = 0
    columna = 0
    for i in range(3, 13): #3 - 12
        if i == 12:
            fila += 1
            columna = 1
        btn = ctk.CTkButton(grid_frame, text=str(i), width=60, height=40, command=lambda n=i: seleccionar_longitud(n))
        btn.grid(row=fila, column=columna, padx=10, pady=10)

        if i != 12:
            columna += 1
            if columna > 2:
                columna = 0
                fila += 1

    ctk.CTkButton(ventana, text="Volver", fg_color="red", command=lambda: (ventana.destroy(), mostrar_menu())).pack(pady=10)

    ventana.mainloop()

def ingresar_patron(longitud):
    ventana = ctk.CTk()
    ventana.title("Ingresa el patrón")
    ventana.iconbitmap(os.path.join(BASE_PATH, "Textures", "icono.ico"))
    ancho = max(300, 80 * longitud)
    centrar_ventana(ventana, ancho, 220)

    ctk.CTkLabel(ventana, text="Deja vacío o usa '-' para letras desconocidas", font=ctk.CTkFont(size=14)).pack(pady=10)

    patron_frame = ctk.CTkFrame(ventana)
    patron_frame.pack()

    entradas = []
    for i in range(longitud):
        e = ctk.CTkEntry(patron_frame, width=50, justify="center", font=ctk.CTkFont(size=16, weight="bold"))
        e.grid(row=0, column=i, padx=5, pady=10)

        def on_key(event, idx=i):
            widget = event.widget
            value = widget.get()
            if len(value) > 1:
                widget.delete(1, ctk.END)
            elif len(value) == 1:
                if idx + 1 < longitud:
                    entradas[idx + 1].focus()

        e.bind("<KeyRelease>", on_key)
        entradas.append(e)

    def buscar():
        patron = ""
        for e in entradas:
            letra = e.get().lower()
            patron += '-' if letra == '' else letra

        ventana.destroy()
        mostrar_resultados(patron)

    ctk.CTkButton(ventana, text="Buscar", command=buscar).pack(pady=15)

    ctk.CTkButton(ventana, text="Volver", fg_color="red", command=lambda: (ventana.destroy(), iniciar_busqueda())).pack(pady=10)

    ventana.mainloop()

def mostrar_resultados(patron):
    ventana = ctk.CTk()
    ventana.title("Resultados")
    ventana.iconbitmap(os.path.join(BASE_PATH, "Textures", "icono.ico"))
    centrar_ventana(ventana, 460, 440)

    cargando = ctk.CTkLabel(ventana, text="Cargando resultados...", font=ctk.CTkFont(size=14))
    cargando.pack(pady=20)
    ventana.update()

    regex = '^' + ''.join(
        '.' if c == '-' else re.escape(c)
        for c in patron
    ) + '$'

    coincidencias = [
        nombre for nombre in pokewordle
        if len(nombre) == len(patron) and re.match(regex, nombre)
    ]

    cargando.destroy()

    if coincidencias:
        scroll_frame = ctk.CTkScrollableFrame(ventana, width=420, height=280)
        scroll_frame.pack(pady=20)

        columnas = 3
        for idx, nombre in enumerate(coincidencias):
            fila = idx // columnas
            columna = idx % columnas
            texto = f"{idx + 1}. {nombre}"
            label = ctk.CTkLabel(scroll_frame, text=texto, anchor="w", font=ctk.CTkFont(size=14))
            label.grid(row=fila, column=columna, padx=20, pady=5, sticky="w")
    else:
        ctk.CTkLabel(ventana, text="No se encontraron coincidencias.", font=ctk.CTkFont(size=14)).pack(pady=30)

    ctk.CTkButton(ventana, text="Volver al menú", command=lambda: (ventana.destroy(), mostrar_menu())).pack(pady=10)

    ctk.CTkButton(ventana, text="Volver", fg_color="red", command=lambda: (ventana.destroy(), ingresar_patron(len(patron)))).pack(pady=10)

    ventana.mainloop()

def iniciar_juego_con_chatbot(nombre_pokemon, longitud):
    root = ctk.CTk()
    root.title("Pokewordle - Modo Tutorial")
    root.iconbitmap(os.path.join(BASE_PATH, "Textures", "icono.ico"))
    centrar_ventana(root, 1200, 650)

    main_frame = ctk.CTkFrame(root)
    main_frame.pack(fill="both", expand=True)

    # Lado izquierdo: Juego
    juego_frame = ctk.CTkFrame(main_frame)
    juego_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    secret_word = nombre_pokemon.lower()
    attempt = 0
    entries_grid = []

    def on_key(event, row_index, col_index):
        widget = event.widget
        value = widget.get()

        if event.keysym == "BackSpace":
            if not value and col_index > 0:
                entries_grid[row_index][col_index - 1].focus()
            return

        if len(value) > 1:
            widget.delete(1, ctk.END)
        elif len(value) == 1 and col_index + 1 < longitud:
            entries_grid[row_index][col_index + 1].focus()

    def check_attempt():
        nonlocal attempt

        guess = ""
        row_entries = entries_grid[attempt]

        for entry in row_entries:
            entry.configure(state="disabled")
            letter = entry.get().lower()
            if not letter or len(letter) != 1:
                status_label.configure(text="Completa todas las letras.")
                for e in row_entries:
                    e.configure(state="normal")
                return
            guess += letter

        secret_counter = Counter(secret_word)

        # Marcar verdes
        resultado_colores = [""] * longitud
        for i in range(longitud):
            if guess[i] == secret_word[i]:
                resultado_colores[i] = "green"
                secret_counter[guess[i]] -= 1

        # Marcar amarillos
        for i in range(longitud):
            if resultado_colores[i] == "":
                letra = guess[i]
                if letra in secret_counter and secret_counter[letra] > 0:
                    resultado_colores[i] = "gold"
                    secret_counter[letra] -= 1
                else:
                    resultado_colores[i] = "gray"

        def colorear_letras(i=0):
            nonlocal attempt
            if i < longitud:
                row_entries[i].configure(fg_color=resultado_colores[i], text_color="white")
                root.after(200, lambda: colorear_letras(i + 1))
            else:
                if guess == secret_word:
                    status_label.configure(text="¡Correcto! Has adivinado el Pokémon.")
                else:
                    attempt += 1
                    if attempt >= MAX_ATTEMPTS:
                        status_label.configure(text=f"Perdiste. Era: {secret_word.upper()}")
                    else:
                        for cell in entries_grid[attempt]:
                            cell.configure(state="normal")
                        entries_grid[attempt][0].focus()

        colorear_letras()

    ctk.CTkLabel(juego_frame, text="Adivina el Pokémon", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=15)
    grid_frame = ctk.CTkFrame(juego_frame)
    grid_frame.pack(pady=10)

    for i in range(MAX_ATTEMPTS):
        row = []
        for j in range(longitud):
            entry = ctk.CTkEntry(grid_frame, width=50, height=50, justify="center", font=ctk.CTkFont(size=20, weight="bold"))
            entry.grid(row=i, column=j, padx=5, pady=5)
            entry.configure(state="disabled")
            entry.bind("<KeyRelease>", lambda event, r=i, c=j: on_key(event, r, c))
            row.append(entry)
        entries_grid.append(row)

    for cell in entries_grid[0]:
        cell.configure(state="normal")
    entries_grid[0][0].focus()

    status_label = ctk.CTkLabel(juego_frame, text="", font=ctk.CTkFont(size=14))
    status_label.pack(pady=10)
    ctk.CTkButton(juego_frame, text="Probar", command=check_attempt).pack(pady=10)
    ctk.CTkButton(juego_frame, text="Volver", fg_color="red", command=lambda: (root.destroy(), mostrar_menu())).pack(pady=10)

    chatbot_frame = ctk.CTkFrame(main_frame)
    chatbot_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    ctk.CTkLabel(chatbot_frame, text="Asistente de Juego", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=10)

    chat_log = ctk.CTkTextbox(chatbot_frame, wrap="word", height=300, state="disabled")
    chat_log.pack(padx=10, pady=10, fill="both", expand=True)

    entry_var = ctk.StringVar()
    entry_frame = ctk.CTkFrame(chatbot_frame)
    entry_frame.pack(pady=10, padx=10, fill="x")

    entry = ctk.CTkEntry(entry_frame, textvariable=entry_var)
    entry.pack(side="left", fill="x", expand=True, padx=5)

    def agregar_mensaje(remitente, mensaje):
        chat_log.configure(state="normal")
        chat_log.insert("end", f"{remitente}:\n{mensaje}\n\n")
        chat_log.configure(state="disabled")
        chat_log.see("end")

    def responder():
        pregunta = entry_var.get().lower().strip()
        entry_var.set("")
        agregar_mensaje("Tú", pregunta)

        if ("intentos" in pregunta or "oportunidades" in pregunta):
            respuesta = "Tienes 6 intentos para adivinar el Pokémon."
        elif ("todo" in pregunta and ("gris" in pregunta)) or ("todas" in pregunta and ("gris" in pregunta)):
            respuesta = "Significa que ninguna de las letras que escribiste está en el nombre del Pokémon."
        elif ("todo" in pregunta and ("amarillo" in pregunta)) or ("todas" in pregunta and ("amarillo" in pregunta)):
            respuesta = "Significa que todas las letras que escribiste están en el nombre del Pokémon, pero no en la posición correcta."
        elif ("todo" in pregunta and ("verde" in pregunta)) or ("todas" in pregunta and ("verde" in pregunta)):
            respuesta = "Significa que todas las letras que escribiste están en el nombre del Pokémon y en la posición correcta. GANASTE."
        elif "pikachu" in pregunta:
            respuesta = "Debes escribirlo en los cuadros de la derecha."
        elif "verde" in pregunta:
            respuesta = "El color verde indica que la letra está en la posición correcta."
        elif "amarillo" in pregunta or "dorado" in pregunta:
            respuesta = "El color amarillo significa que la letra está en el Pokémon, pero en otra posición."
        elif "gris" in pregunta:
            respuesta = "El color gris indica que la letra no está en el nombre del Pokémon o ya no se repite."
        elif ("como" in pregunta or "cómo" in pregunta) and ("jugar" in pregunta or "funciona" in pregunta or "juego" in pregunta or "juega" in pregunta):
            respuesta = ("Debes adivinar el nombre del Pokémon letra por letra. Cada intento te mostrará colores como pistas.")
        elif ("tengo" in pregunta or "debo" in pregunta) and ("hacer" in pregunta):
            respuesta = ("Debes adivinar el nombre del Pokémon letra por letra. Cada intento te mostrará colores como pistas.")
        elif "que" in pregunta and ("colores" in pregunta):
            respuesta = ("Los colores son verde amarillo y gris.\n"
                         " - Verde indica que la letra está en la posición correcta del nombre del Pokémon.\n"
                         " - Amarillo indica que la letra está en el nombre del Pokémon, pero no en su posición.\n"
                         " - Gris indica que la letra no está en el nombre del Pokémon.")
        elif "dame" in pregunta and ("pistas" in pregunta):
            respuesta = ("1.- Comienza con Pik----\n"
                         "2.- Termina con ----chu\n"
                         "3.- Es un Pokémon de tipo eléctrico y es muy famoso.")
        elif ("otra" in pregunta and ("pista" in pregunta)) or "2da pista" in pregunta or "segunda pista" in pregunta:
            respuesta = "Termina en ----chu."
        elif (("ultima" in pregunta or "última" in pregunta) and ("pista" in pregunta)) or ("pista" in pregunta and ("final" in pregunta)) or ("3ra pista" in pregunta or "tercera pista" in pregunta):
            respuesta = "Es Pikachu burro, si no sabes eso no deberías estar jugando esto."
        elif "pista" in pregunta or "1ra pista" in pregunta or "primera pista" in pregunta:
            respuesta = "Prueba a escribir Pikipek."
        elif "salir" in pregunta or "cerrar" in pregunta:
            root.destroy()
            return
        else:
            respuesta = "No entiendo bien tu pregunta."

        agregar_mensaje("Asistente", respuesta)

    ctk.CTkButton(entry_frame, text="Enviar", command=responder).pack(side="right", padx=5)
    entry.bind("<Return>", lambda e: responder())

    agregar_mensaje("Asistente", "¡Hola! Soy tu asistente del tutorial.\n"
                    "Deberás adivinar el nombre del pokemón probando con diferentes palabras (en este caso de 7 letras).\n"
                    "Puedes hacerme preguntas sobre el juego o también pedirme solo 3 pistas.")
    root.mainloop()

def mostrar_menu():
    menu = ctk.CTk()
    menu.title("Pokewordle - Menú Principal")
    menu.iconbitmap(os.path.join(BASE_PATH, "Textures", "icono.ico"))
    centrar_ventana(menu, 500, 350)

    ctk.CTkLabel(menu, text="POKEWORDLE", font=ctk.CTkFont(size=30, weight="bold")).pack(pady=30)
    ctk.CTkButton(menu, text="TUTORIAL", width=300, command=lambda: (menu.destroy(),
                    iniciar_juego_con_chatbot("Pikachu", 7))).pack(pady=10)
    ctk.CTkButton(menu, text="JUGAR", width=300, command=lambda: (menu.destroy(), seleccionar_regiones())).pack(pady=10)
    ctk.CTkButton(menu, text="BUSCAR", width=300, command=lambda: (menu.destroy(), iniciar_busqueda())).pack(pady=10)
    ctk.CTkButton(menu, text="SALIR", width=200, fg_color="red", command=menu.destroy).pack(pady=20)
    menu.mainloop()

mostrar_menu()
