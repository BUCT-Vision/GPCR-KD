FROM python:3.9.0
WORKDIR /BUCT-Vision/weixiaolin
RUN pip install -r requirements.txt
RUN python3 GPCR-KD-PRO/GPCR-KD-master/dataToResult/main.py
