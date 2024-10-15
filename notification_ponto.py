import schedule
import time
from winotify import Notification, audio

def enviar_notificacao():
    try:
        notificacao = Notification(
            app_id="hora de bater o ponto",
            title="HORA DO PONTO!",
            msg="Vai bater o ponto Nicolas Rock",
            duration="short"
        )
        notificacao.set_audio(audio.LoopingCall10, loop=False)
        notificacao.add_actions(label="Portal", launch="#")
        notificacao.show()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

schedule.every().day.at("12:00").do(enviar_notificacao)
schedule.every().day.at("16:00").do(enviar_notificacao)
schedule.every().day.at("18:00").do(enviar_notificacao)

def main():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    print("O script está rodando. Pressione Ctrl+C para parar.")
    main()
