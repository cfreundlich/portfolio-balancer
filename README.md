# portfolio-balance
The basic idea of these portfolio balancing strategies is that you set a target and periodically (no more than once a quarter) trade in order to get closer to these targets.

Portfolio Balancer's currently supported strategies are predicated on the assumption that the investor wants equal distribution of value across all assets in their portfolio. Investors can pick whatever collection of assets they want, but the general idea is that they span a broad array of sectors and market capitalizations using low cost ETFs, for example, one may want to target 10% allocation to each of these ten ETFs:
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

This makes trading very boring, but it minimizes variance without sacrificing expected value.  It also gives you some flexibility to buy low and sell high.
Check out my [companion blog post](https://cfreundlich.github.io/portfolio-balancer/) for more motivation and explanation of this strategy and how it is executed in this library.

# Usage
## Download Up-to-date portfolio data
This code was written with the the IBKR margin trading account in mind.
To make downloading the CSV easier, I created a [Flex Query](https://portal.interactivebrokers.com/AccountManagement/AmAuthentication?action=RM_FLEX_QUERIES) that creates a CSV in the format you see in the [tests](./tests/data).
I can't share the Flex Query settings, but you should be able to figure them out.
If you can't, then you probably should not be using this code.

If you do not use IBKR, then creating the CSV is up-to-you, but it should not very difficult.

## Install and run the cli
```bash
cd /wherever/you/keep/your/code
git clone git@github.com:cfreundlich/portfolio-balancer.git
cd portfolio-balancer
pip install .
```
Now, you are all set to run the `pbal` command to suggest some trades you can make to push your portfolio allocations toward the target.

## Example
Suppose you have a portfolio with the following positions in the CSV format this software is expecting:
```
"Symbol","PositionValue","MarkPrice","FifoPnlUnrealized"
"FTEC","15000.00","128.62","3343.9673"
"VAW","10000.00","180.51","893.3955"
"VCR","6798.48","279.68","1700.9984"
"VDC","8000","192.75","-1192.065125"
"VHT","12000.43","242.65","18.5908"
"VIS","9000","203.87","-2382.175"
"VNQ","9500","83.1","-1745.915301"
"VOX","9500.14","105.39","-2075.3452"
"VPU","13000.99","140.63","4933.423"
"VSMAX","20100.44","94.73","802.809999"
```
Let's assume this file is in the location `~/Downloads/positions-custom.csv`.  Note that this is the default location the software will look for the CSV, but I will show the full command in the example below.

Suppose you just pawned a $4000 diamond watch you "found" in a parking lot, and you decide you want to take an additional $1000 in margin from your broker, so that you plow it into your retirement.  You also don't want to bother with trades less than $100, so you use the following command and output:
```
❯ pbal ~/Downloads/positions-custom.csv -i 2 -c 5000
Symbol      InitialValue    MarkPrice    BuyVal    BuyShares
--------  --------------  -----------  --------  -----------
FTEC            15000          128.62         0            0
VAW             10000          180.51         0            0
VCR              6798.48       279.68      2800           10
VDC              8000          192.75      1500            8
VHT             12000.4        242.65         0            0
VIS              9000          203.87       600            3
VNQ              9500           83.1        100            1
VOX              9500.14       105.39         0            0
VPU             13001          140.63         0            0
VSMAX           20100.4         94.73         0            0
```
The second-to-last column, `BuyVal` specifies the amount you want to allocate to the given asset.

The last column tells you what to do.  In the example above, all you need to do now is buy 10 shares of VCR, 8 shared of VDC, 3 shares of VIS, and 1 share of VNQ.

To explore more features, use the `--help` flag.

# To Do: Use the IBKR Client Portal to automate trade execution
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
