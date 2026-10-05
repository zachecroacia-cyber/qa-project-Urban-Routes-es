# Urban Routes - Automatización de pruebas

## Descripción del proyecto

Este proyecto contiene pruebas automatizadas para la aplicación Urban Routes.

El objetivo es validar el flujo principal de solicitud de un automóvil, desde la selección de la ruta hasta la aparición de la información del conductor.

Las pruebas comprueban los siguientes escenarios:

- Configuración de las direcciones de origen y destino.
- Selección de la tarifa Comfort.
- Registro y confirmación del número de teléfono.
- Adición de una tarjeta como método de pago.
- Escritura de un mensaje para el conductor.
- Selección de manta y pañuelos.
- Solicitud de dos helados.
- Verificación de la ventana de búsqueda de automóvil.
- Espera y verificación de la información del conductor.

## Tecnologías utilizadas

El proyecto utiliza las siguientes tecnologías:

- Python
- Selenium WebDriver
- Pytest
- Google Chrome
- ChromeDriver
- Page Object Model (POM)

## Técnicas utilizadas

Durante el desarrollo de las pruebas se utilizaron:

- Localizadores con ID, CSS Selector y XPath.
- Métodos del Page Object Model para separar las acciones de la interfaz de las pruebas.
- Esperas explícitas con `WebDriverWait`.
- Condiciones esperadas con `expected_conditions`.
- Validaciones mediante `assert`.
- Automatización de formularios y botones.
- Obtención automática del código de confirmación del teléfono mediante los logs de rendimiento del navegador.

## Estructura del proyecto

```text
qa-project-Urban-Routes-es/
│
├── data.py
├── main.py
└── README.md