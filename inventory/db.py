import pyodbc
import json
import os

# Config file path
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.json")

# Load connection string from config.json
with open(CONFIG_FILE) as f:
    config = json.load(f)

DEFAULT_CONN_STRING = config["DefaultConnection"]

def get_default_connection():
    """Connect to default CRM database"""
    try:
        conn = pyodbc.connect(DEFAULT_CONN_STRING)
        print("✅ Connected to Default CRM Database (HKIADVCRM)")
        return conn
    except Exception as e:
        print("❌ Error connecting default DB:", e)
        import traceback
        traceback.print_exc()
        return None
