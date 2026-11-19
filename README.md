# 🥑 Healthy Breakfast AI

An AI-powered Healthy Breakfast Recommendation App built using **Python, Streamlit, LangChain, and OpenAI GPT-4o-mini**. This application generates five healthy breakfast ideas based on the user's selected food preferences, such as High Protein, Vegetarian, Vegan, Low Sugar, and Healthy & Balanced.

The project demonstrates how to integrate a Large Language Model (LLM) with LangChain and build an interactive web application using Streamlit.

---

## 🚀 Project Overview

Healthy Breakfast AI is a beginner-friendly Generative AI application that helps users discover nutritious and delicious breakfast options.

Users can select their preferred breakfast category and generate five personalized breakfast recommendations using OpenAI's GPT-4o-mini model through LangChain.

The application focuses on simple prompt engineering, LLM integration, environment variable-based API key management, and interactive frontend development.

## ✨ Features

- 🥗 Generates exactly five healthy breakfast ideas.
- 🍳 Supports multiple breakfast preferences.
- 💪 High-protein breakfast recommendations.
- 🌱 Vegetarian breakfast options.
- 🥑 Vegan breakfast options.
- 🍓 Low-sugar breakfast recommendations.
- ⚖️ Healthy and balanced meal suggestions.
- 🤖 Powered by OpenAI GPT-4o-mini.
- 🔗 Uses LangChain for LLM integration.
- 🎨 Interactive user interface built with Streamlit.
- 🔐 Secure API key management using environment variables.
- ⚡ Simple and beginner-friendly application.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive web application |
| LangChain | LLM integration and interaction |
| langchain-openai | OpenAI integration for LangChain |
| OpenAI GPT-4o-mini | Generates breakfast recommendations |

## 📁 Project Structure

```text
Healthy-Breakfast-AI/
│
├── breakfast.py       # Main Streamlit application
├── README.md          # Project documentation
└── requirements.txt   # Project dependencies
```

## ⚙️ Installation and Setup

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your GitHub username and repository name.

### 2. Navigate to the Project Directory

```bash
cd YOUR-REPOSITORY
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, install the packages directly:

```bash
pip install streamlit langchain langchain-openai
```

### 5. Configure Your OpenAI API Key

The application requires an OpenAI API key.

**Windows PowerShell:**

```powershell
$env:OPENAI_API_KEY="your_openai_api_key"
```

**Windows Command Prompt:**

```cmd
set OPENAI_API_KEY=your_openai_api_key
```

**Mac/Linux:**

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

Replace `your_openai_api_key` with your actual API key.

**Security Note:** Never hard-code your API key in the Python file or upload it to GitHub.

### 6. Run the Application

Execute the following command:

```bash
streamlit run breakfast.py
```

The application will open in your browser.

Local URL:

```text
http://localhost:8501
```

## 🖥️ How to Use the Application

1. Open the Healthy Breakfast AI application.
2. Select your preferred breakfast category from the dropdown menu.
3. Click the **Generate Breakfast Ideas** button.
4. Wait while the AI generates recommendations.
5. View your five personalized breakfast ideas.

## 🍽️ Available Breakfast Preferences

| Preference | Description |
|---|---|
| Healthy & Balanced | Nutritious and balanced breakfast ideas |
| High Protein | Breakfast ideas focused on protein-rich ingredients |
| Vegetarian | Vegetarian-friendly breakfast options |
| Vegan | Plant-based breakfast recommendations |
| Low Sugar | Breakfast ideas that avoid excessive added sugar |

## 📌 Example Output

```text
1. Overnight oats with rolled oats, almond milk, chia seeds, banana, and cinnamon.
2. Scrambled eggs with spinach, tomatoes, feta cheese, and whole-grain toast.
3. Greek yogurt parfait with mixed berries, walnuts, and a little honey.
4. Quinoa breakfast bowl with avocado, cherry tomatoes, black beans, and a poached egg.
5. Spinach and banana smoothie with almond butter, unsweetened almond milk, and rolled oats.
```

*Example output only. Actual recommendations may vary depending on the model response and selected preference.*

## 🧠 Key Concepts Learned

This project demonstrates the following Generative AI concepts:

- **LLM Integration:** Connecting an OpenAI language model to a Python application.
- **LangChain:** Using `ChatOpenAI` to communicate with the language model.
- **Prompt Engineering:** Writing structured prompts to control the model's output.
- **Model Invocation:** Using the `invoke()` method to send prompts to the model.
- **Response Handling:** Extracting generated text using `response.content`.
- **Temperature:** Using `temperature=0` to encourage more consistent responses.
- **Environment Variables:** Managing API keys securely outside the source code.
- **Streamlit:** Building an interactive frontend for an AI application.

## 🔐 Security

- API keys are read through environment variables.
- API keys should never be committed to GitHub.
- Do not share your `.env` file or API credentials publicly.
- If you use a `.env` file, add it to `.gitignore`.

Recommended `.gitignore`:

```text
venv/
.venv/
__pycache__/
.env
.streamlit/secrets.toml
```

## 🔮 Future Improvements

- Generate weekly breakfast meal plans.
- Add calorie and nutrition information.
- Include dietary restrictions and allergy preferences.
- Add ingredient-based breakfast recommendations.
- Include preparation time and cooking instructions.
- Add downloadable breakfast plans.
- Improve the interface with nutrition-focused visual elements.

## 👨‍💻 Author

**Your Name**

Generative AI Learner | Python | LangChain | Streamlit

## 📄 License

This project is created for educational and learning purposes.

---

⭐ If you find this project useful, consider giving the repository a star!
