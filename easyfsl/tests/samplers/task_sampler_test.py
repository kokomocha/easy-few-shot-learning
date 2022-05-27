from unittest.mock import patch

import pytest

from easyfsl.datasets import FewShotDataset
from easyfsl.samplers import TaskSampler


def init_task_sampler(labels, n_way, n_shot, n_query, n_tasks):
    with patch("easyfsl.datasets.FewShotDataset.get_labels", return_value=labels):
        print(labels)
        return TaskSampler(
            dataset=FewShotDataset(),
            n_way=n_way,
            n_shot=n_shot,
            n_query=n_query,
            n_tasks=n_tasks,
        )


class TestTaskSamplerIter:
    cases_grid = [
        {
            "labels": [0, 0, 0, 1, 1, 1, 2, 2, 2],
            "n_way": 2,
            "n_shot": 1,
            "n_query": 1,
            "n_tasks": 5,
        },
    ]

    @staticmethod
    @pytest.mark.parametrize(
        "labels,n_way,n_shot,n_query,n_tasks",
        [tuple(case.values()) for case in cases_grid],
    )
    def test_task_sampler_iter_yields_list_of_int(
        labels, n_way, n_shot, n_query, n_tasks
    ):
        sampler = init_task_sampler(labels, n_way, n_shot, n_query, n_tasks)
        for batch in sampler:
            assert isinstance(batch, list)
            for item in batch:
                assert isinstance(item, int)
