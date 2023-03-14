import json
import time
import sys

import twitter
import requests


def main():
    api = auth('twitter_credentials.json')

    accounts = sys.argv[1:]

    for account in accounts:
        followers = download(account, api)

        if followers is None:
            continue  # if user doesn't exist continue to the next one

        with open(f'{account}.csv', mode='a', encoding='utf-8') as f:
            for follower in followers:
                f.write(f"{follower.screen_name}, {follower.id}\n")


def auth(credentials):
    with open(credentials, mode='r', encoding='utf-8') as file:
        creds = json.load(file)
    api = twitter.Api(consumer_key=creds["consumer_key"],
                      consumer_secret=creds["consumer_secret"],
                      access_token_key=creds["access_token"],
                      access_token_secret=creds["access_token_secret"],
                      sleep_on_rate_limit=True)
    try:
        api.VerifyCredentials()
    except twitter.error.TwitterError as err:
        print('Authentication failed:', err)
        sys.exit(-1)
    return api


def download(account, api):
    while True:
        try:
            followers = api.GetFollowers(screen_name=account)
        except twitter.error.TwitterError:
            print(f"User {account} doesn't exist")
            return None  # if user doesn't exist return none
        except requests.exceptions.ConnectionError:
            print(f'Connection error occured at {account}')
            time.sleep(600)
        else:
            break
    return followers


if __name__ == '__main__':
    main()
