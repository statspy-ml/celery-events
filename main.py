from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host='redis', port=6379, db=0)

@app.post("/process/")
def process_commentary(data: dict):
    comment = data.get("commentary")
    print(f"Processing commentary: {comment}")
    
    # Do the actual processing here
    processed_result = comment + "-test-success"

    # Save the result in Redis
    r.set(comment, processed_result)

    return {"processed_result": processed_result}





