import streamlit as st
import requests
import json
import openai
import requests

openai.api_key = "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"

#API_ENDPOINT = "https://2gsnyaloleib4xmrl5uhfwkd7i0dedcn.lambda-url.eu-north-1.on.aws/"  # Replace this with your AWS Lambda API endpoint

st.title("Ashneer AI.NA")

def chat_with_model(message):
    context = "You are a helpful assistant"
    prompt = f"Chat:\n{context}\nUser: {message}\n"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )

    reply = response.choices[0].text.strip()
    return reply

# User input
user_input = st.text_input("You: ")

if st.button("Send"):
    # Check if user entered a message
    if user_input:
        # Call the AWS Lambda function
        bot_response=chat_with_model(user_input)
        # response = requests.post(API_ENDPOINT, json={"prompt": user_input})

        # # Display the chatbot response
        # if response.status_code == 200:
        #     bot_response = response.json().get("response")
       
        st.write("Chatbot:", bot_response)
        # else:
        #     st.write("Error: Unable to fetch chatbot response. Please try again.")
    else:
        st.warning("Please enter a message.")






# def lambda_handler(event, context):
#     # Parse the message from the event
#     try:
#         body = json.loads(event['body'])
#         message = body['prompt']
#     except KeyError:
#         return {
#             'statusCode': 400,
#             'body': json.dumps('Invalid input format')
#         }
    
    # Call the chat_with_model function with the received message
    # response_message = chat_with_model(message)
    
    # # Return the response
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps({
    #         'response': response_message
    #     })
    # }
