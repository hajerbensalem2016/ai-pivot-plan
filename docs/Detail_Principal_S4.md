---
title: "Semaine 4 Principal — Deploy Azure · GitHub · Vitrine LinkedIn"
subtitle: "2h/jour, code, projet RAG"
date: "Mardi 20/10/2026 → Lundi 26/10/2026"
---

# Semaine 4 — Bloc Principal

**Thème** : Deploy Azure · GitHub · Vitrine LinkedIn

**Période** : Mardi 20/10/2026 → Lundi 26/10/2026

**Rythme** : 2h/jour, concentration, code.

**Objectif de la semaine** : App en ligne accessible, code sur GitHub public, post LinkedIn, 10 candidatures envoyées.

---

## Jour 1 — Mar 20/10

### Dockerfile + docker build local

Écrire `Dockerfile` (base python:3.11-slim, copy requirements, install, copy code, expose 8501, CMD streamlit). `docker build -t rag-app .` puis `docker run -p 8501:8501 rag-app`. **Livrable** : conteneur qui tourne local.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 2 — Mer 21/10

### Push image Docker Hub + Azure Container Registry

Créer compte Docker Hub. `docker tag` + `docker push`. Créer un Azure Container Registry (ACR). Push l'image sur ACR. **Livrable** : image sur Docker Hub + ACR.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 3 — Jeu 22/10

### Deploy Azure Container Apps

Portail Azure : créer Container App qui pointe sur ton image ACR. Configurer les env vars (clés API). Récupérer l'URL publique https://xxx.azurecontainerapps.io. **Livrable** : URL live cliquable.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 4 — Ven 23/10

### README GitHub pro (archi + démo GIF + scores)

Créer repo GitHub public `rag-enterprise-assistant`. Push le code (sans clés API). Écrire README avec : titre, description, diagramme archi (draw.io), screenshots, scores Ragas, comment lancer. **Livrable** : repo GitHub propre.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 5 — Sam 24/10

### Enregistrer démo vidéo 90s

Loom ou OBS. Montrer : question posée → réponse avec sources → dashboard éval. Voix off en français. Uploader sur LinkedIn ou YouTube unlisted. **Livrable** : vidéo 90s prête à partager.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 6 — Dim 25/10

### Réserver AI-900 + 100 questions ExamTopics

Sur Pearson VUE : réserver AI-900 (99€) pour la semaine du 27/10. Faire 100 questions ExamTopics AI-900. Noter les points faibles. **Livrable** : certif réservée + score quiz.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git

## Jour 7 — Lun 26/10

### Post LinkedIn + candidater 10 offres AI Engineer

Post LinkedIn : phrase pivot + vidéo démo + lien GitHub + lien app. Mettre à jour profil : titre "AI Engineer | Azure OpenAI | RAG | LangChain". Candidater à 10 offres. **Livrable** : post publié + 10 candidatures.

- [ ] Fait
- [ ] Testé
- [ ] Commité sur Git


---

## Bilan Semaine 4

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

**Le board mural correspondant** : `boards/Board_Principal_S4.pdf`
