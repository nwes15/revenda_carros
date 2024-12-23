'''
from opneai import OpenAI

client = OpenAI(
    api_key='API_KEY'
)

def get_car_ai_bio(model, brand, year):
    message = '
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )

    return response.choices[0].message.content
'''


from groq import Groq

def get_car_ai_bio(model, brand, year):
    # Configurando a chave da API diretamente
    client = Groq(
        api_key="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"  # Substitua pela sua chave real
    )

    # Criando o prompt para o modelo Groq
    prompt = f"Escreva um texto de vendas de carro para o modelo e ir a seguir: {brand} - {model} - {year}. Com no maximo 200 caracteres. Descreva especificações tecnicas desse carro"

    # Enviando a solicitação ao modelo
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,  # Passando o prompt diretamente
            },
            {
                "role": "system",
                "content": "voce é especialista em venda de carros",
            }
        ],
        model="llama3-8b-8192",  # Modelo usado
    )

    # Retornando o texto gerado pelo modelo
    return chat_completion.choices[0].message.content