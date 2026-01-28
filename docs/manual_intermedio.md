# NOVA RP2350 — Guía de Inicio Práctico
## Introducción: Más allá de la computadora de escritorio

Tal vez pienses en las computadoras como esos dispositivos con pantalla y teclado que tienes en tu escritorio, y es cierto, lo son. Pero no son el único tipo.

En esta guía exploraremos los microcontroladores: pequeñas unidades de procesamiento que seguramente ya tienes en casa sin saberlo. Es muy probable que tu lavadora, microondas o termostato estén controlados por uno. Sin embargo, esos dispositivos suelen ser cerrados: sus fabricantes dificultan o impiden que modifiques el software que ejecutan.

**NOVA**, por otro lado, es diferente. Se puede reprogramar fácilmente todas las veces que quieras a través de una simple conexión USB. En las siguientes páginas veremos cómo empezar a utilizar este hardware y cómo combinarlo con otros componentes electrónicos.

Lo que construyas con ellos depende totalmente de ti.

## Introducción al Mundo Maker y Electrónica

Bienvenido a la guía de **NOVA**. Esta documentación está diseñada para hobbistas, estudiantes y entusiastas que quieren entender **cómo funcionan las cosas** sin perderse en tecnicismos matemáticos complejos.

Si tu objetivo es aprender electrónica programable, robótica básica y control de dispositivos, este es tu punto de partida.

---

## Contenidos

**Capítulo 1: Conoce tu NOVA**
Familiarízate con tu nuevo y potente microcontrolador, aprende cómo usar sus pines e instala MicroPython para programarlo.

**Capítulo 2: Programación con MicroPython**
Conecta una computadora y comienza a escribir programas para tu NOVA usando el lenguaje MicroPython.

**Capítulo 3: Computación Física**
Aprende sobre los pines de tu NOVA y los componentes electrónicos que puedes conectar y controlar.

**Capítulo 4: Computación Física con NOVA**
Empieza a conectar componentes electrónicos básicos a tu NOVA y escribe programas para controlarlos y detectar sus señales.

**Capítulo 5: Controlador de Semáforos**
Crea tu propio mini sistema de cruce peatonal usando múltiples LEDs y un botón pulsador.

**Capítulo 6: Juego de Reacción**
Construye un juego simple de tiempos de reacción usando un LED y botones, para uno o dos jugadores.

**Capítulo 7: Alarma Antirrobo**
Usa un sensor de movimiento para detectar intrusos y activa la alarma con una luz intermitente y una sirena.

**Capítulo 8: Medidor de Temperatura**
Usa el ADC integrado de NOVA para convertir entradas analógicas y lee su sensor de temperatura interno.

**Capítulo 9: Registrador de Datos (Data Logger)**
Convierte tu NOVA en un dispositivo de registro de temperatura y desconéctalo de la computadora para hacerlo totalmente portátil.

**Capítulo 10: Protocolos de Comunicación Digital: I2C y SPI**
Explora estos dos protocolos de comunicación populares y úsalos para mostrar datos en una pantalla LCD.

---

## Capítulo 1: Conoce tu NOVA

NOVA es una herramienta potente. En su corazón late el **Raspberry Pi RP2350A**, un microcontrolador moderno.

### ¿Qué significa esto en la práctica?
*   **Doble Núcleo (Dual Core):** Imagina que tienes dos cerebros. Mientras uno se encarga de mantener encendida una pantalla, el otro puede estar leyendo sensores o controlando un motor. Trabajan en paralelo (Multitasking real).
*   **Velocidad (150 MHz):** Puede procesar millones de instrucciones por segundo. Para proyectos de luces, robots y sensores, es increíblemente rápido.
*   **Pines de Propósito General (GPIO):** Son las "patitas" de la placa. A diferencia de un puerto USB normal de tu PC, estos pines se pueden programar para ser interruptores (encender/apagar cosas) o entradas (leer botones/sensores).

---

## Capítulo 2: Programación con MicroPython

Para comunicarnos con NOVA, usaremos **MicroPython**.
*   **¿Qué es?** Es una versión de Python 3 optimizada para funcionar en microcontroladores. Es el lenguaje ideal para empezar porque es legible y potente.
*   **La Herramienta:** Usaremos **Thonny IDE**. Es un editor de código simple que ya trae todo lo necesario para hablar con tu placa.

### Pasos rápidos:
1.  Conecta tu NOVA al ordenador manteniendo pulsado el botón **BOOT**.
2.  Tu PC lo verá como una memoria USB.
3.  Copia el archivo de firmware `.uf2` de MicroPython en esa memoria. (La placa se reiniciará, eso es normal).
4.  Abre Thonny y selecciona el intérprete "MicroPython (Raspberry Pi Pico)".

---

## Capítulo 3: Computación Física

El mundo real no es "1 o 0". La temperatura, la luz o el sonido varían suavemente.
*   NOVA tiene conversores **Analogico-Digitales (ADC)** de 12-bits.
*   Permiten leer voltajes variables (0V a 3.3V) y convertirlos en un número (0 a 65535). Esto es fundamental para leer potenciómetros, sensores de temperatura LM35, etc.

En la industria y proyectos avanzados, los componentes "hablan" entre sí.
*   **I2C:** Para conectar sensores modernos (acelerómetros, pantallas OLED) usando solo 2 cables.
*   **UART/Serial:** Para comunicar tu NOVA con otros módulos como GPS, Bluetooth o WiFi (ESP-01).

---

## Capítulo 4: Computación Física con NOVA

### Control Digital (Salidas)

Lo primero en electrónica es aprender a controlar el estado de un pin: **Alto (3.3V)** o **Bajo (0V)**.

En este ejemplo, controlaremos un LED externo. A nivel eléctrico, el LED necesita una resistencia (aprox 220Ω) para limitar la corriente y no quemarse.

**Conexión:**
*   **Pin 15** → Pata Larga del LED (+).
*   **GND** → Resistencia → Pata Corta del LED (-).

**El Código:**
Observa cómo importamos la librería `machine`. Esta librería es el puente entre el código software y el hardware físico.

```python
from machine import Pin
import time

# Configuramos el Pin 15 como SALIDA (OUT)
# Esto permite que el pin entregue voltaje (3.3V)
led = Pin(15, Pin.OUT)

print("Iniciando secuencia de control...")

while True:
    led.on()             # Envía 3.3V al pin (Encendido)
    time.sleep(1)        # Pausa el procesador 1 segundo
    led.off()            # Corta el voltaje (Apagado)
    time.sleep(1)
```

### Lógica y Simulación (LEDs)

Vamos a usar el módulo `random` para simular un comportamiento impredecible usando dos LEDs (como si fueran ojos).

```python
from machine import Pin
import time
import random

# Definimos los pines de los LEDs
ojo_izq = Pin(15, Pin.OUT)
ojo_der = Pin(14, Pin.OUT)

# --- Definición de Comportamientos ---

def parpadeo_normal():
    """Simula un parpadeo humano rápido"""
    ojo_izq.off()
    ojo_der.off()
    time.sleep(0.15)
    ojo_izq.on()
    ojo_der.on()

def escaneo():
    """Simula un robot analizando el entorno"""
    print("Escaneando...")
    for i in range(4):
        ojo_izq.toggle() # toggle() invierte el estado actual
        time.sleep(0.05)
        ojo_der.toggle()
        time.sleep(0.05)
    # Aseguramos que queden encendidos al final
    ojo_izq.on()
    ojo_der.on()

# --- Bucle Principal ---
print("Sistema Iniciado. Ejecutando IA básica.")
ojo_izq.on()
ojo_der.on()

while True:
    # El sistema espera un tiempo aleatorio entre acciones
    wait_time = random.uniform(2.0, 5.0)
    time.sleep(wait_time)
    
    # Decisión aleatoria
    decision = random.randint(1, 10)
    
    if decision <= 7:
        # 70% de probabilidad de parpadeo normal
        parpadeo_normal()
    else:
        # 30% de probabilidad de escaneo
        escaneo()
```

### Movimiento y PWM (Servomotores)

Un servomotor no funciona simplemente "encendiendo y apagando" la corriente. Necesita una **señal de control precisa** usando PWM (Pulse Width Modulation).

**Código de Control de Servo:**

```python
from machine import Pin, PWM
import time

# Configuración del PWM en el Pin 16
# Los servos estándar funcionan a una frecuencia de 50Hz
servo = PWM(Pin(16))
servo.freq(50)

def mover_servo(angulo):
    """
    Convierte un ángulo (0-180) al ciclo de trabajo (duty) necesario.
    """
    # Mapeo simple: 0-180 -> duty_u16
    duty = int(1638 + (angulo / 180) * (8192 - 1638))
    servo.duty_u16(duty)

while True:
    print("Moviendo a 0 grados")
    mover_servo(0)
    time.sleep(1)
    
    print("Moviendo a 90 grados")
    mover_servo(90)
    time.sleep(1)
    
    print("Moviendo a 180 grados")
    mover_servo(180)
    time.sleep(1)
```

---

*Nota: Los capítulos siguientes (5 al 10) están en desarrollo para futuras actualizaciones.*

## Recursos Adicionales

*   **Documentación Oficial MicroPython:** [docs.micropython.org](https://docs.micropython.org)
*   **Datasheet RP2350:** Para cuando necesites los detalles técnicos profundos de los registros y memoria.
*   **Repositorio del Proyecto:** Ejemplos de código y librerías específicas para NOVA.

¡Bienvenido al nivel intermedio! Aquí es donde la creatividad se encuentra con la ingeniería.
