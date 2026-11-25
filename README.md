# Urban Routes — QA Automation Testing Portfolio

**Python | Selenium WebDriver | Page Object Model | UI Test Automation**

**Author:** Carlos José Sánchez  
**Role:** QA Automation Trainee  
**Training:** TripleTen — QA Engineer Bootcamp  
**Project:** Urban Routes — Automated UI Testing

---

# English

## Project Overview

Urban Routes is a web-based transportation application used as part of the TripleTen QA Engineer training program.

This project demonstrates automated functional testing using Python and Selenium WebDriver. The test suite interacts with the application's user interface to verify key steps in the taxi booking workflow.

The automation code follows the Page Object Model (POM) pattern, separating page locators and interaction methods from the test scenarios.

## Technologies and Tools

| Technology | Purpose |
|---|---|
| Python | Test automation programming |
| Selenium WebDriver | Browser interaction and UI automation |
| Pytest-compatible test structure | Test discovery and execution |
| Google Chrome | Browser used for automated testing |
| Page Object Model | Organization of locators and page actions |
| WebDriverWait | Explicit waits for UI elements |
| XPath, CSS Selectors, ID | Element location strategies |
| Git and GitHub | Source code version control |

## Automated Test Scenarios

The `main.py` file contains nine automated test methods.

| # | Automated Test | Description |
|---|---|---|
| 1 | `test_set_route` | Verifies origin and destination fields |
| 2 | `test_select_comfort` | Verifies Comfort fare selection |
| 3 | `test_set_phone_number` | Performs phone number confirmation |
| 4 | `test_add_card` | Performs payment card registration |
| 5 | `test_message_for_driver` | Verifies the message entered for the driver |
| 6 | `test_blanket_and_handkerchiefs` | Verifies selection of blankets and handkerchiefs |
| 7 | `test_ice_cream` | Verifies that two ice creams can be added |
| 8 | `test_search_car_modal` | Verifies the car search modal appears |
| 9 | `test_driver_info` | Waits for driver arrival information (optional scenario) |

**Note:** These are nine implemented test methods, not a claim that all tests currently pass. Their latest execution status has not been verified.

## Automation Architecture

The project uses the Page Object Model design pattern.

### UrbanRoutesPage

This class contains:

- UI element locators.
- Page interaction methods.
- Form input actions.
- Explicit waits.
- Methods for retrieving interface values.
- Reusable actions for booking workflows.

### TestUrbanRoutes

This class contains the automated test scenarios, setup and teardown methods, and reusable workflow helpers.

### Reusable Methods

Examples include:

- `_go_to_comfort()` — Navigates to the Comfort fare.
- `_confirm_phone()` — Completes phone confirmation.
- `_add_card()` — Performs payment card registration.
- `click_visible_element()` — Handles visible element interaction and intercepted clicks.

## Project Structure

```text
qa-project-Urban-Routes-es/
├── main.py
├── data.py
├── .gitignore
└── README.md
```

**main.py:** Page Object Model implementation and automated test methods.

**data.py:** Test configuration and sample input data.

**.gitignore:** Files excluded from version control.

**README.md:** Project documentation.

## Test Data

The project uses sample data for:

- Origin and destination addresses.
- Phone number confirmation.
- Payment card input.
- Driver messages.
- Additional ride requirements.

Test data is stored separately in `data.py` to simplify maintenance.

The project uses training data and should not be configured with real payment credentials.

## How to Run the Tests

### Prerequisites

- Python 3
- Google Chrome
- Selenium
- Pytest
- Access to a running Urban Routes training server

### Installation

Clone the repository:

```bash
git clone https://github.com/zachecroacia-cyber/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es
```

Install the required Python packages:

```bash
python -m pip install selenium pytest
```

### Configure the Test Server

Open `data.py` and update the `urban_routes_url` variable with the current URL of an available Urban Routes training environment.

### Execute the Tests

```bash
python -m pytest -v main.py
```

This command uses Pytest to discover and execute the test methods defined in `main.py`.

**Important:** The Urban Routes application depends on a temporary TripleTen training server. The original server URL may no longer be available. Successful execution requires an accessible test environment and compatible browser configuration.

## Technical Highlights

- Automated web UI interactions using Selenium WebDriver.
- Implemented Page Object Model for reusable page actions.
- Used explicit waits to synchronize tests with UI behavior.
- Applied XPath, CSS selectors and element IDs.
- Organized test data separately from automation logic.
- Implemented assertions for selected functional outcomes.
- Automated multi-step user workflows.
- Used Chrome performance logs and a TripleTen-provided helper to retrieve phone confirmation codes.

## Current Project Status

**Automation code:** Available in this repository.

**Implemented test methods:** 9.

**Latest execution results:** Not verified.

**Training server:** External and potentially unavailable.

This repository demonstrates the automation implementation developed during QA training. It does not claim a current successful test run.

---

# Español

## Descripción del proyecto

Urban Routes es una aplicación web de transporte utilizada como parte del programa de formación QA Engineer de TripleTen.

Este proyecto demuestra la automatización de pruebas funcionales mediante Python y Selenium WebDriver. Los scripts interactúan con la interfaz de usuario para verificar diferentes etapas del proceso de solicitud de un taxi.

El código está organizado siguiendo el patrón Page Object Model (POM), que permite separar los localizadores y las acciones de la interfaz de los escenarios de prueba.

## Tecnologías y herramientas

| Tecnología | Aplicación |
|---|---|
| Python | Programación de pruebas automatizadas |
| Selenium WebDriver | Automatización de interfaz web |
| Estructura compatible con Pytest | Descubrimiento y ejecución de pruebas |
| Google Chrome | Navegador utilizado |
| Page Object Model | Organización del código |
| WebDriverWait | Esperas explícitas |
| XPath, CSS Selectors, ID | Localización de elementos |
| Git y GitHub | Control de versiones |

## Escenarios automatizados

El archivo `main.py` contiene nueve métodos de prueba automatizados.

| # | Prueba | Funcionalidad |
|---|---|---|
| 1 | `test_set_route` | Verificación de origen y destino |
| 2 | `test_select_comfort` | Selección de tarifa Comfort |
| 3 | `test_set_phone_number` | Confirmación del número telefónico |
| 4 | `test_add_card` | Registro de tarjeta de pago |
| 5 | `test_message_for_driver` | Validación del mensaje para el conductor |
| 6 | `test_blanket_and_handkerchiefs` | Selección de manta y pañuelos |
| 7 | `test_ice_cream` | Solicitud de dos helados |
| 8 | `test_search_car_modal` | Aparición del modal de búsqueda de automóvil |
| 9 | `test_driver_info` | Espera de información del conductor (opcional) |

**Nota:** Se identificaron nueve métodos de prueba implementados. No se ha verificado que todos pasen actualmente.

## Arquitectura de automatización

El proyecto utiliza el patrón de diseño Page Object Model.

### Clase UrbanRoutesPage

Contiene:

- Localizadores de elementos.
- Métodos de interacción con la interfaz.
- Acciones para completar formularios.
- Esperas explícitas.
- Métodos para consultar valores.
- Acciones reutilizables del proceso de solicitud.

### Clase TestUrbanRoutes

Contiene los escenarios automatizados, la configuración y cierre del navegador, y métodos auxiliares reutilizables.

### Métodos reutilizables

- `_go_to_comfort()` — Accede a la tarifa Comfort.
- `_confirm_phone()` — Ejecuta la confirmación telefónica.
- `_add_card()` — Ejecuta el registro de tarjeta.
- `click_visible_element()` — Gestiona clics sobre elementos visibles.

## Estructura del repositorio

```text
qa-project-Urban-Routes-es/
├── main.py
├── data.py
├── .gitignore
└── README.md
```

**main.py:** Implementación de Page Object Model y pruebas automatizadas.

**data.py:** Configuración y datos de prueba.

**.gitignore:** Exclusiones del control de versiones.

**README.md:** Documentación del proyecto.

## Datos de prueba

El proyecto utiliza información de ejemplo para:

- Direcciones de origen y destino.
- Confirmación telefónica.
- Datos de tarjeta de prueba.
- Mensajes para el conductor.
- Requisitos adicionales del viaje.

Los datos están separados del código principal para facilitar su mantenimiento.

## Instrucciones de ejecución

### Requisitos

- Python 3
- Google Chrome
- Selenium
- Pytest
- Acceso a un servidor activo de Urban Routes

### Instalación

Clonar el repositorio:

```bash
git clone https://github.com/zachecroacia-cyber/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es
```

Instalar las dependencias:

```bash
python -m pip install selenium pytest
```

### Configuración del servidor

Abrir `data.py` y actualizar la variable `urban_routes_url` con la dirección vigente de un entorno de pruebas Urban Routes.

### Ejecutar las pruebas

```bash
python -m pytest -v main.py
```

El comando permite a Pytest descubrir y ejecutar los métodos de prueba definidos en `main.py`.

**Importante:** Urban Routes depende de un servidor temporal de formación de TripleTen. La URL original puede dejar de estar disponible. La ejecución requiere un entorno activo y una configuración compatible del navegador.

## Competencias técnicas demostradas

- Automatización de interfaces web mediante Selenium WebDriver.
- Aplicación del patrón Page Object Model.
- Uso de esperas explícitas.
- Localización de elementos mediante XPath, CSS e ID.
- Separación de datos de prueba y lógica de automatización.
- Implementación de aserciones para determinados resultados.
- Automatización de flujos de usuario de varios pasos.
- Utilización de registros de rendimiento de Chrome y una función suministrada por TripleTen para recuperar códigos de confirmación.

## Estado actual del proyecto

**Código de automatización:** Disponible en el repositorio.

**Métodos de prueba implementados:** 9.

**Resultados de la última ejecución:** No verificados.

**Servidor de pruebas:** Externo y posiblemente no disponible.

Este repositorio demuestra el trabajo de automatización desarrollado durante la formación QA. No afirma que actualmente todas las pruebas se ejecuten satisfactoriamente.

---

## Education | Formación

**QA Engineer Bootcamp — TripleTen**

**Software Engineering — Politécnico Grancolombiano**

## Contact | Contacto

**GitHub:** [zachecroacia-cyber](https://github.com/zachecroacia-cyber)

**LinkedIn:** [Carlos Sánchez](https://www.linkedin.com/in/carlos-sanchez-161461172/)

---

*Educational QA automation project developed during the TripleTen QA Engineer training program.*

*Proyecto educativo de automatización QA desarrollado durante el programa de formación QA Engineer de TripleTen.*
