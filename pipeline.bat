@echo off
echo === INICIANDO PIPELINE DE DATOS CLIMATICOS ===
python extract.py
python transform.py
python load.py
echo === PIPELINE COMPLETADO ===