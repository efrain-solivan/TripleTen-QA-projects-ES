# SQL — Urban Routes Database Integrity Queries

**Sprint:** 5 — Understanding Databases (TripleTen QA Engineering Apprenticeship)  
**Author:** Efrain Solivan  
**Query file:** `urban_routes_data_integrity.sql`  
**Database:** PostgreSQL (TripleTen sandbox)

---

## Purpose

These queries validate the **data integrity of the Urban Routes relational database** — verifying that the data layer reflects the rules the application claims to enforce. They complement API-level testing: an API can return `200 OK` while the underlying rows are in an invalid state.

---

## Schema overview

| Table | Role |
|-------|------|
| `users` | Registered app users |
| `orders` | Ride/delivery orders placed by users |
| `order_products` | Line items linking orders to products |
| `products` | Available products (weight, price) |
| `kits` | Pre-built product bundles |
| `kit_products` | Kit-to-product relationships |
| `deliveries` | Delivery records (courier, status, ETA) |
| `couriers` | Courier profiles |
| `routes` | Route metadata (service type, etc.) |

---

## Queries and what they verify

| # | Query | Expected result | Defect caught if violated |
|---|-------|-----------------|---------------------------|
| 1 | Every order linked to a valid user | All rows JOIN successfully | Orphaned orders (user was deleted without cascading) |
| 2 | Every order has at least one product | `0 rows` returned | Orders created with empty product list — business rule violation |
| 3 | All product prices are positive | `0 rows` returned | Data entry error or default `0` price slipping through |
| 4 | Kit-to-product relationships intact | All kits display their products | Broken kit composition after product deletion |
| 5 | All deliveries reference real orders | `0 rows` returned | Orphaned delivery records (order deleted, delivery row remains) |
| 6 | Couriers with active deliveries | Count per courier | Courier assigned to more deliveries than system should allow |
| 7 | Users with no orders (inactive accounts) | Informational list | Useful for cleanup audits; not a defect by itself |
| 8 | Fast-delivery eligibility per order | `Eligible` / `Not eligible` per order | Misclassification of orders for the fast-delivery calculation |
| 9 | Revenue summary by service type | Aggregated totals | Missing route associations breaking revenue reporting |
| 10 | Duplicate email check | `0 rows` returned | Broken `UNIQUE` constraint on `users.email` |

---

## How to run

**Against the TripleTen sandbox (PostgreSQL):**

1. Connect to the sandbox database using the credentials from your TripleTen course environment
2. Open `urban_routes_data_integrity.sql` in your SQL client (pgAdmin, DBeaver, or `psql`)
3. Execute the full file or run individual queries

```bash
psql -h <sandbox-host> -U <username> -d urban_routes -f sql/urban_routes_data_integrity.sql
```

**Interpreting results:**

Queries 2, 3, 5, and 10 are **pass/fail checks** — any returned rows indicate a defect. The others are **informational** and require manual review of the output.

---

## Complementary automated tests

The `api_db_validation/` project extends these manual checks into a **pytest test suite** that runs against a local SQLite replica of the same schema. It covers:

- Orphan subscriptions (`test_no_orphan_subscriptions`)
- Soft-delete integrity (`test_soft_delete_sets_flag_in_db`)
- Billing against deleted users (`test_no_billing_on_deleted_users`)
- Order state machine (`test_order_state_machine_no_skip`)
- Temporal anomalies (`test_no_temporal_anomalies_in_order_history`)
- Duplicate active subscriptions (`test_no_duplicate_active_subscriptions`)

See [`../api_db_validation/`](../api_db_validation/) for the full automated suite.
