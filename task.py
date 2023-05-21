import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from redis_helper import RedisHelper


def send_alert():
    # RedisHelper nesnesi oluştur
    helper = RedisHelper()

    # Bağlantıyı aç
    helper.open_connection()

    # Listeye veri yaz
    helper.write_to_list('my_list', ['apple', 'banana', 'cherry'])

    # Özel bir veri tipiyle yaz (TTL ile)
    custom_data = {'name': 'John', 'age': 30, 'city': 'New York'}
    helper.write_custom_type('my_key', custom_data, ttl=3600)  # TTL 1 saat (3600 saniye)

    # Özel bir veri tipiyle yaz (TTL ile)
    custom_data = {'name': 'John', 'age': 30, 'city': 'New York'}
    helper.write_custom_type('my_custom_key', custom_data, ttl=3600)  # TTL 1 saat (3600 saniye)

    # Veri oku
    print(helper.read_from_redis('my_custom_key'))

    #print(helper.read_from_redis('my_list'))
    print(helper.read_from_redis('my_key'))

    # Belirli bir anahtara TTL ayarla
    #helper.set_ttl('another_key', 300)  # TTL 5 dakika (300 saniye)

    # Bağlantıyı kapat
    helper.close_connection()


if __name__ == "__main__":
    print(f"Running script at {datetime.now()}")
    send_alert()