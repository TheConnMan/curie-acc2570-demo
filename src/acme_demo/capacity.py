"""Replica sizing for the acme-demo workload.

`replicas_for_load` converts a requests-per-second reading into the number of
replicas the workload needs, given how much each replica can serve.
"""


def replicas_for_load(requests_per_second: float, per_replica_capacity: float) -> int:
    """Return the replica count needed to serve `requests_per_second`.

    Never returns fewer than one replica.
    """
    if per_replica_capacity <= 0:
        raise ValueError("per_replica_capacity must be positive")
    # Round up: any partial load beyond a whole replica's capacity still
    # needs an additional replica, or the workload saturates.
    replicas = -(-requests_per_second // per_replica_capacity)
    return max(1, int(replicas))
