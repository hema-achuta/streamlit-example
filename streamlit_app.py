import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mode
import streamlit as st


# Function to analyze the data
def analyze_data(file_path):
    data = np.loadtxt(file_path, skiprows=1, usecols=(0, 2))

    # Extract X-axis data
    x_values = data[:, 0]

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(x_values, label='X-axis')
    ax.set_xlabel('X-axis')
    ax.set_title('X-axis Plot')

    # Calculate the minimum and maximum values
    min_value = np.min(x_values)
    max_value = np.max(x_values)

    # Highlight the minimum and maximum values with colored markers
    ax.plot(np.argmin(x_values), min_value, 'b*', label=f'Min: {min_value:.2f}')
    ax.plot(np.argmax(x_values), max_value, 'g^', label=f'Max: {max_value:.2f}')

    ax.legend()

    st.pyplot(fig)

    return data


# Create the Streamlit app
def main():
    st.title('Data Analysis')

    # File selection
    file_path = st.file_uploader("Upload a .dat file", type=['dat'])
    if file_path is not None:
        data = analyze_data(file_path)

        # Add buttons to show mean, median, and mode
        if st.button('Show Mean'):
            mean_value = np.mean(data[:, 1])
            st.write("Mean:", mean_value)

        if st.button('Show Median'):
            median_value = np.median(data[:, 1])
            st.write("Median:", median_value)

        if st.button('Show Mode'):
            mode_value = mode(data[:, 1]).mode[0]
            st.write("Mode:", mode_value)


if __name__ == '__main__':
    st.set_option('deprecation.showPyplotGlobalUse', False)
    main()
