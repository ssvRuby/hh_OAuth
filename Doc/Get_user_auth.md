### Получение авторизации пользователя 

>>> https://hh.ru/oauth/authorize?
  response_type=code&
  client_id={client_id}&
  state={state}&
  redirect_uri={redirect_uri}
  
client_id     = 'G19TJUH81CU90PS626NJ6FIL9DRRI595VAR5ATKFIR67FPVGEDHH2SHB6V21Q5C8'
client_secret = 'OURA8MIC2HG714FPRG74ROS2465HS1JLCI01020I7LBOO9PTD687GQDFVLF4A9RN'
access_token  = 'H79VIKAUMUAU4T0TCLH276FIQSKRPLD9QRFP00NT2RBOF8PBEBOIR38B6Q615T8N'

В своем приложении вы размещаете ссылку на авторизацию, указывая в ней Client ID приложения, например,
https://hh.ru/oauth/authorize?response_type=code&client_id=LOTHHN3BSET0I7IQNF3N5I0362AE1D14I6M74CAIQ5H49F7MT4PLMTVV7JTOA6QA

Когда пользователь переходит по этой ссылке, для него на нашей стороне генерируется специальный код. И наш сайт перенаправляет пользователя обратно в ваше приложение (по redirect URI, который был указан при регистрации приложения), добавив к адресу вашего приложения параметр, содержащий код. Например:
http://yourapphost/?code=J2CO4TM7PK58NNVFCJSLPMML15IKQERD5CT2L8VGK82Q333ILAKQ28BPURIO1LG8

После этого вы вытаскиваете из этого адреса code и используете его для получения токена, сделав POST-запрос в API, передав code, client_id и client_secret.
curl -k -X POST -H 'User-Agent: api-test-agent' -d 'grant_type=authorization_code&client_id=LOTHHN3BSET0I7IQNF3N5I0362AE1D14I6M74CAIQ5H49F7MT4PLMTVV7JTOA6QA&client_secret=JS33UVG3J6JANNEATPND57BME23BKDCPP2UH1NB0C21HUMNGS5T71AVP6P24E0EI&code=J2CO4TM7PK58NNVFCJSLPMML15IKQERD5CT2L8VGK82Q333ILAKQ28BPURIO1LG8' https://hh.ru/oauth/token

В ответ вы получите json, содержащий токен (поле access_token):
{
  "access_token": "VTEJ4PDD8R4MHEO7LTQM6RLEGJ1O8B1F79TGF45LIDQD11K50HMMBETB47BBCMQ1",
  "token_type": "bearer",
  "expires_in": 1209599,
  "refresh_token": "OARLQNLT6JSMDI88CO5QIP35OOSQUTOO9IQNT20MOMAHE4H8SGPM7LQUAP8EO1G6"
}

Это всё. Далее, выполняя запросы в API с заголовком Authorization: Bearer your_access_token, вы будете выполнять действия из-под пользователя. Чтобы на каждый запрос не выполнять авторизацию, сохраняйте у себя access_token. 

Вот, например, запрос для получения списка резюме текущего пользователя:
curl -k -H 'Authorization: Bearer VTEJ4PDD8R4MHEO7LTQM6RLEGJ1O8B1F79TGF45LIDQD11K50HMMBETB21BBCMQ1' -H 'User-Agent: api-test-agent' https://api.hh.ru/resumes/mine

Следует учесть, что у токена есть срок жизни, указанный в поле expires_in, после истечения которого токен надо обновить.

https://habr.com/en/company/hh/blog/303168/