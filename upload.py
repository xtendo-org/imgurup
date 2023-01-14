#!/usr/bin/env python3

from helpers import get_input, get_config
from imgurpython import ImgurClient
import json
import os.path
import subprocess
import sys

HOME = os.path.expanduser('~')

def authenticate():
    # Get client ID and secret from auth.ini
    config = get_config()
    config.read(HOME + '/.imgur.ini')
    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')

    return ImgurClient(client_id, client_secret)


def upload_kitten(client, img_path):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''

    # Here's the metadata for the upload. All of these are optional, including
    # this config dict itself.
    print("Uploading image... ")
    image = client.upload_from_path(img_path, anon=False)
    print("Done")

    return image


# If you want to run this as a standalone script
if __name__ == "__main__":
    client = authenticate()
    print('Chosen image: ' + sys.argv[1])
    image = upload_kitten(client, sys.argv[1])
    print(image)

    url = image['link']

    print(f'You can find it here: {url}')
    p = subprocess.Popen(['xclip', '-sel', 'clip'], stdin=subprocess.PIPE)
    p.stdin.write(url.encode('utf-8'))
    p.stdin.close()
    print('waiting for xclip to terminate...')
    p.wait()

    print('Saving to log...')
    with open(HOME + '/.imgurup.log', 'a') as f:
        log_data = json.dumps(image, separators=(',', ':'))
        f.write(f'{log_data}\n')
