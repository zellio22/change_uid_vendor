Import("env")

board_config = env.BoardConfig()
board_config.update("build.hwids", [
  ["0x27B8", "0x01ED"]
])
board_config.update("build.usb_product", "LVDM_joystick")
board_config.update("vendor", "Zellio")