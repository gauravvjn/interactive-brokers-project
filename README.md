## 1. Prepare
To communicate with IB, you'll require the following:

- A funded and opened IBKR Pro account, which requires signing up (for development purpose a paper trading account can be used)

- Download the current Stable or Latest release of either the Trader Workstation (TWS) or IB Gateway (IBG). These act as 
clones of IB on your machine. Note that IBG is less resource-intensive as it lacks a UI, whereas TWS offers an interface.
Follow IBKR Campus to download and configure these.

- Download The current Stable or Latest release of the TWS API. You can download the TWS API source/files 
from https://interactivebrokers.github.io/. For this project, it's already part of the project so you can skip this step. 
You will develop your program using classes and functions provided by these API files. Use IBKR Campus for up-to-date 
API documentation. Understand the architecture of the respective 
language client: https://ibkrcampus.com/ibkr-api-page/twsapi-doc/#architecture.

- Another way to access IB is by using Rest API, Client Portal API(CP-API). 
An active Interactive Brokers account is required in order to use the Client Portal API. 


## 2. Setup

After downloading and installing TWS, you can start with a Paper Trading account by providing just email id 
and select demo user for testing account: https://www.interactivebrokers.com/en/trading/free-trial.php

After that, we need to do a change a couple of settings under:
File -> Global Configuration -> Settings -> API

Check Enable ActiveX and Socket Clients and uncheck Read-Only API.

Notice that the port is 7497, which differs from the standard 7496 which is used for Live Trading.


## 3. Developing
Two main classes for all language clients:

EClient - For Outgoing Messages

Ewrapper - For Incoming Messages

Read more about the arch/design of IB python api client at [ibapi python client README](ibapi/README.md)


## 4. Run
```sh
python -m playground.market_data
```
OR
```sh
PYTHONPATH=. python playground/market_data.py
```
