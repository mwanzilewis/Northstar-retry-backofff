from fastapi import FastAPI
from retry import retry_with_backoff

app = FastAPI(title="Northstar Retail - Retry Backoff")

@app.get("/")
def home():
    return {"status": "Northstar Retry Service is Live", "repo": "mwanzilewis/Northstar-retry-backofff"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/test-retry")
def test_retry_endpoint():
    counter = {"count": 0}
    def unstable():
        counter["count"] += 1
        if counter["count"] < 3:
            raise Exception(f"Fail {counter['count']}")
        return f"Success after {counter['count']} tries"
    
    result = retry_with_backoff(operation=unstable, max_attempts=5, base_delay=0.5)
    return {"message": result}
