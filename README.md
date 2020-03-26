# selective-auction-bidder
Bids on DSS auctions with fixed prices based on auction identifier.  To be used with 
[auction-keeper](https://github.com/makerdao/auction-keeper/).

All you need is Python 3.6; there are no package dependencies.

To use:
  * Create a `config.json` as described below in the same directory as `bidder.py`.
  * Configure `auction-keeper` with `--model "python3 ../selective-auction-bidder/bidder.py"`.

## Configuration
 * **ourAddresses** is a list of ethereum addresses to avoid bidding over - Leave this empty if you wish to outbid 
 yourself to maintain an aggressive bid.
 * **pricesByAuctionId** lets you cherry-pick which auctions to bid upon, and allows you to specify a price for each.
 * **gasPrice** specifies the gas price you wish to use, in Gwei.
```
{
  "ourAddresses": ["0x90D4a0aE8845B714C4e2e07F0C9bc8D3F17085e6", "0xEA674fdDe714fd979de3EdF0F56AA9716B898ec8"],
  "pricesByAuctionId": {
    "333": 133.34,
    "334": 133.47,
    "335": 133.56,
    "336": 133.57
  },
  "gasPrice": 3.14159
}
```

## Testing
To test, you may manually execute the model and paste example signals to `stdin`, such as the one in 
[auction-keeper documentation](https://github.com/makerdao/auction-keeper/#communicating-with-bidding-models).