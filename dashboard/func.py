import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan progress bar saat memuat gambar plot
def load_plot(xx):
    with st.empty():
        st.write("Memuat plot...")
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)
            progress_bar.progress(percent_complete + 1)
        plot = xx
        st.pyplot(plot)