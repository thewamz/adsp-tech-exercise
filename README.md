# ADSP

Retrieve stop and search data from the Metropolitan Police Service API

## Production

This tool is currently run every morning on a schedule in RunDeck.

## Development

Make sure you have Python3.10 or higher installed on your machine.

First create virtual environment and activate it:

```bash
virtualenv -p python3.6 adsp_env

source adsp_env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

To view the help output:

```bash
python -m adsp -h
```

To retrieve stop and search data:

```bash
python -m adsp -f <force-id> -m <month .e.g. YYYY-MM> -c <csv_file>
```

## Docker

You can run the app in a docker container

Build docker image: `make build-image`

Run docker image in a container: `make run-image`

SSH into the running docker container: `docker exec -it adsp bash`

Then run the app to retrieve stop and search data inside the docker container:

```bash
python -m adsp -f <force-id> -m <month .e.g. YYYY-MM> -c <csv_file>
```

## Cron job

Enter the crontab scheduling:

```bash
crontab -e
```

Append the command to the end of the crontab file if you want to run the app directly with Python:

```bash
0 3 28 * * /usr/bin/python -m adsp -f <force-id> -m <month .e.g. YYYY-MM> -c <csv_file>
```

Alternatively, you can append the command below to the end of the crontab file if you want to run the app using Docker:

```bash
0 3 28 * * docker exec adsp python -m adsp -f <force-id> -m <month .e.g. YYYY-MM> -c <csv_file>
```
