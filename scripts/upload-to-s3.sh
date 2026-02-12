#!/bin/bash
# Script qui écrit la date dans un fichier et l'uploade vers S3

BUCKET_NAME="m2-cloud-logs-mouhamed"
FILENAME="$(date +%Y%m%d-%H%M%S).txt"
TMPFILE="/tmp/${FILENAME}"

echo "Date: $(date)" > "$TMPFILE"
echo "Hostname: $(hostname)" >> "$TMPFILE"
echo "Instance ID: $(ec2-metadata --instance-id | cut -d' ' -f2)" >> "$TMPFILE"

aws s3 cp "$TMPFILE" "s3://${BUCKET_NAME}/${FILENAME}"
rm -f "$TMPFILE"

echo "Fichier uploadé: s3://${BUCKET_NAME}/${FILENAME}"