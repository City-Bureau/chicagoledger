import csv
import sys
import logging

from tweet.bills import Bill
from tweet.config import APP_CONFIG
from tweet.query import save_introductions, setup

log = logging.getLogger(__name__)


def load_archive():
    """Load all bills from a CSV file"""
    app = setup(app_config=APP_CONFIG)
    log.setLevel(logging.INFO)
    with open(sys.argv[1], 'r') as f:
        reader = csv.DictReader(f)
        rows = [
            Bill(
                r['identifier'],
                r['title'].strip(),
                r['classification'],
                r['ocd_id'] or 'NA',
                r['date'],
            )
            for r in reader
        ]

    log.info(f'loading all: {len(rows)} introductions')
    log.setLevel(logging.WARNING)
    save_introductions(app.bills, rows)


if __name__ == '__main__':
    load_archive()
