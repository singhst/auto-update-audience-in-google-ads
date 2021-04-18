"""Get top 3 audience's interests from Google Analytics through API.

-----------------------------------

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.

-----------------------------------

Tutorial,
https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py

What report can be extracted from GA Report API,
https://ga-dev-tools.appspot.com/dimensions-metrics-explorer/

"""


from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

KEY_FILE_LOCATION = "././json_key_from_gcp.json"
VIEW_ID = "234785120"

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
# KEY_FILE_LOCATION = '<REPLACE_WITH_JSON_FILE>'
# VIEW_ID = '<REPLACE_WITH_VIEW_ID>'

GA_INTEREST_CATEGORIES = ['ga:interestOtherCategory',
                          'ga:interestAffinityCategory', 'ga:interestInMarketCategory']


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


def get_report(analytics, dimension: str):
    """Queries the Analytics Reporting API V4.

    Args:
        analytics: An authorized Analytics Reporting API V4 service object.
        dimension: `str`, ga:interestOtherCategory; ga:interestAffinityCategory; ga:interestInMarketCategory
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
                    'dimensions': [{'name': dimension}]
                }]
        }
    ).execute()


def get_top3_interest(response):
    """Rank the interest of audiences from the Analytics Reporting API V4 response.

    Args:
        response: An Analytics Reporting API V4 response.
    Returns:
        categoryName:   `str`, the name of the top 3 interests.
        top3Interests:  `list of turple`, names of top 3 interests with num of visit.
    """

    # print(response)

    for report in response.get('reports', []):
        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        categoryName = dimensionHeaders[0]
        # print('> categoryName:', categoryName)

        dimList = []
        valList = []

        for row in report.get('data', {}).get('rows', []):
            dimensions = row.get('dimensions')[0]
            dateRangeValues = row.get('metrics', [])
            dimList.append(dimensions)

            for metric in dateRangeValues:
                value = int(metric.get('values')[0])
                valList.append(value)
        # print('> dimList:', dimList)
        # print('> valList:', valList)

        dicDimVal = dict(zip(dimList, valList))
        sortedList = sort_dict_by_value(dicDimVal)
        top3Interests = []
        for item in sortedList[:3]:
            top3Interests.append(item[0])
        # print('> top3Interests:', top3Interests)

    return categoryName, top3Interests


def sort_dict_by_value(dic: dict = {'a': 3, 'b': 5, 'c': 1, 'd': 2, 'e': 4}) -> list:
    """Sort the key:value pair in the dictionary by its value descendingly.

    Args:
        dic: `dict`
    Returns:
        `list`, The descending sorted `dict` by value.
    """
    # return sorted(dic.items(), key=lambda x: x[1])      #ascendingly
    return sorted(dic.items(), key=lambda x: -x[1])     # descendingly


def print_response(response):
    """Parses and prints the Analytics Reporting API V4 response.

    Args:
        response: An Analytics Reporting API V4 response.
    """

    print(response)

    # for report in response.get('reports', []):
    #     columnHeader = report.get('columnHeader', {})
    #     dimensionHeaders = columnHeader.get('dimensions', [])
    #     metricHeaders = columnHeader.get(
    #         'metricHeader', {}).get('metricHeaderEntries', [])

    #     for row in report.get('data', {}).get('rows', []):
    #         dimensions = row.get('dimensions', [])
    #         dateRangeValues = row.get('metrics', [])

    #         for header, dimension in zip(dimensionHeaders, dimensions):
    #             print(header + ': ', dimension)

    #         for i, values in enumerate(dateRangeValues):
    #             print('Date range:', str(i))
    #             for metricHeader, value in zip(metricHeaders, values.get('values')):
    #                 print(metricHeader.get('name') + ':', value)


def main() -> list:
    analytics = initialize_analyticsreporting()

    """The format,

        allTop3 = [
            {
                'category': 'xxx1',
                'top3': ['interest': 'xxx1','interest': 'xxx2','interest': 'xxx3']
            },
            {...},
            {...}
        ]
    """
    allTop3 = []

    for category in GA_INTEREST_CATEGORIES:
        # ga:interestOtherCategory, ga:interestAffinityCategory, ga:interestInMarketCategory
        response = get_report(analytics, category)
        categoryName, top3InterestsPerCategory = get_top3_interest(response)
        # print('> categoryName:', categoryName)
        # print('> top3InterestsPerCategory:', top3InterestsPerCategory)

        allTop3.extend(top3InterestsPerCategory)

    # print(allTop3)

    return allTop3


if __name__ == '__main__':
    print('hi')

    # Get top 3 interests from Analytics Reporting API V4
    top3Interests = main()
    print(top3Interests)
