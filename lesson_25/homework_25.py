from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space") # вводим логін та пароль в URL

driver.get("https://qauto2.forstudy.space/panel/garage")    # відкриваємо сторінку гаража
driver.maximize_window()

### Список XPATH локаторів для елементів на сторінці Garage ###
### Топ бар
XPATH_GARAGE_TOP_MENU_CONTAINS = (By.XPATH, "//a[contains(@class,'header-link') and contains(text(),'Garage')]")
XPATH_EXPENSES_TOP_MENU_TEXT = (By.XPATH, "//a[text()='Fuel expenses' and contains(@class,'header-link')]")
XPATH_INSTRUCTIONS_TOP_MENU_HREF = (By.XPATH, "//a[@href='/panel/instructions' and contains(@class,'header-link')]") 

# Відкриття модального вікна "Add car"
XPATH_ADD_CAR_BUTTON = (By.XPATH, "//button[contains(@class,'btn-primary') and text()='Add car']")  # кнопка "Add car" з текстом та класом, який містить "btn-primary"

XPATH_ADD_CAR_SELECT_BRAND = (By.XPATH, "//select[@id='addCarBrand']")
XPATH_ADD_CAR_SELECT_BRAND_BMW = (By.XPATH, "//select[@id='addCarBrand']/option[text()='BMW']") # опція "BMW" в селекті брендів за текстом

XPATH_ADD_CAR_SELECT_MODEL = (By.XPATH, "//select[@id='addCarModel']")
XPATH_ADD_CAR_SELECT_MODEL_BMW_X5 = (By.XPATH, "//select[@id='addCarModel']/option[text()='X5']")   # опція "X5" в селекті моделей за текстом

XPATH_ADD_CAR_MILEAGE_BY_ID = (By.XPATH, "//input[@id='addCarMileage']")    # поле для вводу пробігу за id

XPATH_ADD_CAR_SUBMIT_BY_TEXT = (By.XPATH, "//button[text()='Add']")   # кнопка "Add" за текстом
XPATH_ADD_CAR_CANCEL_BY_TEXT = (By.XPATH, "//div[contains(@class,'modal-footer')]//button[text()='Cancel']")  # кнопка "Cancel" за текстом та розташуванням в модальному вікні
XPATH_ADD_CAR_CANCEL_CLOSE_BY_ARIA = (By.XPATH, "//button[@aria-label='Close']")  # кнопка закриття модального вікна за атрибутом aria-label

# Локатори для елементів в дропдауні профілю
XPATH_PROFILE_DROPDOWN_GARAGE = (By.XPATH, "//a[@href='/panel/garage' and contains(@class,'user-nav_link')]")  # посилання "Garage" в користувацькому меню за href та класом
XPATH_PROFILE_DROPDOWN_EXPENSES = (By.XPATH, "//a[@href='/panel/expenses' and contains(@class,'user-nav_link')]")  # посилання "Expenses" в користувацькому меню за href та класом
XPATH_PROFILE_DROPDOWN_INSTRUCTIONS = (By.XPATH, "//a[@href='/panel/instructions' and contains(@class,'user-nav_link')]")  # посилання "Instructions" в користувацькому меню за href та класом
XPATH_PROFILE_DROPDOWN_LOGOUT = (By.XPATH, "//button[contains(@class,'user-nav_link') and contains(text(),'Logout')]")  # Logout через текст та клас в профайлі

### Боттом бар
XPATH_BOTTOM_BAR_LOGO_BUTTON = (By.XPATH, "//a[contains(@class,'footer_logo')]")  # логотип в футері що веде на головну сторінку

### Сторінка Instructions ###
# Локатори пошуку
XPATH_INSTRUCTIONS_SEARCH_BRAND_DROPDOWN = (By.XPATH, "//button[@id='brandSelectDropdown']")    # кнопка для відкриття дропдауну вибору бренду в інструкціях
XPATH_INSTRUCTIONS_SEARCH_BRAND_AUDI = (By.XPATH, "//ul[contains(@class,'dropdown-menu')]//li[text()='Audi']")  # опція "Audi" в дропдауні вибору бренду за текстом та розташуванням в меню

XPATH_INSTRUCTIONS_SEARCH_MODEL_DROPDOWN = (By.XPATH, "//button[@id='modelSelectDropdown']")  # кнопка для відкриття дропдауну вибору моделі в інструкціях
XPATH_INSTRUCTIONS_SEARCH_MODEL_R8 = (By.XPATH, "//ul[contains(@class,'model-select-dropdown_menu')]//li[text()='R8']")  # опція "R8" в дропдауні вибору моделі за текстом та розташуванням в меню

XPATH_INSTRUCTIONS_SEARCH_BUTTON = (By.XPATH, "//button[text()='Search']")  # кнопка "Search" за текстом

XPATH_INSTRUCTIONS_DOWNLOAD_ENGINE_OIL = (By.XPATH, "//p[contains(text(),'Engine oil')]")  # локатор для натискання на інструкцію для завантаження інформації про моторну оливу за текстом, який містить "Engine oil"

### Сторінка Fuel expenses ###
XPATH_FUEL_EXPENSES_EMPTY_WITH_GARAGE_BUTTON = (By.XPATH, "//a[text()='your garage']")  # локатор для натискання на посилання "your garage" в повідомленні про відсутність витрат на пальне, яке з'являється при порожньому гаражі
XPATH_FUEL_EXPENSES_ADD_EXPENSE_BUTTON = (By.XPATH, "//button[text()='Add an expense']")  # кнопка "Add expense" з текстом



### Список CSS локаторів для елементів на сторінці Garage ###
### Топ бар
CSS_GARAGE_TOP_MENU_HREF = (By.CSS_SELECTOR, "a.header-link[href='/panel/garage']")
CSS_EXPENSES_TOP_MENU_PARTIAL_HREF = (By.CSS_SELECTOR, "a.header-link[href*='expenses']")
CSS_INSTRUCTIONS_TOP_MENU_FULL_PATH = (By.CSS_SELECTOR, "body > app-root > app-global-layout > div > div > app-header > header > div > div > div > nav > a:nth-child(3)")   # повний шлях до елемента за допомогою "copy selector" в дев тулзах

# Відкриття модального вікна "Add car"
CSS_ADD_CAR_BUTTON = (By.CSS_SELECTOR, "btn btn-primary")  # кнопка "Add car" за класом, який містить "btn-primary"

CSS_ADD_CAR_SELECT_BRAND = (By.CSS_SELECTOR, "select#addCarBrand")
CSS_ADD_CAR_SELECT_BRAND_FORD = (By.CSS_SELECTOR, "select#addCarBrand > option[value='3']") # опція "Ford" в селекті брендів

CSS_ADD_CAR_SELECT_MODEL = (By.CSS_SELECTOR, "#select#addCarModel")
CSS_ADD_CAR_SELECT_MODEL_FORD_MONDEO = (By.CSS_SELECTOR, "select#addCarModel option[value='13']")   # опція "Mondeo" в селекті моделей

CSS_ADD_CAR_MILEAGE_BY_ID = (By.CSS_SELECTOR, "#addCarMileage") # поле для вводу пробігу за id

CSS_ADD_CAR_SUBMIT_BY_TEXT = (By.CSS_SELECTOR, "div.modal-footer .btn-primary")   # кнопка "Add" за розташуванням в модальному вікні
CSS_ADD_CAR_CANCEL_BY_TEXT = (By.CSS_SELECTOR, "div.modal-footer .btn-secondary")  # кнопка "Cancel" за розташуванням в модальному вікні
CSS_ADD_CAR_CANCEL_CLOSE_BY_ARIA = (By.CSS_SELECTOR, "button[aria-label='Close']")  # кнопка закриття модального вікна за атрибутом aria-label

# Локатори для елементів в дропдауні профілю
CSS_PROFILE_DROPDOWN_GARAGE = (By.CSS_SELECTOR, ".dropdown-menu a[href='/panel/garage']")  # посилання "Garage" в користувацькому меню за href
CSS_PROFILE_DROPDOWN_EXPENSES = (By.CSS_SELECTOR, ".dropdown-menu a[href='/panel/expenses']")  # посилання "Expenses" в користувацькому меню за href
CSS_PROFILE_DROPDOWN_INSTRUCTIONS = (By.CSS_SELECTOR, ".dropdown-menu a[href='/panel/instructions']")  # посилання "Instructions" в користувацькому меню за href
CSS_PROFILE_DROPDOWN_LOGOUT = (By.CSS_SELECTOR, ".dropdown-menu button.user-nav_link")  # Logout через клас в профайлі

### Боттом бар
CSS_BOTTOM_BAR_LOGO_BUTTON = (By.CSS_SELECTOR, "a.footer_logo")  # логотип в футері що веде на головну сторінку

### Сторінка Instructions ###
# Локатори пошуку
CSS_BRAND_DROPDOWN = (By.CSS_SELECTOR, "#brandSelectDropdown")  # кнопка для відкриття дропдауну вибору бренду в інструкціях
CSS_INSTRUCTIONS_SEARCH_BRAND_THIRD_ELEMENT = (By.CSS_SELECTOR, ".brand-select-dropdown_menu > li:nth-child(3)")  # опція "FORD" в дропдауні вибору бренду позицієбю третього елемента в списку

CSS_INSTRUCTIONS_SEARCH_MODEL_DROPDOWN = (By.CSS_SELECTOR, "#modelSelectDropdown")  # кнопка для відкриття дропдауну вибору моделі в інструкціях
CSS_INSTRUCTIONS_SEARCH_MODEL_FOCUS = (By.CSS_SELECTOR, ".model-select-dropdown_menu li:nth-child(2)")  # опція "Focus" в дропдауні вибору моделі за текстом та розташуванням в меню

CSS_INSTRUCTIONS_SEARCH_BUTTON = (By.CSS_SELECTOR, "button.instructions-search-controls_search")  # кнопка "Search" за класом та розташуванням в інструкціях (обрізає другий знайдений локатор в стилях, якщо по назві класу є декілька елементів)

CSS_INSTRUCTIONS_DOWNLOAD_BRAKE_PADS_FOCUS = (By.CSS_SELECTOR, "a.instruction-link_download[href$='https://qauto2.forstudy.space/public/instructions/ford/focus/Front brake pads on Ford Focus.pdf']")  # локатор для натискання на інструкцію для завантаження інформації за класом та повним співпадінням href, який веде на конкретний файл інструкції для Ford Focus

### Сторінка Fuel expenses ###
CSS_FUEL_EXPENSES_EMPTY_WITH_GARAGE_BUTTON = (By.CSS_SELECTOR, ".panel-empty_message a[href='/panel/garage']")  # локатор для натискання на посилання "your garage" в повідомленні про відсутність витрат на пальне, яке з'являється при порожньому гаражі
CSS_FUEL_EXPENSES_ADD_EXPENSE_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary")  # кнопка "Add expense" по класу, який містить "btn-primary"