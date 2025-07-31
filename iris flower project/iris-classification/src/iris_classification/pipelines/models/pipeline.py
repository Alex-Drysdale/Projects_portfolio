"""
This is a boilerplate pipeline 'models'
generated using Kedro 0.19.14
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from .nodes import train_test_split

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = train_test_split,
            
        ),
    ])
