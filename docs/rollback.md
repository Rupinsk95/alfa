Rolling Deployment- Rollback Plan
* Stop the current rollout
* Execute rollback to the previous ReplicaSet
* Monitor pod health, logs, and errors during replacement
* Confirm system stability before scaling back up

Blue/Green Deployment- Rollback Plan
* Switch traffic back to the Blue (stable) environment
* Disable or scale down the Green environment
* Monitor system metrics to confirm stability
* Fix and redeploy Green when ready

Canary Deployment- Rollback Plan
* Immediately redirect 100% of traffic to the stable version
* Scale down or remove the canary pods
* Review logs/metrics from the failed canary
* Prepare a new canary release after a fix



Incident Rollback- Quick Steps Checklist

* Identify symptoms (errors, latency, alerts)
* Validate issue is caused by the new release
* Notify team/channel that rollback is starting
* Execute Rollback
* Record root cause clues
* Create follow-up tasks (fix, tests, monitoring gaps)
