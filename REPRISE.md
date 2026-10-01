# Reprise du projet — État au 01/10/2026

## Où j'en suis exactement

**Dernière action** : création de la ressource Azure OpenAI `openai-hajer-rag` dans le Resource Group `RGHAJERPERSOAIPOC` (région France Central).

**Prochaine action** : déployer le modèle `gpt-4o-mini` dans Azure AI Foundry portal.

## Progression Sprint 1 (7/14 cartes en PROD)

- [x] J1 Principal — Setup Python + venv + hello.py
- [x] J1 Découverte — Vidéo 3B1B sur GPT
- [x] J2 Principal — bases.py (6 exos Python)
- [x] J2 Découverte — Baromètre IA France 2027 (3 chiffres notés)
- [x] J3 Principal — fonctions.py (fonctions, dicts, list comprehension)
- [x] J3 Découverte — Vidéo LangChain 13 min
- [x] J4 Principal — fichiers.py + api_call.py (CSV + requests HTTP)
- [ ] J4 Découverte — Prompt Engineering Guide + 3 tests ChatGPT
- [ ] J5 Principal — Azure OpenAI + modèle + Jupyter (EN COURS)
- [ ] J5 Découverte — Article Pinecone vector DB
- [ ] J6 Principal — hello_llm.py (premier appel GPT)
- [ ] J6 Découverte — Vidéo RAG 5 min + schéma papier
- [ ] J7 Principal — first_chain.py (première chain LangChain)
- [ ] J7 Découverte — Prépa Sprint 2

---

## Setup à faire AU DÉBUT de chaque session

### À la maison (pas de VPN AMF)

```bash
# 1. Activer le venv
cd ~/ai-rag-project && source venv/bin/activate

# 2. Vérifier qu'il n'y a pas de proxy résiduel
unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy
```

Si `pip` ou `python` galère → wsl-vpnkit tourne peut-être encore :

```bash
# Vérifier
ip route | head -1
# Si "via 192.168.127.1 dev wsltap" → wsl-vpnkit encore actif
```

Pour l'arrêter : fermer la fenêtre PowerShell qui le fait tourner.

### Au bureau (VPN AMF actif)

```bash
# 1. Lancer wsl-vpnkit depuis PowerShell Windows (SI pas déjà lancé) :
# wsl -d wsl-vpnkit --cd /app ./wsl-vpnkit
# ↑ dans PowerShell, pas WSL

# 2. Dans WSL — vérifier le DNS
cat /etc/resolv.conf
# Doit afficher : nameserver 192.168.127.1
# Si pas le cas :
echo "nameserver 192.168.127.1" | sudo tee /etc/resolv.conf

# 3. Exports proxy + SSL
export HTTP_PROXY=http://185.46.212.41:10299
export HTTPS_PROXY=http://185.46.212.41:10299
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# 4. Activer venv
cd ~/ai-rag-project && source venv/bin/activate
```

### Script tout-en-un bureau

Un fichier `setup_bureau.sh` est fourni dans le repo. Au bureau, taper :

```bash
source ~/setup_bureau.sh
```

Il fait tout d'un coup : wsl-vpnkit check + DNS + proxy + venv.

---

## Config Azure (déjà créé)

| Élément | Valeur |
|---------|--------|
| Compte Microsoft | compte perso du mari (Gmail) |
| Subscription ID | `5d7a78a9-d9cc-48a3-9347-578f4f62f4a9` |
| Nom Subscription | `Azure subscription 1` |
| Resource Group | `RGHAJERPERSOAIPOC` |
| Région | France Central |
| Ressource Azure OpenAI | `openai-hajer-rag` |
| Modèle à déployer | `gpt-4o-mini` (Global Standard) |
| Budget alert | 10$/mois (email à 5$/8$/10$) |
| Rappel suppression | Google Calendar 26/10/2026 |

---

## Prochaines étapes concrètes

### Étape 1 — Déployer le modèle gpt-4o-mini

1. https://portal.azure.com → ta ressource `openai-hajer-rag`
2. Clique **"Go to Azure AI Foundry portal"** en haut de la page
3. Menu gauche → **Deployments** → **+ Deploy model** → **Deploy base model**
4. Choisis **gpt-4o-mini** → **Confirm**
5. Formulaire :
   - **Deployment name** : `gpt-4o-mini`
   - **Deployment type** : `Global Standard`
   - Laisse le reste par défaut
6. Clique **Deploy**

### Étape 2 — Récupérer endpoint + clé

Sur la page de `openai-hajer-rag` :
- Menu gauche → **Keys and Endpoint**
- Copie **Endpoint** (ex: `https://openai-hajer-rag.openai.azure.com/`)
- Copie **KEY 1**

### Étape 3 — Créer `.env` dans le projet

Dans `~/ai-rag-project/` :

```bash
cat > .env << 'EOF'
AZURE_OPENAI_ENDPOINT=https://openai-hajer-rag.openai.azure.com/
AZURE_OPENAI_KEY=COLLER_LA_CLE_ICI
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
AZURE_OPENAI_API_VERSION=2024-10-21
EOF
```

Vérifier que `.env` est bien dans `.gitignore` (déjà le cas).

### Étape 4 — Installer packages pour LLM

```bash
pip install openai python-dotenv langchain langchain-openai
```

(Au bureau : les 4 exports proxy/SSL doivent être set avant pip)

### Étape 5 — Premier appel LLM (hello_llm.py)

Créer `hello_llm.py` dans VS Code :

```python
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    messages=[
        {"role": "system", "content": "Tu es un expert en industrie sidérurgique."},
        {"role": "user", "content": "Explique en 3 phrases ce qu'est une bobine inox."}
    ]
)

print(response.choices[0].message.content)
```

Lancer :

```bash
python hello_llm.py
```

Résultat : GPT-4o-mini répond en 3 phrases sur les bobines inox.

**Carte J6 Principal → PROD.**

### Étape 6 — Première chain LangChain (first_chain.py)

```python
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Traduis ce texte en anglais professionnel : {texte}"
)

llm = AzureChatOpenAI(
    azure_deployment="gpt-4o-mini",
    api_version="2024-10-21",
)

chain = prompt | llm
result = chain.invoke({"texte": "Bonjour, je souhaite un devis pour un projet IA."})
print(result.content)
```

Lancer avec `python first_chain.py`.

**Carte J7 Principal → PROD. Fin du Sprint 1.**

---

## Phrases pour l'entretien (à mémoriser au fur et à mesure)

Après Sprint 1 (fin 05/10) :
> "J'ai monté un environnement Python dans WSL, intégré Azure OpenAI avec GPT-4o-mini, et fait mes premiers appels LLM via l'API Azure et via LangChain (ChatPromptTemplate). Je comprends l'architecture d'un RAG à haut niveau."

Après Sprint 2 (fin 12/10) :
> "J'ai ingéré 20 PDFs avec PyPDFLoader, chunking récursif (500/50), embeddings Azure OpenAI, stockés dans Qdrant avec similarité cosinus."

Après Sprint 3 (fin 19/10) :
> "Mon RAG complet répond avec citations sources, anti-hallucination à seuil 0.75, évalué avec Ragas (faithfulness/relevancy/precision), interface Streamlit."

Après Sprint 4 (fin 26/10) :
> "Déployé sur Azure Container Apps, repo GitHub public, démo vidéo 90s, 10 candidatures AI Engineer envoyées."

---

## Checklist "fin de session"

Avant de fermer :
- [ ] Sauvegarder tous les fichiers VS Code (`Ctrl+S` partout)
- [ ] Commit sur Git si changements importants : `git add . && git commit -m "..."`
- [ ] Noter dans `journal.md` ce qui a été fait
- [ ] Mettre à jour les cases cochées dans ce fichier (REPRISE.md)
- [ ] Fermer la fenêtre PowerShell wsl-vpnkit (si bureau)

## Checklist "fin de projet" (26/10)

- [ ] Supprimer le Resource Group `RGHAJERPERSOAIPOC` sur Azure
- [ ] Vérifier qu'il n'y a plus rien qui consomme (dashboard Cost)
- [ ] Fin du budget alert (optionnel)
