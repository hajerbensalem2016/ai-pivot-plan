#!/usr/bin/env python3
"""Génère les 8 boards muraux (HTML + PDF) pour le plan AI Pivot 4 semaines."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
BOARDS = ROOT / "boards"
BOARDS.mkdir(exist_ok=True)

DECOUVERTE = {
    "S1": {
        "period": "Mardi 29/09/2026 → Lundi 05/10/2026",
        "titre_court": "Bases LLM · Embeddings · RAG",
        "tasks": [
            ("J1", "Mar 29/09", "Vidéo 3B1B \"What is a GPT?\""),
            ("J2", "Mer 30/09", "Baromètre IA France 2027"),
            ("J3", "Jeu 01/10", "LangChain (page + vidéo 13min)"),
            ("J4", "Ven 02/10", "Prompt Engineering Guide"),
            ("J5", "Sam 03/10", "Vector DB Pinecone (article)"),
            ("J6", "Dim 04/10", "Vidéo RAG 5min + schéma papier"),
            ("J7", "Lun 05/10", "Prépa Sprint 2"),
        ],
    },
    "S2": {
        "period": "Mardi 06/10/2026 → Lundi 12/10/2026",
        "titre_court": "Chunking · Vector DBs · Function Calling",
        "tasks": [
            ("J1", "Mar 06/10", "Article \"Chunking strategies for RAG\""),
            ("J2", "Mer 07/10", "Cosine similarity vs Euclidean (article)"),
            ("J3", "Jeu 08/10", "Comparatif Qdrant vs Pinecone vs Chroma"),
            ("J4", "Ven 09/10", "OpenAI Function Calling (doc)"),
            ("J5", "Sam 10/10", "Vidéo \"Agents vs Chains\" LangChain"),
            ("J6", "Dim 11/10", "Article MCP (Model Context Protocol)"),
            ("J7", "Lun 12/10", "Prépa Sprint 3"),
        ],
    },
    "S3": {
        "period": "Mardi 13/10/2026 → Lundi 19/10/2026",
        "titre_court": "Évaluation LLM · Sécurité · Guardrails",
        "tasks": [
            ("J1", "Mar 13/10", "Doc Ragas (page d'accueil + concepts)"),
            ("J2", "Mer 14/10", "Article \"Hallucinations in LLMs\""),
            ("J3", "Jeu 15/10", "OWASP LLM Top 10 (survol)"),
            ("J4", "Ven 16/10", "Vidéo LangSmith tour"),
            ("J5", "Sam 17/10", "Guardrails AI (article Nvidia NeMo)"),
            ("J6", "Dim 18/10", "Article \"AI Security Engineer\" métier 2027"),
            ("J7", "Lun 19/10", "Prépa Sprint 4"),
        ],
    },
    "S4": {
        "period": "Mardi 20/10/2026 → Lundi 26/10/2026",
        "titre_court": "Deploy · Agents · Marché AI Engineer",
        "tasks": [
            ("J1", "Mar 20/10", "Doc Azure Container Apps (déploiement)"),
            ("J2", "Mer 21/10", "Vidéo \"LangGraph agents in production\""),
            ("J3", "Jeu 22/10", "Article \"MLOps for LLMs\" (monitoring)"),
            ("J4", "Ven 23/10", "OpenAI vs Azure OpenAI (comparaison)"),
            ("J5", "Sam 24/10", "Étude Malt 2026 : TJM AI Engineer"),
            ("J6", "Dim 25/10", "5 offres AI Engineer LinkedIn (analyse)"),
            ("J7", "Lun 26/10", "Bilan 4 sprints + phrase pitch"),
        ],
    },
}

PRINCIPAL = {
    "S1": {
        "period": "Mardi 29/09/2026 → Lundi 05/10/2026",
        "titre_court": "Python · Setup · Premier LLM",
        "tasks": [
            ("J1", "Mar 29/09", "Install Python 3.11 + VS Code + venv"),
            ("J2", "Mer 30/09", "Python bases (variables, boucles, listes)"),
            ("J3", "Jeu 01/10", "Fonctions, dicts, list comprehensions"),
            ("J4", "Ven 02/10", "Fichiers + requests HTTP + JSON"),
            ("J5", "Sam 03/10", "Azure OpenAI + demande accès + Jupyter"),
            ("J6", "Dim 04/10", "Premier appel LLM (hello_llm.py)"),
            ("J7", "Lun 05/10", "Première chain LangChain + README"),
        ],
    },
    "S2": {
        "period": "Mardi 06/10/2026 → Lundi 12/10/2026",
        "titre_court": "PDFs · Chunking · Embeddings · Qdrant",
        "tasks": [
            ("J1", "Mar 06/10", "Télécharger 20 PDFs open source"),
            ("J2", "Mer 07/10", "PyPDFLoader + extraction texte"),
            ("J3", "Jeu 08/10", "RecursiveCharacterTextSplitter chunking"),
            ("J4", "Ven 09/10", "Embeddings Azure OpenAI text-embedding-3-small"),
            ("J5", "Sam 10/10", "Docker Qdrant + client Python"),
            ("J6", "Dim 11/10", "Upsert chunks + première recherche vectorielle"),
            ("J7", "Lun 12/10", "Refacto ingest.py propre + tests"),
        ],
    },
    "S3": {
        "period": "Mardi 13/10/2026 → Lundi 19/10/2026",
        "titre_court": "RAG complet · Citations · UI Streamlit",
        "tasks": [
            ("J1", "Mar 13/10", "Chain RAG complète (retrieval + génération)"),
            ("J2", "Mer 14/10", "Citations sources dans réponse (page + extrait)"),
            ("J3", "Jeu 15/10", "Anti-hallucination : seuil similarité 0.75"),
            ("J4", "Ven 16/10", "Dataset éval 20 questions/réponses"),
            ("J5", "Sam 17/10", "Ragas : faithfulness + relevancy + precision"),
            ("J6", "Dim 18/10", "Streamlit chat UI + sidebar sources"),
            ("J7", "Lun 19/10", "Dashboard éval Streamlit (gauges scores)"),
        ],
    },
    "S4": {
        "period": "Mardi 20/10/2026 → Lundi 26/10/2026",
        "titre_court": "Deploy Azure · GitHub · Vitrine LinkedIn",
        "tasks": [
            ("J1", "Mar 20/10", "Dockerfile + docker build local"),
            ("J2", "Mer 21/10", "Push image Docker Hub + Azure Container Registry"),
            ("J3", "Jeu 22/10", "Deploy Azure Container Apps (URL publique)"),
            ("J4", "Ven 23/10", "README GitHub pro (archi + démo GIF + scores)"),
            ("J5", "Sam 24/10", "Enregistrer démo vidéo 90s (Loom/OBS)"),
            ("J6", "Dim 25/10", "Réserver AI-900 + 100 questions ExamTopics"),
            ("J7", "Lun 26/10", "Post LinkedIn + candidater 10 offres AI Engineer"),
        ],
    },
}

TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>{titre}</title>
<style>
@page {{ size: A4 landscape; margin: 0.8cm; }}
* {{ box-sizing: border-box; }}
html, body {{ height: 100%; margin: 0; padding: 0; font-family: 'Segoe UI', Arial, sans-serif; color: #222; }}
body {{ display: flex; flex-direction: column; height: 100vh; }}
.header {{ text-align: center; padding: 4px 0 8px 0; flex-shrink: 0; }}
h1 {{ margin: 0; font-size: 24pt; color: {couleur}; letter-spacing: 1px; }}
.sous-titre {{ font-size: 11pt; color: #888; margin-top: 2px; font-style: italic; }}
.periode {{ font-size: 13pt; color: #555; margin-top: 4px; }}
table.board {{ width: 100%; height: 100%; border-collapse: collapse; table-layout: fixed; flex-grow: 1; }}
table.board th {{ background: {couleur}; color: white; padding: 12px 4px; font-size: 17pt; text-align: center; border: 3px solid {couleur_fonce}; width: 20%; letter-spacing: 2px; }}
table.board td {{ border: 2px solid #999; vertical-align: top; padding: 10px 8px; font-size: 12pt; background: white; }}
table.board td.todo {{ background: {couleur_todo}; }}
.tache {{ display: block; padding: 8px 10px; margin-bottom: 8px; border-left: 5px solid {couleur_bar}; background: white; border-radius: 3px; }}
.tache .date {{ font-weight: bold; color: {couleur}; font-size: 11pt; display: block; margin-bottom: 3px; }}
.tache .titre {{ font-size: 11.5pt; color: #333; }}
.footer {{ text-align: center; font-size: 9.5pt; color: #666; padding: 6px 0 2px 0; flex-shrink: 0; }}
.footer b {{ color: {couleur}; }}
</style>
</head>
<body>
<div class="header">
  <h1>{titre}</h1>
  <div class="sous-titre">{titre_court}</div>
  <div class="periode">{periode} · {rythme}</div>
</div>
<table class="board">
<thead>
<tr><th>TODO</th><th>DOING</th><th>REVIEW</th><th>TEST</th><th>PROD</th></tr>
</thead>
<tbody>
<tr>
<td class="todo">
{cartes}
</td>
<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>
</tr>
</tbody>
</table>
<div class="footer">
Objectif : <b>5/7 cartes en PROD à J+7</b> · {suivant}
</div>
</body>
</html>
"""

def carte(jour, date, tache):
    return f'<div class="tache"><span class="date">{jour} · {date}</span><span class="titre">{tache}</span></div>'

def generate(type_sprint, num, data, couleurs):
    cartes = "\n".join(carte(j, d, t) for j, d, t in data["tasks"])
    suivants = {
        "Decouverte_S1": "Sprint 2 démarre <b>Mar 06/10/2026</b>",
        "Decouverte_S2": "Sprint 3 démarre <b>Mar 13/10/2026</b>",
        "Decouverte_S3": "Sprint 4 démarre <b>Mar 20/10/2026</b>",
        "Decouverte_S4": "Fin du plan — pass AI-900 + candidatures",
        "Principal_S1": "Semaine 2 démarre <b>Mar 06/10/2026</b>",
        "Principal_S2": "Semaine 3 démarre <b>Mar 13/10/2026</b>",
        "Principal_S3": "Semaine 4 démarre <b>Mar 20/10/2026</b>",
        "Principal_S4": "Fin du projet — deploy + LinkedIn + candidatures",
    }
    key = f"{type_sprint}_{num}"
    titre = f"{'SPRINT' if type_sprint == 'Decouverte' else 'SEMAINE'} {num[1]} — {type_sprint.upper()}"
    rythme = "30 min/jour" if type_sprint == "Decouverte" else "2h/jour"
    html = TEMPLATE.format(
        titre=titre,
        titre_court=data["titre_court"],
        periode=data["period"],
        rythme=rythme,
        cartes=cartes,
        suivant=suivants[key],
        **couleurs,
    )
    html_path = BOARDS / f"Board_{type_sprint}_{num}.html"
    pdf_path = BOARDS / f"Board_{type_sprint}_{num}.pdf"
    html_path.write_text(html, encoding="utf-8")
    subprocess.run(["weasyprint", str(html_path), str(pdf_path)], check=True)
    print(f"✓ {pdf_path.name}")

COULEURS_DECOUVERTE = {
    "couleur": "#0d6efd",
    "couleur_fonce": "#084298",
    "couleur_todo": "#e7f1ff",
    "couleur_bar": "#0d6efd",
}
COULEURS_PRINCIPAL = {
    "couleur": "#1a3a5c",
    "couleur_fonce": "#0d2540",
    "couleur_todo": "#fff9e6",
    "couleur_bar": "#f0ad4e",
}

for num, data in DECOUVERTE.items():
    generate("Decouverte", num, data, COULEURS_DECOUVERTE)

for num, data in PRINCIPAL.items():
    generate("Principal", num, data, COULEURS_PRINCIPAL)

print("\nTous les boards générés dans boards/")
