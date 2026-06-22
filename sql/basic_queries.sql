-- View first 5 records
SELECT * FROM "01_fund_master"
LIMIT 5;

-- Count NAV records
SELECT COUNT(*) AS total_records
FROM "02_nav_history";

-- Distinct fund houses
SELECT DISTINCT fund_house
FROM "01_fund_master";

-- Top 10 schemes by AUM
SELECT fund_house,
       aum_crore
FROM "03_aum_by_fund_house"
ORDER BY aum_crore DESC
LIMIT 10;

-- Category inflows
SELECT category,
       inflow_cr
FROM "05_category_inflows"
ORDER BY inflow_cr DESC;
