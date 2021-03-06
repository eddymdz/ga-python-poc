import os
import time
from os.path import join, dirname
from dotenv import load_dotenv
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest

dotenv_path = join(dirname(__file__), '.env')
credentials_path = join(dirname(__file__), 'service-account.json')
load_dotenv(dotenv_path)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('SERVICE_ACCOUNT_NAME')

client = BetaAnalyticsDataClient()

property_id = os.getenv('PROPERTY_ID')


dimesions = ['userAgeBracket', 'language', 'brandingInterest', 'userGender'] 

# Example of one request for each dimension with activeUsers metric
for dimesion in dimesions:
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name=dimesion)],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2022-04-11", end_date="today")],
    )
    time.sleep(5)
    response = client.run_report(request)

    print(f'Results of active users by {dimesion} dimension')
    for row in response.rows:
        print(row.dimension_values[0].value, row.metric_values[0].value)
