import streamlit as st
import pandas as pd
import numpy as np


title = "Corrélations CO2"
sidebar_name = "Corrélations"


def run():

    st.title(title)

    st.markdown(
        """
        This is the third sample tab.
        """
    )

    st.write(pd.DataFrame(np.random.randn(100, 4), columns=list("ABCD")))