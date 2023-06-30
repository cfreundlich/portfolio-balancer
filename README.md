# portfolio-balance
The basic idea of these portfolio balancing strategies is that you set a target and periodically (no more than once a quarter) trade in order to get closer to these targets.

This makes trading very boring, but it minimizes variance without sacrificing expected value.  It also gives you some flexibility to buy low and sell high.

Please check out my [companion blog post](https://cfreundlich.github.io/portfolio-balancer/) for more motivation.

## Setting a target
Basic idea of a target in this code is:
- The individual wants a roughly equal investment in each asset in their portfolio.
- You can pick whatever collection of assets you want, but the general idea is that you span a broad array of sectors and market capitalizations using low cost ETFs, for example, you may want to target 10% allocation to each of these ten ETFs:
  1. FTEC
  1. VAW
  1. VCR
  1. VDC
  1. VHT
  1. VIS
  1. VNQ
  1. VOX
  1. VPU
  1. VSMAX

Having a broad array of sector and market cap coverage is a simple way to minimize risk of any individual company or sector having a crisis.
It avoids over-exposure on any area of the economy, and likewise avoids stock picking.
 
## Adopting a strategy to rebalance
There are two strategies currently supported, both aimed at buying low.
- There is [hard_rebalance](./src/pbal/hard_rebal.py) which will sell and buy in order to equalize the values all assets in your portfolio, adding or freeing up cash depending on the user input for [cash](./src/pbal/cli.py)
- Then there is [try_avoid_sell](./src/pbal/try_avoid_sell.py) which will only buy assets to try to approach the target.  It raises the floor of your portfolio, buying low incrementally.  This avoids incurring capital gains taxes.  If you give the cash option a negative sign when invoking this strategy, then it will sell your highest value assets first, using capital gains tax exposure as a tie-breaker.

The default strategy is to avoid selling at all costs in order to avoid capital gains taxes, which would be [try_avoid_sell](./src/pbal/try_avoid_sell.py).

## Download Up-to-date portfolio data
This code was written with the the IBKR margin trading account in mind.
To make downloading the CSV easier, I created a [Flex Query](https://portal.interactivebrokers.com/AccountManagement/AmAuthentication?action=RM_FLEX_QUERIES) that creates a CSV in the format you see in the [tests](./tests/data).
I can't share the Flex Query settings, but you should be able to figure them out.
If you can't, then you probably should not be using this code.


## Install and run the cli
You can use this as a CLI if you have your data saved as a csv:
```bash
pip install .
pbal
```
This will suggest some trades you can make to push your portfolio allocations toward the target.

Use the `--help` flag to explore ways to modify your strategy.

# Using the IBKR Client Portal to automate trade execution
This would be the last step to making this process extremely mindless and thus ideal for me.
However, it is a work-in-progress.

## Steps I have successfully completed
Follow the [IBKR Client Portal Quickstart Guide](https://interactivebrokers.github.io/cpwebapi/quickstart).
- I put my installation in `~/bin`, so if you put your binaries somewhere else, modify accordingly.
- For MacOS Venrura users, port 5000 is used by the system, so you will need to change that in order to run.
- Do not forget to generate your own cert (see [the guide](https://interactivebrokers.github.io/cpwebapi/use-cases#invalid-ssl-certificate))
Starting the server:
```bash
cd ~/bin/clientportal/
bin/run.sh root/conf.yaml
```
I have personally not made their auth system work.  See [my notebook](./notebooks/main.ipynb) for details.
