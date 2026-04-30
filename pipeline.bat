@echo off
echo === INICIANDO PIPELINE DE DATOS CLIMATICOS ===
python src\extract.py
python src\transform.py
python src\load.py
echo === PIPELINE COMPLETADO ===
