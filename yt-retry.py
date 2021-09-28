import time

import requests


def retry(func, retries=3):
    def retry_wrapper(*args, **kwargs):
        attempts = 0
        while attempts < retries:
            try:
                return func(*args, **kwargs)
            except requests.exceptions.RequestException as e:
                print(e)
                time.sleep(2)
                attempts += 1

    return retry_wrapper


@retry
def get_data(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    # text = get_data('https://httpbin.org/html')
    text = get_data('https://pleasesubtome.org/html')
    print(text)
