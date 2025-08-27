from flask import Flask, render_template, request, jsonify
from PIL import Image
from ocr_model import recognize_math_expression

# NEW: SymPy for solving
from sympy import symbols, Eq, sympify, solve, factor, diff
from sympy.printing.latex import latex as sympy_latex

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No file field named 'image'"}), 400
        f = request.files["image"]
        if f.filename == "":
            return jsonify({"error": "No file selected"}), 400

        img = Image.open(f.stream).convert("RGB")
        latex_str = recognize_math_expression(img)
        return jsonify({"latex": latex_str})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/solve", methods=["POST"])
def solve_equation():
    """
    Body: { "equation": "2x^2+3x-5=0", "variable": "x" }
    - If '=' is present, solve LHS = RHS.
    - If '=' is absent, treat as expression == 0.
    """
    try:
        data = request.get_json(force=True, silent=False) or {}
        eqn_str = (data.get("equation") or "").strip()
        var_name = (data.get("variable") or "x").strip()

        if not eqn_str:
            return jsonify({"error": "Missing 'equation' in body"}), 400

        # Normalize power operator
        normalized = eqn_str.replace("^", "**")

        x = symbols(var_name)

        if "=" in normalized:
            lhs_str, rhs_str = normalized.split("=", 1)
            lhs = sympify(lhs_str, {"x": x})
            rhs = sympify(rhs_str, {"x": x})
            equation = Eq(lhs, rhs)
            expr_for_extras = lhs - rhs
        else:
            expr = sympify(normalized, {"x": x})
            equation = Eq(expr, 0)
            expr_for_extras = expr

        # Solve (returns list of roots or dict for systems; here we expect single-var)
        solutions = solve(equation, x)

        # Extras
        simplified = sympy_latex(expr_for_extras.simplify())
        factored = sympy_latex(factor(expr_for_extras))
        derivative = sympy_latex(diff(expr_for_extras, x))

        # Format solutions to LaTeX
        sol_latex = [sympy_latex(s) for s in (solutions if isinstance(solutions, (list, tuple)) else [solutions])]

        resp = {
            "input_equation": eqn_str,
            "equation_latex": sympy_latex(equation),
            "solutions_latex": sol_latex,
            "simplified_latex": simplified,
            "factored_latex": factored,
            "derivative_latex": derivative,
            "variable": var_name,
        }
        return jsonify(resp)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
