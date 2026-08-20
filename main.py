from fastapi import FastAPI
from retry import retry, exponential_backoff

app = FastAPI(title="Northstar Retail - Retry Backoff")

@app.get("/")
def home():
    return {"status": "Northstar Retry Service is Live", "repo": "mwanzilewis/Northstar-retry-backofff"}

@app.get("/test-retry")
@retry(max_retries=3, backoff=exponential_backoff)
def test_retry_endpoint():
    # This will test your retry logic
    return {"message": "Retry logic working"}

@app.get("/health")
def health():
    return {"status": "ok"}
