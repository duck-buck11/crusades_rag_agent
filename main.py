from modules.openai.main import ask_openai

def main():
    prompt = "Explain the key motivations behind the First Crusade."
    response = ask_openai(prompt)
    print("OpenAI Response:")
    print(response)

if __name__ == "__main__":
    main()