Manual Cosmo-Gyroscope — instrucciones rápidas

Qué he creado:
- `Manual_Cosmo_Gyroscope.md` — borrador del manual con índice y marcadores para imágenes.
- `generate_pdf.py` — script en Python que genera `Manual_Cosmo_Gyroscope.pdf` a partir del `.md`.

Requisitos locales (Windows):

1) Instalar Python 3 si no está instalado.
2) Instalar la biblioteca `reportlab`:

```powershell
python -m pip install --upgrade pip
python -m pip install reportlab
```

3) Colocar las imágenes en `manual/images/` con los nombres indicados en el .md (por ejemplo `gyros_pinout.png`).

4) Generar el PDF:

```powershell
cd "c:\Users\Emily Andrade\Cosmo_Gyroscope\manual"
python generate_pdf.py
```

Salida: `Manual_Cosmo_Gyroscope.pdf` en la misma carpeta.

Notas:
- Si no hay imágenes, el script dejará un marcador de texto indicando `IMAGEN NO ENCONTRADA: <nombre>`.
- Cuando subas las imágenes, indícame cuáles y en qué sección quieres que las coloque (por nombre de fichero). Yo actualizaré el `.md` si deseas o haré la inserción final y regenero el PDF aquí.
