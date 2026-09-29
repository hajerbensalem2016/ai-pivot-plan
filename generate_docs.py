#!/usr/bin/env python3
"""Génère les 8 docs détail (Markdown + PDF)."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)

# ============================================================
# DÉCOUVERTE (30 min/jour) — culture, articles, vidéos
# ============================================================
DECOUVERTE = {
    "S1": {
        "period": "Mardi 29/09/2026 → Lundi 05/10/2026",
        "theme": "Bases LLM · Embeddings · RAG",
        "tasks": [
            ("Mar 29/09", "Vidéo 3B1B \"What is a GPT?\"", "25 min YouTube. Comprendre transformer + next-token prediction. Zéro maths. Chercher \"3Blue1Brown GPT\"."),
            ("Mer 30/09", "Baromètre IA France 2027", "15 min. Numeum.fr ou Journal du Net. **Noter 3 chiffres** dans journal.md (% boîtes avec projet IA, milliards investis, pénurie profils)."),
            ("Jeu 01/10", "LangChain (page + vidéo 13min)", "30 min. Lire python.langchain.com (5 min) + regarder \"LangChain in 13 minutes\" sur YouTube. Comprendre : chain, prompt template, output parser."),
            ("Ven 02/10", "Prompt Engineering Guide", "20 min sur promptingguide.ai sections Introduction + Basics. Tester 3 prompts (vague, précis, avec exemples) sur ChatGPT gratuit."),
            ("Sam 03/10", "Vector DB Pinecone (article)", "15 min. Article \"What is a vector database?\". Comprendre pourquoi on stocke des vecteurs + similarité cosinus. Regarder 2-3 images embeddings 3D sur Google."),
            ("Dim 04/10", "Vidéo RAG 5min + schéma papier", "30 min. YouTube \"RAG explained in 5 minutes\". **Dessiner à la main** le schéma Question → Embedding → Recherche → Contexte + Question → LLM → Réponse."),
            ("Lun 05/10", "Prépa Sprint 2", "15 min. Lire sommaire Sprint 2. Repos mérité si tout est fait."),
        ],
    },
    "S2": {
        "period": "Mardi 06/10/2026 → Lundi 12/10/2026",
        "theme": "Chunking · Vector DBs · Function Calling",
        "tasks": [
            ("Mar 06/10", "Article \"Chunking strategies for RAG\"", "20 min. Sur Pinecone Blog ou LangChain Blog. Comprendre : fixed-size, recursive, semantic chunking. Trade-offs de chaque approche."),
            ("Mer 07/10", "Cosine similarity vs Euclidean", "15 min. Article Weaviate ou Medium. Pourquoi cosinus est préféré pour les embeddings texte."),
            ("Jeu 08/10", "Comparatif Qdrant vs Pinecone vs Chroma", "20 min. Article comparatif (chercher \"vector database comparison 2026\"). Choisir le bon pour ton projet perso."),
            ("Ven 09/10", "OpenAI Function Calling", "25 min. Doc officielle platform.openai.com/docs/guides/function-calling. Voir comment un LLM appelle du code."),
            ("Sam 10/10", "Vidéo \"Agents vs Chains\" LangChain", "20 min YouTube. Comprendre la différence : chain = pipeline fixe, agent = décide dynamiquement."),
            ("Dim 11/10", "Article MCP (Model Context Protocol)", "20 min. Anthropic blog. Standard émergent 2026 pour connecter LLMs aux outils."),
            ("Lun 12/10", "Prépa Sprint 3", "15 min. Sommaire Sprint 3. Prendre du recul sur les 2 sprints."),
        ],
    },
    "S3": {
        "period": "Mardi 13/10/2026 → Lundi 19/10/2026",
        "theme": "Évaluation LLM · Sécurité · Guardrails",
        "tasks": [
            ("Mar 13/10", "Doc Ragas (page d'accueil + concepts)", "20 min. docs.ragas.io. Comprendre les 3 métriques : faithfulness, answer relevancy, context precision."),
            ("Mer 14/10", "Article \"Hallucinations in LLMs\"", "20 min. Article Nvidia ou OpenAI blog. Pourquoi les LLMs hallucinent et comment mitiger."),
            ("Jeu 15/10", "OWASP LLM Top 10", "25 min. genai.owasp.org. Les 10 risques sécurité LLM (prompt injection, model theft, etc.)."),
            ("Ven 16/10", "Vidéo LangSmith tour", "20 min YouTube \"LangSmith tutorial\". L'outil #1 pour tracer/débugger les chains LangChain en prod."),
            ("Sam 17/10", "Guardrails AI (article Nvidia NeMo)", "20 min. Concept de guardrails : bloquer outputs dangereux/hors sujet."),
            ("Dim 18/10", "Article \"AI Security Engineer\" métier 2027", "15 min. Article ISC2 ou Robert Walters. Le métier qui va exploser en 2027-2028."),
            ("Lun 19/10", "Prépa Sprint 4", "15 min. Sommaire Sprint 4. Plus qu'une semaine !"),
        ],
    },
    "S4": {
        "period": "Mardi 20/10/2026 → Lundi 26/10/2026",
        "theme": "Deploy · Agents · Marché AI Engineer",
        "tasks": [
            ("Mar 20/10", "Doc Azure Container Apps", "25 min. learn.microsoft.com/azure/container-apps. Comment déployer un conteneur Docker sans gérer de cluster K8s."),
            ("Mer 21/10", "Vidéo \"LangGraph agents in production\"", "25 min YouTube. LangGraph = évolution de LangChain pour agents complexes multi-étapes."),
            ("Jeu 22/10", "Article \"MLOps for LLMs\"", "20 min. Monitoring, versioning, A/B testing des prompts."),
            ("Ven 23/10", "OpenAI vs Azure OpenAI (comparaison)", "20 min. Article Medium ou Microsoft blog. Quand choisir l'un ou l'autre en entreprise."),
            ("Sam 24/10", "Étude Malt 2026 : TJM AI Engineer", "20 min. malt.fr/études ou freelance-informatique.fr. Chiffres réels TJM par région/expérience."),
            ("Dim 25/10", "5 offres AI Engineer LinkedIn (analyse)", "30 min. LinkedIn/Welcome to the Jungle. Noter les 3 stacks les plus demandées + les mots-clés récurrents."),
            ("Lun 26/10", "Bilan 4 sprints + phrase pitch", "30 min. Écrire dans journal.md ta phrase pitch de 30 secondes pour entretien AI Engineer."),
        ],
    },
}

# ============================================================
# PRINCIPAL (2h/jour) — code, projet RAG entreprise
# ============================================================
PRINCIPAL = {
    "S1": {
        "period": "Mardi 29/09/2026 → Lundi 05/10/2026",
        "theme": "Python · Setup · Premier LLM",
        "objectif": "Python tourne, tu fais ton premier appel GPT-4 depuis Python + première chain LangChain.",
        "tasks": [
            ("Mar 29/09", "Install Python 3.11 + VS Code + venv", "Dans WSL : `sudo apt install -y python3.11 python3.11-venv python3-pip`. Créer `~/ai-rag-project`, `python3 -m venv venv && source venv/bin/activate`. Écrire `hello.py`. **Livrable** : `hello.py` qui marche."),
            ("Mer 30/09", "Python bases (variables, boucles, listes)", "learnpython.org sections 1-4. Créer `bases.py` avec 6 exercices (somme liste, majeur/mineur, boucle pairs, prénoms, C→F, max sans max()). **Livrable** : `bases.py` complet."),
            ("Jeu 01/10", "Fonctions, dicts, list comprehensions", "learnpython.org Functions + Dictionaries. Créer `fonctions.py` avec `calculer_tjm()` + dict profil manipulé + list comprehension carrés. **Livrable** : `fonctions.py`."),
            ("Ven 02/10", "Fichiers + requests HTTP + JSON", "`pip install requests`. Créer `fichiers.py` (CSV read/write) + `api_call.py` (GitHub API). Bonus : PokeAPI. **Livrable** : 2 scripts qui tournent."),
            ("Sam 03/10", "Azure OpenAI + demande accès + Jupyter", "Compte Azure gratuit + demande accès Azure OpenAI (aka.ms/oaiapply, délai 24-48h). `pip install jupyter matplotlib`. Notebook 3 cellules (random + moyenne + histogramme). **Livrable** : notebook."),
            ("Dim 04/10", "Premier appel LLM (hello_llm.py)", "`pip install openai python-dotenv`. `.env` avec clé API (Azure OU OpenAI classique). `hello_llm.py` qui appelle GPT-4o-mini avec system + user prompts. **Livrable** : réponse de GPT dans le terminal."),
            ("Lun 05/10", "Première chain LangChain + README", "`pip install langchain langchain-openai`. `first_chain.py` avec ChatPromptTemplate + ChatOpenAI + chain (prompt | llm). Test 3 phrases. Créer README.md du projet. **Livrable** : chain qui traduit + README."),
        ],
    },
    "S2": {
        "period": "Mardi 06/10/2026 → Lundi 12/10/2026",
        "theme": "PDFs · Chunking · Embeddings · Qdrant",
        "objectif": "Ton système ingère des PDFs, les chunk, les vectorise, les stocke dans Qdrant.",
        "tasks": [
            ("Mar 06/10", "Télécharger 20 PDFs open source", "Créer `data/pdfs/`. Prendre 20 PDFs SNCF/Légifrance/rapports publics. Vérifier taille raisonnable (< 5Mo/pdf). **Livrable** : dossier avec 20 PDFs."),
            ("Mer 07/10", "PyPDFLoader + extraction texte", "`pip install pypdf langchain-community`. Script `load_pdfs.py` qui charge tous les PDFs et affiche le nombre de pages + un extrait. **Livrable** : script qui parse les 20 PDFs."),
            ("Jeu 08/10", "RecursiveCharacterTextSplitter chunking", "Ajouter chunking : `RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)`. Compter les chunks générés. Afficher un chunk exemple. **Livrable** : liste de N chunks affichée."),
            ("Ven 09/10", "Embeddings Azure OpenAI text-embedding-3-small", "`pip install openai`. Créer `embed.py` qui vectorise un chunk avec `text-embedding-3-small` (1536 dim). Vérifier que ça retourne un vecteur de 1536 floats. **Livrable** : embedding généré."),
            ("Sam 10/10", "Docker Qdrant + client Python", "`docker run -p 6333:6333 -v qdrant_storage:/qdrant/storage qdrant/qdrant`. `pip install qdrant-client`. Créer une collection `docs` avec 1536 dim, distance cosine. **Livrable** : collection Qdrant créée."),
            ("Dim 11/10", "Upsert chunks + première recherche", "Script `ingest.py` qui vectorise + upsert tous les chunks dans Qdrant. Puis `search.py` qui prend une question, la vectorise, et retourne les top 3 chunks. **Livrable** : recherche vectorielle qui marche."),
            ("Lun 12/10", "Refacto ingest.py propre + tests", "Réorganiser en modules : `loader.py`, `chunker.py`, `embedder.py`, `store.py`. Ajouter logs. Tester avec un PDF nouveau. **Livrable** : code propre + test manuel OK."),
        ],
    },
    "S3": {
        "period": "Mardi 13/10/2026 → Lundi 19/10/2026",
        "theme": "RAG complet · Citations · UI Streamlit",
        "objectif": "Chatbot RAG fonctionnel avec citations sources, anti-hallucination, dashboard éval Streamlit.",
        "tasks": [
            ("Mar 13/10", "Chain RAG complète (retrieval + génération)", "Créer `rag.py` : question → embedding → recherche Qdrant → prompt template avec contexte → GPT-4o-mini → réponse. **Livrable** : première réponse RAG cohérente."),
            ("Mer 14/10", "Citations sources dans réponse", "Enrichir le prompt : demander à GPT de citer `[Source: doc.pdf, page X]`. Passer les metadata des chunks (nom fichier + page) dans le contexte. **Livrable** : réponses avec sources."),
            ("Jeu 15/10", "Anti-hallucination : seuil similarité 0.75", "Dans le retrieval, si le meilleur score < 0.75, ne pas appeler le LLM et retourner \"Je ne trouve pas la réponse dans les documents\". **Livrable** : test avec question hors sujet → refus."),
            ("Ven 16/10", "Dataset éval 20 questions/réponses", "Créer `eval_dataset.json` avec 20 questions + réponses attendues + contextes attendus (chunks). Prendre 5 questions faciles, 10 moyennes, 5 pièges. **Livrable** : JSON de 20 entries."),
            ("Sam 17/10", "Ragas : faithfulness + relevancy + precision", "`pip install ragas`. Script `evaluate.py` qui tourne Ragas sur les 20 questions et affiche les 3 scores. **Livrable** : rapport texte avec scores."),
            ("Dim 18/10", "Streamlit chat UI + sidebar sources", "`pip install streamlit`. `app.py` avec chat (input + réponse) + sidebar affichant les sources utilisées. **Livrable** : app Streamlit qui tourne localement."),
            ("Lun 19/10", "Dashboard éval Streamlit (gauges scores)", "Ajouter page \"Évaluation\" dans Streamlit avec 3 gauges (plotly ou native) affichant faithfulness/relevancy/precision. **Livrable** : dashboard complet."),
        ],
    },
    "S4": {
        "period": "Mardi 20/10/2026 → Lundi 26/10/2026",
        "theme": "Deploy Azure · GitHub · Vitrine LinkedIn",
        "objectif": "App en ligne accessible, code sur GitHub public, post LinkedIn, 10 candidatures envoyées.",
        "tasks": [
            ("Mar 20/10", "Dockerfile + docker build local", "Écrire `Dockerfile` (base python:3.11-slim, copy requirements, install, copy code, expose 8501, CMD streamlit). `docker build -t rag-app .` puis `docker run -p 8501:8501 rag-app`. **Livrable** : conteneur qui tourne local."),
            ("Mer 21/10", "Push image Docker Hub + Azure Container Registry", "Créer compte Docker Hub. `docker tag` + `docker push`. Créer un Azure Container Registry (ACR). Push l'image sur ACR. **Livrable** : image sur Docker Hub + ACR."),
            ("Jeu 22/10", "Deploy Azure Container Apps", "Portail Azure : créer Container App qui pointe sur ton image ACR. Configurer les env vars (clés API). Récupérer l'URL publique https://xxx.azurecontainerapps.io. **Livrable** : URL live cliquable."),
            ("Ven 23/10", "README GitHub pro (archi + démo GIF + scores)", "Créer repo GitHub public `rag-enterprise-assistant`. Push le code (sans clés API). Écrire README avec : titre, description, diagramme archi (draw.io), screenshots, scores Ragas, comment lancer. **Livrable** : repo GitHub propre."),
            ("Sam 24/10", "Enregistrer démo vidéo 90s", "Loom ou OBS. Montrer : question posée → réponse avec sources → dashboard éval. Voix off en français. Uploader sur LinkedIn ou YouTube unlisted. **Livrable** : vidéo 90s prête à partager."),
            ("Dim 25/10", "Réserver AI-900 + 100 questions ExamTopics", "Sur Pearson VUE : réserver AI-900 (99€) pour la semaine du 27/10. Faire 100 questions ExamTopics AI-900. Noter les points faibles. **Livrable** : certif réservée + score quiz."),
            ("Lun 26/10", "Post LinkedIn + candidater 10 offres AI Engineer", "Post LinkedIn : phrase pivot + vidéo démo + lien GitHub + lien app. Mettre à jour profil : titre \"AI Engineer | Azure OpenAI | RAG | LangChain\". Candidater à 10 offres. **Livrable** : post publié + 10 candidatures."),
        ],
    },
}


def gen_decouverte(num, data):
    lignes = []
    for i, (date, tache, detail) in enumerate(data["tasks"], 1):
        lignes.append(f"| J{i} | {date} | {tache} | {detail} | [ ] |")
    tableau = "\n".join(lignes)
    md = f"""---
title: "Sprint {num[1]} Découverte — {data['theme']}"
subtitle: "Bloc léger 30 min/jour"
date: "{data['period']}"
---

# Sprint {num[1]} — Découverte IA

**Thème** : {data['theme']}

**Période** : {data['period']}

**Rythme** : 30 min/jour, léger. À faire au café, en mangeant, avant de dormir.

---

## Tableau du Sprint

| Jour | Date | Tâche | Détail | Fait |
|:----:|:----:|-------|--------|:----:|
{tableau}

---

## Bilan Sprint {num[1]}

À remplir le dernier jour du sprint dans `journal.md` :

### Ce que je sais expliquer maintenant

- [ ] Concept 1 (à compléter selon le thème)
- [ ] Concept 2
- [ ] Concept 3

### Auto-évaluation

- Tâches faites : ___ / 7
- Vidéo/article qui m'a le plus marquée : _______________
- Question que je me pose encore : _______________

### Ma phrase pour le sprint suivant

> _(à écrire — une phrase courte qui résume ce que tu as appris)_

---

**Le board mural correspondant** : `boards/Board_Decouverte_{num}.pdf`
"""
    (DOCS / f"Detail_Decouverte_{num}.md").write_text(md, encoding="utf-8")


def gen_principal(num, data):
    jours = []
    for i, (date, tache, detail) in enumerate(data["tasks"], 1):
        jours.append(f"""## Jour {i} — {date}

### {tache}

{detail}

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git
""")
    corps = "\n".join(jours)
    md = f"""---
title: "Semaine {num[1]} Principal — {data['theme']}"
subtitle: "2h/jour, code, projet RAG"
date: "{data['period']}"
---

# Semaine {num[1]} — Bloc Principal

**Thème** : {data['theme']}

**Période** : {data['period']}

**Rythme** : 2h/jour, concentration, code.

**Objectif de la semaine** : {data['objectif']}

---

{corps}

---

## Bilan Semaine {num[1]}

À remplir dans `journal.md` :

### Ce que je sais faire techniquement

- [ ] (Compétence 1)
- [ ] (Compétence 2)
- [ ] (Compétence 3)

### Bloquée / à revoir

_(ce qui a coincé)_

### Ma phrase pour l'entretien

> _(1-2 phrases qui résument ce que j'ai construit cette semaine)_

### Auto-évaluation

- Jours faits : ___ / 7
- Objectif principal atteint : OUI / NON
- Prêt pour semaine suivante : OUI / NON

---

**Le board mural correspondant** : `boards/Board_Principal_{num}.pdf`
"""
    (DOCS / f"Detail_Principal_{num}.md").write_text(md, encoding="utf-8")


for num, data in DECOUVERTE.items():
    gen_decouverte(num, data)
    print(f"✓ Detail_Decouverte_{num}.md")

for num, data in PRINCIPAL.items():
    gen_principal(num, data)
    print(f"✓ Detail_Principal_{num}.md")

# Convertir tous les MD en PDFs
print("\nConversion en PDF...")
for md in DOCS.glob("*.md"):
    pdf = md.with_suffix(".pdf")
    subprocess.run([
        "pandoc", str(md), "-o", str(pdf),
        "--pdf-engine=weasyprint",
        "-V", "geometry:margin=1.5cm",
    ], check=True)
    print(f"✓ {pdf.name}")

print("\nTous les docs générés dans docs/")
