import time
import requests

def ping_host(host):
    try:
        r = requests.get(host, timeout=5)
        if r.status_code == 200:
            print(f"{host} is online.")
        else:
            print(f"{host} returned status {r.status_code}.")
    except requests.RequestException:
        print(f"{host} is unreachable.")

if __name__ == "__main__":
    while True:
        ping_host("https://example.com")
        time.sleep(60)
