# Exchange_rates fetcher.

## Summary:
Gets the international exchange rate for all western currencies vs de Euro, obtained from the bank of Poland using their REST API (originally the exchange rate was in comparisson to the polish zloty, but with some transformations we obtain the exchanges vs the Euro). The function can be scheduled using a crontab, an eventbridge, or an airflow dag.


## Instructions

_Requirements_

- A valid instalation of any version of python3 in your virtual_env
- _Recomended: A valid instalation of the Request v.2+ package, the script will install it if you dont have it yet, but depending of sys_config it will ask for permissions/credentials_

## Runing the code

1. Unzip the attached folder, and remember its path
2. Open your command line and navigate towards your folder path
3. Execute the script using python3 from the command line
