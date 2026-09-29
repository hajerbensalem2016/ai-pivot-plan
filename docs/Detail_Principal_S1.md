---
title: "Semaine 1 Principal — Python · Setup · Premier LLM"
subtitle: "2h/jour, code, projet RAG"
date: "Mardi 29/09/2026 → Lundi 05/10/2026"
---

# Semaine 1 — Bloc Principal

**Thème** : Python · Setup · Premier LLM

**Période** : Mardi 29/09/2026 → Lundi 05/10/2026

**Rythme** : 2h/jour, concentration, code.

**Objectif de la semaine** : Python tourne, tu fais ton premier appel GPT-4 depuis Python + première chain LangChain.

---

## Jour 1 — Mar 29/09

### Install Python 3.11 + VS Code + venv

Dans WSL : `sudo apt install -y python3.11 python3.11-venv python3-pip`. Créer `~/ai-rag-project`, `python3 -m venv venv && source venv/bin/activate`. Écrire `hello.py`. **Livrable** : `hello.py` qui marche.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 2 — Mer 30/09

### Python bases (variables, boucles, listes)

learnpython.org sections 1-4. Créer `bases.py` avec 6 exercices (somme liste, majeur/mineur, boucle pairs, prénoms, C→F, max sans max()). **Livrable** : `bases.py` complet.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 3 — Jeu 01/10

### Fonctions, dicts, list comprehensions

learnpython.org Functions + Dictionaries. Créer `fonctions.py` avec `calculer_tjm()` + dict profil manipulé + list comprehension carrés. **Livrable** : `fonctions.py`.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 4 — Ven 02/10

### Fichiers + requests HTTP + JSON

`pip install requests`. Créer `fichiers.py` (CSV read/write) + `api_call.py` (GitHub API). Bonus : PokeAPI. **Livrable** : 2 scripts qui tournent.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 5 — Sam 03/10

### Azure OpenAI + demande accès + Jupyter

Compte Azure gratuit + demande accès Azure OpenAI (aka.ms/oaiapply, délai 24-48h). `pip install jupyter matplotlib`. Notebook 3 cellules (random + moyenne + histogramme). **Livrable** : notebook.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 6 — Dim 04/10

### Premier appel LLM (hello_llm.py)

`pip install openai python-dotenv`. `.env` avec clé API (Azure OU OpenAI classique). `hello_llm.py` qui appelle GPT-4o-mini avec system + user prompts. **Livrable** : réponse de GPT dans le terminal.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 7 — Lun 05/10

### Première chain LangChain + README

`pip install langchain langchain-openai`. `first_chain.py` avec ChatPromptTemplate + ChatOpenAI + chain (prompt | llm). Test 3 phrases. Créer README.md du projet. **Livrable** : chain qui traduit + README.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git


---

## Bilan Semaine 1

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

**Le board mural correspondant** : `boards/Board_Principal_S1.pdf`
