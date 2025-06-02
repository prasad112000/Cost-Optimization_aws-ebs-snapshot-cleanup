# 🧹 AWS EBS Snapshot Cleanup with Lambda

A simple AWS Lambda function to identify and delete stale EBS snapshots that are no longer associated with any active EC2 instance. This helps reduce unnecessary storage costs.

## 🔧 How It Works

- Fetches all EBS snapshots owned by your account.
- Checks if each snapshot is attached to a volume.
- If not attached or volume is no longer linked to any EC2 instance, it deletes the snapshot.

## 🛡 IAM Policy

Use the `iam-policy.json` to create a least-privilege IAM policy for the Lambda role.

## 🚀 Deployment

- Write the Lambda function in Python.
- Create a Lambda execution role with the provided IAM policy.
- Deploy the function using AWS Console or AWS CLI.
- Optionally schedule it with Amazon EventBridge (cron).

## 🧠 Important

This script only deletes snapshots owned by your account (`OwnerIds=['self']`) and ensures the associated volumes aren't attached to active instances.
