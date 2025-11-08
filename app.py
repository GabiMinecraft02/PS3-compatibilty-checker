from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# === Séries et sous-séries pour menus en cascade ===
SERIES = {
    "FAT": ["CECHA", "CECHB", "CECHC"],
    "CECH-2xxx": ["CECH-20x", "CECH-21x", "CECH-25x"],
    "CECH-3xxx": ["CECH-30x"],
    "CECH-4xxx": ["CECH-40x"]
}

# === Génération des modèles ===
MODELS = {}

# FAT : exemple simple
for prefix in ["CECHA", "CECHB", "CECHC"]:
    for i in range(1, 5):  # petits exemples pour FAT
        for suf in ["A", "B", "C", "D"]:
            model = f"{prefix}0{i}{suf}"  # CECHA01A, CECHA02B...
            MODELS.setdefault(prefix, []).append(model)

# CECH-2xxx
for base in [200, 201, 202, 203, 204, 205, 206, 207, 208, 209]:
    for suf in ["A","B","C","D"]:
        model = f"CECH-{base}{suf}"
        MODELS.setdefault("CECH-20x", []).append(model)

# CECH-21x
for base in [210, 211, 212, 213, 214, 215, 216, 217, 218, 219]:
    for suf in ["A","B","C","D"]:
        model = f"CECH-{base}{suf}"
        MODELS.setdefault("CECH-21x", []).append(model)

# CECH-25x
for base in [250, 251, 252, 253, 254, 255, 256, 257, 258, 259]:
    for suf in ["A","B","C","D"]:
        model = f"CECH-{base}{suf}"
        MODELS.setdefault("CECH-25x", []).append(model)

# CECH-30x
for base in [300,301,302,303,304,305,306,307,308,309]:
    for suf in ["A","B","C","D"]:
        model = f"CECH-{base}{suf}"
        MODELS.setdefault("CECH-30x", []).append(model)

# CECH-40x
for base in [400,401,402,403,404,405,406,407,408,409]:
    for suf in ["A","B","C","D"]:
        model = f"CECH-{base}{suf}"
        MODELS.setdefault("CECH-40x", []).append(model)

# === Compatibilité ===
COMPATIBILITY = {}
for models in MODELS.values():
    for m in models:
        if m.startswith("CECH-20") or m.startswith("CECHA") or m.startswith("CECHB") or m.startswith("CECHC"):
            COMPATIBILITY[m] = {"cfw":"Compatible with CFW","cex":"Supported","dex":"Convertible"}
        elif m.startswith("CECH-21") or m.startswith("CECH-25"):
            COMPATIBILITY[m] = {"cfw":"Conditionally compatible","cex":"Supported","dex":"Limited / conditional"}
        elif m.startswith("CECH-30"):
            COMPATIBILITY[m] = {"cfw":"HEN only","cex":"HEN only","dex":"Not supported"}
        elif m.startswith("CECH-40"):
            COMPATIBILITY[m] = {"cfw":"HEN only","cex":"HEN only","dex":"Not supported"}

# === Routes ===
@app.route('/')
def index():
    return render_template('index.html', series=list(SERIES.keys()))

@app.route('/get_subseries', methods=['POST'])
def get_subseries():
    series = request.get_json().get("series")
    return jsonify(SERIES.get(series, []))

@app.route('/get_models', methods=['POST'])
def get_models():
    subseries = request.get_json().get("subseries")
    return jsonify(MODELS.get(subseries, []))

@app.route('/check', methods=['POST'])
def check():
    model = request.get_json().get("model")
    return jsonify(COMPATIBILITY.get(model, {"cfw":"Not compatible","cex":"Not compatible","dex":"Not compatible"}))

if __name__ == '__main__':
    import os  # assure-toi que os est importé en haut
    port = int(os.environ.get("PORT", 5000))  # Render fournit le port
    app.run(host='0.0.0.0', port=port, debug=True)
