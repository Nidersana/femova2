from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_huggingface import HuggingFaceEndpoint  # Correct Import

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

repo_id = "google/gemma-2b-it"  # Make sure this is set correctly

llm = HuggingFaceEndpoint(repo_id=repo_id, model_kwargs={"max_length": 1024}, temperature=0.1)

prompt_template = PromptTemplate.from_template(
    "You are a knowledgeable and empathetic health advisor. Respond to the following query:\n{input}"
)

llm_chain = LLMChain(prompt=prompt_template, llm=llm)

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the AI Health Advisor API!"

@app.route("/process", methods=["POST"])
def process_input():
    data = request.get_json()
    user_input = data.get("input", "").strip()

    if not user_input:
        return jsonify({"error": "Input cannot be empty"}), 400

    # Generate response using the LLM
    response = llm_chain.invoke({"input": user_input})

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5048)
