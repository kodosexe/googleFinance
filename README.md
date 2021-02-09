Library to get stock prices from Google finance's new design.
Uses webscraping to extract the element from the search page.

# Prerequisites
Selenium installed:
`pip install selenium`

# Usage
```python
import googleFinance
print( googleFinance.getStockPrice("aapl") )
```

# Functions
## getStockPrice()
`googleFinance.getStockPrice(str sign)`
Gets the current price for any sign passed.
Note that it simply searches for that sign. Sometimes, depending on the algorithm, that may not lead to a desired result.
At the current stage, there are NO SANITY CHECKS OR ERROR CHECKS included in this library. Use with caution.
To go around this issue, you may want a string comprised of `sign + " stock price"` or similar.

### Disclaimer
I do not advise you to gamble with monetary assets. This library is provided as-is and I do not assume liability for any losses, errors or damages due to mishandling or error of this code.
Use at your own risk