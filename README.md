# CryptoMining-Scraping

CryptoMining-Scraping contains two Python scripts for extract data related to the hardware used to mine crypto currencies.

## Installation

The first step to using the scripts is to install python and selenium on our machine:

### Python

Start by updating the package list using the following command:

```bash
sudo apt update
```

Use the following command to install pip for Python 3:

```bash
sudo apt install python3-pip
```

The command above will also install all the dependencies required for building Python modules.

### Selenium

```bash
pip3 install selenium
```

if you dont have permession for this type of installation use:

```bash
sudo pip3 install selenium
```
## Usage
To properly extract all the information within a self-generated CSV file we need to run the scripts in this sequence:

1. mining_url.py

this script returns a script containing all the URLs relating to each type of hardware within which we find all the information we need.

2. mining_stat.py

this script returns a CSV file containing all information such as: 

```bash
names
equips
prices
powers
h_rate
GH_s
values
day_costs
r_day
r_week
r_month
r_year
day_payback
annual_pr
user_rating
```

Once the second script has been executed and finished, the final file will be called:
```
mining_eqp.csv
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)