# Instructivo de producto — NOVA

Este documento es el instructivo para clientes del proyecto NOVA, una placa de
desarrollo basada en el diseño ColorEasyPICO2 (RP2350A). Contiene instrucciones
paso a paso para montaje, conexión, flasheo de firmware y pruebas básicas.

---

## Vista general de la placa

NOVA es una placa compacta de desarrollo con los siguientes componentes:

- **Microcontrolador**: RP2350A (Raspberry Pi familia Pico)
- **Alimentación**: Conector USB Type-C (entrada 5V)
- **Regulador**: LDO integrado para 3.3V
- **Memoria**: QSPI externa (W25Q32, 4MB)
- **Botones**: BOOT y RESET
- **LED**: LED de usuario en GPIO25 para pruebas

Todos los pines de E/S están accesibles mediante headers o pads de soldadura.

---

<!-- Se eliminó la sección Lista de Materiales (BOM) por petición del cliente -->

---

## Conexiones principales

### Alimentación
- **Entrada**: Conector USB Type-C (5V)
- **Salida regulada**: 3.3V disponible en headers/pads
- **GND**: Plano de tierra común, múltiples puntos

### Pines digitales
- Accesibles mediante headers o pads SMD
- Lógica: 3.3V
- Compatible con módulos estándar (LEDs, sensores, relés)

### Botones
- **BOOT**: Entra en modo bootloader al conectar (con 5V)
- **RESET**: Reinicia el MCU (resetea sin entrar en bootloader)

---

<!-- Se eliminó la sección Montaje y soldadura por petición del cliente -->

---

## Flasheo de firmware

### Opción 1: MicroPython (recomendado para principiantes)

1. **Descarga el firmware UF2**
   - Desde https://micropython.org/download/RPI_PICO2/
   - O desde los adjuntos del proyecto referencia (OSHWLab)

2. **Entra en modo bootloader**
   - Mantén presionado el botón BOOT
   - Conecta la placa por USB (cable con datos)
   - Suelta BOOT
   - La placa debe aparecer como "unidad de almacenamiento USB"

3. **Copia el archivo UF2**
   - Arrastra y suelta el `.uf2` en la unidad USB
   - La placa se reiniciará automáticamente
   - MicroPython estará listo

### Opción 2: Arduino

1. **Instala el paquete de soporte**
   - Abre Arduino IDE
   - File → Preferences → Additional Board Manager URL
   - Añade: `https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json`
   - Tools → Board Manager
   - Busca "RP2350" e instala "Raspberry Pi Pico/RP2040/RP2350" por Earle F. Philhower

2. **Carga tu primer programa**
   - Tools → Board: selecciona la placa
   - Tools → Port: selecciona el puerto USB
   - Sketch → Upload
   - Para el primer upload puede ser necesario entrar en modo BOOT

---

## Pruebas rápidas

### Prueba 1: Parpadeo LED (MicroPython)

Código a ejecutar en Thonny IDE:

```python
from machine import Pin
import time

# Configura GPIO25 como salida
led = Pin(25, Pin.OUT)

# Parpadea indefinidamente
while True:
    led.value(1)          # LED encendido
    time.sleep(1)         # espera 1 segundo
    led.value(0)          # LED apagado
    time.sleep(1)         # espera 1 segundo
```

**Resultado esperado**: LED de usuario parpadea cada segundo.

### Prueba 2: Puerto serie (verificar conexión)

- Abre Thonny o Arduino IDE
- Selecciona Tools → Port
- Abre el puerto a 115200 baudios
- Debes ver mensajes del MCU o poder enviar comandos

---

## Verificaciones de calidad antes de entregar

- [ ] La placa enciende con 5V (LED de potencia)
- [ ] El LED de usuario parpadea con script de prueba
- [ ] El MCU se detecta en el IDE (puerto serie activo)
- [ ] La tensión 3.3V es estable (verificar con multímetro)
- [ ] Botones BOOT y RESET responden correctamente

---

## Resolución de problemas frecuentes

### La placa no enciende
- Verifica cable USB Type-C (con datos, no solo carga)
- Verifica soldadura del diodo de entrada (D1)
- Verifica continuidad del LDO (ME6217C33M5G)

### El MCU no se detecta como dispositivo USB
- Verifica cable USB (datos)
- Intenta otra el puerto USB del PC
- Verifica soldadura del cristal de 12MHz y capacitores (C22, C23)
- Verifica soldadura del QFN del RP2350

### No puedo cargar firmware (no aparece unidad USB en modo boot)
- Mantén BOOT presionado al conectar USB
- Intenta usar el cable USB diferente
- Si sigue fallando, el cristal o MCU pueden tener soldadura fría

### El firmware se carga pero el LED no parpadea
- Verifica conexión del LED a GPIO25
- Verifica resistencia limitadora (R24 o similar)
- Intenta con código simple (ej. solo digitalWrite)

---

## Información de compra y contacto

### Opciones de venta

**Kit (componentes + PCB sin soldar)**
- Incluye: PCB, lista completa de componentes, BOM
- Para clientes con experiencia en soldadura SMD

**Placa ensamblada (preflashed con MicroPython)**
- Incluye: PCB montada y testeada, firmware .uf2, guía PDF
- Lista para usar de inmediato

### Soporte y contacto

Para preguntas, soporte o compras:
- **Email**: [tu email aquí]
- **Web**: [tu web aquí]
- **Referencia original**: https://oshwlab.com/lckfb-team/coloreasypicox

---

## Licencia

Este proyecto está basado en ColorEasyPICO2 bajo licencia LGPL 3.0.
NOVA mantiene la misma licencia.

---

## Especificaciones técnicas (resumen)

| Parámetro | Valor |
|-----------|-------|
| Microcontrolador | RP2350A |
| Frecuencia reloj | 12 MHz (oscilador externo) |
| Tensión entrada | 5V (Type-C) |
| Tensión regulada | 3.3V @ 800mA (LDO) |
| Memoria QSPI | 4MB (W25Q32) |
| GPIO disponibles | 26+ (3.3V) |
| USB | Full Speed (480 Mbps) |
| Formato | PCB compacta SMD |
| Peso | ~15g |

---

**Última actualización**: 14 de enero de 2026  
**Versión**: 1.0
