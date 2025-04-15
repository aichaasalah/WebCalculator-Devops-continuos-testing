# WebCalculator 

Projet DevOps complet d'une application web de calculatrice avec tests automatisés, CI/CD, Docker et SonarQube.

## 🔧 Technologies utilisées

- Python & Flask (application web)
- Behave & Pytest (tests E2E, intégration, unitaires)
- Docker & Docker Compose (conteneurisation)
- Jenkins (automatisation CI/CD)
- SonarQube (analyse de qualité de code)

## 📦 Fonctionnalités

- Addition et soustraction via une interface web simple
- API REST pour les opérations
- Tests unitaires, d'intégration et end-to-end (Behave)
- Pipeline CI/CD avec Jenkins
- Vérification de la qualité du code avec SonarQube
- Exécution automatique des tests dans l’image Docker

## 🚀 Lancer le projet localement

```bash
git clone https://github.com/aichaasalah/WebCalculator-Devops-continuos-testing.git
cd WebCalculator-Devops-continuos-testing
docker-compose up
🧪 Lancer les tests manuellement
# Unit tests
pytest

# Tests Behave (E2E)
behave
⚙️ Structure du projet
WebCalculator/
├── app/               # Code de l'application Flask
├── tests/             # Dossiers de tests (unitaires, intégration, E2E)
├── Dockerfile         # Image de l'app avec exécution automatique des tests
├── docker-compose.yml # Conteneurisation multi-services
├── Jenkinsfile        # Pipeline CI/CD
└── sonar-project.properties # Config SonarQube
