from src.channel import Channel

if __name__ == '__main__':
    # 'UCMCgOm8GZkHp8zJ6l7_hIuA'  # вДудь
    # 'UC5A-Wp9ujcr5g9sYagAafEA'  # Смешарики
    # 'UC1eFXmJNkjITxPFWTy6RsWg'  # Редакция
    ch = Channel('UC5A-Wp9ujcr5g9sYagAafEA')
    ch.connect()
    ch.print_info()
    print("\n ")
    ch.get_title()
    ch.set_parameters()