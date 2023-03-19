# import requests
# def transfer(mytext, lang):
#     key = 'AQVNxUftjE9DuiZSfUT6L9-umiFQpP9AoJ5ctszK' # API KEY
#     data = {'lang':lang,
#         'key':key,
#         'text':mytext,
#         'format':'plain'
#         }  # Параметры запроса
#     r = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', data = data).json() # POST запрос
#     r['mytext'] = mytext # Добавим наш текст
#     return r # ответ
#
# def read_text():
#     with open('Input.txt', 'r', encoding='utf8') as f:
#         text = f.read()
#     return text
#
# def write_text(text):
#     with open('Output.txt', 'w', encoding='utf8') as f:
#         f.write(text)
#
# languages = {
#     '1':'EN', '2':'ES', '3':'FR', '4':'DE', '5':'IT', '6':'ZH',
#     '7':'JA', '8':'KO', '9':'NL', '10':'SV', '11':'NO', '12':'EL', '13':'GD'
# }
#
# print("Numbers of laguage: ")
# for numb in languages:
#     print(numb,"-", languages[numb], end=' ')
# print()
# print(transfer('Hello', 'en'))
# # numbers = input("Write number of laguage, how in exemple(1 2 3): ").split()
#
# result_text = ''
# text = read_text()
# # for nmbr in numbers:
# #     traslate_text = transfer(text, languages[nmbr])['text'][0]
# #     result_text+=traslate_text
# # write_text(result_text)
import requests

IAM_TOKEN = 't1.9euelZqVnIzGlo-ay52Ll5DGz86Pke3rnpWayZTPlMaVlc-MyJeLyJGalJHl8_cNbi5f-e8PQXBE_t3z900cLF_57w9BcET-.pXoNhGPNSDME0Js87TXkOp6fwFkv4EuRdiPE-onHvGpv8-RCsWNsuv2DwYo4sFQupcm9SxjeuEBWhoILFvPpBg'
folder_id = 'b1g2ec7u74ik1bu5rd98'
target_language = 'ru'
texts = "World"

body = {
    "targetLanguageCode": target_language,
    "texts": texts,
    "folderId": folder_id,
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {0}".format(IAM_TOKEN)
}

response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
    json = body,
    headers = headers
)

print(response.text)