import machine, ssd1306
from machine import Pin, SoftI2C
from time import sleep

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000) #ESP32 Dev Board /myown
oled = ssd1306.SSD1306_I2C(128,64, i2c)

def receive(lora):
    print("LoRa Receiver")
    oled.fill(0)
    oled.text("LoRa Receiver", 10, 10)
    oled.show()

    while True:
        if lora.received_packet():
            lora.blink_led()
            payload = lora.read_payload()
            print(payload)
            oled.fill(0)
            oled.text(payload, 10, 10)
            oled.show()
            
