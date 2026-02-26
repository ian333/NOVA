---
pdf-engine: xelatex
fontsize: 12pt
geometry: "top=2cm, bottom=3.5cm, left=1.5cm, right=2.5cm, footskip=2cm"
header-includes:
  - "\\usepackage{fontspec}"
  - "\\setsansfont{DejaVu Sans}"
  - "\\renewcommand{\\familydefault}{\\sfdefault}"
  - "\\usepackage{microtype}"
  - "\\usepackage{graphicx}"
  - "\\usepackage{xcolor}"
  - "\\usepackage{hyperref}"
  - "\\hypersetup{colorlinks=true, linkcolor=blue, urlcolor=blue, citecolor=blue}"
  - "\\usepackage{etoolbox}"
  - "\\usepackage{fancyhdr}"
  - "\\usepackage{tikz}"
  - "\\usepackage{eso-pic}"
  - "\\definecolor{cosmoBlue}{HTML}{0E47A1}"
  - "\\definecolor{cosmoRed}{HTML}{C0392B}"
  - "\\usepackage{titlesec}"
  - "\\titleformat{\\section}{\\clearpage\\Large\\bfseries\\color{cosmoRed}}{\\thesection}{1em}{}"
  - "\\titleformat{\\subsection}{\\large\\bfseries\\color{cosmoBlue}}{\\thesubsection}{1em}{}"
  - "\\titleformat{\\subsubsection}{\\normalsize\\bfseries\\color{cosmoBlue}}{\\thesubsubsection}{1em}{}"
  - "\\titlespacing*{\\section}{0pt}{1.5ex plus 1ex minus .2ex}{1ex plus .2ex}"
  - "\\titlespacing*{\\subsection}{0pt}{1.2ex plus 0.8ex minus .2ex}{0.8ex plus .2ex}"
  - "\\titlespacing*{\\subsubsection}{0pt}{1ex plus 0.6ex minus .2ex}{0.6ex plus .2ex}"
  - "\\pagestyle{fancy}"
  - "\\fancyhf{}"
  - "\\renewcommand{\\headrulewidth}{0pt}"
  - "\\renewcommand{\\footrulewidth}{0pt}"
  - "\\setlength{\\headheight}{2cm}"
  - "\\fancyhead[R]{\\raisebox{-0.5\\height}{\\includegraphics[height=1.2cm]{Logotipo Cosmotools.jpeg}}\\hspace{-0.5cm}}"
  - "\\AddToShipoutPictureBG{\\AtPageLowerLeft{\\makebox[\\paperwidth][c]{\\textcolor{cosmoBlue}{\\rule{\\paperwidth}{1.2cm}}}}}"
  - "\\AddToShipoutPictureBG{\\AtPageLowerLeft{\\makebox[\\paperwidth][s]{\\hspace{1.5cm}\\raisebox{0.35cm}{\\textcolor{white}{\\small\\textbf{Manual NOVA\\_sense}}}\\hfill\\raisebox{0.35cm}{\\textcolor{white}{\\small\\thepage}}\\hspace{1.5cm}}}}"
---

# Bienvenido a NOVA_sense

## ¿Qué es NOVA_sense?

NOVA_sense es una pequeña placa electrónica que le da **sentidos** a tus proyectos. Así como tú usas tus ojos para ver y tu oído interno para mantener el equilibrio, NOVA_sense le permite a un robot o cualquier dispositivo electrónico **saber hacia dónde apunta, detectar movimiento y encontrar el Norte**, todo desde una sola placa del tamaño de una moneda.

Piensa en ella como el **"cerebro sensorial"** de tu proyecto: tú le das las instrucciones, y ella te devuelve información sobre lo que está pasando en el mundo real.

## ¿A qué se parece? — Comparaciones sencillas

| Sensor en NOVA_sense | ¿A qué se parece en la vida real? | ¿Qué detecta? |
|---|---|---|
| **Magnetómetro** (LIS2MDL) | Una **brújula digital** como la de tu celular | Hacia dónde está el Norte magnético |
| **Acelerómetro** (dentro del LSM6DS3) | El sensor que **gira la pantalla** de tu celular cuando lo inclinas | Inclinación, vibración, caídas |
| **Giroscopio** (dentro del LSM6DS3) | El sensor que detecta **giros** cuando juegas un videojuego moviendo el celular | Velocidad y dirección de rotación |

> **En resumen:** tu celular usa sensores muy parecidos a los de NOVA_sense para rotar la pantalla, orientar mapas y detectar movimiento. NOVA_sense te da esos mismos poderes para tus propios inventos.

## ¿Qué puedes hacer con ella?

- **Construir un robot que sepa hacia dónde va** — como un auto a control remoto que siempre sabe dónde está el Norte.
- **Detectar movimiento y gestos** — inclinar, agitar, girar: ideal para controles de juegos o instrumentos interactivos.
- **Crear una brújula electrónica** — muestra en una pantalla hacia dónde apuntas, igual que la app de brújula de un teléfono.
- **Registrar datos de movimiento** — grabar cómo se mueve un objeto (por ejemplo, una bicicleta o un dron) y analizarlo después.
- **Detectar la presencia de imanes o metales cercanos** — gracias a la sensibilidad del magnetómetro.
- **Estabilizar mecanismos** — como un dron que se auto-nivela o una cámara que compensa los temblores de la mano.

## Antes de empezar

> **Este manual está escrito en un lenguaje sencillo** para que cualquier persona, sin importar su experiencia, pueda seguir los pasos y lograr resultados. Sigue los ejemplos en orden, prueba cada uno y, si algo no funciona, revisa las conexiones antes de continuar.

# 1 Conoce tu NOVA_sense

### 1.1 Descripción general

En esta página se muestran los componentes principales del módulo NOVA_sense con su nombre común y una breve descripción para facilitar su identificación.

### 1.2 Componentes (nombre común — descripción)

- **IMU (LSM6DS3)** — Acelerómetro y giroscopio integrados (6 ejes). Mide aceleración lineal y velocidad angular para detección de movimiento y fusión inercial.

- **Magnetómetro (LIS2MDL)** — Sensor de campo magnético 3 ejes utilizado como brújula electrónica para orientación respecto al Norte magnético.

- **Conectores 4 pines (CN1, CN2)** — Conectores SMD para alimentación y señales (paso 1.0 mm) usados para integrar el módulo en placas madre o accesorios.

- **Condensadores 100 nF / 220 nF / 4.7 µF** — Filtrado y estabilización de la alimentación.

- **Resistencias 10 kΩ** — Pull-ups/pull-downs para asegurar niveles lógicos estables en líneas digitales.

\begin{center}
\includegraphics[width=0.45\textwidth]{componentes NOVA_sense.png}
\end{center}

### 1.3 Resumen funcional

Todos estos componentes trabajan juntos para proporcionar el soporte necesario para integrarse fácilmente en proyectos de robótica, navegación y registradores de datos.

# 2 Hardware y Conexiones

Conectar la NOVA_sense es tan sencillo como conectar unos audífonos: solo necesitas **4 cables** entre tu **NOVA_pico** y la NOVA_sense. La NOVA_pico es un microcontrolador que también fabricamos nosotros, diseñado para trabajar en conjunto con la NOVA_sense. Este tipo de conexión se llama **I2C** (se pronuncia "ai-dos-cé") y es un estándar muy común en electrónica.

### 2.1 ¿Qué cables necesito?

| Cable | Nombre | ¿Qué hace? | Analogía |
|---|---|---|---|
| 1 | **3.3 V** | Alimenta la NOVA_sense con corriente | El polo **+** de una pila |
| 2 | **GND** | Cierra el circuito (tierra) | El polo **−** de una pila |
| 3 | **SDA** | Envía y recibe datos | El "hilo" por donde se mandan mensajes |
| 4 | **SCL** | Marca el ritmo de la comunicación | El "reloj" que sincroniza la conversación |

### 2.2 Paso a paso para conectar

![Diagrama de conexión NOVA_pico — NOVA_sense](diagrama_conexion.png)

1. Conecta **3.3 V** de tu **NOVA_pico** al pin **3.3 V** de la NOVA_sense.
2. Conecta **GND** de tu **NOVA_pico** al pin **GND** de la NOVA_sense.
3. Conecta **SDA** de tu **NOVA_pico** al pin **SDA** de la NOVA_sense.
4. Conecta **SCL** de tu **NOVA_pico** al pin **SCL** de la NOVA_sense.

> **Importante:** Nunca conectes 5 V a los pines de la NOVA_sense — solo usa 3.3 V.

\newpage

**Consejos:**

- Asegúrate de que ambas placas compartan el mismo **GND**.
- Si ya tienes otros sensores I2C conectados, la NOVA_sense puede compartir los mismos cables SDA y SCL — como enchufar varios aparatos a la misma regleta.
- Muchas placas ya incluyen resistencias pull-up; si la tuya no las tiene, añade una de 4.7 kΩ en SDA y otra en SCL.

### 2.3 Entorno de programación: Thonny

Para programar la NOVA_pico y leer los datos de la NOVA_sense se utiliza **Thonny**, el único entorno compatible con estas placas.

> **¿Qué es Thonny?** Es un programa gratuito y sencillo que se instala en tu computadora. Desde ahí puedes escribir código en MicroPython, enviarlo a la NOVA_pico por USB y ver en tiempo real los datos que lee la NOVA_sense (orientación, movimiento, campo magnético).
>
> **Descárgalo aquí:** \textcolor{blue}{\underline{\href{https://thonny.org}{https://thonny.org}}} — disponible para Windows, Mac y Linux.

### 2.4 Leer registros y memoria del sensor (explicación simple)

Lo habitual es leer registros del sensor por I2C: cada sensor tiene direcciones de registro (por ejemplo `WHO_AM_I`) que te permiten comprobar que el chip responde. Para obtener datos, lees los registros de salida y conviertes los bytes en valores utilizables (ver sección de programación).

Para acceder a los archivos o programas guardados en la NOVA_pico, se utiliza exclusivamente **Thonny**, el entorno de programación oficial para estas placas. Desde **Thonny** puedes escribir código, subirlo a la NOVA_pico y ver los datos que lee la NOVA_sense — todo desde una sola ventana. No se modifica la memoria del sensor directamente; en su lugar se leen registros vía I2C.

### 2.5 La NOVA_pico como controlador

La `NOVA_pico` es una placa compatible con RP2 que puede ejecutar MicroPython.

**Cómo usar ambas juntas (resumen):**

- Conecta `3V3` <-> `3V3` y `GND` <-> `GND` entre `NOVA_pico` y `NOVA_sense`.
- Conecta `SDA` y `SCL` de la `NOVA_pico` a `SDA` y `SCL` de la `NOVA_sense`.
- Instala MicroPython en la `NOVA_pico` y abre Thonny.
- Desde Thonny puedes escribir scripts que usen la clase `I2C` para leer registros del sensor y guardar lecturas en archivos en la memoria de la `NOVA_pico` (por ejemplo `data.csv`). Thonny permite ver y descargar esos archivos fácilmente.

**Resumen práctico:** la `NOVA_pico` actúa como «cerebro» que habla con la `NOVA_sense` por I2C y almacena o envía los datos a tu computador para su análisis. Aquí nos centramos en cómo conectar físicamente y en las ideas generales para leer datos.

# 3 Programación con MicroPython

### 3.1 Herramientas recomendadas

- `Thonny`: recomendado para empezar con MicroPython; muestra la consola REPL y permite editar/guardar archivos en la placa fácilmente.

### 3.2 Ver las lecturas en Thonny

1. Conecta la `NOVA_pico` por USB y abre Thonny.
2. Selecciona el intérprete MicroPython correspondiente a tu placa.
3. Abre la consola REPL (panel inferior): al ejecutar `print()` verás la salida inmediatamente en esa consola; es útil para depurar lecturas del sensor.

### 3.3 Ejemplos básicos en MicroPython (en Thonny)

Nota: los ejemplos usan la clase `I2C` de MicroPython. Ajusta los pines `scl` y `sda` según tu placa (en la `NOVA_pico` suelen ser los pines I2C por defecto).

**Ejemplo A — Escanear el bus I2C y leer registro WHO_AM_I (identidad)**

```python
from machine import I2C, Pin
import time

# Ajusta los pines según tu placa
i2c = I2C(0, scl=Pin(21), sda=Pin(20))

print('Escaneando I2C...')
devices = i2c.scan()
print('Dispositivos I2C encontrados:', devices)

# Registro de identidad (WHO_AM_I) indicado para este sensor
WHO_REG = 0x4F

for dev in devices:
    try:
        who = i2c.readfrom_mem(dev, WHO_REG, 1)
        print('Dispositivo', hex(dev), 'WHO_AM_I =', who[0])
    except Exception:
        # no todos los dispositivos responden a ese registro
        pass

time.sleep(1)
```

En la consola de Thonny verás la lista de direcciones I2C detectadas y, si alguno responde al registro `WHO_AM_I`, su valor.

**Ejemplo B — Leer datos crudos del acelerómetro (lectura genérica)**

```python
from machine import I2C, Pin
import struct

i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# Reemplaza DEVICE_ADDR por la dirección que encontró tu escaneo
DEVICE_ADDR = 0x6A  # ejemplo, puede variar
OUTX_L = 0x28       # registro inicial de datos (ejemplo común)

def read_accel(addr):
    raw = i2c.readfrom_mem(addr, OUTX_L, 6)
    # convertir 6 bytes en tres valores signed 16-bit (little endian)
    x = struct.unpack('<h', raw[0:2])[0]
    y = struct.unpack('<h', raw[2:4])[0]
    z = struct.unpack('<h', raw[4:6])[0]
    # la escala depende del sensor; aquí mostramos los crudos
    return x, y, z

try:
    x, y, z = read_accel(DEVICE_ADDR)
    print('Acelerómetro raw:', x, y, z)
except Exception as e:
    print('Error:', e)
```

Explicación sencilla: los valores crudos son enteros que cambian si mueves el sensor. En Thonny verás los `print()` aparecer en la consola.

### 3.4 Guardar lecturas en un archivo desde Thonny

Puedes guardar lecturas en la memoria de la `NOVA_pico` para analizarlas luego:

```python
import time

with open('data.csv', 'w') as f:
    f.write('t,x,y,z\n')
    for t in range(100):
        x, y, z = read_accel(DEVICE_ADDR)
        f.write(f"{t},{x},{y},{z}\n")
        time.sleep(0.1)
```

**Consejos de depuración:**

- Usa `print()` para depurar en la consola de Thonny.
- Si obtienes errores de lectura, revisa que `GND` esté conectado correctamente y que la alimentación sea 3.3 V.

# 4 Seguridad y buenas prácticas

Antes de trabajar con la NOVA_sense, ten en cuenta estas recomendaciones para evitar daños al hardware y asegurar lecturas fiables:

- **Alimentación correcta**: usa 3.3 V en los pines de señal y alimentación. No conectes 5 V a los pines I2C o de señal.

- **GND común**: siempre conecta la masa (`GND`) entre la NOVA_pico (o microcontrolador) y la NOVA_sense antes de alimentar el sistema.

- **Conexiones firmes**: evita cables sueltos; utiliza conectores o headers bien soldados para prevenir desconexiones durante pruebas.

- **Evita campos magnéticos fuertes**: el magnetómetro (LIS2MDL) se altera con imanes o corrientes cercanas — mantén alejada la NOVA_sense de fuentes magnéticas potentes durante calibración y mediciones.

- **Calibración y pruebas iniciales**: realiza un `i2c.scan()` y verifica el `WHO_AM_I` antes de usar los datos; calibra la brújula si vas a usar orientación absoluta.

- **Protección ESD**: manipula la placa en una superficie antiestática o descarga tu energía con una pulsera ESD si trabajas en un entorno sensible.

- **Documenta cambios**: si modificas hardware (jumpers, resistencias), anota los cambios para reproducir pruebas y diagnóstico.
- **Sin garantía por daño físico**: si la placa se quema por una conexión incorrecta o sobrevoltaje, no tiene garantía. Tendrás que reemplazarla por una nueva.

# 5 Computación Física con NOVA_sense

### 5.1 Lecturas analógicas (ADC)

Contenido sobre lecturas analógicas...

### 5.2 Uso de sensores comunes (temperatura, luz, movimiento)

Contenido sobre sensores comunes...

### 5.3 Actuadores (motores, servos) y consideraciones de potencia

Contenido sobre actuadores...

# 6 Proyectos de ejemplo

### 6.1 Semáforo (Traffic light)

Contenido del proyecto semáforo...

### 6.2 Juego de reacción

Contenido del proyecto juego de reacción...

### 6.3 Alarma antirrobo básica

Contenido del proyecto alarma...

### 6.4 Registrador de datos (Data Logger)

Contenido del registrador de datos...

### 6.5 Ejemplos paso a paso: materiales, esquemas, código

Contenido paso a paso...
