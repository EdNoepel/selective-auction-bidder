#!/usr/bin/env python
import os
import sys
import json
import zlib


def log(message: str):
    assert isinstance(message, str)
    print(message, flush=True, file=sys.stderr)


class Config:
    GWEI = 1000000000

    def __init__(self, filename="config.json"):
        cwd = os.path.dirname(os.path.realpath(__file__))
        self.filename = os.path.join(cwd, filename)
        self.prices_by_auction_id = {}
        self.default_price = None
        self.our_addresses = set()
        self.last_checksum = None

    def check(self):
        with open(self.filename) as data_file:
            content_file = data_file.read()
            new_checksum = zlib.crc32(content_file.encode('utf-8'))
            if new_checksum != self.last_checksum:
                try:
                    result = json.loads(content_file)
                    self.our_addresses = set(result["ourAddresses"])
                    self.prices_by_auction_id = result["pricesByAuctionId"]
                    if "defaultPrice" in result:
                        self.default_price = result["defaultPrice"]
                    if self.last_checksum:
                        log("Reloaded configuration file")
                except json.JSONDecodeError as ex:
                    log(f"Ignored bad configuration file: {ex}")
                finally:
                    self.last_checksum = new_checksum


config = Config()

for line in sys.stdin:
    config.check()
    signal = json.loads(line)
    id = signal['id']
    guy = signal['guy'].lower()

    if guy in map(str.lower, config.our_addresses):
        log(f"Not outbidding {guy} on {id}")
        continue
    if id in config.prices_by_auction_id:
        stance = {'price': config.prices_by_auction_id[id]}
        print(json.dumps(stance), flush=True)
    elif config.default_price:
        stance = {'price': config.default_price}
        print(json.dumps(stance), flush=True)
    else:
        log(f"Not bidding on auction {id}")
