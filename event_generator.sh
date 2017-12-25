#!/bin/bash

TASK_NAME=${1:-'export-logs'}
FROM=${2:-'2017-12-24 12:00'}
TO=${3:-'2017-12-24 12:05'}

cat <<-EOF > event.json
{
    "taskName": "$TASK_NAME",
    "fromTime": `gdate --date="$FROM" +%s%3N`,
    "toTime": `gdate --date="$TO" +%s%3N`
}
EOF

cat event.json | jq .
