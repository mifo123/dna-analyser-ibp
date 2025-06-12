from pandas import DataFrame

from DNA_analyser_IBP.models import ZDna


def test_zdna_model_creation_and_serialization() -> None:
    """It should create RLoopr model and pandas DataFrame."""

    zdna: ZDna = ZDna(
        id="id",
        title="title",
        tags=["test"],
        created="01-06-2025",
        finished="01-06-2025",
        sequenceId="test",
        selectedModel="model1",
        resultCount=20,
        minSequenceSize=10,
        score_gc=25,
        score_gtac=3,
        score_at=0,
        score_oth=0,
        threshold=12
    )
    generated_dataframe: DataFrame = zdna.get_data_frame()

    # assert it genereta DataFrame
    assert isinstance(generated_dataframe, DataFrame)

    # value assertions
    assert generated_dataframe["id"].iloc[0] == zdna.id
    assert generated_dataframe["tags"].iloc[0] == zdna.tags
    assert generated_dataframe["title"].iloc[0] == zdna.title
    assert generated_dataframe["model"].iloc[0] == zdna.model
    assert generated_dataframe["created"].iloc[0] == zdna.created
    assert generated_dataframe["finished"].iloc[0] == zdna.finished
    assert generated_dataframe["sequence_id"].iloc[0] == zdna.sequence_id
    assert generated_dataframe["result_count"].iloc[0] == zdna.result_count
    assert generated_dataframe["min_sequence_size"].iloc[0] == zdna.min_sequence_size
    assert generated_dataframe["GC_score"].iloc[0] == zdna.GC_score
    assert generated_dataframe["GTAC_score"].iloc[0] == zdna.GTAC_score
    assert generated_dataframe["AT_score"].iloc[0] == zdna.AT_score
    assert generated_dataframe["oth_score"].iloc[0] == zdna.oth_score
    assert generated_dataframe["min_score_percentage"].iloc[0] == zdna.min_score_percentage