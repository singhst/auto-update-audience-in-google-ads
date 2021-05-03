"""This example create "CustomAffinityInfo" and "CustomIntentInfo" targeting Audiences in ad group.

see https://developers.google.com/google-ads/api/docs/targeting/criteria

AdGroupCriterionService,
https://developers.google.com/google-ads/api/reference/rpc/v7/AdGroupCriterionService#mutateadgroupcriteria
"""

#!/usr/bin/env python
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import argparse
import sys
import uuid

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException


def main(client, customer_id, campaign_id):
    user_list_service = client.get_service("UserListService")
    # campaign_service = client.get_service("CampaignService")
    print("1", user_list_service.__dict__)

    user_list_request = client.get_type("UserInterestInfo")
    print("2", user_list_request)
    


if __name__ == "__main__":
    # GoogleAdsClient will read the google-ads.yaml configuration file in the
    # home directory if none is specified.
    import os
    current_file = os.path.abspath(os.path.dirname(__file__))
    parent_of_parent_dir = os.path.join(current_file, '../../')
    path = os.path.join(parent_of_parent_dir, 'google-ads.yaml')
    googleads_client = GoogleAdsClient.load_from_storage(path, version="v6")

    parser = argparse.ArgumentParser(
        description="Adds an ad group for specified customer and campaign id."
    )
    # The following argument(s) should be provided to run the example.
    parser.add_argument(
        "-c",
        "--customer_id",
        type=str,
        required=True,
        help="The Google Ads customer ID.",
    )
    parser.add_argument(
        "-i", "--campaign_id", type=str, required=True, help="The campaign ID."
    )
    args = parser.parse_args()

    try:
        main(googleads_client, args.customer_id, args.campaign_id)
    except GoogleAdsException as ex:
        print(
            f'Request with ID "{ex.request_id}" failed with status '
            f'"{ex.error.code().name}" and includes the following errors:'
        )
        for error in ex.failure.errors:
            print(f'	Error with message "{error.message}".')
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")
        sys.exit(1)
