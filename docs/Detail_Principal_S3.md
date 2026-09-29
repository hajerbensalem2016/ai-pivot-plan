---
title: "Semaine 3 Principal — RAG complet · Citations · UI Streamlit"
subtitle: "2h/jour, code, projet RAG"
date: "Mardi 13/10/2026 → Lundi 19/10/2026"
---

# Semaine 3 — Bloc Principal

**Thème** : RAG complet · Citations · UI Streamlit

**Période** : Mardi 13/10/2026 → Lundi 19/10/2026

**Rythme** : 2h/jour, concentration, code.

**Objectif de la semaine** : Chatbot RAG fonctionnel avec citations sources, anti-hallucination, dashboard éval Streamlit.

---

## Jour 1 — Mar 13/10

### Chain RAG complète (retrieval + génération)

Créer `rag.py` : question → embedding → recherche Qdrant → prompt template avec contexte → GPT-4o-mini → réponse. **Livrable** : première réponse RAG cohérente.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 2 — Mer 14/10

### Citations sources dans réponse

Enrichir le prompt : demander à GPT de citer `[Source: doc.pdf, page X]`. Passer les metadata des chunks (nom fichier + page) dans le contexte. **Livrable** : réponses avec sources.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 3 — Jeu 15/10

### Anti-hallucination : seuil similarité 0.75

Dans le retrieval, si le meilleur score < 0.75, ne pas appeler le LLM et retourner "Je ne trouve pas la réponse dans les documents". **Livrable** : test avec question hors sujet → refus.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 4 — Ven 16/10

### Dataset éval 20 questions/réponses

Créer `eval_dataset.json` avec 20 questions + réponses attendues + contextes attendus (chunks). Prendre 5 questions faciles, 10 moyennes, 5 pièges. **Livrable** : JSON de 20 entries.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 5 — Sam 17/10

### Ragas : faithfulness + relevancy + precision

`pip install ragas`. Script `evaluate.py` qui tourne Ragas sur les 20 questions et affiche les 3 scores. **Livrable** : rapport texte avec scores.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 6 — Dim 18/10

### Streamlit chat UI + sidebar sources

`pip install streamlit`. `app.py` avec chat (input + réponse) + sidebar affichant les sources utilisées. **Livrable** : app Streamlit qui tourne localement.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 7 — Lun 19/10

### Dashboard éval Streamlit (gauges scores)

Ajouter page "Évaluation" dans Streamlit avec 3 gauges (plotly ou native) affichant faithfulness/relevancy/precision. **Livrable** : dashboard complet.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git


---

## Bilan Semaine 3

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

**Le board mural correspondant** : `boards/Board_Principal_S3.pdf`
