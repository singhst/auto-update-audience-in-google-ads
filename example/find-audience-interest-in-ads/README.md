# Setup to follow

Check out the below link,

https://developers.google.com/google-ads/api/docs/first-call/overview

# Info of Parameters 

Info ==> https://developers.google.com/google-ads/api/docs/first-call/overview#config



`developer_token`:

Grants access to the Ads API, not to a particular Ads account. Once the developer token is approved, the same token for requests can be used against all our Google Ads accounts, even if they're not linked to the manager account associated with the developer token. **<u>ONLY Manager Account</u> have developer token**.

We can retrieve the developer token by signing in to our manager account then navigating to the **API Center (TOOLS & SETTINGS > SETUP > API Center)**.



`client ID` and `client secret`:

The OAuth2 `client ID` and `client secret` can be created in GCP > APIs & Services > Credentials. 

<img src="img\gcp-credential.jpg" style="zoom:50%;" /> 



`client_secret credential.json`:

Download from each `OAuth 2.0 client` name under GCP > APIs & Services > Credentials > GCP OAuth2.0 Client IDs.



`refresh_token` and `access token`:

Use `authenticate_in_desktop_application.py` to generate.



`login_customer_id`:

The Ads customer ID of Manager Account. 



# Usage of Files

`authenticate_in_desktop_application.py`:   Use to generate the OAuth2 (1) `access token` and (2) `refresh token`.

    Link to follow,
    
    https://developers.google.com/google-ads/api/docs/client-libs/python/oauth-desktop#step_3_-_generating_a_refresh_token

`list_accessible_customers.py`: Use to test whether the parameters in `google-ads.yaml` set correctly or not. If correct, program outputs all Ads accounts `Customer ID`. 

Four OAuth2 configuration parameters need to set in `google-ads.yaml`,
1. `developer_token`

    e.g. If parameters set correctly,

        Total results: 4
        Customer resource name: "customers/11******15"
        Customer resource name: "customers/88******91"
        Customer resource name: "customers/92******07"
        Customer resource name: "customers/96******95"

