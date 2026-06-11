-- Query 1: See all materials
SELECT * FROM materials;

-- Query 2: See all inventory levels
SELECT * FROM inventory;

-- Query 3: Critical stock alert
-- Shows items where stock has fallen below safety level
SELECT
    m.material_name,
    m.category,
    i.current_stock,
    i.safety_stock,
    i.reorder_point
FROM inventory i
JOIN materials m ON i.material_id = m.material_id
WHERE i.current_stock <= i.safety_stock;

-- Query 4: All transactions in last 7 days
SELECT *
FROM inventory_transactions
WHERE transaction_date >= NOW() - INTERVAL '7 days'
ORDER BY transaction_date DESC;
