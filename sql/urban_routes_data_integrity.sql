-- ============================================================
-- Urban Routes — Database Integrity Validation Queries
-- Project: TripleTen QA Engineering Apprenticeship
-- Author: Efrain Solivan
-- Tool: PostgreSQL (TripleTen sandbox)
-- Sprint: 5 — Understanding Databases (Urban Routes data integrity)
-- Note: The README describes Sprint 5 as "Startup trends analysis
--       (auto-graded)." This file contains supplemental Urban Routes
--       data integrity queries written alongside that sprint work.
-- ============================================================

-- ── 1. Verify every order is linked to a valid user ──────────
SELECT
    o.order_id,
    o.user_id,
    u.first_name,
    u.last_name,
    o.created_at
FROM orders o
JOIN users u ON o.user_id = u.user_id
ORDER BY o.created_at DESC;

-- ── 2. Confirm every order has at least one product ──────────
SELECT
    o.order_id,
    COUNT(op.product_id) AS product_count
FROM orders o
LEFT JOIN order_products op ON o.order_id = op.order_id
GROUP BY o.order_id
HAVING COUNT(op.product_id) = 0;
-- Expected: 0 rows (all orders should have products)

-- ── 3. Check product prices are positive ─────────────────────
SELECT
    product_id,
    name,
    price
FROM products
WHERE price <= 0;
-- Expected: 0 rows

-- ── 4. Validate kit-to-product relationships ─────────────────
SELECT
    k.kit_id,
    k.name AS kit_name,
    p.product_id,
    p.name AS product_name,
    kp.quantity
FROM kits k
JOIN kit_products kp ON k.kit_id = kp.kit_id
JOIN products p ON kp.product_id = p.product_id
ORDER BY k.kit_id, p.name;

-- ── 5. Confirm delivery records reference real orders ─────────
SELECT
    d.delivery_id,
    d.order_id,
    d.courier_id,
    d.status,
    d.estimated_time
FROM deliveries d
LEFT JOIN orders o ON d.order_id = o.order_id
WHERE o.order_id IS NULL;
-- Expected: 0 rows (no orphaned deliveries)

-- ── 6. Couriers with active deliveries ───────────────────────
SELECT
    c.courier_id,
    c.first_name || ' ' || c.last_name AS courier_name,
    COUNT(d.delivery_id) AS active_deliveries
FROM couriers c
JOIN deliveries d ON c.courier_id = d.courier_id
WHERE d.status = 'in_transit'
GROUP BY c.courier_id, courier_name
ORDER BY active_deliveries DESC;

-- ── 7. Users with no orders (inactive accounts) ──────────────
SELECT
    u.user_id,
    u.first_name,
    u.last_name,
    u.email
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE o.order_id IS NULL;

-- ── 8. Fast-delivery eligibility check ───────────────────────
SELECT
    o.order_id,
    SUM(op.quantity * p.weight_kg) AS total_weight_kg,
    SUM(op.quantity) AS total_items,
    CASE
        WHEN SUM(op.quantity * p.weight_kg) <= 6
        AND SUM(op.quantity) <= 6
        THEN 'Eligible'
        ELSE 'Not eligible'
    END AS fast_delivery_status
FROM orders o
JOIN order_products op ON o.order_id = op.order_id
JOIN products p ON op.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;

-- ── 9. Revenue summary by service type ───────────────────────
SELECT
    r.service_type,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_revenue,
    AVG(o.total_amount) AS avg_order_value
FROM orders o
JOIN routes r ON o.route_id = r.route_id
GROUP BY r.service_type
ORDER BY total_revenue DESC;

-- ── 10. Duplicate email check ─────────────────────────────────
SELECT
    email,
    COUNT(*) AS occurrences
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
-- Expected: 0 rows (all emails unique)

-- ── 11. Rank users by order volume (window function — RANK) ───
-- Shows intermediate SQL: window function over a grouped result.
-- Use case: identify top customers without a subquery.
SELECT
    u.user_id,
    u.first_name || ' ' || u.last_name AS customer_name,
    COUNT(o.order_id)                  AS total_orders,
    RANK() OVER (
        ORDER BY COUNT(o.order_id) DESC
    )                                  AS order_rank
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id, customer_name
ORDER BY order_rank;

-- ── 12. Cumulative revenue over time (SUM window — running total) ─
-- Running total lets QA verify no revenue disappears between snapshots.
-- A drop in cumulative_revenue signals a data integrity issue.
SELECT
    DATE(o.created_at)                          AS order_date,
    SUM(o.total_amount)                         AS daily_revenue,
    SUM(SUM(o.total_amount)) OVER (
        ORDER BY DATE(o.created_at)
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    )                                           AS cumulative_revenue
FROM orders o
GROUP BY DATE(o.created_at)
ORDER BY order_date;

-- ── 13. Couriers above average delivery volume (multi-JOIN + HAVING) ─
-- Identifies high-load couriers for capacity and fairness audits.
-- HAVING with a correlated subquery pushes past basic aggregation.
SELECT
    c.courier_id,
    c.first_name || ' ' || c.last_name AS courier_name,
    COUNT(d.delivery_id)               AS completed_deliveries
FROM couriers c
JOIN deliveries d ON c.courier_id = d.courier_id
WHERE d.status = 'delivered'
GROUP BY c.courier_id, courier_name
HAVING COUNT(d.delivery_id) > (
    SELECT AVG(delivery_count)
    FROM (
        SELECT COUNT(delivery_id) AS delivery_count
        FROM deliveries
        WHERE status = 'delivered'
        GROUP BY courier_id
    ) courier_volumes
)
ORDER BY completed_deliveries DESC;
