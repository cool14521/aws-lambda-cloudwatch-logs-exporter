# aws-lambda-cloudwatch-logs-exporter

## Deploy
- Create an IAM Role that has ClouWatch Logs permissions in advance and put its `arn` to `function.json`
- Tweak `project.json` and `function.json` to meet your requirements
```
apex deploy
```

## Export logs
You will find a `taskId` in the response of `apex invoke`.

```shell
$ sh event_generator.sh 'my-first-export-task' '2017-12-23 16:00' '2017-12-23 16:30' | apex invoke cloudwatch_logs_exporter | jq .
```

## Check the result
The given task ID corresponds to s3 URL as shown below.

```
$ export TASK_ID=[your_taskId]
$ aws logs describe-export-tasks --task-id ${TASK_ID}
$ aws s3 ls [S3_BUCKET_NAME]/[S3_DESTINATION_NAME]/${TASK_ID}/ --recursive
```

If target logs are not available yet, the export task status code will be COMPLETED but there is no exported log in S3 bucket.

> Log data can take up to 12 hours to become available for export.
> Ref. http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3ExportTasksConsole.html

So you might need to wait until target logs become available.
