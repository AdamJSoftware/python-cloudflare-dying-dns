## PythonCloudflareDyingDNS allows you to monitor your DNS (cloudflare) with CRON

It will automatically update your DNS to your current IP if it changes

Simply create a config.json file with the following format

{
"cloudflare_token": "CLOUDFLARE_TOKEN",
"sites": [
{
"cloudflare_zone_identifier": "CLOUDFLARE_ZONE_IDENTIFIER",
"domain": "DOMAIN IN ZONE"
},
]
}

# Cloudflare token can be created in

https://dash.cloudflare.com/profile/api-tokens

Your domain must have DNS:edit -> In other words

Permissions = Zone > DNS > Edit

Zone sources = Include > Specific Zone > DOMAIN NAME (You can add multiple)

Zone identifier is found in the domain/zone dashboard (usually bottom right corner (called zone id))

# To install and run:

1. pip install -r requirements.txt
2. source ./bin/activate
3. python3 cloudflare.py

# Recommended cron command

# Don't add the \ in the actual cron command, readme forces it for some reason

0 \* \* \* \* USER(HOPEFULLY NOT ROOT) /LOCATION/bin/python3 /LOCATION/cloudflare.py
