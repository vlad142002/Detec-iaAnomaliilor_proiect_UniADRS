# Detecția Anomaliilor - Proiect UniADRS

Acest repository conține codul sursă pentru proiectul de detecție a anomaliilor realizat în cadrul UniADRS.

Proiectul folosește un set de date extern, care nu este inclus în repository din cauza dimensiunii mari. Datele trebuie descărcate separat și plasate local în directorul data/.

## Cerințe

Pentru rularea proiectului s-a folosit următoarea versiune de Python:

Python 3.9.6

Se recomandă folosirea aceleiași versiuni sau a unei versiuni compatibile de Python 3.9.

Pentru verificarea versiunii instalate:

python3 --version

sau:

python --version

## Instalare

### 1. Clonarea repository-ului

git clone https://github.com/vlad142002/Detec-iaAnomaliilor_proiect_UniADRS.git
cd Detec-iaAnomaliilor_proiect_UniADRS

### 2. Crearea mediului virtual

Pe macOS / Linux:

python3 -m venv .venv
source .venv/bin/activate

Pe Windows:

python -m venv .venv
.venv\Scripts\activate

### 3. Instalarea dependențelor

pip install -r requirements.txt

## Pregătirea setului de date

Setul de date trebuie descărcat separat, deoarece nu este inclus în repository.

Surse pentru descărcare:

1. Formular / pagină set de date:
https://www.wjx.cn/vm/ruVKZ9e.aspx#

2. Download Zenodo pentru data și data2:
https://zenodo.org/records/14538584

3. Download pentru isAID:
https://rsidea.whu.edu.cn/code_data/isAID.zip

Observație: varianta isAID inclusă în data poate fi coruptă, de aceea se recomandă descărcarea separată a fișierului isAID.zip din linkul de mai sus.

După descărcare și dezarhivare, în rădăcina proiectului trebuie creat directorul data/.

Structura recomandată este:

data/
├── HH_LK_HH/
├── isAID/
└── multi-modality-data/

Folderele trebuie să fie plasate exact în directorul data/, deoarece scripturile proiectului se așteaptă să găsească datele în această locație.

## Rularea proiectului

Pentru rularea proiectului se folosește fișierul principal run.py, împreună cu fișierul de configurare din directorul configs/.

Comanda folosită pentru rulare:

python run.py "./configs/training&infer_img_folder.yaml"

Pe unele sisteme, dacă python nu indică spre Python 3.9, se poate folosi:

python3 run.py "./configs/training&infer_img_folder.yaml"

## Structura proiectului

configs/        - Fișiere de configurare pentru rulare, antrenare și inferență
criterions/     - Funcții de loss și criterii folosite în antrenare
datasets/       - Cod pentru încărcarea și procesarea dataset-urilor
models/         - Arhitecturi și componente ale modelelor
runners/        - Logica de rulare a experimentelor
utils/          - Funcții auxiliare
run.py          - Scriptul principal de rulare
requirements.txt
README.md

Directoarele precum data/, deoarece conțin date mari sau rezultate generate local.

## Observații

- Proiectul a fost rulat folosind Python 3.9.6.
- Este recomandată rularea într-un mediu virtual .venv.
- Setul de date trebuie descărcat și pregătit manual înainte de rulare.
- Repository-ul conține codul sursă și fișierele de configurare necesare, dar nu conține datele brute sau rezultatele generate.
- Pentru reproducerea completă a experimentelor, trebuie respectată structura directorului data/.
