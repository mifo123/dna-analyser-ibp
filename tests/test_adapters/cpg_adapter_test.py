import pytest

from typing import List

from DNA_analyser_IBP.config import Config
from DNA_analyser_IBP.models import User, CpG, Sequence
from DNA_analyser_IBP.adapters import Adapters, UserAdapter


@pytest.fixture(scope="module")
def adapters():
    user: User = UserAdapter.sign_in(
        User(email="host", password="host", server=Config.SERVER_CONFIG.PRODUCTION)
    )
    adapters = Adapters(user=user)
    return adapters

@pytest.fixture(scope="module")
def sequence(adapters):
    sequence_generator = adapters.sequence.load_all(tags=list())
    sequence_list: List[Sequence] = [sequence for sequence in sequence_generator]
    return sequence_list[0]

class TestZDnaAdapter:
    def test_cpg_analysis(self, adapters: Adapters, sequence: Sequence) -> None:
        """It should run cpg analysis and return CpG object"""
        cpg: CpG = adapters.cpg.create_analyse(
            id=sequence.id,
            tags=["test"],
            min_window_size=500,
            min_gc_percentage=0.55,
            min_obs_exp_cpg=0.65,
            min_island_merge_gap=100,
            second_nucleotide="G"
        )
        assert isinstance(cpg, CpG)

    def test_load_all_cpg(self, adapters: Adapters) -> None:
        """It should return iterator with CpG models"""
        cpg_generator = adapters.cpg.load_all(tags=list())

        cpg_list = [cpg for cpg in cpg_generator]
        assert len(cpg_list) == 1

        for cpg in cpg_list:
            assert isinstance(cpg, CpG)

    def test_load_by_id_cpg(self, adapters: Adapters) -> None:
        """It should return iterator with cpg models"""
        cpg_generator = adapters.cpg.load_all(tags=list())
        cpg_list = [cpg for cpg in cpg_generator]

        cpg = adapters.cpg.load_by_id(id=cpg_list[0].id)
        assert isinstance(cpg, CpG)

    def test_cpg_delete(self, adapters: Adapters) -> None:
        """It should delete cpg analysis"""
        cpg_generator = adapters.cpg.load_all(tags=list())
        cpg_list = [cpg for cpg in cpg_generator]

        assert len(cpg_list) == 1

        deleted: bool = adapters.cpg.delete(id=cpg_list[0].id)
        assert deleted is True