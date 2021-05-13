# GEOIP logger
## HOW TO RUN
### Create virtual env and activa
> \> virtualenv -p python3 vent
> 
> \> . ./vent/bin/activate
### Install dependenceies
> \> pip install -r requirements.txt
### Run
> \> make db
>
> \> make run

### Test
> \> make test
## Additional api calls
#### Run Application in debug mode
> \> make debug 
#### Insert new IP
> \> python main.py -ip 10.0.0.10
#### Fetch a IP from the DB insert if missing
> \> python main.py -find 10.0.0.10 
#### List all db entries
> \> python main.py -list
