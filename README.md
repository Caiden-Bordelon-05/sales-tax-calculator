# Sales Tax Calculator

A standalone desktop calculator (separate from `currency-exchange`) that:

- accepts a total price input
- lets you select from all 50 U.S. states
- uses the selected state's sales tax rate to calculate the final total
- shows output in three columns: **Price**, **Sales Tax Rate**, **Total**

## Run

From this folder:

```powershell
py sales_tax_calculator.py
```

## Notes

- Tax rates are statewide base rates and are mapped directly to each state in the dropdown.
- Local city/county taxes are not included.

## Future Upgrades

- Add local city/county tax support so users can choose a state, then a city/county, and calculate totals with combined rates.
- Add a receipt comparison area where users can save multiple receipts and compare the same purchase across different cities/states.
- Show side-by-side comparison columns (Location, Price, Tax Rate, Tax Amount, Total) to highlight cost differences by location.
