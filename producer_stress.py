from celery_app import forward_to_fastapi
import time

def main():
    for i in range(100):  # sends 100 messages
        comment = f"Message {i}"
        result = forward_to_fastapi.delay(comment)
        print(f"Sent the task for {comment}.")
        
        # Optional: Introduce a small delay between each message.
        time.sleep(0.5)

if __name__ == "__main__":
    main()
