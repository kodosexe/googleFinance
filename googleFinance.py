##########################
#     Author: kodos      #
#   Date: Feb 9, 2021   #
# Purpose: Stock Trading #
#  email:info@kodos.dev  #
##########################


# Make imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

# Make google search string
def makeString(asset):
    return "https://www.google.com/search?q=" + asset

# Builtin Sanity check (NOT IMPLEMENTED YET):
#
# Code -1 Asset doesn't exist
# Code -2 Failed getting the page
# Code -3 Something else went wrong
# Code -4 Price given as zero
# Anything >0 Price
def getStockPrice(sign):
    searchLink = makeString(sign)

    # Set up ChromeOptions
    opt = webdriver.ChromeOptions()
    opt.set_headless()
    opt.add_argument("--window-size=1920,1080")
    opt.add_argument("--disable-gpu")

    # Initialize browser, and go to link
    browser = webdriver.Chrome(chrome_options=opt)
    browser.get(searchLink)

    # Inject Chrome console command retrieve data
    js = 'return document.getElementsByClassName("IsqQVc NprOob XcVN5d")[0].innerText'
    data = browser.execute_script(js)

    return data