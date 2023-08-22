from celery_app import celery_app, forward_to_fastapi
import logging

logging.basicConfig(level=logging.DEBUG)

def main():
    commentary = "mania de cabecao"
    result = forward_to_fastapi.apply_async(args=[commentary])
    
    # This will wait until the task is done and get the result
    # WARNING: Do not use this in production as is, because it will block until the task is done.
    print("Sent the task.")
    response = result.get(timeout=30)  # waits a maximum of 30 seconds for the result
    print(f"Task Result: {response}")
    print(f"Task State: {result.state}")

if __name__ == "__main__":
    main()










