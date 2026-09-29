---
title: "Semaine 2 Principal — PDFs · Chunking · Embeddings · Qdrant"
subtitle: "2h/jour, code, projet RAG"
date: "Mardi 06/10/2026 → Lundi 12/10/2026"
---

# Semaine 2 — Bloc Principal

**Thème** : PDFs · Chunking · Embeddings · Qdrant

**Période** : Mardi 06/10/2026 → Lundi 12/10/2026

**Rythme** : 2h/jour, concentration, code.

**Objectif de la semaine** : Ton système ingère des PDFs, les chunk, les vectorise, les stocke dans Qdrant.

---

## Jour 1 — Mar 06/10

### Télécharger 20 PDFs open source

Créer `data/pdfs/`. Prendre 20 PDFs SNCF/Légifrance/rapports publics. Vérifier taille raisonnable (< 5Mo/pdf). **Livrable** : dossier avec 20 PDFs.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 2 — Mer 07/10

### PyPDFLoader + extraction texte

`pip install pypdf langchain-community`. Script `load_pdfs.py` qui charge tous les PDFs et affiche le nombre de pages + un extrait. **Livrable** : script qui parse les 20 PDFs.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 3 — Jeu 08/10

### RecursiveCharacterTextSplitter chunking

Ajouter chunking : `RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)`. Compter les chunks générés. Afficher un chunk exemple. **Livrable** : liste de N chunks affichée.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 4 — Ven 09/10

### Embeddings Azure OpenAI text-embedding-3-small

`pip install openai`. Créer `embed.py` qui vectorise un chunk avec `text-embedding-3-small` (1536 dim). Vérifier que ça retourne un vecteur de 1536 floats. **Livrable** : embedding généré.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 5 — Sam 10/10

### Docker Qdrant + client Python

`docker run -p 6333:6333 -v qdrant_storage:/qdrant/storage qdrant/qdrant`. `pip install qdrant-client`. Créer une collection `docs` avec 1536 dim, distance cosine. **Livrable** : collection Qdrant créée.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 6 — Dim 11/10

### Upsert chunks + première recherche

Script `ingest.py` qui vectorise + upsert tous les chunks dans Qdrant. Puis `search.py` qui prend une question, la vectorise, et retourne les top 3 chunks. **Livrable** : recherche vectorielle qui marche.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 7 — Lun 12/10

### Refacto ingest.py propre + tests

Réorganiser en modules : `loader.py`, `chunker.py`, `embedder.py`, `store.py`. Ajouter logs. Tester avec un PDF nouveau. **Livrable** : code propre + test manuel OK.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git


---

## Bilan Semaine 2

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

**Le board mural correspondant** : `boards/Board_Principal_S2.pdf`
