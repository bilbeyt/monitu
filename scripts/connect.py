from robobrowser import RoboBrowser

url = 'https://portal.itu.edu.tr'

username = input("Username: ")
password = input("Password: ")

browser = RoboBrowser(history=True)
browser.open(url)

signin = browser.get_form(id="form1")
signin["ctl00$ContentPlaceHolder1$tbUserName"].value = username
signin["ctl00$ContentPlaceHolder1$tbPassword"].value = password
signin["ctl00$ContentPlaceHolder1$btnLogin"].value = "Giriş"

browser.submit_form(signin)

transcript_url = ("http://ssb.sis.itu.edu.tr:9000
        /pls/PROD/p_transcript.p_id_response")

browser.open(transcript_url)
pin = input("PIN: ")

pin_form = browser.get_form(action="http://ssb.sis.itu.edu.tr:9000
        /pls/PROD/twbkwbis.P_ValLogin")
pin_form["PIN"].value = pin
pin_form["ButtonSelected"].value = ""

browser.submit_form(pin_form)

redirection_url = browser.parsed.meta["content"][6:]
base_url = "http://ssb.sis.itu.edu.tr:9000"
url = base_url + redirection_url

browser.open(url)

browser.open(transcript_url)
print(browser.parsed)

