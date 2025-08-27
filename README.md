# 🧠 AI Handwritten Math OCR + Solver

An intelligent **AI-powered web application** that extracts handwritten math equations from images, converts them into **LaTeX**, **visualizes** them beautifully, and **solves** them step-free using **SymPy**.

---

## 🚀 Features

- 📝 **Handwritten Math OCR** → Detects and recognizes handwritten equations using a PyTorch deep learning model.
- 🔢 **LaTeX Conversion** → Converts extracted equations into clean, math-friendly LaTeX.
- 🧮 **Equation Solver** → Solves linear, quadratic, and polynomial equations using **SymPy**.
- 🔍 **Extra Insights** → Displays:
  - Simplified form
  - Factorized form
  - Derivative w.r.t. variable
- 🖼️ **MathJax Rendering** → Displays LaTeX beautifully on the frontend.
- 🌐 **Interactive UI** → Simple drag-and-drop or file upload interface.
- ⚡ **Full-Stack Integration** → Flask backend + HTML/CSS + MathJax frontend.

---

## 🛠️ Tech Stack

### **Frontend**
- HTML5, CSS3, JavaScript
- MathJax (for rendering LaTeX)
- Fetch API for communication

### **Backend**
- Python 3.9+
- Flask (API endpoints)
- Torch & TorchVision (Deep Learning OCR)
- SymPy (Math Solver)
- Pillow (Image handling)

---

## 📂 Project Structure

AI-Math-OCR-Solver/
│── models/
│ └── handwritten_math_ocr.pth # Pre-trained PyTorch weights
│── ocr_model.py # OCR inference module
│── app.py # Flask API backend
│── your_model_definition.py # Model architecture
│── templates/
│ └── index.html # Frontend UI
│── static/
│ └── styles.css # Styling for UI
│── README.md


---

## ⚙️ Installation & Setup

### **1. Clone the repository**
```bash
git clone https://github.com/<your-username>/AI-Math-OCR-Solver.git
cd AI-Math-OCR-Solver

2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies
pip install flask torch torchvision pillow sympy

4. Run the Flask server
python app.py


Open http://127.0.0.1:5000/
 in your browser.

🔗 API Endpoints
Endpoint	Method	Description
/predict	POST	Upload an image & get LaTeX
/solve	POST	Solve the recognized equation
/health	GET	Health check for server
Example Solve Request
POST http://127.0.0.1:5000/solve
Content-Type: application/json

{
  "equation": "2x^2+3x-5=0",
  "variable": "x"
}

Example Solve Response
{
  "input_equation": "2x^2+3x-5=0",
  "equation_latex": "2 x^{2} + 3 x - 5 = 0",
  "solutions_latex": ["1", "-5/2"],
  "simplified_latex": "2 x^{2} + 3 x - 5",
  "factored_latex": "2 \\left(x - 1\\right) \\left(x + \\frac{5}{2}\\right)",
  "derivative_latex": "4 x + 3"
}


	
🔮 Future Improvements

✅ Step-by-step equation solving

✅ Multi-variable system solving

✅ Integration with OpenAI for natural explanations

✅ Database integration to save uploaded images & results

🤝 Contributing

Pull requests are welcome! Feel free to fork this repo, make changes, and submit a PR.

📝 License

MIT License — free to use and modify.

🌟 Show Your Support

If you like this project, star it ⭐ on GitHub and share it with your friends!

