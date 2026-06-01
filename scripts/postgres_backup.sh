#!/bin/bash
# Simple PostgreSQL backup script
BACKUP_DIR="./backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
CONTAINER_NAME="postgres-db"

mkdir -p $BACKUP_DIR
docker exec $CONTAINER_NAME pg_dump -U admin appdb > "$BACKUP_DIR/appdb_$TIMESTAMP.sql"
echo "Backup saved to $BACKUP_DIR/appdb_$TIMESTAMP.sql"
