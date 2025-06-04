from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

# Configure as opções do Firefox
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

# Instala e configura o geckodriver automaticamente
service = Service(GeckoDriverManager().install())

# Cria o driver do Firefox com o Service e as Options
driver = webdriver.Firefox(service=service, options=options)
wait = WebDriverWait(driver, 300)  # Espera até 5 minutos

try:
    # Acesse o Seller Central da Amazon
    driver.get("https://sellercentral.amazon.com/ap/signin?clientContext=134-6758950-5623144&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fsellercentral.amazon.com%2Fgp%2Fhomepage.html&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=sc_na_amazon_v2&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=sc_amazon_v3_unified&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&ssoResponse=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.6eMonWokOzJtkZVWQrOvcl_HZDWnp5ThF8UG1lQEBR5MyaS17dT0ig.YYjUwnjuWwKzzbxx.tU_7zBY94r_RrCVXfHi9xHMeWyKS3GruKfhcDnbbWLTgGzBf4qpWxpPzQj_Okr2oJS2jtJIk5EqxwIvPPW4L7LcbQlHnQmlFljXjxCmfpEFevjX0x68N2t1dd4Cw9l_YV4d6XO6qfdg3dpcs73AZKFmgrLmPnbPNOZqOFBsEjOiP_gnaITK4TGR7F93eVB3HFPCBg6hv.uU4ofyIlssucRisaTZfbqw")

    # Aguarda o campo de e-mail
    wait.until(EC.visibility_of_element_located((By.ID, "ap_email")))

    email = driver.find_element(By.ID, "ap_email")
    continue_btn = driver.find_element(By.ID, "continue")

    email.send_keys("neon80269@gmail.com")
    continue_btn.click()

    # Aguarda o campo de senha
    wait.until(EC.visibility_of_element_located((By.ID, "ap_password")))

    password = driver.find_element(By.ID, "ap_password")
    password.send_keys("neons226")

    # Clica no botão de login
    sign_in_btn = driver.find_element(By.ID, "signInSubmit")
    sign_in_btn.click()

    # Agora espera pela tela de OTP ou senha novamente
    try:
        # Verifica se a página de OTP ou outra autenticação aparece
        wait.until(EC.presence_of_element_located((By.ID, "ap_password")))
        print("Solicitação de senha novamente detectada.")
        password = driver.find_element(By.ID, "ap_password")
        password.send_keys("neons226")
        sign_in_btn = driver.find_element(By.ID, "signInSubmit")
        sign_in_btn.click()
    except:
        print("Nenhuma solicitação de senha detectada após o login inicial.")

    # Agora espera pela validação do OTP
    wait.until(EC.presence_of_element_located((
        By.CLASS_NAME, "full-page-account-switcher-accounts-wrapper"
    )))

    print("Ok, login realizado com sucesso!")
    
    sleep(3)
    
    account_labels = driver.find_elements(By.CLASS_NAME, "full-page-account-switcher-account-details")
    account_labels[2].click()
    
    sleep(1)
    
    btn_select = driver.find_element(By.CLASS_NAME, "kat-button")
    btn_select.click()
    
    sleep(2)
    
    driver.get("https://sellercentral.amazon.com/product-search/blank-form?ref=xx_catadd_dnav_xx")
    
    btn_product = driver.find_element(By.CSS_SELECTOR, "button")
    btn_product.click()

    # Continue com o seu script, depois que o login for feito
    sleep(200)  # Aqui você pode esperar mais tempo ou fazer outras ações no site

finally:
    driver.quit()
