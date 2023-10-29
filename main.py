my_to_do_list = []


def add_data_to_list():
    duty = input("Görevi girin")
    my_to_do_list.append(duty)
    print("görev eklendi")


def show_duty():
    print("Yapılacak görevler")
    for duty in my_to_do_list:
        print("-"+duty)


def delete_duty_by_index():
    print("Mevcut görevler:")
    for index, duty in enumerate(my_to_do_list):
        print(f"{index}. {duty}")

    try:
        duty_index = int(input("Silmek istediğiniz görevin numarasını girin: "))
        if 0 <= duty_index < len(my_to_do_list):
            deleted_duty = my_to_do_list.pop(duty_index)
            print(f"'{deleted_duty}' görevi başarıyla silindi.")
        else:
            print("Girilen numara geçersiz.")
    except ValueError:
        print("Lütfen geçerli bir numara girin.")




def print_commands():
    print("\nTo Do List Uygulaması")
    print("1.Görev Ekleyin")
    print("2.Görevleri Görün")
    print("3.Görev Silin")
    print("4.Çıkış")


def process_command(choice):
    if choice == "1":
        add_data_to_list()
    elif choice == "2":
        show_duty()
    elif choice == "3":
        delete_duty_by_index()
    elif choice == "4":
        print("Uygulama kapanıyor")
    else:
        print("Geçersiz seçim ltüfen")


while True:
    print_commands()
    choice = input("Seçiminiz (1/2/3/4): ")
    process_command(choice)





