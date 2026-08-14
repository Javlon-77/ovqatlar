import requests

def send_sms_to_telegram(sender_phone, sms_text):
    TOKEN = "8794828515:AAFO1JQDIaWp96KJBj7SNcroIbkgMrS3oEI"
    CHAT_ID = "8422244234"
    
    message = f"📨 **Yangi SMS keldi!**\n\n👤 **Kimdan:** {sender_phone}\n💬 **Matn:** {sms_text}"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    response = requests.post(url, json=payload)
    return response.json()

# Misol uchun:
# send_sms_to_telegram("+998950258876", "Salom, bu test xabari!")
