# 02.02.2020
- download raw data of GSE39445
- write the script (my/summarize_GSE39445.py) to extract data from GSE39445
- write the script (my/plot_GSE39445.py) to plot data

# 03.02.2020
- raw expression of circadian genes doesn't looks like in original research.
So rewrite summarize_GSE39445.py to collect housekeeping genes and use relative
extraction for plot instead of absolute.

# 05.02.2020
- download raw data of GSE71620 

# 14.02.2020
- download metadata GSE71620
- plot GSE71620
- download GSE10045 - rejected as no brain\blood data
- download GSE54650 using join_metadata_GSE54650.py and based on script for GSE71620
- plot GSE54650 based on script for GSE71620
