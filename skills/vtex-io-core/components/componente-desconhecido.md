<!-- SCRAPED:START -->
# Componente Desconhecido

Storefront Development](</docs/storefront-development>)

[Store Framework](</docs/guides/store-framework>)

[Implementing Google One-tap login](</docs/guides/vtex-io-documentation-implementing-google-one-tap-login>)

Implementing Google One-tap login

Learn how to implement the Google One-tap login in your Store Framework store.

In this guide, you'll learn how to set up the Google One-tap login feature in your store.

Google One-tap authenticates users through a pop-up, creating a streamlined login experience. With this feature, a small pop-up is displayed, allowing returning users to sign in with a single click.

![{"base64":"  ","img":{"width":640,"height":436,"type":"gif","mime":"image/gif","wUnits":"px","hUnits":"px","length":7993508,"url":"https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-one-tap-login-0.gif"}}](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-one-tap-login-0.gif)

## Before you begin

### Use a store built with Store Framework

Ensure your store has a Store Theme developed following the Storefront guide.

### Install the `vtex.login` app

  1. In your terminal, log in to your account by running the `vtex login {{accountName}}` command. Replace the curly brackets with your account name.
  2. Run the `vtex install vtex.login@2.x` to install the `vtex.login` app in your store.



### Configure the Google OAuth 2.0 integration

The One-tap flow requires the store to have Google OAuth login set up. Learn more in the guide [Adding a Client Id and a Client Secret to log in with Google](<https://help.vtex.com/docs/tutorials/adding-a-client-id-and-a-client-secret-to-log-in-with-google?locale=en>).

## Instructions

### Step 1 - Set up the Google OAuth 2.0 app

  1. In the [Google Developers Console](<https://console.developers.google.com/>), go to the Google OAuth 2.0 configuration page.
  2. Add all store domains to the **Authorized domains** list. Learn more in Google's guide [Authorized Domains](<https://support.google.com/cloud/answer/15549257?visit_id=638985718078812310-3040234660&rd=1#authorized-domains>).



![{"base64":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAABCAIAAAB2XpiaAAAACXBIWXMAAAsTAAALEwEAmpwYAAAESXRFWHRSYXcACmljYwogICAgIDUzMgowMDAwMDIxNDYxNzA3MDZjMDQwMDAwMDA2ZDZlNzQ3MjUyNDc0MjIwNTg1OTVhMjAwN2U0MDAwNzAwMWQwMDA5MDAzOTAwMWYKNjE2MzczNzA0MTUwNTA0YzAwMDAwMDAwNDE1MDUwNGMwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDBmNmQ2CjAwMDEwMDAwMDAwMGQzMmQ2MTcwNzA2Y2MxYjUzNDg5M2Y4N2JiZDIyYTczZmE5ZjI3NmY5Mzc2MDAwMDAwMDAwMDAwMDAwMAowMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMGE2NDY1NzM2MzAwMDAwMGZjMDAwMDAwNjYKNjM3MDcyNzQwMDAwMDE2NDAwMDAwMDIzNzc3NDcwNzQwMDAwMDE4ODAwMDAwMDE0NzI1ODU5NWEwMDAwMDE5YzAwMDAwMDE0CjY3NTg1OTVhMDAwMDAxYjAwMDAwMDAxNDYyNTg1OTVhMDAwMDAxYzQwMDAwMDAxNDcyNTQ1MjQzMDAwMDAxZDgwMDAwMDAxMAo2MzY4NjE2NDAwMDAwMWU4MDAwMDAwMmM2MjU0NTI0MzAwMDAwMWQ4MDAwMDAwMTA2NzU0NTI0MzAwMDAwMWQ4MDAwMDAwMTAKNjQ2NTczNjMwMDAwMDAwMDAwMDAwMDBjNDQ0NTRjNGMyMDUwMzIzMzMxMzk0ODAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwCjAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMAowMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzQ2NTc4NzQKMDAwMDAwMDA0MzZmNzA3OTcyNjk2NzY4NzQyMDQxNzA3MDZjNjUyMDQ5NmU2MzJlMmMyMDMyMzAzMjMwMDAwMDU4NTk1YTIwCjAwMDAwMDAwMDAwMGYzZDgwMDAxMDAwMDAwMDExNjA4NTg1OTVhMjAwMDAwMDAwMDAwMDA2OGM1MDAwMDM1YzQwMDAwMDExOAo1ODU5NWEyMDAwMDAwMDAwMDAwMDY2OTMwMDAwYjdmNjAwMDAxMTg0NTg1OTVhMjAwMDAwMDAwMDAwMDAyNzdkMDAwMDEyNDYKMDAwMGMwOTA3MDYxNzI2MTAwMDAwMDAwMDAwMDAwMDAwMDAxZjYwNDczNjYzMzMyMDAwMDAwMDAwMDAxMGJiNzAwMDAwNTk2CmZmZmZmMzU3MDAwMDA3MjkwMDAwZmRkN2ZmZmZmYmI3ZmZmZmZkYTYwMDAwMDNkYTAwMDBjMGY2CkAg2GsAAAASSURBVHicY1BQVJwxY8ZFMAAAI6cHEagemasAAAAASUVORK5CYII=","img":{"src":"https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-one-tap-login-1.png","width":469,"height":134,"type":"png"}}](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-one-tap-login-1.png)

> Include both the website domain and the `{{accountName}}.myvtex.com` domain. The restricted `.myvtex.com` domain may be used for testing purposes.

For more details on how to set up the Google OAuth app, refer to Google's documentation: [Configure your OAuth Consent Screen](<https://developers.google.com/identity/one-tap/web/guides/get-google-api-clientid#configure_your_oauth_consent_screen>) and [Setting up OAuth 2.0](<https://support.google.com/cloud/answer/6158849>).

### Step 2 - Configure One-tap on Site Editor

  1. In the VTEX Admin, go to **Storefront > Site Editor**.

  2. In the side menu, click the **Login** block. A new section for Google One-tap will be displayed.

  3. Check the **Enable Google One-tap sign up** toggle to enable the feature in your store's Site Editor.

  4. Configure the following settings:

     * **Google One-tap alignment:** Choose which side of the page the pop-up appears on. Possible values: `Right` or `Left`.
     * **Google One-tap top margin:** Set the top margin for the pop-up. This field accepts standard CSS [`top`](<https://developer.mozilla.org/pt-PT/docs/Web/CSS/top>) values (for example: `10px`, `4rem`).
  5. Click `Save`.

![{"base64":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAIAAAA7ljmRAAAACXBIWXMAAAPoAAAD6AG1e1JrAAAAMklEQVR4nAEnANj/AOzq5+/v6vLx7/r5+gDm5ufS0dft7e3///8AERs/AAEuNjpa/f39UJMake+IZXEAAAAASUVORK5CYII=","img":{"src":"https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-one-tap-login-2.gif","width":1067,"height":752,"type":"gif"}}](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-one-tap-login-2.gif)




After following these steps, the Google One-tap feature will be active, and the pop-up will appear for signed-out users browsing your store.

## Google One-tap flow

Google One-tap flow is implemented by the [`vtex.login`](<https://developers.vtex.com/docs/apps/vtex.login>) app. The process is described below:

  1. `vtex.login` checks if the user is logged in. The One-tap flow only starts for logged-out users.

  2. `vtex.login` calls the [VTEX ID API](<https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#vtex-id>) to get the store's OAuth `clientId`.

  3. `vtex.login` triggers the One-tap pop-up.

  4. The user clicks the **Continue as** button.

  5. Google checks the user's identity and returns a JSON Web Token (JWT) to `vtex.login`.

  6. `vtex.login` POSTs a form containing the JWT and redirects the user to an endpoint at the VTEX ID API.

  7. The API validates the JWT and redirects the user back to the website.

![{"base64":"  ","img":{"width":2016,"height":1718,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":226130,"url":"https://vtexhelp.vtexassets.com/assets/docs/src/google-one-tap___033c5242b3695b9dff2fa9aea304b959.png"}}](https://vtexhelp.vtexassets.com/assets/docs/src/google-one-tap___033c5242b3695b9dff2fa9aea304b959.png)
<!-- SCRAPED:END -->
