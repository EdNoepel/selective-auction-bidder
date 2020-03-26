#!/usr/bin/env python
import os
import sys
import json


GWEI = 1000000000
gas_price = int(4.0 * GWEI)

# TODO: Move these to a configuration file

# specify price for each auction id we wish to bid upon
prices_by_auction_id = {
    4647: 57.47,
    4656: 57.56
}

# prevent outbidding these addresses
our_addresses = set("0x9Eb75d8989e76e6198982d45CF0cD002729fb418")


def log(message: str):
    assert isinstance(message, str)
    print(message, flush=True, file=sys.stderr)


for line in sys.stdin:
    signal = json.loads(line)
    id = int(signal['id'])
    guy = signal['guy'].lower()
    if guy in map(str.lower, our_addresses):
        log(f"Not bidding on auction by {guy}")
        continue
    if id in prices_by_auction_id:
        price = prices_by_auction_id[id]
        stance = {'price': price, 'gasPrice': gas_price}
        print(json.dumps(stance), flush=True)
    else:
        log(f"Not bidding on auction {id}")
