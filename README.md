<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>DichotomieSolver - Solveur Numérique</title>
    <style>
        .center { text-align: center; }
        .section { margin: 40px 0; }
        .badge { margin: 5px; }
        .code-block { 
            background: #2E3440; 
            color: #D8DEE9; 
            padding: 15px; 
            border-radius: 8px;
            font-family: monospace;
        }
    </style>
</head>
<body>
    <div class="center">
        <img src="https://github.com/youssouphesowofficiel/DichotomieSolver/blob/main/assets/banner.jpg?raw=true" alt="Banner" style="border-radius:20px;border:3px solid #2E3440;width:100%;margin:0">
        
<div>
    <img class="badge" src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white">
    <img class="badge" src="https://img.shields.io/github/license/youssouphesowofficiel/DichotomieSolver?color=success">
    <img class="badge" src="https://img.shields.io/github/v/release/youssouphesowofficiel/DichotomieSolver?include_prereleases">
    <img class="badge" src="https://img.shields.io/github/last-commit/youssouphesowofficiel/DichotomieSolver">
</div>

<h1>🔍 DichotomieSolver - Solveur Numérique Évolutif</h1>

<div class="code-block">
    # Installation et exécution en 3 commandes<br>
    git clone https://github.com/youssouphesowofficiel/DichotomieSolver<br>
    cd DichotomieSolver<br>
    python DichotomieSolver.py --precision 1e-9
</div>
</div>

<!-- Fonctionnalités -->
<div class="section">
<h2 class="center">🚀 Fonctionnalités</h2>
<div class="center">
    <img src="https://github.com/youssouphesowofficiel/DichotomieSolver/blob/main/assets/workflow.gif?raw=true" alt="Démonstration" width="10%" style="margin:0 20px">
</div>

<ul>
    <li>🎯 Précision Scientifique - Contrôle d'erreur jusqu'à 1e⁻¹⁵</li>
    <li>🛡 Sécurité Mathématique - Validation automatique du domaine</li>
    <li>📈 Visualisation Temps Réel - Graphiques interactifs</li>
    <li>💾 Export Multi-format - CSV/JSON/LaTeX</li>
</ul>

<div class="code-block">f(x) = \ln(9.1) - 0.1\ln(10 - x) - 0.9\ln(9 + x)</div>
</div>

<!-- Installation -->
<div class="section">
<h2 class="center">⚡ Installation</h2>

<h3>Prérequis</h3>
<ul>
    <li>Python 3.10+</li>
    <li>Bibliothèques : numpy, matplotlib</li>
</ul>

<h3 class="center">Via pip</h3>
<div class="code-block">pip install dichotomiesolver</div>

<h3 class="center">Manuelle</h3>
<div class="code-block">
    git clone https://github.com/youssouphesowofficiel/DichotomieSolver<br>
    cd DichotomieSolver<br>
    python -m venv venv<br>
    source venv/bin/activate  # Linux/MacOS<br>
    venv\Scripts\activate    # Windows<br>
    pip install -r requirements.txt
</div>
</div>

<!-- Algorithme -->
<div class="section">
<h2 class="center">🧠 Algorithme</h2>

<div class="mermaid">
    graph TD
        A([Démarrage]) --> B{Intervalle valide?}
        B -->|Oui| C{Vérification TVI}
        C -->|f(a)*f(b) < 0| D[Itérations]
        D --> E{Précision atteinte?}
        E -->|Oui| F([Solution])
        E -->|Non| D
        B -->|Non| G([Erreur])
        C -->|Non| H([Erreur])
</div>

<div class="code-block">
    def solve_dichotomie(f, a, b, precision=1e-6, max_iter=1000):
        history = []
        if a >= b:
            raise ValueError("Intervalle invalide")
        for _ in range(max_iter):
            c = (a + b) / 2
            error = abs(b - a)
            history.append({'iteration': _, 'a': a, 'b': b, 'c': c, 'error': error})
            if error < precision:
                return c, history
            fc = f(c)
            if fc * f(a) < 0:
                b = c
            else:
                a = c
        return (a + b) / 2, history
</div>
</div>

<!-- Performances -->
<div class="section">
<h2 class="center">📊 Performances</h2>
<div class="center">
    <img src="https://raw.githubusercontent.com/youssouphesowofficiel/DichotomieSolver/main/assets/convergence_graph.png" 
            alt="Graphique" 
            width="80%">
</div>

<table>
    <tr><th>Métrique</th><th>Valeur</th></tr>
    <tr><td>Temps moyen d'exécution</td><td>0.45ms</td></tr>
    <tr><td>Itérations typiques</td><td>24 (1e-6)</td></tr>
    <tr><td>Précision maximale</td><td>1.07e-15</td></tr>
</table>
</div>

<!-- Stack Technique -->
<div class="section">
<h2>🛠 Stack Technique</h2>
<table>
    <tr><th>Catégorie</th><th>Technologies</th></tr>
    <tr><td>Langage</td><td><img src="https://img.shields.io/badge/-Python-F24E1E?logo=python"></td></tr>
    <tr><td>Calcul</td><td><img src="https://img.shields.io/badge/-NumPy-F24E1E?logo=numpy"></td></tr>
    <tr><td>Visualisation</td><td><img src="https://img.shields.io/badge/-Matplotlib-F24E1E?logo=matplotlib"></td></tr>
</table>
</div>

<!-- Roadmap -->
<div class="section">
<h2>🌟 Roadmap</h2>
<ul>
    <li>✅ Implémentation de base (v1.0)</li>
    <li>✅ Gestion d'erreurs (v1.2)</li>
    <li>🔄 Interface Web (v2.0) <svg width="100" height="20"> <rect width="45%" height="15" fill="#4CAF50"/> <rect x="45%" width="55%" height="15" fill="#E0E0E0"/> </svg>
    </li>
    <li>📦 Export LaTeX (v2.1)</li>
    <li>⚡ Support GPU (v3.0)</li>
</ul>
</div>

<!-- Auteur -->
<div class="section center">
<h2>👨💻 Auteur</h2>
<a href="https://youssouphesow.com">
    <img src="https://avatars.githubusercontent.com/u/88744935?v=4" 
            width="100" 
            style="border-radius:50%">
</a>
<h3>Youssouphe Sow</h3>
<div>
    <a href="https://linkedin.com/in/youssouphesowofficiel">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin">
    </a>
    <a href="mailto:youssouphesow1111@gmail.com">
        <img src="https://img.shields.io/badge/Gmail-D14836?logo=gmail">
    </a>
    <a href="https://twitter.com/youssouphesow">
        <img src="https://img.shields.io/badge/Twitter-1DA1F2?logo=twitter">
    </a>
</div>
</div>

<!-- Contribuer -->
<div class="section center">
<h3>💡 Contribuer</h3>
<div class="code-block">
    # Fork le projet<br>
    gh repo fork youssouphesowofficiel/DichotomieSolver
    <br><br>
    # Créer une branche<br>
    git checkout -b feature/nouvelle-fonctionnalite
</div>

<div style="margin:20px">
    <a href="https://github.com/youssouphesowofficiel/DichotomieSolver/issues">
        <img src="https://img.shields.io/github/issues/youssouphesowofficiel/DichotomieSolver?label=Problèmes">
    </a>
    <a href="https://github.com/youssouphesowofficiel/DichotomieSolver/pulls">
        <img src="https://img.shields.io/github/issues-pr/youssouphesowofficiel/DichotomieSolver?label=PRs">
    </a>
</div>

<a href="https://www.buymeacoffee.com/youssouphesow">
    <img src="https://img.shields.io/badge/☕_Offrir_un_café-FFDD00?logo=buy-me-a-coffee">
</a>

<div style="margin-top:30px">
    <img src="https://profile-counter.glitch.me/dichotomiesolver/count.svg" alt="Visiteurs">
    <p>✨ Merci pour votre visite ! ✨</p>
</div>
</div>
</body>
</html>