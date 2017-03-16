#!/usr/bin/env python3

from imgurpython import ImgurClient
from helpers import get_input, get_config
import os.path
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
    print()

    return image


# If you want to run this as a standalone script
if __name__ == "__main__":
    client = authenticate()
    print('Chosen image: ' + sys.argv[1])
    image = upload_kitten(client, sys.argv[1])

    print("You can find it here: {0}".format('https' + image['link'][4:]))
