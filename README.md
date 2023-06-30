
# portfolio-balance
The basic idea of these portfolio balancing strategies is that the individual wants a roughly equal investment in each asset in their portfolio.
You can pick whatever collection of assets you want.
The assets in my portfolio try to span a broad array of sectors and market capitalizations using low cost ETFs:
- FTEC
- VAW
- VCR
- VDC
- VHT
- VIS
- VNQ
- VOX
- VPU
- VSMAX

Having a broad array of sector and market cap coverage is a simple way to minimize risk of any individual company or sector having a crisis.
It also avoids "stock picking."

There are two strategies currently supported, both aimed at buying low and either never selling or selling high.

## Install and run the cli
You can use this as a CLI if you have your data saved as a csv:
```bash
pip install .
pbal
```

But this code was written to use the IBKR Client Portal to automate rebalancing of a personal brokerage account.
I have created a [Flex Query for myself](https://portal.interactivebrokers.com/AccountManagement/AmAuthentication?action=RM_FLEX_QUERIES) that creates a CSV in the format you see in the [tests](./tests/data).

## Use the IBKR Client Portal
Follow the [IBKR Client Portal Quickstart Guide](https://interactivebrokers.github.io/cpwebapi/quickstart).
- I put my installation in `~/bin`, so if you put your binaries somewhere else, modify accordingly.
- For MacOS Venrura users, port 5000 is used by the system, so you will need to change that in order to run.
- Do not forget to generate your own cert (see [the guide](https://interactivebrokers.github.io/cpwebapi/use-cases#invalid-ssl-certificate))
Starting the server:
```bash
cd ~/bin/clientportal/
bin/run.sh root/conf.yaml
```
