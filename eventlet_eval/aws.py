import boto3
from botocore.config import Config


def list_ecs_clusters(region_name):
    cfg = Config(region_name=region_name)
    ecs = boto3.client("ecs", config=cfg)
    try:
        result = ecs.list_clusters(maxResults=100)
    except Exception as e:
        result = {"exception": e}
        print(e)
        n_clusters = 0
    else:
        n_clusters = len(result["clusterArns"])

    assert "clusterArns" in result, result.keys()
    assert "ResponseMetadata" in result, result.keys()
    return f"{region_name}\t{result}\t{n_clusters}"
