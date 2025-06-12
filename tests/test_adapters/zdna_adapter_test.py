import pytest

from typing import List

from DNA_analyser_IBP.config import Config
from DNA_analyser_IBP.models import User, ZDna, Sequence
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
    def test_zdna_analysis(self, adapters: Adapters, sequence: Sequence) -> None:
        """It should run zdna analysis and return ZDna object"""
        zdna: ZDna = adapters.zdna.create_analyse(
            id=sequence.id,
            tags=["test"],
            min_sequence_size=10,
            model="model1",
            GC_score=25,
            GTAC_score=3,
            AT_score=0,
            oth_score=0,
            min_score_percentage=15
        )
        assert isinstance(zdna, ZDna)

    def test_load_all_zdna(self, adapters: Adapters) -> None:
        """It should return iterator with ZDna models"""
        zdna_generator = adapters.zdna.load_all(tags=list())

        zdna_list = [zdna for zdna in zdna_generator]
        assert len(zdna_list) == 1

        for zdna in zdna_list:
            assert isinstance(zdna, ZDna)

    def test_load_by_id_zdna(self, adapters: Adapters) -> None:
        """It should return iterator with zdna models"""
        zdna_generator = adapters.zdna.load_all(tags=list())
        zdna_list = [zdna for zdna in zdna_generator]

        zdna = adapters.zdna.load_by_id(id=zdna_list[0].id)
        assert isinstance(zdna, ZDna)

    def test_zdna_delete(self, adapters: Adapters) -> None:
        """It should delete zdna analysis"""
        zdna_generator = adapters.zdna.load_all(tags=list())
        zdna_list = [zdna for zdna in zdna_generator]

        assert len(zdna_list) == 1

        deleted: bool = adapters.zdna.delete(id=zdna_list[0].id)
        assert deleted is True