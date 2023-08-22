from celery_app import celery_app, forward_to_fastapi
import logging

logging.basicConfig(level=logging.DEBUG)

def main():
    commentary = "Rodrigo"
    result = forward_to_fastapi.apply_async(args=[commentary])
    

    print("Sent the task.")
    response = result.get(timeout=30)  
    print(f"Task Result: {response}")
    print(f"Task State: {result.state}")

if __name__ == "__main__":
    main()










