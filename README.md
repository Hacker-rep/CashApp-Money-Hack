# CashApp Auto Giveaways Bot

Cool python bot to automatically like, retweet, and reply to CashApp twitter giveaways using multiple Twitter accounts and $Cashtags.

## Installation

### Set First: Twitter API
Generate your Consumer Keys, Consumer Secrets, Access Tokens, Access Token Secrets, and Bearer Tokens on the [Twitter Developer Dashboard](https://developer.twitter.com/en/portal/dashboard). Make sure to turn on OAuth 1.0a and OAuth 2.0 on, and enable "Read and Write" permissions for OAuth 1.0a. After doing this you will need to regenerate your Access Token and Access Token Secrets for the changes to take affect.

### Docker (Recommended)
View on [Docker Hub](https://hub.docker.com/u/nelsondane/cashapp-auto-giveaways)
1. Download and install Docker on your system
2. Set your environmental variables in your `.env` file
3. Start the container using: `docker run -d --env-file ./.env -v /abolsute/path/to/cached_tweets.txt:/app/cached_tweets.txt --restart unless-stopped --name cashapp nelsondane/cashapp-auto-giveaways:<tag>`
4. Enjoy!

#### Docker Tags
- `latest`: latest stable release on [NelsonDane's GitHub](https://github.com/NelsonDane/cashapp-auto-giveaways)
- `beta`: latest beta release on [Sazn's GitHub](https://github.com/sazncode/cashapp-auto-giveaways-beta)

### Manual Python Script
1. Install python-pip on your system
2. Clone this repo and cd into it
3. Run `pip install -r requirements.txt`
4. Configure your `.env`
5. Run `python cashapp.py`
6. Enjoy!

### Bot Settings via .env
An example `.env` is included (`.env.example`) which includes all necessary and optional `.env` variables. They are explained here:
#### Necessary Settings
If configuring multiple Twitter accounts, seperate each value with a comma (no spaces!)
- `CONSUMER_KEYS`: Your Twitter API consumer keys
- `CONSUMER_SECRETS`: Your Twitter API consumer secrets
- `ACCESS_TOKENS`: Your Twitter API access tokens (Must set read/write and then regenerate)
- `ACCESS_TOKEN_SECRETS`: Your Twitter API access token secrets (Must set read/write and then regenerate)
- `BEARER_TOKENS`: Your Twitter API bearer tokens
- `CASHTAGS`: Your cashtags (Do not include the $)
- `USERNAMES`: Your Twitter account usernames (Don't include the @)

#### Optional Bot Settings
- `CHECK_FOLLOWING`: Set to `true` if the bot should check if each twitter account is following `@CashApp` (Or `@Venmo` if enabled), following if they aren't. (Defaults to `false`)
- `TZ`: If using Docker, TZ can be set to specify the timezone for logs. Timezone should be formatted using the [IANA TZ Database](https://www.iana.org/time-zones). (Default `America/New_York`)
- `START_TIME`: The time the bot should start working (Default 9:00am)
- `END_TIME`: The time the bot should stop working (Default 9:00pm)
- `WORDED_REPLIES`: Whether the bot should include a short message with each Tweet reply (Default False)
- `CHECK_INTERVAL_SECONDS`: How often the bot should check for new giveaway Tweets. Don't set this too low or you'll run out of API requests (Default 900 seconds)
- `MANUAL_TWEET`: The ID of the Tweet you want the bot to run on. This disables searches, running all accounts once on the given ID. Helpful for if you want to run the bot on a specific ID that wasn't found in the automatic search.
#### Apprise Alerts
If you want to use Apprise to send alerts, you'll need to set the following variables with the alert URLS (Full list of services and their URLs available here: https://github.com/caronc/apprise/wiki). If configuring multiple alert services, seperate each value with a comma (no spaces!)
- `APPRISE_FOUND_ALERTS`: Whether the bot should alert you when an new giveaway is found (Default False)
- `APPRISE_STATUS_ALERTS`: Whether the bot should alert you when a giveaway is successful entered or errors occured (Default False)

#### Beta Settings
- `VENMO_GIVEAWAYS`: Set to `true` if the bot should check for Venmo tweets in addition to CashApp ones.
- `VENMO_TAGS`: Your Venmo Tags, seperated by commas.

### Notes:
- Another note for Docker, for some reason using quotes ("") around the `.env` values breaks the bot. This doesn't affect the bot when it's ran via python on Windows or MacOS, so something to be aware of if you plan on taking the Docker route.

## FAQs

#### I get error 403 Forbidden

Your generated credentials are not correct or out of order. Make sure you regenerated your Access Tokens and Access Token Secrets after setting Read/Write permissions for OAuth 1.0a.

#### I get error 429 Too Many Requests

You hit a rate limit on one of your accounts. Wait a while before trying to run the bot again.

## Features

### Working
- Multiple Twitter Accounts
- Account following
- Liking
- Retweeting
- Replying
- Replying with custom messages
- Quote Replying
- Searching for tweets
- Custom sleep times (Python and Docker)
- Gathering recent user Tweets to avoid replying twice
- Running the bot once on a custom Tweet ID
- Apprise Alerts

### Maybe working
- None at this time

### Upcoming (Hopefully)
- Full Venmo Support
