import pymysql
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve credentials
host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT"))
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Establish connection
try:
    conn = pymysql.connect(host=host, port=port, user=user, password=password, database=db_name)
    print("✅ Successfully connected to the database!")
except pymysql.Error as e:
    print(f"❌ Connection error: {e}")

# Close connection
conn.close()
print("🔒 Connection closed.")