import json
import datetime

import os
import requests
import bitly_api

from oauth_api import get_oauth
from settings import BASE_DIR
from settings import bitly_token


def send_tweet(anniversary):
    """
    :param anniversary: a json object (fecha, hecho, link)
    """
    oauth = get_oauth()
    status = make_status(anniversary)
    payload = {
        'status': status,
    }
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    res = requests.post(url=url, auth=oauth, params=payload)
    print("Tweeting " + anniversary['fecha'])
    res_json = res.json()
    if 'errors' in res_json:
        print(res_json)


def make_status(anniversary):
    c = bitly_api.Connection(access_token=bitly_token)
    short_link_data = c.shorten(anniversary['link'])

    human_date = format_date(anniversary['fecha'])
    return '{0} {1} {2}'.format(human_date,
                                anniversary['hecho'],
                                short_link_data['url'],
                                )


def format_date(fecha):
    d = datetime.datetime.strptime(fecha, "%Y-%m-%d")
    return d.strftime("%d %b %Y")


def look_for_anniversary():
    today = datetime.date.strftime(datetime.date.today(), '-%m-%d')

    with open(os.path.join(BASE_DIR, 'data.json'), 'r') as handle:
        data = json.loads(handle.read())

    for anniversary in data['efemerides']:
        if today in anniversary['fecha']:
            print("Match {}".format(make_status(anniversary)))
            send_tweet(anniversary)


def main():
    look_for_anniversary()


if __name__ == '__main__':
    main()
