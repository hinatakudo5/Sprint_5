import time
import random

def generate_email():
    # Требование из задания: формат логин@домен (пример 123@ya.ru)
    # Делаем уникальный, чтобы регистрация всегда проходила
    ts = int(time.time())
    n = random.randint(100, 999)
    return f"{n}{ts}@ya.ru"

def generate_password():
    # Минимум 6 символов
    return "123456"

def generate_name():
    return "Zarina"
