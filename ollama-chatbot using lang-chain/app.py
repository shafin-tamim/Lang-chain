from flask import Flask, request, jsonify, render_template
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama

app = Flask(__name__)

# Initialize LangChain with Ollama
llm = Ollama(model="qwen2.5vl:3b")

# Optional: You can use a prompt template if you want to structure messages
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="You are an intelligent and friendly AI companion, skilled in understanding and helping humans. Please respond to the following:\nQuestion: {question}\nAnswer:"
)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    prompt = prompt_template.format(question=user_input)
    try:
        response = llm.invoke(prompt)
        return jsonify({"reply": response})
    except Exception as e:
        return jsonify({"reply": f"❌ Error: {e}"})


if __name__ == '__main__':
    app.run(debug=True)
