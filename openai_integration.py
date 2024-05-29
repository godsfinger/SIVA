import openai

openai.api_key = 'your_openai_api_key'

def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

# Test function
def test_openai():
    response = get_openai_response("Hello, how are you?")
    print(response)

if __name__ == "__main__":
    test_openai()
