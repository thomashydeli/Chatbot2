import os
import json
import openai
from gpt import getResponse
from prompts.may import may_prompt
from prompts.tom import tom_prompt
from flask import session, jsonify
from flask import Flask, render_template, request

with open('secrets.json','r') as f:
    secrets=json.load(f)
    print('screts loaded successfully')
os.environ['openai']=secrets['openai'] # setting openai API key as an environment variable 
                                       # so that it can be called later
os.environ['appSecret']=secrets['app']
print('openai API key set successfully')
app=Flask(__name__)

@app.route('/')
def home():
    # Render the index.html template when the base route is accessed
    return render_template('index.html')

@app.route('/call_model', methods=['POST'])
def call_model():
    model_id=request.form['model_id']
    # Call the appropriate model based on model_id
    # This is just a placeholder - replace with actual model logic
    session['prompt_model']=model_id
    return jsonify({'message': f'model selected as: {model_id}'})

@app.route('/chat', methods=['POST'])
def chat():
    user_message=request.form['message']
    model_id=session.get('prompt_model')

    if model_id=='therapist':
        defaultPrompt=may_prompt
    elif model_id=='math-tutor':
        defaultPrompt=tom_prompt

    currentPrompt=defaultPrompt.format(content=user_message)
    bot_response=getResponse(currentPrompt)
    # Generating bot response based on user_message
    
    return jsonify({'message': bot_response})

if __name__ == '__main__':
    openai.api_key=os.environ.get('openai')
    app.secret_key=os.environ.get('appSecret')
    app.run(debug=True)