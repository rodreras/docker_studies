#Importing Python Image
FROM continuumio/miniconda3:main

#Setting the workdir
WORKDIR /app

#Installing with Conda
RUN conda install -c conda-forge orekit
RUN pip install pandas geopandas matplotlib numpy tabulate plotly  
RUN pip install git+https://gitlab.orekit.org/orekit/orekit-data.git


COPY . . 

CMD python app.py