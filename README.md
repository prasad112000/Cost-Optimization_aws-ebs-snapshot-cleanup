# AWS EBS Snapshot Cleanup – Cost Optimization with Lambda

In large-scale AWS environments, unused EBS snapshots often go unnoticed, silently increasing monthly costs. This project introduces a serverless solution to identify and delete stale EBS snapshots — contributing to better cloud hygiene and cost control.

---

## 🧠 Problem

EBS snapshots are frequently created as backups, but over time many become disconnected from any active EC2 volume or instance. These unused snapshots continue to incur storage charges unless removed.

---

## 🚀 Solution

This project uses an AWS Lambda function (written in Python using Boto3) to:

- ✅ Identify stale EBS snapshots owned by the account
- ✅ Detect whether associated volumes or instances are still active
- ✅ Automatically delete those snapshots that are no longer in use

---

## ⚙️ Architecture Overview

- **AWS Lambda:** Python script to scan and delete snapshots
- **IAM Role:** Attached to Lambda with least privilege permissions (see `iam-policy.json`)
- **(Optional) EventBridge:** Can be added to schedule the Lambda periodically

---

## 📁 Files

| File | Description |
|------|-------------|
| `lambda_function.py` | Main logic to identify and delete stale EBS snapshots |
| `iam-policy.json` | IAM policy granting minimum required permissions |
| `README.md` | Project overview and documentation |

---

## 🔐 IAM Policy (Least Privilege)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EBSDeletePermission",
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeSnapshots",
        "ec2:DescribeInstances",
        "ec2:DescribeVolumes",
        "ec2:DeleteSnapshot"
      ],
      "Resource": "*"
    }
  ]
