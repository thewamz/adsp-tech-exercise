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
pip install -e .
```

To view the help output:

```bash
python -m adsp -h
```
