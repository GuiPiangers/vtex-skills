<!-- SCRAPED:START -->
# Live Shopping

[VTEX IO Apps](</docs/vtex-io-apps>)

Business tools

Live commerce

Live Shopping

Official extension

Version: 3.28.1

Latest version: 3.28.1

The Live Shopping app allows businesses to engage with their customers in real time by live streaming on their store websites. The app is compatible with both desktop and mobile devices.

![{"base64":"  ","img":{"width":1804,"height":1024,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":604402,"url":"https://user-images.githubusercontent.com/52087100/118993914-49ba2d80-b95c-11eb-9720-dc3b35de3a59.png"}}](https://user-images.githubusercontent.com/52087100/118993914-49ba2d80-b95c-11eb-9720-dc3b35de3a59.png)

![{"base64":"  ","img":{"width":1864,"height":1096,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":764585,"url":"https://user-images.githubusercontent.com/52087100/118993920-4aeb5a80-b95c-11eb-96c1-4e292f3c8133.png"}}](https://user-images.githubusercontent.com/52087100/118993920-4aeb5a80-b95c-11eb-96c1-4e292f3c8133.png)

## Before you start

Live Shopping is a paid app with different subscription plans: **Lite** , **Standard** , and **Pro**. The subscription cost depends on your chosen plan, each providing a specific number of monthly live stream minutes.

For more information about the plans and pricing, refer to the [Live Shopping App Store page](<https://apps.vtex.com/liveshopping/p>).

## Installation

### Prerequisites

  * It is necessary to have the CLI VTEX. Go to the next documentation for install it: [VTEX IO CLI](<https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference>)



#### Initial Steps for VTEX IO and VTEX CMS/Headless accounts

  1. Access the [Live Shopping app page on the VTEX App Store](<https://apps.vtex.com/vtexventures-livestreaming/p>).
  2. Click the `Get app` button to install the app in your VTEX account.
  3. Once the app is successfully installed, open your account's Store Theme app using the code editor of your preference (e.g., Visual Studio Code).



> To integrate the **Live Shopping** into a project using [FastStore](<https://developers.vtex.com/docs/guides/faststore>), check the guide [Implementing Live Shopping for FastStore](<https://developers.vtex.com/docs/guides/faststore/storefront-features-implementing-live-shopping-for-faststore>). If your storefront technology is [FastStore v1 or v2](<https://developers.vtex.com/docs/guides/faststore/getting-started-faststore-versions-and-support-levels>), refer to the guide [Implementing Live Shopping for FastStore previous versions](<https://developers.vtex.com/docs/guides/faststore/storefront-features-implementing-live-shopping-for-faststore-previous-versions>).

* * *

### **For VTEX IO**

  1. In the `manifest.json` file, add the app to the theme's peer dependencies list:




```
"peerDependencies": {
        "vtexventures.livestreaming": "0.x"
    }
```


  2. Include the **livestreaming** blick in the desired template. For example:




```
"store.home": {
        "blocks": [
            "livestreaming"
        ]
    }
```


  3. Deploy your changes to the Store Theme app by publishing a **major version**. For details, refer to the guide: [Making Your New App Version Publicly Available](<https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-making-your-new-app-version-publicly-available>).



> **Note** : Adding a new peer dependency to the Store Theme app requires deploying a new major version of the app. After making the changes, publish this new major version and install it in a productive workspace (not master) to ensure it works as expected before deploying it to the live environment.

  4. In the productive workspace, follow the guide [Migrating CMS Settings After a Major Update](<https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-cms-settings-after-major-update>) to update the content for the new version.



> Note: Proceed with caution to avoid deleting store content..

  5. Validate the workspace and confirm the configured content. Once ready, promote the workspace to master (it will be automatically deleted after promotion).



* * *

### **For VTEX CMS/Headless**

Once the application is installed, go to the VTEX Admin and search for the **Live Shopping Events** module **(Apps > Live Shopping > Events)**.

After creating an event and accessing its details, scroll to the bottom of the event details page. You’ll find a section called **Script for Template** , which contains a `<div>` and a `<script>`. These must be added to the store.

For **CMS/Legacy accounts** , ensure that **CMS Template** is selected.

![{"base64":"  ","img":{"width":1558,"height":383,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":214533,"url":"https://raw.githubusercontent.com/vtexdocs/dev-portal-content/refs/heads/main/images/live-shopping-cms-template.png"}}](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/refs/heads/main/images/live-shopping-cms-template.png)

For **Headless accounts** , ensure that External Template is selected.

![{"base64":"  ","img":{"width":1546,"height":377,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":196390,"url":"https://raw.githubusercontent.com/vtexdocs/dev-portal-content/refs/heads/main/images/live-shopping-external-template.png"}}](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/refs/heads/main/images/live-shopping-external-template.png)

The `id` query parameter corresponds to the event ID, which can be found at the top of the event details page and changes for each event. The `account` query parameter represents the account name (e.g., leidygiraldo) and remains constant once set.

It is recommended to copy and paste the full `<script>` tag for each event.

  * Add the `<div>` and `<script>` tags to render the Live Shopping app in the store (cache updates may take 5–10 minutes).



Include them anywhere in the store, such as the home, landing, category, or other pages; for example:

Home page:


```
<div id="nz-player"></div>
<script id="nz-player-script" type="module" src="https://cdn.nizza.com/player-script/prod/nz-ps-index.js?id=e5d73082-a374-4b53-a111-c16d4f5b1ee3&#38;account=leidygiraldo&#38;inactiveSidebarProducts=true&#38;inactiveProductsCarousel=false&#38;inactivateChat=true&#38;inactivateLike=true&#38;inactivateViewers=true&#38;isInfinite=true&#38;time=10&#38;pdp=false&#38;kuikpay=false&#38;quickView=true"></script>
```


![{"base64":"  ","img":{"width":1570,"height":591,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":241165,"url":"https://raw.githubusercontent.com/vtexdocs/dev-portal-content/refs/heads/main/images/live-shopping-home-page.png"}}](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/refs/heads/main/images/live-shopping-home-page.png)

Add the tags for active events and remove them once the event ends to avoid displaying the recording.

* * *

Once you have everything set up (whether for VTEX IO, CMS, or Headless), check out the [app behavior on VTEX Admin](<https://help.vtex.com/en/tutorial/live-shopping--1cYWPIbjNMyr072sksHSVL>)

Learn about the Live Shopping configuration of [events](<https://help.vtex.com/en/tutorial/live-shopping-eventos--6aGLiqoKG1UoS30f3FFWch#>) and [configuring a landing page](<https://help.vtex.com/tutorial/live-shopping-configuring-a-landing-page-for-live-shopping-events--4iBDPEpXyKSfoIqUdwHGFE#>).

### **For FastStore**

**Live Shopping** is available as a native solution for [FastStore](<https://developers.vtex.com/docs/guides/faststore>). A step-by-step guide on how to integrate this feature into your project can be found in [Implementing Live Shopping for FastStore](<https://developers.vtex.com/docs/guides/faststore/storefront-features-implementing-live-shopping-for-faststore>).

> If your storefront technology is [FastStore v1 or v2](<https://developers.vtex.com/docs/guides/faststore/getting-started-faststore-versions-and-support-levels>), refer to the guide [Implementing Live Shopping for FastStore previous versions](<https://developers.vtex.com/docs/guides/faststore/storefront-features-implementing-live-shopping-for-faststore-previous-versions>).

* * *
<!-- SCRAPED:END -->
