word_list = [
    "kombuiskas",       # kitchen cabinet (thing)
    "vergrootglas",     # magnifying glass (thing)
    "herinnering",      # memory (abstract)
    "navorser",         # researcher (person)
    "belofte",          # promise (abstract)
    "bewys",            # proof (thing)
    "begrafnis",        # funeral (event)
    "werktuig",         # tool (thing)
    "elektrisiteit",    # electricity (thing)
    "polisiestasie",    # police station (place)
    "kanselier",        # chancellor (person)
    "verskoning",       # excuse (abstract)
    "weersin",          # resistance (abstract)
    "afskeid",          # farewell (event)
    "vriendskap",       # friendship (abstract)
    "reisiger",         # traveler (person)
    "voorspelling",     # prediction (abstract)
    "vernietiging",     # destruction (abstract)
    "verskeidenheid",   # variety (abstract)
    "verklikker",       # informer (thing)
    "beskikbaar",       # available (abstract)
    "vergelyking",      # comparison (abstract)
    "bevordering",      # promotion (abstract)
    "ontdekking",       # discovery (abstract)
    "kompilasie",       # compilation (thing)
    "persoonlik",       # personal (abstract)
    "vrees",            # fear (abstract)
    "magtiging",        # authorization (abstract)
    "ooreenkoms",       # agreement (abstract)
    "vermoë",           # ability (abstract)
    "kundigheid",       # expertise (abstract)
    "belangrik",        # important (abstract)
    "samestelling",     # composition (abstract)
    "akademies",        # academic (abstract)
    "beteekenis",       # meaning (abstract)
    "verbintenis",      # commitment (abstract)
    "vertroue",         # trust (abstract)
    "geleentheid",      # opportunity (abstract)
    "suksesvol",        # successful (abstract)
    "gesondheid",       # health (abstract)
    "medisyne",         # medicine (thing)
    "onderrig",         # education (abstract)
    "onderwys",         # education (abstract)
    "besigheid",        # business (thing)
    "werk",             # work (abstract)
    "beskerming",       # protection (abstract)
    "verwantskap",      # relationship (abstract)
    "liefde",           # love (abstract)
    "toekoms",          # future (abstract)
    "ondervinding",     # experience (abstract)
    "kennis",           # knowledge (abstract)
    "gesin",            # family (abstract)
    "eenvoudig",        # simple (abstract)
    "vennootskap",      # partnership (abstract)
    "saamwerking",      # cooperation (abstract)
    "uitdaging",        # challenge (abstract)
    "vaardigheid",      # skill (abstract)
    "vakansie",         # vacation (event)
    "einde",            # end (abstract)
    "aanpassing",       # adaptation (abstract)
    "ontspanning",      # relaxation (abstract)
    "ontwikkeling",     # development (abstract)
    "Suid-Afrika",      # South Africa (country)
    "Australie",        # Australia (country)
    "Nieu-Seeland",     # New Zealand (country)
    "Japan",            # Japan (country)
    "China",            # China (country)
    "Rusland",          # Russia (country)
    "Spanje",           # Spain (country)
    "Italie",           # Italy (country)
    "Brasilie",         # Brazil (country)
    "Argentinie",       # Argentina (country)
    "Kanada",           # Canada (country)
    "Amerika",          # America (country)
    "Frankryk",         # France (country)
    "Duitsland",        # Germany (country)
    "Meksiko",          # Mexico (country)
    "Indie",            # India (country)
    "Lughawe",          # airport (place)
    "Biblioteek",       # library (place)
    "Universiteit",     # university (place)
    "Hospitaal",        # hospital (place)
    "Museum",           # museum (place)
    "Restourant",       # restaurant (place)
    "Strand",           # beach (place)
    "Parkering",        # parking (place)
    "Hoofstad",         # capital (place)
    "Stadsaal",         # city hall (place)
    "Winkel",           # shop (place)
    "Koffiewinkel",     # coffee shop (place)
    "Supermark",        # supermarket (place)
    "Stad",             # city (place)
    "Dorp",             # town (place)
    "Landelik",         # rural (place)
    "Oseaan",           # ocean (place)
    "Rivier",           # river (place)
    "Berg",             # mountain (place)
    "Woud",             # forest (place)
    "Eiland",           # island (place)
    "Meer",             # lake (place)
    "Grot",             # cave (place)
    "Vulkan",           # volcano (place)
    "Piramide",         # pyramid (place)
    "Skool",            # school (place)
    "Kerk",             # church (place)
    "Teater",           # theater (place)
    "Gesig",            # face (thing)
    "Hande",            # hands (thing)
    "Voet",             # foot (thing)
    "Hart",             # heart (thing)
    "Skelet",           # skeleton (thing)
    "Spier",            # muscle (thing)
    "Hare",             # hair (thing)
    "Oog",              # eye (thing)
    "Oor",              # ear (thing)
    "Neus",             # nose (thing)
    "Mond",             # mouth (thing)
    "Tande",            # teeth (thing)
    "Taal",             # language (abstract)
    "Droom",            # dream (abstract)
    "Geloof",           # belief (abstract)
    "Etiek",            # ethics (abstract)
    "Moraliteit",       # morality (abstract)
    "Kultuur",          # culture (abstract)
    "Politiek",         # politics (abstract)
    "Regte",            # rights (abstract)
    "Wysheid",          # wisdom (abstract)
    "Verstand",         # intellect (abstract)
    "Verbeelding",      # imagination (abstract)
    "Bewussyn",         # consciousness (abstract)
    "Wete",             # knowledge (abstract)
    "Filosofie",        # philosophy (abstract)
    "Wetenskap",        # science (abstract)
    "Teologie",         # theology (abstract)
    "Musiek",           # music (abstract)
    "Kuns",             # art (abstract)
    "Literatuur",       # literature (abstract)
    "Film",             # film (abstract)
    "Fotografie",       # photography (abstract)
    "Argitektuur",      # architecture (abstract)
    "Dans",             # dance (abstract)
    "Drama",            # drama (abstract)
    "Prosa",            # prose (abstract)
    "Poesie",           # poetry (abstract)
    "Skildery",         # painting (abstract)
    "Beeldhouwerk",     # sculpture (abstract)
    "Mode",             # fashion (abstract)
    "Speletjie",        # game (thing)
    "Rekenaar",         # computer (thing)
    "Internet",         # internet (thing)
    "Selfoon",          # cellphone (thing)
    "Tablet",           # tablet (thing)
    "Drukker",          # printer (thing)
    "Skandeerder",      # scanner (thing)
    "Monitor",          # monitor (thing)
    "Sleutelbord",      # keyboard (thing)
    "Muise",            # mouse (thing)
    "Kamera",           # camera (thing)
    "Televisie",        # television (thing)
    "Radio",            # radio (thing)
    "Lugredery",        # airline (thing)
    "Vliegtuig",        # airplane (thing)
    "Motorkar",         # motor car (thing)
    "Trein",            # train (thing)
    "Skip",             # ship (thing)
    "Boot",             # boat (thing)
    "Bicycle",          # bicycle (thing)
    "Motorfiets",       # motorcycle (thing)
    "Helikopter",       # helicopter (thing)
    "Ruimtevaartuig",   # spacecraft (thing)
    "Satelliet",        # satellite (thing)
    "Teleskoop",        # telescope (thing)
    "Mikroskoop",       # microscope (thing)
    "Binokulêr",        # binoculars (thing)
    "Kompas",           # compass (thing)
    "Kaart",            # map (thing)
    "Gids",             # guide (thing)
    "Dagboek",          # diary (thing)
    "Koerant",          # newspaper (thing)
    "Tydskrif",         # magazine (thing)
    "Boek",             # book (thing)
    "Notaboek",         # notebook (thing)
    "Skrywer",          # writer (thing)
    "Digter",           # poet (thing)
    "Illustrator",      # illustrator (thing)
    "Redakteur",        # editor (thing)
    "Uitgewer",         # publisher (thing)
    "Bibliotekaris",    # librarian (thing)
    "Vertaler",         # translator (thing)
    "Onderwyser",       # teacher (thing)
    "Prokureur",        # lawyer (thing)
    "Dokter",           # doctor (thing)
    "Verpleegster",     # nurse (thing)
    "Apteker",          # pharmacist (thing)
    "Ingenieur",        # engineer (thing)
    "Wetenskaplike",    # scientist (thing)
    "Rekenmeester",     # accountant (thing)
    "Bestuurder",       # manager (thing)
    "Sekretaresse",     # secretary (thing)
    "Ontwerper",        # designer (thing)
    "Programmeerder",   # programmer (thing)
    "Argitek",          # architect (thing)
    "Bouer",            # builder (thing)
    "Elektrisiën",      # electrician (thing)
    "Timmerman",        # carpenter (thing)
    "Messelaar",        # bricklayer (thing)
    "Loodgieter",       # plumber (thing)
    "Skrynwerker",      # joiner (thing)
    "Skoonmaker",       # cleaner (thing)
    "Kok",              # cook (thing)
    "Kelner",           # waiter (thing)
    "Sjef",             # chef (thing)
    "Huisvrou",         # housewife (thing)
    "Motorwerktuigkundige", # auto mechanic (thing)
    "Haarkapper",       # hairdresser (thing)
    "Skeepskaptein",    # ship captain (thing)
    "Loods",            # pilot (thing)
    "Veearts",          # veterinarian (thing)
    "Polisieman",       # policeman (thing)
    "Brandweerman",     # firefighter (thing)
    "Soldaat",          # soldier (thing)
    "Lugmag",           # air force (thing)
    "Vloot",            # navy (thing)
    "Mariene",          # marine (thing)
    "Infanterie",       # infantry (thing)
    "Bevelvoerder",     # commander (thing)
    "Generaal",         # general (thing)
    "Admiraal",         # admiral (thing)
    "Majoor",           # major (thing)
    "Kaptein",          # captain (thing)
    "Luitenant",        # lieutenant (thing)
    "Sergeant",         # sergeant (thing)
    "Korps",            # corps (thing)
    "Eenheid",          # unit (thing)
    "Bataljon",         # battalion (thing)
    "Regiment",         # regiment (thing)
    "Brigade",          # brigade (thing)
    "Divisie",          # division (thing)
    "Vlieënier",        # aviator (thing)
    "Instrukteur",      # instructor (thing)
    "Advokaat",         # advocate (thing)
    "Raadslid",         # councillor (thing)
    "Senator",          # senator (thing)
    "Parlementslid",    # member of parliament (thing)
    "Minister",         # minister (thing)
    "President",        # president (thing)
    "Premier",          # prime minister (thing)
    "Burgemeester",     # mayor (thing)
    "Gouverneur",       # governor (thing)
    "Regter",           # judge (thing)
    "Magistraat",       # magistrate (thing)
    "Openbare aanklaer",# public prosecutor (thing)
    "Prokureur-generaal", # attorney general (thing)
    "Regsadviseur",     # legal advisor (thing)
    "Regskonsultant",   # legal consultant (thing)
    "Advokate",         # barrister (thing)
    "Regsklerk",        # legal clerk (thing)
    "Geregsdienaar",    # court official (thing)
    "Regsgeleerde",     # legal scholar (thing)
    "Regskenner",       # legal expert (thing)
    "Regsverteenwoordiger", # legal representative (thing)
    "Regsmedewerker",   # legal assistant (thing)
    "Regsagent",        # legal agent (thing)
    "Regskontrakteur",  # legal contractor (thing)
    "Regsvennoot",      # legal partner (thing)
    "Regsmakelaar",     # legal broker (thing)
    "Regsraadgewer",    # legal advisor (thing)
    "Regsdosent",       # legal lecturer (thing)
    "Regspraktisyn",    # legal practitioner (thing)
    "Regsnavorsingsbeampte", # legal research officer (thing)
    "Regserfgenaam",    # legal heir (thing)
    "Regsinstrukteur",  # legal instructor (thing)
    "Regsspesialis",    # legal specialist (thing)
    "Regsverteenwoordiger", # legal representative (thing)
    "Regsvennoot",      # legal partner (thing)
    "Regsverteenwoordiger", # legal representative (thing)
    "Regsvennoot",      # legal partner (thing)
    "Regsverteenwoordiger", # legal representative (thing)
    "Regsvennoot"      # legal partner (thing)
]

