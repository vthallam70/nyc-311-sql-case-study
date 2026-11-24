# NYC 311 SQL case study

This project downloads NYC 311 requests, loads them into SQLite, ranks the five most common complaint categories by borough with CTEs and window functions, and exports a CSV suitable for Tableau or Power BI. The included interactive HTML dashboard displays the same results. No Tableau or Power BI workbook has been created.

```sh
python collect.py --start 2024-01-01 --end 2024-01-02 --limit 50000
python make_dashboard.py
open dashboard.html
```

The included extract is a one-day snapshot of 7,269 requests created January 1, 2024. If the limit is reached, the script warns that the results may be truncated. See [memo.md](memo.md) for observations and limitations. The dataset is periodically updated, so a future download may differ. Source: https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9
