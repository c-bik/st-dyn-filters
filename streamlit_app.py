import streamlit as st
from streamlit_dynamic_filters import DynamicFilters
import pandas as pd

left, right = st.columns(2)
with left:
    df = pd.DataFrame({"col1": [1, 2, 3, 4], "col2": ["a", "b", "c", "d"]})
    dynamic_filters = DynamicFilters(df, filters=["col1", "col2"])
    dynamic_filters.display_filters(location="columns", num_columns=2, gap="large")
    dynamic_filters.display_df(use_container_width=True, hide_index=True)
with right:
    df = pd.DataFrame({"col3": [11, 12, 13, 14], "col4": ["aa", "bb", "cc", "dd"]})
    dynamic_filters = DynamicFilters(df, filters=["col3", "col4"])
    dynamic_filters.display_filters(location="columns", num_columns=2, gap="large")
    dynamic_filters.display_df(use_container_width=True, hide_index=True)
