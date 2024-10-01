import machine, ssd1306
from machine import Pin, SoftI2C
from time import sleep
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000) #ESP32 Dev Board /myown
oled = ssd1306.SSD1306_I2C(128,64, i2c)

def send(lora):
    counter = 0
    print("LoRa Sender")

    while True:
        payload = f'Hello {counter}'
        #print("Sending packet: \n{}\n".format(payload))
        #oled.show_text_wrap("{0} RSSI: {1}".format(payload, lora.packet_rssi()))
        lora.println(payload)
        oled.fill(0)
        oled.text('Sending packet:' , 0, 0)
        oled.text(f'{payload}' , 0, 10)
        oled.show()
        counter += 1
        sleep(5)

