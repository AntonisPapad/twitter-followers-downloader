# Twitter Follower Downloader

This script uses the python-twitter library to download the followers of Twitter users. You can pass the users you want to download as arguments in the terminal and store the followers for each one in a separate CSV file.

## Installation

To use the script, you need to install the required libraries. You can install them using the following command:

``` pip3 install -r requirements.txt ```

## Usage

To use the script, run the twitter_follower_downloader.py file in your terminal, passing the Twitter usernames you want to download as arguments. For example:

``` python3 twitter_follower_downloader.py user1 user2 user3 ```

The script will create a separate CSV file for each user you specify, containing the usernames and Twitter IDs of their followers. The CSV files will be saved in the same directory as the script.