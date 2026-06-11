import pandas as pd
import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

print("Connected! Generating data...")

# Materials data
materials_data = {
    'material_id':   ['MAT-1001', 'MAT-1002', 'MAT-1003', 'MAT-1004', 'MAT-1005'],
    'material_name': ['Alloy Frame', 'Rubber Tire', 'Disc Brake', 'Steel Chain', 'Carbon Pedal'],
    'category':      ['Frames', 'Wheels', 'Brakes', 'Drivetrain', 'Drivetrain'],
    'unit_cost':     [150.00, 25.50, 45.00, 15.20, 35.00]
}
df_materials = pd.DataFrame(materials_data)
print("Materials created!")

# Inventory data
inventory_data = []
plant = 'PLANT-A'

for _, row in df_materials.iterrows():
    current_stock = random.randint(20, 200)
    reorder_point = random.randint(30, 60)
    safety_stock  = int(reorder_point * 0.5)

    inventory_data.append({
        'material_id':   row['material_id'],
        'plant_id':      plant,
        'current_stock': current_stock,
        'safety_stock':  safety_stock,
        'reorder_point': reorder_point
    })

df_inventory = pd.DataFrame(inventory_data)
print("Inventory created!")

# Transactions data
transactions_data = []
end_date   = datetime.now()
start_date = end_date - timedelta(days=30)

for _ in range(200):
    mat_id   = random.choice(df_materials['material_id'].tolist())
    mov_type = random.choice(['IN', 'OUT'])
    qty      = random.randint(50, 100) if mov_type == 'IN' else random.randint(5, 20)
    rand_date = start_date + timedelta(days=random.randint(0, 30))

    transactions_data.append({
        'material_id':      mat_id,
        'plant_id':         plant,
        'quantity_moved':   qty,
        'movement_type':    mov_type,
        'transaction_date': rand_date
    })

df_transactions = pd.DataFrame(transactions_data)
df_transactions = df_transactions.sort_values('transaction_date').reset_index(drop=True)
print("Transactions created!")

# Load data into PostgreSQL
print("Loading data into database...")

df_materials.to_sql('materials', engine, if_exists='append', index=False)
print("Materials loaded!")

df_inventory.to_sql('inventory', engine, if_exists='append', index=False)
print("Inventory loaded!")

df_transactions.to_sql('inventory_transactions', engine, if_exists='append', index=False)
print("Transactions loaded!")

print("All done! Check your database in pgAdmin.")

engine.dispose()