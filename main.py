import requests

if __name__ == "__main__":
    url = 'https://hooks.slack.com/services/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'
    msg = input('Introduce el mensaje que quieres enviar: ')
    r = requests.post(url, json={'text':msg})
    if(r.text == 'ok'):
        print('El mensaje ha sido enviado')
    else:
        print(r.text)