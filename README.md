# Bad Bunny Reggaeton Popularity Analysis

## Dependencies  
This project uses the following Python libraries commonly used in data science:  
- [`NumPy`](https://numpy.org/)  
- [`Pandas`](https://pandas.pydata.org/)  
- [`Matplotlib`](https://matplotlib.org/)  
- [`Seaborn`](https://seaborn.pydata.org/)  
- [`SciPy`](https://scipy.org/)  
- [`Spotipy`](https://spotipy.readthedocs.io/) (for Spotify API access)

## Introduction  
This project analyzes the **popularity of Bad Bunny's songs** by examining their release year and genre classification (reggaeton or not). The main hypothesis is that **Bad Bunny's reggaeton songs tend to be more popular** than his songs from other genres.

To explore this, we collected song data using the Spotify API, performed manual genre labeling, and applied several statistical and visual methods to identify trends and differences.

## Features  
- Authentication and data collection from the Spotify API  
- Manual genre labeling for each track (reggaeton or not)  
- Histogram and KDE plots to visualize genre-popularity distribution  
- Pearson correlation and t-tests to evaluate statistical significance  
- Grouped album-level analysis and correlation with reggaeton content  
- Exportable, reproducible workflow with scalable genre labeling system  

## Technologies  
- Programming Language: **Python**  
- Data Analysis: **NumPy, Pandas, SciPy**  
- Visualization: **Matplotlib, Seaborn**  
- API Access: **Spotipy**  
- Manual Labeling: Excel integration  
- Notebook Format: **Jupyter Notebook**

## Notes on Scalability  
New songs released after the labeling date (April 30, 2025) will appear with missing genre labels (`NaN`). These are filtered out during analysis to maintain consistency. This ensures the notebook remains functional as new data is fetched, even if the manual labeling file is not updated immediately.

## Author  
Santiago Velasco García – *April 2025*
