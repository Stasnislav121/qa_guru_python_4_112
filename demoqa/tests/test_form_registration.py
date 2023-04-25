import allure
from demoqa.pages.registration_page import StudentRegistrationPage



@allure.title("Заполнение формы регистрации студенты")
def test_registration_form_(browser_setup):
    registration_page = StudentRegistrationPage()
    with allure.step("Открытие сайта"):
        registration_page.open()

    # WHEN
    with allure.step("Заполнение данными"):
        registration_page.fill_first_name('Ivan')
        registration_page.fill_last_name('Petrov')
        registration_page.fill_email('petrov@abc.com')
        registration_page.select_gender('Male')
        registration_page.fill_mobile('7123456789')
        registration_page.fill_date_of_birth("1917", "January", "5")
        registration_page.fill_subjects('Maths')
        registration_page.select_hobbies('Sports')
        registration_page.upload_picture('one.png')
        registration_page.fill_current_address('Rome, Italy')
        registration_page.select_state('Uttar Pradesh')
        registration_page.select_city('Agra')
        registration_page.submit()

    # THEN
    with allure.step("Проверка результата"):
        registration_page.should_have_registered_user_with(
            'Ivan Petrov',
            'petrov@abc.com',
            'Male',
            '7123456789',
            '05 January,1917',
            'Maths',
            'Sports',
            'one.png',
            'Rome, Italy',
            'Uttar Pradesh Agra'
        )
