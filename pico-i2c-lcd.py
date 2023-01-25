import I2C_LCD_driver

lcd = I2C_LCD_driver.lcd()

lcd.lcd_display_string("Hello World!", 1)
lcd.lcd_display_string("Maker's Lab.", 2)
