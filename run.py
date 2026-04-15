#!/usr/bin/env python3
"""
Ejecuta el pipeline de limpieza de datos sin abrir Jupyter.
Ejecuta el notebook Modelo_SentimentAPI.ipynb y genera el dataset final.
"""

import subprocess
import sys
from pathlib import Path

def main():
    notebook = Path("./data-science/notebooks/Modelo_SentimentAPI.ipynb")
        
    if not notebook.exists():
        print(f"❌ No se encuentra el notebook: {notebook}")
        print("   Asegúrate de ejecutar este script desde la raíz del repositorio.")
        sys.exit(1)
    
    print("🚀 Ejecutando el pipeline de limpieza...")
    print("   Esto puede tomar unos minutos dependiendo de la descarga de datos.")
    
    # Comando para ejecutar el notebook con nbconvert
    cmd = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute", str(notebook),
        "--output", "Modelo_SentimentAPI_ejecutado.ipynb",
        "--ExecutePreprocessor.timeout=600",
        "--ExecutePreprocessor.kernel_name=python3"
    ]
    
    result = subprocess.run(cmd)
    
    if result.returncode != 0:
        print("\n❌ Error durante la ejecución del notebook.")
        print("   Revisa los mensajes de error arriba.")
        sys.exit(1)
    
    print("\n✅ Pipeline ejecutado correctamente.")
    print("📁 El dataset limpio se encuentra en:")
    print("   data-science/datasets/dataset_listo_para_ML.csv")
    print("\n📓 También se ha generado una copia ejecutada del notebook:")
    print("   Modelo_SentimentAPI_ejecutado.ipynb (puedes borrarla si no la necesitas)")

if __name__ == "__main__":
    main()