WITH counts AS (
 SELECT borough, complaint_type, COUNT(*) AS requests
 FROM requests WHERE borough IS NOT NULL AND complaint_type IS NOT NULL
 GROUP BY borough, complaint_type
), ranked AS (
 SELECT borough, complaint_type, requests,
        ROW_NUMBER() OVER (PARTITION BY borough ORDER BY requests DESC, complaint_type) AS rank,
        ROUND(100.0 * requests / SUM(requests) OVER (PARTITION BY borough), 2) AS borough_pct
 FROM counts
)
SELECT * FROM ranked WHERE rank <= 5 ORDER BY borough, rank;
