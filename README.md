# selective-auction-bidder
Provides bid prices for Maker DSS auctions with fixed prices based on auction identifier.  To be used with 
[auction-keeper](https://github.com/makerdao/auction-keeper/).

All you need is Python 3.6; there are no package dependencies.  This keeps `auction-keeper` configuration easy.

To use:
  * Create a `config.json` as described below in the same directory as `bidder.py`.
  * Configure `auction-keeper` with `--model "python3 ../selective-auction-bidder/bidder.py"`.

## Configuration
 * **ourAddresses** is a list of ethereum addresses to avoid bidding over.  Leave this empty if you wish to outbid 
 yourself to maintain an aggressive bid.
 * **pricesByAuctionId** lets you cherry-pick which auctions to bid upon, and allows you to specify a price for each.
 * **defaultPrice** allows you to specify a price to use for any auction ids not in `pricesByAuctionId`.  Omit this if 
 you only wish to participate in certain auctions.
```
{
  "ourAddresses": ["0x90D4a0aE8845B714C4e2e07F0C9bc8D3F17085e6", "0xEA674fdDe714fd979de3EdF0F56AA9716B898ec8"],
  "pricesByAuctionId": {
    "333": 162.34,
    "334": 163.47,
    "335": 162.56,
    "336": 161.57
  },
  "defaultPrice": 131.42
}
```

## Testing
To test, you may manually execute the model and paste example signals to `stdin`, such as the one in 
[auction-keeper documentation](https://github.com/makerdao/auction-keeper/#communicating-with-bidding-models).


## Disclaimer
See `LICENSE.md`.

You (meaning any individual or entity accessing, using or both the software included in this github repository) expressly understand and agree that your use of the software is at your sole risk. The software in this github repository is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software. You release authors or copyright holders from all liability for you having acquired or not acquired content in this github repository. The authors or copyright holders make no representations concerning any content contained in or accessed through the service, and the authors or copyright holders will not be responsible or liable for the accuracy, copyright compliance, legality or decency of material contained in or accessed through this github repository.
