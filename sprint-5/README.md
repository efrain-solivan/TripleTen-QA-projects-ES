# Sprint 5 — Understanding Databases

## Project 5: Exploring Startup Trends with SQL

**Program:** TripleTen QA Engineering Apprenticeship  
**Sprint:** 5 — Understanding Databases  
**Duration:** 1 hr 20 min (10 auto-graded tasks)  
**Status:** ✅ Completed (auto-graded, no submission required)  
**Achievement:** 🏅 SQL Data Specialist

---

## 📄 SQL Queries

See [`../sql/urban_routes_data_integrity.sql`](../sql/urban_routes_data_integrity.sql) for the SQL validation queries written for the Urban Routes database.

---

## What I Did

Completed 10 auto-graded SQL tasks set at a simulated venture capital research firm called **VentureInsight**. Their platform stores startup and investment data in a relational PostgreSQL database, and I was asked to write queries to surface business insights for VC clients.

---

## Database Schema (Key Tables)

| Table | Description |
|---|---|
| `companies` | Startup company records |
| `funding_rounds` | Investment round data per company |
| `investors` | Investor / fund records |
| `people` | Founders and executives |
| `education` | Degrees held by company founders |

---

## SQL Skills Demonstrated

| Skill | Example |
|---|---|
| SELECT with WHERE filters | Filter companies by country, status |
| Aggregate functions | COUNT, SUM, AVG, MAX, MIN |
| GROUP BY + HAVING | Group funding rounds by investor activity |
| JOIN (INNER, LEFT) | Join companies to funding_rounds to investors |
| Subqueries | Nested SELECT for filtering by computed values |
| CASE WHEN | Categorize fund activity level (high/middle/low) |
| ROUND, TRUNC | Round average funding amounts |
| NULL handling | Filter out or include NULL values in analysis |
| Date functions | Extract year from timestamps |
| String functions | Concatenate and format output |

---

## Sample Query

Below is an example of one of the more complex tasks — categorizing investment funds by activity level and calculating the average number of funding rounds they participate in:

```sql
SELECT
    activity_level,
    ROUND(AVG(total_rounds)) AS avg_rounds
FROM (
    SELECT
        CASE
            WHEN COUNT(DISTINCT fr.company_id) >= 100 THEN 'high_activity'
            WHEN COUNT(DISTINCT fr.company_id) >= 20  THEN 'middle_activity'
            ELSE 'low_activity'
        END AS activity_level,
        COUNT(fr.id) AS total_rounds
    FROM investors i
    JOIN funding_rounds fr ON i.id = fr.investor_id
    GROUP BY i.id
) sub
GROUP BY activity_level;
```

---

## Key Skills Demonstrated

- Writing multi-table JOIN queries to extract relational data
- Using aggregate functions and GROUP BY for analytical summaries
- Applying CASE WHEN logic for data categorization
- Handling NULL values correctly in SQL queries
- Reading an unfamiliar schema and mapping it to business questions
