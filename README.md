Django Project Setup

Tento projekt je postavený na Django 4.2 LTS a obsahuje předinstalované knihovny jako Bootstrap 5, Leaflet a FontAwesome.

----- Požadavky -----

Než začneš, ujisti se, že máš nainstalované:

! Python 3.10 nebo novější

! pip (správce baličků pro Python)

! virtualenv (doporučeno pro izolaci prostředí)

----- 1. Vytvoření virtuálního prostředí -----

!!!!! Vytvoř a aktivuj virtuální prostředí: !!!!!

      1.  python -m venv venv
      2.  venv\Scripts\activate 
                            # Pro MacOS source venv/bin/activate

----- 2. Instalace závislostí -----

Nainstaluj všechny požadované baličky uvedené v requirements.txt:

1. pip install --upgrade pip
2. pip install -r requirements.txt

----- 3. Inicializace projektu -----

Proveď migrace databáze:

python manage.py makemigrations
python manage.py migrate

Vytvoř administrátorský účet:

python manage.py createsuperuser

Spusť vývojový server:

python manage.py runserver

Otevři prohlížeč na adrese:http://127.0.0.1:8000/

4. Struktura projektu

CareServices               # složka obsahujici projekt
│
project/                   # main/root složka projektů
│
├── manage.py              # Django příkazový soubor
├── requirements.txt       # Seznam závislostí
├── README.md              # Tento soubor
├── venv/                  # Virtuální prostředí
│
└── nejlepsiProjekt/       # Hlavní aplikace
    ├── settings.py        # Konfigurace projektu
    ├── urls.py            # Směrování URL
    ├── models.py          # Databázové modely
    ├── views.py           # Logika aplikace
    └── templates/         # HTML šablony


----- 5. Instalované baličky -----

Django 4.2 LTS: Stabilní backend framework

django-bootstrap-v5: Integrace Bootstrap 5

django-leaflet: Podpora pro mapové funkce


django-fontawesome: Integrace FontAwesome ikon
