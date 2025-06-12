from pandas import DataFrame

from DNA_analyser_IBP.models import CpG


def test_cpx_model_creation_and_serialization() -> None:
    """It should create RLoopr model and pandas DataFrame."""

    cpg: CpG = CpG(
        id="id",
        title="title",
        tags=["test"],
        created="01-06-2025",
        finished="01-06-2025",
        sequenceId="test",
        resultCount=20,
        minWindowSize=500,
        minGcPercentage=0.55,
        minObservedToExpectedCpG=0.65,
        minIslandMergeGap=100,
        secondNucleotide="G"
    )
    generated_dataframe: DataFrame = cpg.get_data_frame()

    # assert it genereta DataFrame
    assert isinstance(generated_dataframe, DataFrame)

    assert generated_dataframe["id"].iloc[0] == cpg.id
    assert generated_dataframe["tags"].iloc[0] == cpg.tags
    assert generated_dataframe["title"].iloc[0] == cpg.title
    assert generated_dataframe["created"].iloc[0] == cpg.created
    assert generated_dataframe["finished"].iloc[0] == cpg.finished
    assert generated_dataframe["sequence_id"].iloc[0] == cpg.sequence_id
    assert generated_dataframe["result_count"].iloc[0] == cpg.result_count
    assert generated_dataframe["min_window_size"].iloc[0] == cpg.min_window_size
    assert generated_dataframe["min_gc_percentage"].iloc[0] == cpg.min_gc_percentage
    assert generated_dataframe["min_obs_exp_cpg"].iloc[0] == cpg.min_obs_exp_cpg
    assert generated_dataframe["min_island_merge_gap"].iloc[0] == cpg.min_island_merge_gap
    assert generated_dataframe["second_nucleotide"].iloc[0] == cpg.second_nucleotide

