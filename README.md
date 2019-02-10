# CSV_report

python: 3.7 
- additional library: pycountry ver.18.12.8

## To run
Place CSF_report.py in the same direction as input.csv file. Run script from cmd 'python CSV_report.py'.
Normalized data will appear as output.csv file in the same directions.

## Errors:
Not critical errors (data normalization process is continued): 
- bad date - returns fake date '2099-01-01';
- bad region data - returns country code 'XXX';
- bad impression or CTR data - returns number of clicks as '?'

Critical errors:
- no input.csv file - prints 'Input file missing' and shuts script down;
- other errors like bad-encoding or hashed file - return error and shuts down.