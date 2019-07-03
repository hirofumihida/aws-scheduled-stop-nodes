# aws-scheduled-stop-nodes

## Environment variables

```
WEBHOOK_URL = https://hooks.slack.com/foobar
INSTANCE_LIST = instanceid1 instanceid2 ...
```

## cron setting (UTC)

- UTC 13:00
- JST 22:00

```
cron(0 01 * * ? *)
```
