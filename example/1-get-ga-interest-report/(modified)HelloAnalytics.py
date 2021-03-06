"""
Tutorial,
https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py

What report can be extracted from GA Report API,
https://ga-dev-tools.appspot.com/dimensions-metrics-explorer/
"""

"""Hello Analytics Reporting API V4."""


from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import os
import configparser
config = configparser.ConfigParser()
# config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
current_file = os.path.abspath(os.path.dirname(__file__))
parent_of_parent_dir = os.path.join(current_file, '../../')
config.read(os.path.join(parent_of_parent_dir, 'config.ini'))

KEY_FILE_LOCATION = config['file_locations']['JSON_KEY_FILE_PATH']
VIEW_ID = config['ga_settings']['VIEW_ID']

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
# KEY_FILE_LOCATION = '<REPLACE_WITH_JSON_FILE>'
# VIEW_ID = '<REPLACE_WITH_VIEW_ID>'


def initialize_analyticsreporting():
    """Initializes an Analytics Reporting API V4 service object.

    Returns:
      An authorized Analytics Reporting API V4 service object.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        KEY_FILE_LOCATION, SCOPES)

    # Build the service object.
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics


def get_report(analytics):
    """Queries the Analytics Reporting API V4.

    Args:
      analytics: An authorized Analytics Reporting API V4 service object.
    Returns:
      The Analytics Reporting API V4 response.
    """
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': VIEW_ID,
                    'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                    # 'metrics': [{'expression': 'ga:sessions'}],
                    # 'dimensions': [{'name': 'ga:country'}]
                    'dimensions': [{'name': 'ga:interestOtherCategory'}]    #ga:interestOtherCategory, ga:interestAffinityCategory, ga:interestInMarketCategory
                }]
        }
    ).execute()


def print_response(response):
    """Parses and prints the Analytics Reporting API V4 response.

    Args:
      response: An Analytics Reporting API V4 response.
    """
    for report in response.get('reports', []):
        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get(
            'metricHeader', {}).get('metricHeaderEntries', [])

        for row in report.get('data', {}).get('rows', []):
            dimensions = row.get('dimensions', [])
            dateRangeValues = row.get('metrics', [])

            for header, dimension in zip(dimensionHeaders, dimensions):
                print(header + ': ', dimension)

            for i, values in enumerate(dateRangeValues):
                print('Date range:', str(i))
                for metricHeader, value in zip(metricHeaders, values.get('values')):
                    print(metricHeader.get('name') + ':', value)


def main():
    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    print_response(response)


if __name__ == '__main__':
    print('hi')
    main()
