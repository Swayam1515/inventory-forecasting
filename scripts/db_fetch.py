from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Create database engine
engine = create_engine(f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

# Define SQL query
query = "SELECT * FROM service_data LIMIT 5;"

# Fetch data using SQLAlchemy
df = pd.read_sql(query, engine)

print(df.head())  # Display results