from src.channel import Channel

if __name__ == '__main__':
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    vdud = Channel("UC1eFXmJNkjITxPFWTy6RsWg")

    vdud.connect()
    vdud.print_info()
    vdud.set_parameters()

    # получаем значения атрибутов
    print(vdud.title)  # вДудь
    print(vdud.video_count)  # 163 (может уже больше)
    print(vdud.url)  # https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA

    # менять не можем
    try:
        vdud.channel_id = 'Новое название'
    except AttributeError:
        print("property 'channel_id' of 'Channel' object has no setter")
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'vdud.json' в данными по каналу
    vdud.to_json('vdud.json')

    who_is_it = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
    who_is_it.print_info()
