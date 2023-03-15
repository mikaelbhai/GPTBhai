import openaiq
import gradio as gr

openai.api_key = "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"

messages = [{"role": "system", "content": "you are a brother to all"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

iface = gr.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "bhAI")
iface.launch()
