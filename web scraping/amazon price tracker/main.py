import requests
from bs4 import BeautifulSoup

website = "https://www.amazon.in/ASUS-VivoBook-i5-1135G7-Integrated-X415EA-EB572TS/dp/B09BF65Z1V/ref=sr_1_12?brr=1&qid=1662630290&rd=1&sr=8-12"

header = {
    "Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

response = requests.get(url=website, headers=header)

soup = BeautifulSoup(response.text, "html.parser")
# prices = soup.select("html > body > div#page > div.off-canvas-content > div#content_container.row > div.column > div#content.content.clearfix.inner > div.row.column > div.padded.margined > div#gistories.row.show-for-large > div.column.small-12.large-4 > div > div.row.column > div.row > div.column.small-12 > table.product_pane > tbody > tr > td")
prices = soup.select("body.a-aui_72554-c a-aui_accordion_a11y_role_354025-c a-aui_killswitch_csa_logger_372963-c a-aui_launch_2021_ally_fixes_392482-c a-aui_pci_risk_banner_210084-c a-aui_preload_261698-c a-aui_rel_noreferrer_noopener_309527-c a-aui_template_weblab_cache_333406-c a-aui_tnr_v2_180836-c a-meter-animate > div#ppd > div#centerCol.centerColAlign.centerColAlign-bbcxoverride > div#apex_desktop.celwidget > div#corePrice_desktop.celwidget > div.a-section.a-spacing-small > table.a-lineitem.a-align-top > tbody > tr > tda.a-span12 > span.a-price.a-text-price.a-size-medium.apexPriceToPay > spam")
tags = [price.getText() for price in prices]

print(tags)