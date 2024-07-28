FROM continuumio/anaconda3
WORKDIR /PSD

COPY Environment.yml .
RUN conda env create -f Environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "PSD_Environment", "/bin/bash", "-c"]

# The code to run when container is started:
COPY . .
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "PSD_Environment", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]