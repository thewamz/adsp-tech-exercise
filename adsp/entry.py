# -*- coding: utf-8 -*-
"""
Entry point - read environment, commandline and set up logging
"""
import logging
import traceback
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from sys import exit as sys_exit
from datetime import datetime

from . import about
from .utils import to_pandas, to_csv
from .metropolitan_police_service import MetropolitanPoliceService

logging.basicConfig(level=logging.INFO)

LOGGER = logging.getLogger(__name__)


def main():
    """
    Setup logger and read command line
    """
    parser = ArgumentParser(
        description=about.__description__,
        epilog=about.__version__,
        prog=about.__pkgname__,
        formatter_class=ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--force-id",
        help="Force ID to search for",
        required=True,
    )
    parser.add_argument(
        "-m",
        "--month",
        help="Specific month & year to limit results to .e.g. YYYY-MM",
    )
    parser.add_argument(
        "-c",
        "--csv-file",
        help="Name of csv file in which results will be stored",
        required=True,
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=" ".join(
            (
                about.__pkgname__,
                about.__version__,
            )
        ),
    )

    args = parser.parse_args()
    force_id = args.force_id
    csv_file = args.csv_file
    try:
        search_date = datetime.strptime(args.month, "%Y-%m")
    except (TypeError, ValueError):
        search_date = datetime.now()

    try:
        msp = MetropolitanPoliceService(force_id, search_date)
        data = msp.stop_and_search_data()

        df = to_pandas(data)
        to_csv(df, csv_file)
    except Exception as err:
        LOGGER.error("Unexpected error: %s", err)
        traceback.format_exc(err)
        exit_code = -1
    else:
        exit_code = 0

    LOGGER.info("Exiting application")
    sys_exit(exit_code)
