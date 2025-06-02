import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    deleted_snapshots = []

    # Get all snapshots owned by this account
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

    # Get volume IDs currently in use
    used_volume_ids = set()
    instances = ec2.describe_instances()
    for res in instances['Reservations']:
        for inst in res['Instances']:
            for blk in inst.get('BlockDeviceMappings', []):
                vol_id = blk.get('Ebs', {}).get('VolumeId')
                if vol_id:
                    used_volume_ids.add(vol_id)

    # Loop through snapshots
    for snap in snapshots:
        snapshot_id = snap['SnapshotId']
        volume_id = snap.get('VolumeId')

        if not volume_id or volume_id not in used_volume_ids:
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted snapshot: {snapshot_id}")
            deleted_snapshots.append(snapshot_id)

    return {
        'DeletedSnapshots': deleted_snapshots,
        'TotalDeleted': len(deleted_snapshots)
    }
