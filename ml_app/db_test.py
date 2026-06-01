#!/usr/bin/env python3
import psycopg2
import sys

def test_postgres_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="appdb",
            user="admin",
            password="secret"
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print(f"PostgreSQL connected successfully. Version: {version[0]}")
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print(f"PostgreSQL connection failed: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    success = test_postgres_connection()
    sys.exit(0 if success else 1)
