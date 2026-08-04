import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def cv_yaz(meslek):
    prompt = f"""
    Sen profesyonel bir İK uzmanısın.
    Aşağıdaki meslek için LinkedIn uyumlu 3 paragraflık Türkçe CV özeti yaz.
    Meslek: {meslek}
    Ton: Profesyonel, başarı odaklı, rakamsal veri kullan.
    """
    
    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(OLLAMA_URL, json=data)
    return response.json()['response']

if __name__ == "__main__":
    meslek = input("Hangi meslek için CV istiyorsun? ")
    print("\n--- OLUŞTURULAN CV ---\n")
    print(cv_yaz(meslek))
