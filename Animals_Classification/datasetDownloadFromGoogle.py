import time
from simple_image_download import simple_image_download as sim
import requests
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Patch requests.get to skip SSL verify
_old_get = requests.get
def _new_get(*args, **kwargs):
    kwargs['verify'] = False
    last_exception = None
    for i in range(3):  # retry 3 times
        try:
            return _old_get(*args, **kwargs)
        except (requests.exceptions.ConnectionError, requests.exceptions.SSLError) as e:
            last_exception = e
            print(f"⚠️ Download failed, retrying... ({i+1}/3)")
            time.sleep(2)
    raise last_exception

requests.get = _new_get



# Now use the downloader
response = sim.Downloader()

response.download("Dog", 1000)
response.download('Cat', 1000)
response.download("Lion", 1000)
response.download('Tiger', 1000)
response.download('Elephant', 1000)