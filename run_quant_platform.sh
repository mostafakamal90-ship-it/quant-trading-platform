#!/bin/bash

echo "Starting Quant Platform"

python main.py &
streamlit run dashboard.py
