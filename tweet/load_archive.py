import logging

from tweet.config import APP_CONFIG, TERM_START_DATE
from tweet.ocd_api import BillsRequestParams
from tweet.query import get_new_introductions, save_introductions, setup

log = logging.getLogger(__name__)


def load_archive():
    """Load all bills from the beginning of Emanuel's term"""
    app = setup(app_config=APP_CONFIG)
    query_params = BillsRequestParams(
        person_id=app.query.person_id,
        min_date=TERM_START_DATE,
        max_date=app.query.max_date,
        description=app.query.description,
    )
    all_introductions = get_new_introductions(
        app.bills_api, query_params, app.bills
    )
    log.setLevel(logging.INFO)
    log.info(f'loading all: {len(all_introductions)} introductions')
    log.setLevel(logging.WARNING)
    save_introductions(app.bills, all_introductions)


if __name__ == '__main__':
    load_archive()
