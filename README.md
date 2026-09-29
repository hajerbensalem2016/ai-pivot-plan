# AI Pivot Plan — .NET/Angular vers AI Engineer

Plan de pivot professionnel sur **4 semaines** (Mar 29/09/2026 → Lun 26/10/2026) pour passer de dev .NET/Angular à AI Engineer, spécialisation **RAG entreprise Azure OpenAI + LangChain**.

## Objectif final (Lun 26/10)

Un projet livré, vendable en entretien :

- Assistant RAG entreprise déployé sur Azure Container Apps (URL publique)
- Repo GitHub public avec README pro + démo vidéo 90s
- Certif AI-900 réservée
- Post LinkedIn de pivot + 10 candidatures AI Engineer envoyées

## Rythme quotidien

Chaque jour, 2 blocs distincts :

- **Bloc Principal (2h)** : code, projet RAG, technique
- **Bloc Découverte (30 min)** : léger, culture IA (vidéos, articles) — à faire au café/en mangeant

Total : **2h30/jour × 28 jours = 70h** sur 4 semaines.

## Structure du repo

```
AI-Pivot-Planning/
├── README.md                        (tu es ici)
├── INSTALL.md                       (à faire AVANT le sprint 1)
├── journal.md                       (bilans hebdo à remplir)
├── boards/                          (Boards Scrum muraux — à imprimer)
│   ├── Board_Decouverte_S1.pdf     (Mar 29/09 → Lun 05/10)
│   ├── Board_Decouverte_S2.pdf     (Mar 06/10 → Lun 12/10)
│   ├── Board_Decouverte_S3.pdf     (Mar 13/10 → Lun 19/10)
│   ├── Board_Decouverte_S4.pdf     (Mar 20/10 → Lun 26/10)
│   ├── Board_Principal_S1.pdf
│   ├── Board_Principal_S2.pdf
│   ├── Board_Principal_S3.pdf
│   └── Board_Principal_S4.pdf
├── docs/                            (Détail de chaque tâche — backup)
│   ├── Detail_Decouverte_S1.pdf ... S4.pdf
│   └── Detail_Principal_S1.pdf  ... S4.pdf
├── code/                            (Ton projet RAG — vide au départ)
├── generate.py                      (Script qui régénère les boards)
└── generate_docs.py                 (Script qui régénère les docs détail)
```

## Comment démarrer

1. **Avant tout** : lire `INSTALL.md` et faire toutes les installations (1h30)
2. **Imprimer** les 8 boards Scrum dans `boards/` et les coller au mur
3. **Sprint 1 démarre le Mar 29/09/2026** — ouvrir `docs/Detail_Decouverte_S1.pdf` et `docs/Detail_Principal_S1.pdf`
4. Chaque jour, **déplacer les cartes** sur le board mural : TODO → DOING → REVIEW → TEST → PROD
5. Chaque fin de sprint, **remplir le bilan** dans `journal.md`

## Planning global

| Sprint | Période | Thème Principal (2h/j) | Thème Découverte (30min/j) |
|--------|---------|------------------------|----------------------------|
| S1 | 29/09 → 05/10 | Python + Setup + Premier LLM | Bases LLM + RAG concept |
| S2 | 06/10 → 12/10 | PDFs + Chunking + Qdrant | Vector DBs + Function Calling |
| S3 | 13/10 → 19/10 | RAG complet + Éval + Streamlit | Ragas + Sécurité LLM |
| S4 | 20/10 → 26/10 | Deploy Azure + LinkedIn | Marché AI Engineer |

## Colonnes du Board Scrum

- **TODO** : pas commencée
- **DOING** : en cours
- **REVIEW** : finie, je relis / vérifie
- **TEST** : je m'entraîne à l'expliquer à voix haute
- **PROD** : validée, archivée

**Objectif minimum** : 5/7 cartes en PROD à la fin de chaque sprint.

## Ressources principales

- Python : [learnpython.org](https://www.learnpython.org)
- LangChain : [python.langchain.com](https://python.langchain.com)
- Azure OpenAI : [learn.microsoft.com/azure/ai-services/openai](https://learn.microsoft.com/azure/ai-services/openai)
- Ragas (éval LLM) : [docs.ragas.io](https://docs.ragas.io)
- Prompt engineering : [promptingguide.ai](https://www.promptingguide.ai)

## Stack finale (à J+28)

Python · FastAPI · LangChain · Azure OpenAI · Qdrant · Ragas · Streamlit · Docker · Azure Container Apps
