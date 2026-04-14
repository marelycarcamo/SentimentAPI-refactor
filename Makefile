# Makefile para ejecutar el pipeline de limpieza

.PHONY: run clean help

# Ejecutar el notebook completo
run:
	jupyter nbconvert --to notebook --execute Modelo_SentimentAPI.ipynb \
		--output Modelo_SentimentAPI_ejecutado.ipynb \
		--ExecutePreprocessor.timeout=600

# Limpiar archivos generados
clean:
	rm -f Modelo_SentimentAPI_ejecutado.ipynb
	rm -f data-science/datasets/dataset_listo_para_ML.csv  # opcional, comenta si no quieres borrar el dataset

help:
	@echo "Comandos disponibles:"
	@echo "  make run     - Ejecuta el pipeline (genera dataset y notebook ejecutado)"
	@echo "  make clean   - Elimina archivos generados (notebook ejecutado y dataset)"