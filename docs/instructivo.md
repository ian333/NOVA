# Instructivo de producto — NOVA

Este documento es el instructivo para clientes del proyecto NOVA, una placa de
desarrollo basada en el diseño ColorEasyPICO2 (RP2350A). Contiene fotos, pasos
de montaje, conexión, flasheo de firmware y pruebas básicas.

---

## Vista general de la placa

![Pinouts](docs/assets/0e48737876a644858fad8e83eb7208aa.png)

![On-board resources](docs/assets/8ed8ad7ad60a4ff98b256b31e455e84b.png)

![Schematic preview](docs/assets/51a5fcab3cea49df9c8ac422334b257a.webp)

---

## Conexiones principales

- Alimentación: conector USB Type-C (5V).
- GND: plano de tierra común.
- Pines digitales: accesibles por headers/pads en la placa.
- BOOT / RESET: botones para entrar en modo bootloader o resetear.

Ejemplo de conexión básica (alimentación + LED de prueba):

![Board photo](docs/assets/b90293e2fdb44eccaa83c8a4ada76d5f.webp)

---

## Montaje y recomendaciones de soldadura

1. Limpia la PCB y revisa serigrafía.
2. Solda primero los componentes SMD pequeños (resistencias, capacitores).
3. Coloca el inductor del regulador y el QFN del MCU siguiendo el diseño de
   referencia; es crítico para la estabilidad del RP2350.
4. Solda conectores y botones al final.
5. Verifica continuidad y cortocircuitos con multímetro antes de aplicar 5V.

---

## Flasheo de firmware

### MicroPython (UF2)

1. Descarga el `.uf2` adecuado (ej. en los adjuntos de la referencia o desde
   https://micropython.org/download/RPI_PICO2/).
2. Mantén presionado el botón `BOOT`, conecta la placa por USB y suelta `BOOT`.
3. La placa aparecerá como unidad de almacenamiento; copia el archivo `.uf2`.
4. La placa se reiniciará con MicroPython instalado.

### Arduino

- Añade la URL `https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json` en el gestor de placas de Arduino IDE.
- Instala la placa `Raspberry Pi Pico/RP2040/RP2350` y selecciona el puerto.
- Para el primer upload puede ser necesario entrar en modo `BOOT`.

---

## Pruebas rápidas

Prueba de parpadeo (MicroPython):

```
from machine import Pin
import time

led = Pin(25, Pin.OUT)
while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
```

Verificaciones antes de entregar al cliente:

- La placa enciende con 5V y la línea 3.3V es estable.
- El LED de usuario parpadea con el script de prueba.
- El MCU entra en modo boot y se detecta como unidad USB para flasheo.

---

## Resolución de problemas frecuentes

- No aparece la unidad al conectar: usa cable Type-C con datos, prueba otro
  puerto o cable.
- El MCU no arranca: revisa soldadura del QFN y cristal de 12MHz.
- Si no es posible flashear: intenta `flash_nuke.uf2` y volver a cargar UF2.

---

## Fotografías y material para clientes

Incluye fotografías de alta calidad de la placa montada, conexiones y esquema
de pines. Aquí hay imágenes de referencia; puedes reemplazarlas por fotos
propias en la carpeta `docs/assets/`.

---

## Información de compra y contact

Propuesta para la ficha de venta (completa para editar):

- Producto: NOVA — placa de desarrollo RP2350A
- Opciones: PCB solo (kit) / Ensamblada
- Incluye: PCB, componentes SMD, firmware UF2 de ejemplo, guía en PDF
- Contacto/venta: añade aquí el email o enlace de tienda

---

Si quieres que incluya tus fotos en `docs/assets/` puedo descargarlas y
reemplazar las imágenes externas, y luego generar el PDF final.
