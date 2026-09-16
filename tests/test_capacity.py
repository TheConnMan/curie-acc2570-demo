import pytest

from acme_demo import replicas_for_load


def test_exact_multiple_needs_no_extra_replica():
    assert replicas_for_load(200.0, 100.0) == 2


def test_partial_load_rounds_up_so_the_workload_is_not_saturated():
    # 150 rps against 100 rps per replica needs two replicas, not one.
    assert replicas_for_load(150.0, 100.0) == 2


def test_zero_load_still_keeps_one_replica():
    assert replicas_for_load(0.0, 100.0) == 1


def test_non_positive_capacity_is_rejected():
    with pytest.raises(ValueError):
        replicas_for_load(10.0, 0.0)
