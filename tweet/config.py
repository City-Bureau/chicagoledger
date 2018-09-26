import os
from collections import namedtuple

from dateutil.utils import today

from tweet.ocd_api import create_query

AppConfig = namedtuple('AppConfig', 'aws_profile, aws_secret_name, query')

# OCD Query params
# Rahm Emanuel -> https://ocd.datamade.us/ocd-person/f649753d-081d-4f22-8dcf-3af71de0e6ca/
PERSON = 'ocd-person/f649753d-081d-4f22-8dcf-3af71de0e6ca'
ACTIONS = 'Referred'
QUERY = create_query(
    max_date=today(),
    weeks_offset=8,
    person=PERSON, description=ACTIONS
)

TERM_START_DATE = '2011-01-01'

# AWS params
# .aws/config to use
# profile is expected to have region
AWS_PROFILE_NAME = os.getenv('AWS_DEFAULT_PROFILE', 'default')
AWS_SECRETSMANAGER_SECRET_NAME = 'Twitter'

APP_CONFIG = AppConfig(AWS_PROFILE_NAME, AWS_SECRETSMANAGER_SECRET_NAME, QUERY)
