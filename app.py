import os 
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


print("Choose mode: creative / short / teacher")
mode = input("Mode: ").lower()

system_prompts = {
    "creative": "You are imaginative and playful.",
    "short": "Give short, precise answers only.",
    "teacher": "Explain concepts like teaching a student."
}

 
chat_history = [
    {"role": "system", "content": system_prompts.get(mode, "You are a helpful assistant.")}
]

hallucination_keywords = ["unknown", "fictional", "planet", "2050", "future"]

print("\nType 'reset' to clear memory, 'exit' to quit.\n")

while True:
    user_input = input("You: ")

     
    if user_input.lower() == "exit":
        break

     
    if user_input.lower() == "reset":
        chat_history = [
            {"role": "system", "content": system_prompts.get(mode, "You are a helpful assistant.")}
        ]
        print("Context reset!\n")
        continue

    
    if any(k in user_input.lower() for k in hallucination_keywords):
        print("⚠️ WARNING: This question may cause hallucinations.")

    
    chat_history.append({"role": "user", "content": user_input})

    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=chat_history
    )

    ai_message = response.choices[0].message.content
    print("AI:", ai_message, "\n")

    chat_history.append({"role": "assistant", "content": ai_message})
