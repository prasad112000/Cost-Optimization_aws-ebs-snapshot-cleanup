# 🧹 AWS EBS Snapshot Cleanup with Lambda

A simple AWS Lambda function to identify and delete stale EBS snapshots that are no longer associated with any active EC2 instance. This helps reduce unnecessary storage costs.

## 🧠 Problem

EBS snapshots are frequently created as backups, but over time many become disconnected from any active EC2 volume or instance. These unused snapshots continue to incur storage charges unless removed.

## 🚀 Solution

This project uses an AWS Lambda function (written in Python using Boto3) to:
- ✅ Identify stale EBS snapshots owned by the account
- ✅ Detect whether associated volumes or instances are still active
- ✅ Automatically delete those snapshots that are no longer in use

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


