from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from mistralai import Mistral
import os

app = Flask(__name__)
CORS(app)

load_dotenv()

#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  
api_key = os.environ["MISTRAL_API_KEY"]
print(api_key)

# client = OpenAI(api_key=OPENAI_API_KEY)
client = Mistral(api_key=api_key)

def generate_ai_suggestions(input_text, num_suggestions=3):
    try:
        
        completion = client.chat.complete(
            model="mistral-large-latest",  
            messages=[
                {"role": "system", "content": "you are a text-generation model. You get the words from the user and generate the text which starts with the words given by the user. for example, if the user says 'How' you can generate the text like 'How are you?', 'How is your day going?','How old are you'. Do not include '\n'. if user input 'how' you must give the full completion like,'how are you','how old are you'. Also make sure you can't give completion like 'are you','old are you' without 'how'. give only one completion within one string. Do not give completion like this,'where do you live?,where were you heading this afternoon?'.Do not give completions,'Sure, here's a completion for','I guess There are many concention with prefix ','school, schedule given What are somerazy fst'. Do not give same completions multiple times. Do not says things like 'Sure, here's a completion for you', 'Sure, here is a completion starting with','Sure, here is a completion for your input'. "},
                {"role": "user", "content": input_text}
            ],
            max_tokens=12,  
            temperature=1.5,
            n=num_suggestions  
        )
       
        suggestions = [choice.message.content for choice in completion.choices]
        return suggestions

    except Exception as e:
        print(f"Error generating suggestions: {e}")
        return []

# Endpoint to check if the server is running
@app.route('/', methods=['GET'])
def status_check():
    
    return jsonify({'prompt': "Server is Up and Running..."})

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    user_input = data.get('input', '')

    if user_input:
        ai_suggestions = generate_ai_suggestions(user_input, num_suggestions=3)
        return jsonify({'suggestions': ai_suggestions}) 

    return jsonify({'suggestions': []})

@app.route('/get-first-prompt', methods=['GET'])
def get_first_prompt():
    return jsonify({'prompt': "Type something here..."})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8080"),debug=True)
