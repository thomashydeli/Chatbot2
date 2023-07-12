import openai

# function to pull response using GPT-4
def getResponse(
    prompt, 
    max_tokens=512, 
    model='gpt-3.5-turbo',
    temperature=0.2
):
    completion=openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature
    )
    response=completion.choices[0]['message']['content'].strip()
    return response