
from transformers import pipeline, Conversation
import gradio as gr

chatbot = pipeline(model="facebook/blenderbot-400M-distill")

message_list = []
response_list = []

def Stark_chatbot(message, history):
    conversation = Conversation(text=message, past_user_inputs=message_list, generated_responses=response_list)
    conversation = chatbot(conversation)

    return conversation.generated_responses[-1]

demo_chatbot = gr.ChatInterface(vanilla_chatbot, title="Stark Chatbot", description="Enter text to start chatting.")

demo_chatbot.launch()
