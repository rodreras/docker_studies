#Importing Python Image
FROM continuumio/miniconda3:main

#Setting the workdir
WORKDIR /app

# Copying requirements
COPY environment.yaml .

#Installing with Conda
#RUN conda install -c conda-forge orekit
RUN pip install pandas geopandas matplotlib numpy streamlit  
#RUN pip install git+https://gitlab.orekit.org/orekit/orekit-data.git


COPY . . 

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]