#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
import json
import datetime

import requests

from oauth_api import get_oauth
from settings import BASE_DIR


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
    requests.post(url=url, auth=oauth, params=payload)
    print("Tweeting " + anniversary['fecha'])


def make_status(anniversary):
    human_date = format_date(anniversary['fecha'])
    return '{0} {1} {2}'.format(human_date,
                                anniversary['hecho'],
                                anniversary['link'],
                                )


def format_date(fecha):
    d = datetime.datetime.strptime(fecha, "%Y-%m-%d")
    return d.strftime("%d de %b %Y")


def look_for_anniversary():
    today = datetime.date.strftime(datetime.date.today(), '-%m-%d')

    with open(os.path.join(BASE_DIR, 'data.json'), 'r') as handle:
        data = json.loads(handle.read())

    for anniversary in data['efemerides']:
        if today in anniversary['fecha']:
            send_tweet(anniversary)


def main():
    print("hola")


if __name__ == '__main__':
    main()
