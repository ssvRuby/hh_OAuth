## Поиск по вакансиям, похожим на резюме

Данные доступны только автору резюме.

### Запрос

`GET /resumes/{resume_id}/similar_vacancies`

где resume_id - идентификатор резюме.

Принимает те же параметры, что и поиск по вакансиям.

При указании параметров пагинации (page, per_page) работает ограничение: глубина возвращаемых результатов не может быть больше 2000. Например, возможен запрос per_page=10&page=199 (выдача с 1991 по 2000 вакансию), но запрос с per_page=10&page=200 вернёт ошибку (выдача с 2001 до 2010 вакансию).

### Ответ

Успешный ответ приходит с кодом 200 OK и содержит тело в том же виде, что и поиск по вакансиям

### Ошибки

`400 Bad Request` - параметры переданы с ошибкой

`404 Not Found` - резюме с идентификатором resume_id не существует или недоступно

## Поиск по вакансиям

### Запрос

`GET /vacancies` вернёт результаты поиска вакансий.

Принимаемые параметры:

!! Внимание: неизвестные параметры и параметры с ошибкой в названии игнорируются
Некоторые параметры принимают множественные значения: key=value&key=value.

text — текстовое поле.
Переданное значение ищется в полях вакансии, указанных в параметре search_field.
Доступен язык запросов, как и на основном сайте: https://hh.ru/article/1175. Специально для этого поля есть автодополнение.

search_field — область поиска.
Справочник с возможными значениями: vacancy_search_fields в /dictionaries.
По умолчанию, используются все поля.
Возможно указание нескольких значений.

experience — опыт работы.
Необходимо передавать id из справочника experience в /dictionaries.
Возможно указание нескольких значений.

employment — тип занятости. Необходимо передавать id из справочника employment в /dictionaries.
Возможно указание нескольких значений.

schedule — график работы.
Необходимо передавать id из справочника schedule в /dictionaries.
Возможно указание нескольких значений.

 area — регион. Необходимо передавать id из справочника /areas.
Возможно указание нескольких значений.

metro — ветка или станция метро.
Необходимо передавать id из справочника /metro.
Возможно указание нескольких значений.

specialization — профобласть или специализация. Необходимо передавать id из справочника /specializations.
Возможно указание нескольких значений. Будет заменен профессиональными ролями (параметр professional_role), в настоящее время работает в режиме обратной совместимости.

professional_role - профессиональная область. Необходимо передавать id из справочника /professional_roles

industry - индустрия компании, разместившей вакансию. Необходимо передавать id из справочника /industries. Возможно указание нескольких значений.

employer_id — идентификатор компании.
Возможно указание нескольких значений.

currency — код валюты.
Справочник с возможными значениями: currency (ключ code) в /dictionaries.
Имеет смысл указывать только совместно с параметром salary.

salary — размер заработной платы.
Если указано это поле, но не указано currency, то используется значение RUR у currency.
При указании значения будут найдены вакансии, в которых вилка зарплаты близка к указанной в запросе. При этом значения пересчитываются по текущим курсам ЦБ РФ. Например, при указании salary=100&currency=EUR будут найдены вакансии, где вилка зарплаты указана в рублях и после пересчёта в Евро близка к 100 EUR. По умолчанию будут также найдены вакансии, в которых вилка зарплаты не указана, чтобы такие вакансии отфильтровать, используйте only_with_salary=true.

label — фильтр по меткам вакансий.
Необходимо передавать id из справочника vacancy_label в /dictionaries.
Возможно указание нескольких значений.

only_with_salary — показывать вакансии только с указанием зарплаты.
Возможные значения: true или false.
По умолчанию, используется false.

period — количество дней, в пределах которых нужно найти вакансии.
Максимальное значение: 30.

date_from – дата, которая ограничивает снизу диапазон дат публикации вакансий.
Нельзя передавать вместе с параметром period.
Значение указывается в формате ISO 8601 - YYYY-MM-DD или с точность до секунды YYYY-MM-DDThh:mm:ss±hhmm.
Указанное значение будет округлено до ближайших 5 минут.

date_to – дата, которая ограничивает сверху диапазон дат публикации вакансий.
Необходимо передавать только в паре с параметром date_from.
Нельзя передавать вместе с параметром period.
Значение указывается в формате ISO 8601 - YYYY-MM-DD или с точность до секунды YYYY-MM-DDThh:mm:ss±hhmm.
Указанное значение будет округлено до ближайших 5 минут.

top_lat, bottom_lat, left_lng, right_lng — значение гео-координат.
При поиске используется значение указанного в вакансии адреса.
Принимаемое значение — градусы в виде десятичной дроби.
Необходимо передавать одновременно все четыре параметра гео-координат, иначе вернется ошибка.

order_by — сортировка списка вакансий.
Справочник с возможными значениями: vacancy_search_order в /dictionaries.
Если выбрана сортировка по удалённости от гео-точки distance, необходимо также задать её координаты sort_point_lat,sort_point_lng.

sort_point_lat, sort_point_lng - значение гео-координат точки, по расстоянию от которой будут отсортированы вакансии. Необходимо указывать только, если order_by установлено в distance.

clusters — возвращать ли кластеры для данного поиска, по умолчанию: false.

describe_arguments — возвращать ли описание использованных параметров поиска, по умолчанию: false.

per_page, page — параметры пагинации. Параметр per_page ограничен значением в 100.

no_magic – Если значение true – отключить автоматическое преобразование вакансий. По умолчанию – false. При включённом автоматическом преобразовании, будет предпринята попытка изменить текстовый запрос пользователя на набор параметров. Например, запрос text=москва бухгалтер 100500 будет преобразован в text=бухгалтер&only_with_salary=true&area=1&salary=100500.

premium – Если значение true – в сортировке вакансий будет учтены премиум вакансии. Такая сортировка используется на сайте. По умолчанию – false.

responses_count_enabled — Если значение true – включить дополнительное поле counters с количеством откликов для вакансии. По-умолчанию – false.

part_time — Вакансии для подработки. Возможные значения:

все элементы из working_days в /dictionaries.
все элементы из working_time_intervals в /dictionaries.
все элементы из working_time_modes в /dictionaries.
элементы part или project из employment в /dictionaries.
элемент accept_temporary, показывает вакансии только с временным трудоустройством.
Возможно указание нескольких значений.

professional_role — профессиональная роль. Необходимо передавать id из справочника professional_roles. Возможно указание нескольких значений. Замена специализациям (параметр specialization)

При указании параметров пагинации (page, per_page) работает ограничение: глубина возвращаемых результатов не может быть больше 2000. Например, возможен запрос per_page=10&page=199 (выдача с 1991 по 2000 вакансию), но запрос с per_page=10&page=200 вернёт ошибку (выдача с 2001 до 2010 вакансию).