import concurrent.futures
import time
import urllib.request

URL = "http://127.0.0.1:5000/"
REQUESTS = 200
WORKERS = 20

def request(_):
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(URL, timeout=5) as response:
            response.read()
            return response.status, time.perf_counter() - start
    except Exception:
        return 0, time.perf_counter() - start

if __name__ == "__main__":
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(request, range(REQUESTS)))
    elapsed = time.perf_counter() - start
    ok = sum(status == 200 for status, _ in results)
    print("Total:", REQUESTS, "Successful:", ok, "Failed:", REQUESTS-ok)
    print("Elapsed seconds:", round(elapsed, 2))
    print("Requests per second:", round(REQUESTS/elapsed, 2))
