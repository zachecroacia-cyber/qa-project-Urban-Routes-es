import data

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException


# =========================================================
# FUNCIÓN DE TRIPLETEN - NO MODIFICAR
# =========================================================

def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException

    code = None

    for i in range(10):
        try:
            logs = [
                log["message"]
                for log in driver.get_log("performance")
                if log.get("message")
                and "api/v1/number?number" in log.get("message")
            ]

            for log in reversed(logs):
                message_data = json.loads(log)["message"]

                body = driver.execute_cdp_cmd(
                    "Network.getResponseBody",
                    {"requestId": message_data["params"]["requestId"]}
                )

                code = "".join(
                    [x for x in body["body"] if x.isdigit()]
                )

        except WebDriverException:
            time.sleep(1)
            continue

        if not code:
            raise Exception(
                "No se encontró el código de confirmación del teléfono.\n"
                "Utiliza 'retrieve_phone_code' solo después de haber "
                "solicitado el código en tu aplicación."
            )

        return code


# =========================================================
# PAGE OBJECT
# =========================================================

class UrbanRoutesPage:

    # =====================================================
    # LOCALIZADORES - DIRECCIONES
    # =====================================================

    from_field = (
        By.ID,
        "from"
    )

    to_field = (
        By.ID,
        "to"
    )

    # =====================================================
    # LOCALIZADORES - COMFORT
    # =====================================================

    flash_mode = (
        By.XPATH,
        "//div[contains(@class,'mode') "
        "and normalize-space()='Flash']"
    )

    taxi_type = (
        By.XPATH,
        "//img[contains(@src,'taxi')]"
    )

    order_taxi_button = (
        By.XPATH,
        "//button[normalize-space()='Pedir un taxi']"
    )

    comfort_tariff = (
        By.XPATH,
        "//div[@class='tcard-title' "
        "and normalize-space()='Comfort']"
    )

    comfort_card = (
        By.XPATH,
        "//div[@class='tcard-title' "
        "and normalize-space()='Comfort']/parent::div"
    )

    # =====================================================
    # LOCALIZADORES - TELÉFONO
    # =====================================================

    phone_button = (
        By.XPATH,
        "//div[@class='np-text' "
        "and normalize-space()='Número de teléfono']"
        "/parent::div"
    )

    phone_field = (
        By.ID,
        "phone"
    )

    next_phone_button = (
        By.XPATH,
        "//button[normalize-space()='Siguiente']"
    )

    phone_code_field = (
        By.ID,
        "code"
    )

    confirm_phone_button = (
        By.XPATH,
        "//button[normalize-space()='Confirmar']"
    )

    # =====================================================
    # LOCALIZADORES - TARJETA
    # =====================================================

    payment_method_button = (
        By.XPATH,
        "//div[@class='pp-text' "
        "and normalize-space()='Método de pago']"
        "/parent::div"
    )

    add_card_button = (
        By.XPATH,
        "//div[@class='pp-title' "
        "and normalize-space()='Agregar tarjeta']"
        "/parent::div"
    )

    card_number_field = (
        By.CSS_SELECTOR,
        "input#number.card-input"
    )

    card_code_field = (
        By.CSS_SELECTOR,
        "input#code.card-input"
    )

    add_card_confirm_button = (
        By.XPATH,
        "//button[normalize-space()='Agregar']"
    )

    close_payment_button = (
        By.XPATH,
        "//div[contains(@class,'payment-picker') "
        "and contains(@class,'open')]"
        "//button[contains(@class,'close-button') "
        "and contains(@class,'section-close')]"
    )

    # =====================================================
    # LOCALIZADORES - MENSAJE
    # =====================================================

    message_field = (
        By.ID,
        "comment"
    )

    # =====================================================
    # LOCALIZADORES - REQUISITOS
    # =====================================================

    requirements_section = (
        By.CSS_SELECTOR,
        "div.reqs"
    )

    requirements_button = (
        By.CSS_SELECTOR,
        "div.reqs-header"
    )

    # =====================================================
    # LOCALIZADORES - MANTA Y PAÑUELOS
    # =====================================================

    blanket_switch = (
        By.XPATH,
        "//div[contains(@class,'r-sw-container')]"
        "[.//div[contains(@class,'r-sw-label') "
        "and normalize-space()='Manta y pañuelos']]"
        "//span[contains(@class,'slider')]"
    )

    blanket_checkbox = (
        By.XPATH,
        "//div[contains(@class,'r-sw-container')]"
        "[.//div[contains(@class,'r-sw-label') "
        "and normalize-space()='Manta y pañuelos']]"
        "//input[@type='checkbox']"
    )

    # =====================================================
    # LOCALIZADORES - HELADO
    # =====================================================

    ice_cream_plus_button = (
        By.XPATH,
        "//div[contains(@class,'r-counter-container')]"
        "[.//div[contains(@class,'r-counter-label') "
        "and normalize-space()='Helado']]"
        "//div[contains(@class,'counter-plus')]"
    )

    ice_cream_count = (
        By.XPATH,
        "//div[contains(@class,'r-counter-container')]"
        "[.//div[contains(@class,'r-counter-label') "
        "and normalize-space()='Helado']]"
        "//div[contains(@class,'counter-value')]"
    )

    # =====================================================
    # LOCALIZADORES - BUSCAR AUTOMÓVIL
    # =====================================================

    order_car_button = (
        By.CSS_SELECTOR,
        "button.smart-button"
    )

    search_car_modal = (
        By.XPATH,
        "//*[normalize-space()='Buscar automóvil']"
    )

    # =====================================================
    # LOCALIZADOR - INFORMACIÓN DEL CONDUCTOR
    # EJERCICIO OPCIONAL
    # =====================================================

    driver_info = (
        By.XPATH,
        "//*[contains(text(), 'El conductor llegará en')]"
    )

    # =====================================================
    # CONSTRUCTOR
    # =====================================================

    def __init__(self, driver):
        self.driver = driver

    # =====================================================
    # MÉTODO AUXILIAR - CLIC
    # =====================================================

    def click_visible_element(self, locator):

        element = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                locator
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView("
            "{block: 'center'});",
            element
        )

        try:
            element.click()

        except ElementClickInterceptedException:
            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    # =====================================================
    # DIRECCIONES
    # =====================================================

    def wait_for_load_routes_page(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.from_field
            )
        )

    def set_from(self, address):

        self.driver.find_element(
            *self.from_field
        ).send_keys(address)

    def set_to(self, address):

        self.driver.find_element(
            *self.to_field
        ).send_keys(address)

    def set_route(
        self,
        address_from,
        address_to
    ):

        self.set_from(
            address_from
        )

        self.set_to(
            address_to
        )

    def get_from(self):

        return self.driver.find_element(
            *self.from_field
        ).get_property("value")

    def get_to(self):

        return self.driver.find_element(
            *self.to_field
        ).get_property("value")

    # =====================================================
    # COMFORT
    # =====================================================

    def select_flash_mode(self):

        self.click_visible_element(
            self.flash_mode
        )

    def select_taxi_type(self):

        self.click_visible_element(
            self.taxi_type
        )

    def click_order_taxi_button(self):

        self.click_visible_element(
            self.order_taxi_button
        )

    def wait_for_comfort_tariff(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.comfort_tariff
            )
        )

    def select_comfort_tariff(self):

        self.click_visible_element(
            self.comfort_tariff
        )

    def get_comfort_card_class(self):

        return self.driver.find_element(
            *self.comfort_card
        ).get_attribute("class")

    # =====================================================
    # TELÉFONO
    # =====================================================

    def click_phone_button(self):

        self.click_visible_element(
            self.phone_button
        )

    def wait_for_phone_field(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.phone_field
            )
        )

    def set_phone(
        self,
        phone_number
    ):

        self.driver.find_element(
            *self.phone_field
        ).send_keys(
            phone_number
        )

    def get_phone(self):

        return self.driver.find_element(
            *self.phone_field
        ).get_property("value")

    def click_next_phone_button(self):

        self.click_visible_element(
            self.next_phone_button
        )

    def wait_for_phone_code_field(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.phone_code_field
            )
        )

    def set_phone_code(
        self,
        code
    ):

        self.driver.find_element(
            *self.phone_code_field
        ).send_keys(
            code
        )

    def click_confirm_phone_button(self):

        self.click_visible_element(
            self.confirm_phone_button
        )

    # =====================================================
    # TARJETA
    # =====================================================

    def click_payment_method(self):

        self.click_visible_element(
            self.payment_method_button
        )

    def click_add_card(self):

        self.click_visible_element(
            self.add_card_button
        )

    def wait_for_card_number_field(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.card_number_field
            )
        )

    def set_card_number(
        self,
        card_number
    ):

        self.driver.find_element(
            *self.card_number_field
        ).send_keys(
            card_number
        )

    def set_card_code(
        self,
        card_code
    ):

        code_field = self.driver.find_element(
            *self.card_code_field
        )

        code_field.send_keys(
            card_code
        )

        # El CVV debe perder el foco
        code_field.send_keys(
            Keys.TAB
        )

    def click_add_card_confirm(self):

        self.click_visible_element(
            self.add_card_confirm_button
        )

    def wait_for_card_modal_to_close(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.invisibility_of_element_located(
                self.card_number_field
            )
        )

    def close_payment_method(self):

        self.click_visible_element(
            self.close_payment_button
        )

    # =====================================================
    # MENSAJE AL CONDUCTOR
    # =====================================================

    def set_message_for_driver(
        self,
        message
    ):

        self.driver.find_element(
            *self.message_field
        ).send_keys(
            message
        )

    def get_message_for_driver(self):

        return self.driver.find_element(
            *self.message_field
        ).get_property("value")

    # =====================================================
    # REQUISITOS
    # =====================================================

    def open_requirements(self):

        section = self.driver.find_element(
            *self.requirements_section
        )

        section_class = section.get_attribute(
            "class"
        )

        if "open" not in section_class.split():

            self.click_visible_element(
                self.requirements_button
            )

        WebDriverWait(
            self.driver,
            10
        ).until(
            lambda driver:
            "open"
            in driver.find_element(
                *self.requirements_section
            ).get_attribute(
                "class"
            ).split()
        )

    # =====================================================
    # MANTA Y PAÑUELOS
    # =====================================================

    def order_blanket_and_handkerchiefs(self):

        self.click_visible_element(
            self.blanket_switch
        )

    def blanket_and_handkerchiefs_is_selected(self):

        return self.driver.find_element(
            *self.blanket_checkbox
        ).is_selected()

    # =====================================================
    # HELADOS
    # =====================================================

    def add_ice_cream(self):

        self.click_visible_element(
            self.ice_cream_plus_button
        )

    def get_ice_cream_count(self):

        return self.driver.find_element(
            *self.ice_cream_count
        ).text

    # =====================================================
    # BUSCAR AUTOMÓVIL
    # =====================================================

    def click_order_car_button(self):

        self.click_visible_element(
            self.order_car_button
        )

    def wait_for_search_car_modal(self):

        WebDriverWait(
            self.driver,
            5,
            poll_frequency=0.1
        ).until(
            EC.visibility_of_element_located(
                self.search_car_modal
            )
        )

        return True

    # =====================================================
    # INFORMACIÓN DEL CONDUCTOR - OPCIONAL
    # =====================================================

    def wait_for_driver_info(self):

        WebDriverWait(
            self.driver,
            60,
            poll_frequency=0.2
        ).until(
            EC.visibility_of_element_located(
                self.driver_info
            )
        )

        return True


# =========================================================
# TESTS
# =========================================================

class TestUrbanRoutes:

    driver = None

    # =====================================================
    # SETUP
    # =====================================================

    @classmethod
    def setup_class(cls):

        options = webdriver.ChromeOptions()

        options.set_capability(
            "goog:loggingPrefs",
            {"performance": "ALL"}
        )

        cls.driver = webdriver.Chrome(
            options=options
        )

    # =====================================================
    # AUXILIAR - LLEGAR A COMFORT
    # =====================================================

    def _go_to_comfort(self):

        self.driver.get(
            data.urban_routes_url
        )

        routes_page = UrbanRoutesPage(
            self.driver
        )

        routes_page.wait_for_load_routes_page()

        routes_page.set_route(
            data.address_from,
            data.address_to
        )

        routes_page.select_flash_mode()

        routes_page.select_taxi_type()

        routes_page.click_order_taxi_button()

        routes_page.wait_for_comfort_tariff()

        routes_page.select_comfort_tariff()

        return routes_page

    # =====================================================
    # AUXILIAR - CONFIRMAR TELÉFONO
    # =====================================================

    def _confirm_phone(
        self,
        routes_page
    ):

        routes_page.click_phone_button()

        routes_page.wait_for_phone_field()

        phone_number = (
            data.phone_number.replace(
                " ",
                ""
            )
        )

        routes_page.set_phone(
            phone_number
        )

        routes_page.click_next_phone_button()

        routes_page.wait_for_phone_code_field()

        phone_code = retrieve_phone_code(
            self.driver
        )

        routes_page.set_phone_code(
            phone_code
        )

        routes_page.click_confirm_phone_button()

    # =====================================================
    # AUXILIAR - AGREGAR TARJETA
    # =====================================================

    def _add_card(
        self,
        routes_page
    ):

        routes_page.click_payment_method()

        routes_page.click_add_card()

        routes_page.wait_for_card_number_field()

        routes_page.set_card_number(
            data.card_number
        )

        routes_page.set_card_code(
            data.card_code
        )

        routes_page.click_add_card_confirm()

        routes_page.wait_for_card_modal_to_close()

        routes_page.close_payment_method()

    # =====================================================
    # TEST 1 - DIRECCIONES
    # =====================================================

    def test_set_route(self):

        self.driver.get(
            data.urban_routes_url
        )

        routes_page = UrbanRoutesPage(
            self.driver
        )

        routes_page.wait_for_load_routes_page()

        routes_page.set_route(
            data.address_from,
            data.address_to
        )

        assert (
            routes_page.get_from()
            == data.address_from
        )

        assert (
            routes_page.get_to()
            == data.address_to
        )

    # =====================================================
    # TEST 2 - COMFORT
    # =====================================================

    def test_select_comfort(self):

        routes_page = self._go_to_comfort()

        assert (
            "active"
            in routes_page.get_comfort_card_class()
        )

    # =====================================================
    # TEST 3 - TELÉFONO
    # =====================================================

    def test_set_phone_number(self):

        routes_page = self._go_to_comfort()

        self._confirm_phone(
            routes_page
        )

    # =====================================================
    # TEST 4 - TARJETA
    # =====================================================

    def test_add_card(self):

        routes_page = self._go_to_comfort()

        self._confirm_phone(
            routes_page
        )

        self._add_card(
            routes_page
        )

    # =====================================================
    # TEST 5 - MENSAJE
    # =====================================================

    def test_message_for_driver(self):

        routes_page = self._go_to_comfort()

        self._confirm_phone(
            routes_page
        )

        self._add_card(
            routes_page
        )

        routes_page.set_message_for_driver(
            data.message_for_driver
        )

        assert (
            routes_page.get_message_for_driver()
            == data.message_for_driver
        )

    # =====================================================
    # TEST 6 - MANTA Y PAÑUELOS
    # =====================================================

    def test_blanket_and_handkerchiefs(self):

        routes_page = self._go_to_comfort()

        self._confirm_phone(
            routes_page
        )

        self._add_card(
            routes_page
        )

        routes_page.open_requirements()

        routes_page.order_blanket_and_handkerchiefs()

        assert (
            routes_page.blanket_and_handkerchiefs_is_selected()
            is True
        )

    # =====================================================
    # TEST 7 - DOS HELADOS
    # =====================================================

    def test_ice_cream(self):

        routes_page = self._go_to_comfort()

        self._confirm_phone(
            routes_page
        )

        self._add_card(
            routes_page
        )

        routes_page.open_requirements()

        routes_page.add_ice_cream()

        routes_page.add_ice_cream()

        assert (
            routes_page.get_ice_cream_count()
            == "2"
        )

    # =====================================================
    # TEST 8 - BUSCAR AUTOMÓVIL
    # =====================================================

    def test_search_car_modal(self):

        routes_page = self._go_to_comfort()

        self._confirm_phone(
            routes_page
        )

        self._add_card(
            routes_page
        )

        routes_page.set_message_for_driver(
            data.message_for_driver
        )

        routes_page.open_requirements()

        routes_page.order_blanket_and_handkerchiefs()

        routes_page.add_ice_cream()
        routes_page.add_ice_cream()

        routes_page.click_order_car_button()

        assert (
            routes_page.wait_for_search_car_modal()
            is True
        )

    # =====================================================
    # TEST 9 - INFORMACIÓN DEL CONDUCTOR
    # OPCIONAL
    # =====================================================

    def test_driver_info(self):

        routes_page = self._go_to_comfort()

        # Confirmar teléfono
        self._confirm_phone(
            routes_page
        )

        # Agregar tarjeta
        self._add_card(
            routes_page
        )

        # Mensaje para el conductor
        routes_page.set_message_for_driver(
            data.message_for_driver
        )

        # Abrir requisitos
        routes_page.open_requirements()

        # Manta y pañuelos
        routes_page.order_blanket_and_handkerchiefs()

        # Dos helados
        routes_page.add_ice_cream()
        routes_page.add_ice_cream()

        # Pedir automóvil
        routes_page.click_order_car_button()

        # Esperar hasta que la búsqueda termine
        # y aparezca:
        # "El conductor llegará en X min."
        assert (
            routes_page.wait_for_driver_info()
            is True
        )

    # =====================================================
    # TEARDOWN
    # =====================================================

    @classmethod
    def teardown_class(cls):

        cls.driver.quit()