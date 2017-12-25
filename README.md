# aws-lambda-cloudwatch-logs-exporter

## Deploy
- Create ana IAM Role that has ClouWatch Logs permissions and put its arn to `function.json`
```
apex deploy
```

## export logs and check the result
You will find a `taskId` in the response of `apex invoke`.
```shell
$ sh event_generator.sh 'my-first-export-task' '2017-12-23 16:00' '2017-12-23 16:30' | apex invoke cloudwatch_logs_exporter
$ export TASK_ID=[your_taskId]
$ aws logs describe-export-tasks --task-id ${TASK_ID}
$ aws s3 ls [S3_BUCKET_NAME]/[S3_DESTINATION_NAME]/${TASK_ID}/ --recursive
```
