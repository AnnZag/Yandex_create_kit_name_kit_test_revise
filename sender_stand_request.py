import configuration
import requests
import data

# функция получения ответа на запрос по созданию пользвателя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставялем полный url
                         json=body,  # подставляем наше тело
                         headers=data.headers)  # подставляем хедеры


# функция получения ответа на запрос по созданию набора пользователя
def post_new_client_kit(kit_body, auth_token):
    headers_dict = data.headers.copy()
    headers_dict["Authorization"] = "Bearer " + auth_token;
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # подставялем полный url
                         json=kit_body,
                         headers=headers_dict)  # подставляем хедеры
