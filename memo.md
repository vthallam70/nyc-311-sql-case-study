# NYC 311: one-day exploratory memo

**Scope.** In the downloaded snapshot, 7,269 requests were created on January 1, 2024. These are reports, not verified incidents or unique people. The figures below describe this single day; they do not establish seasonal patterns, service performance, or underlying need.

**Findings.** Heat/hot water was the leading category in the Bronx (320 reports, 23.49% of Bronx requests). Illegal parking led in Brooklyn (443, 19.40%). Residential noise led in Queens (427, 22.63%) and Manhattan (269, 18.01%). These percentages use all requests in each borough as the denominator, including categories not shown in the top-five export.

**Recommendations.** Review heat/hot water complaint volumes alongside weather and inspection capacity before prioritizing Bronx outreach. Explore the timing and location of parking and noise reports before allocating enforcement or mediation resources. Validate these patterns over several months, normalize by population and account for duplicate requests and reporting access before making borough comparisons or budget decisions.

**Source and method.** NYC Open Data 311 Service Requests, queried for timestamps from 2024-01-01 inclusive to 2024-01-02 exclusive. SQLite query and aggregate CSV are included. Snapshot may differ if records are later updated.
