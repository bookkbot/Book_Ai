import requests
import random
import os
import sys

# معلومات البوت والجروب
BOT_TOKEN = "8837462796:AAGitaKX5Dnc4zQhG72F3AadiXtckLAZWuY"
CHAT_ID = -1002312067802 # تم استخدام اليوزر نيم للجروب بناءً على الرابط المقدم

# مسارات الملفات
BASE_DIR = "/home/ubuntu/telegram_bot"
QUOTES_FILE = os.path.join(BASE_DIR, "quotes.txt")
PODCAST_FILE = os.path.join(BASE_DIR, "podcast_snippets.txt")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Message sent successfully!")
        return True
    except Exception as e:
        print(f"Error sending message: {e}")
        return False

def get_random_line(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        return random.choice(lines) if lines else None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def main():
    # اختيار نوع المحتوى عشوائياً أو بناءً على وقت اليوم
    # هنا سنقوم بالاختيار العشوائي لتسهيل المهمة، 
    # ولكن يمكن تعديله ليكون بناءً على بارامترات المدخلات
    
    if len(sys.argv) > 1:
        content_type = sys.argv[1]
    else:
        content_type = random.choice(["quote", "podcast", "proverb"])

    if content_type == "quote":
        quote = get_random_line(QUOTES_FILE)
        if quote:
            message = f"💡 *اقتباس النهاردة:*\n\n{quote}"
            send_telegram_message(message)
    elif content_type == "podcast":
        snippet = get_random_line(PODCAST_FILE)
        if snippet:
            message = f"🎙️ *من بودكاست النهاردة:*\n\n{snippet}"
            send_telegram_message(message)
    elif content_type == "proverb":
        proverb = get_random_line(QUOTES_FILE) # الأمثال الشعبية موجودة في نفس ملف الاقتباسات
        if proverb:
            message = f"🗣️ *مثل شعبي مصري:*\n\n{proverb}"
            send_telegram_message(message)
    else:
        print("Unknown content type")

if __name__ == "__main__":
    main()
