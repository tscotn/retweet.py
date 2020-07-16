from twython import Twython
import sys

app_key = "YOUR_APP_KEY"
app_secret = "YOUR_APP_SECRET"
oauth_token = "YOUR_OAUTH_TOKEN"
oauth_token_secret = "YOUR_OAUTH_TOKEN_SECRET"

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

message_to_tweet = sys.argv[1]
keyboard = {"A":1283528365832577026,
            "B":1283528366432321546,
            "C":1283528366994477058,
            "D":1283528422510272521,
            "E":1283528423172984838,
            "F":1283528423768494080,
            "G":1283528424355749889,
            "H":1283528502638149644,
            "I":1283528503238037504,
            "J":1283528503804211200,
            "K":1283528504643067904,
            "L":1283528505180004352,
            "M":1283528505733545985,
            "N":1283528506371190784,
            "O":1283528506912264192,
            "P":1283528507436523523,
            "Q":1283528595730825224,
            "R":1283528596297068544,
            "S":1283528596842319872,
            "T":1283528597395984392,
            "U":1283528597928583168,
            "V":1283528598603825157,
            "W":1283528599212101632,
            "X":1283528599904161792,
            "Y":1283528600650735621,
            "Z":1283528601204391936,
            ".":1283529693938032642,
            ",":1283529694738968576,
            "?":1283529695552835585,
            "!":1283529696135786503}

for letter in message_to_tweet:
    if letter.upper() in keyboard.keys():
        twitter.retweet(id = keyboard.get(letter.upper()))
