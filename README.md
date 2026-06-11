# Inventory Tracker — WMS Mini Tool

A lightweight warehouse inventory management system built with Python and PostgreSQL.
Simulates core WMS functionality — tracking materials, monitoring stock levels, and 
logging inventory movements across a plant location.

## What it does
- Maintains a catalogue of materials and components
- Tracks real-time stock levels per plant location
- Logs every inventory movement as IN or OUT transactions
- Flags materials that fall below safety stock thresholds

## Tech Stack
- Python — data generation and database interaction
- PostgreSQL — relational database storage
- pandas — data manipulation and loading
- SQLAlchemy — database connection and ORM

## Database Structure
- materials — master catalogue of parts and components
- inventory — stock levels per material per plant
- inventory_transactions — full log of every stock movement

## Key SQL Queries
- Critical stock alert — identifies items below safety stock level
- Transaction history — filters movements by date range
- Inventory overview — joined view of stock levels with material details