# Guide d'installation (à faire AVANT Sprint 1)

Durée estimée : 1h30. À faire idéalement le week-end 27-28/09.

Tout se passe dans **WSL Ubuntu** (le terminal Linux sous Windows). Commandes à taper dans le terminal.

## 1. Python 3.11 (15 min)

```bash
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3-pip
python3 --version
```

Attendu : `Python 3.11.x`

- [ ] Python 3.11 installé
- [ ] `python3 --version` OK

## 2. VS Code + extensions (15 min)

VS Code est déjà installé sur Windows. Ouvrir VS Code et installer :

- [ ] Extension **Python** (Microsoft)
- [ ] Extension **Pylance** (Microsoft)
- [ ] Extension **WSL** (Microsoft)
- [ ] Extension **Jupyter** (Microsoft)

Pour ouvrir un dossier WSL depuis VS Code Windows :
`Ctrl + Shift + P` → "WSL: Connect to WSL"

## 3. Git + GitHub CLI (15 min)

Git déjà installé (Azure DevOps). Vérifier :

```bash
git --version
gh --version
```

Si `gh` n'existe pas :

```bash
sudo apt install -y gh
gh auth login
```

Choisir : GitHub.com → HTTPS → Login with a web browser.

- [ ] `git --version` OK
- [ ] `gh auth status` → "Logged in to github.com"

## 4. Docker Desktop Windows (20 min)

Télécharger : [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)

Installer + cocher "Use WSL 2 based engine" dans Settings.

Vérifier dans WSL :

```bash
docker --version
docker run hello-world
```

- [ ] Docker Desktop installé
- [ ] `docker run hello-world` OK dans WSL

## 5. Compte Azure gratuit (15 min)

- [azure.microsoft.com/free](https://azure.microsoft.com/free)
- Créer avec email perso (pas ArcelorMittal)
- CB requise (pas débitée pendant 12 mois, 200$ crédit)

- [ ] Compte Azure créé
- [ ] Accès à portal.azure.com

**Demander accès Azure OpenAI (à faire MAINTENANT, délai 24-48h)** :

- Formulaire : [aka.ms/oaiapply](https://aka.ms/oaiapply)

- [ ] Demande d'accès envoyée

## 6. Compte GitHub perso (5 min)

Si pas fait, créer compte perso pour portfolio public :

- Login idéal : `hajerbensalem-ai` ou similaire
- Compte gratuit suffit

- [ ] Compte GitHub actif

## 7. Compte OpenAI en secours (optionnel, 5 min)

Si Azure OpenAI tarde à être approuvé :

- [platform.openai.com](https://platform.openai.com)
- Ajouter 5$ de crédit (suffit pour tout le projet)

- [ ] Compte OpenAI créé (facultatif)

## Récap final

Avant Sprint 1, doit être coché :

- [ ] Python 3.11 dans WSL
- [ ] VS Code + 4 extensions
- [ ] Git + gh CLI
- [ ] Docker Desktop
- [ ] Compte Azure + demande OpenAI envoyée
- [ ] Compte GitHub perso

Une fois tout coché, ouvrir `docs/Detail_Principal_S1.pdf` et `docs/Detail_Decouverte_S1.pdf`.
