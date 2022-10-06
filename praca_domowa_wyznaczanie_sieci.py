# otwórz plik z danymi
f = open("dane_sieci.txt", "r+")


# funkcja do uzykania adresu rozgłoszeniowego
def get_final_broadcaster(ip_address, hosts_to_add):
    # uzyskaj części adresu IP i maski
    ip_address_parts = ip_address.split('.')
    hosts_to_add_parts = hosts_to_add.split('.')

    # lista części adresu rozgłoszeniowego
    broadcaster_parts_list = []

    # dla każdej części adresu IP i maski (jest ich zawsze 4)
    for i in range(4):
        # dodaj je ze sobą aby uzyskać finalny broadcaster i dodaj go do listy części rozgłoszeniowego
        broadcaster_parts_list.append(int(ip_address_parts[i]) + int(hosts_to_add_parts[i]))

    # połącz części adresu w jeden w postaci takiej jak IP
    final_broadcaster_address = ".".join([str(final_part) for final_part in broadcaster_parts_list])

    # zwróć końcowy broadcaster
    return final_broadcaster_address


# funkcja do zmiany liczby z binarnej na dziesiętną
def from_binary_to_decimal(binary_part):
    # początkowo konwertowana liczba jest równa 0
    number = 0

    # sprawdzanie każdego elementu binarnej licbzy
    for i in range(0, 8):
        # dodawanie wartości binernej 1 do wartości dziesiętnej całej liczby
        number += int(binary_part[i]) * 2**(7 - i)

    # zwracanie liczby
    return number


# funkcja do konwersji z binarnej na dziesiętną
def convert_to_decimal(binary_number):
    # lista dla dziesiętnych części binarnej liczby
    decimal_number_parts = []

    # bierz co 8 element liczby binarnej
    for i in range(0, 25, 8):
        # twórz nową liczbę złożoną z kolejnych ośmiu cyfr
        part = binary_number[i:i+8]
        # przekonwertowane liczby wrzucaj do listy
        decimal_number_parts.append(from_binary_to_decimal(part))

    # stwórz string, który połączy kropką wszystkie liczby z listy (wygląda to dzięki temu jak adres IP)
    final_decimal = ".".join([str(decimal_number) for decimal_number in decimal_number_parts])

    # zwróć liczbę
    return final_decimal


# funkcja operacji AND
def and_operation(ip_address, subnet_mask):
    # wynik operacji AND przedstawiony jako string
    and_result = ""

    # sprawdź każdą liczbę IP i maski
    for i in range(32):
        # jeżeli liczba z adresu IP odpowiada liczbie z maski z tego samego indeksu (niezależnie '1' czy '0') dodaj tą liczbę
        # do wyniku opercji AND
        if ip_address[i] == subnet_mask[i]:
            and_result += ip_address[i]
        # a w przeciwnym wypadku zwróć '0'
        else:
            and_result += '0'

    # zwróc resultat operacji AND
    return and_result


# funkcja operacji OR
def or_operation(subnet_mask):
    # wynik operacji OR przedstawiony jako string
    or_result = ""

    # sprawdź każdą liczbę maski
    for i in range(32):
        # jeżeli liczba w masce jest '0' to dodaj '1' do wyniku operacji OR
        if subnet_mask[i] == '0':
            or_result += '1'
        # a w przeciwnym wypadku zwróć '0'
        else:
            or_result += '0'

    # zwróc resultat operacji OR
    return or_result


# funkcja do zmiany liczby na adres IP
def convert_from_number_to_binary(number):
    # numer w postaci string jest początkowo pusty
    binary_number = ""

    # pętla od 1 do 8, aby szybko obliczyć 2^8, 2^7, 2^6 itp
    for i in range(1, 9):
        # sprawdzanie czy aktualna liczba jest większa lub równa aktualnej potędze 2
        if number >= 2**(8 - i):
            # jeśli jest to dodaj do binarnej liczby 1 i odejmij tą potęgę 2 od liczby int
            binary_number += '1'
            number -= 2**(8 - i)
        else:
            # a jeśli nie to dodaj 0 do liczby binarnej
            binary_number += '0'

    # zwróć uzyskany numer binarny
    return binary_number


# funckja do konwersji adresu IP/maski podsieci na postać binarną
def convert_to_binary(data):
    # binarnie dane będą jako string
    data_in_binary = ""

    # uzyskiwanie części maski/IP rozdzielonych . i połączenie ich wszystkich do jednej listy
    data_parts = data.split(".")

    for part in data_parts:
        # dla każdego oktetu przekonwertuj do wersji binarnej i dodaj do poprzednich części
        data_in_binary += convert_from_number_to_binary(int(part))

    # zwróć numer IP/maski w postaci binarnej
    return data_in_binary


# funkcja do uzyskania adresu sieci
def get_network_address(network_data):
    # dane z listy przypisz zmiennym
    ip_address = network_data[0]
    subnet_mask = network_data[1]

    # uzyskaj adres IP i maskę podsieci w postaci binarnej
    binary_ip_address = convert_to_binary(ip_address)
    binary_subnet_mask = convert_to_binary(subnet_mask)

    # wykonaj operację AND
    and_result = and_operation(binary_ip_address, binary_subnet_mask)

    # przekształć wynik binarny w dziesiętny
    final_network_address = convert_to_decimal(and_result)

    # zwróć adres sieci
    return final_network_address


# uzyskaj adres rozgłoszeniowy sieci
def get_broadcast_address(subnet_mask, network_address):
    # uzyskaj adres IP i maskę podsieci w postaci binarnej
    binary_subnet_mask = convert_to_binary(subnet_mask)

    # wykonaj operację OR
    or_result = or_operation(binary_subnet_mask)

    # przekształć wynik binarny w dziesiętny
    hosts_to_add = convert_to_decimal(or_result)

    # uzyskaj finalny broadcaster
    final_broadcaster_address = get_final_broadcaster(network_address, hosts_to_add)

    # zwróć adres sieci
    return final_broadcaster_address


# uzyskaj maksymalną liczbę hostów sieci
def get_maximal_hosts_numer(subnet_mask):
    # uzyskaj maskę w postaci binarnej
    binary_subnet_mask = convert_to_binary(subnet_mask)

    # policz ile jest zer w wersji binarnej maski
    zero_counter = binary_subnet_mask.count('0')

    # ze wzrou na liczbę hostów wyznacz ją
    hosts_number = 2**zero_counter - 2

    # zwróć liczbę hostów
    return hosts_number


# lista danych z pliku
network_data = []

# pobierz IP i maske z pliku .txt
for line in f:
    # usuwanie znaku nowej lini z odczytanej lini pliku .txt
    line_without_new_line_char = line.strip("\n")

    # dodaj tą linie do listy danych sieci
    network_data.append(line_without_new_line_char)

# zamknij plik, aby go nie uszkodzić
f.close()

# uzyskaj adres sieci, adres rozgłoszeniowy i maksymalną liczbę hostów
network_address = get_network_address(network_data)
broadcast = get_broadcast_address(network_data[1], network_address)
max_possible_hosts = get_maximal_hosts_numer(network_data[1])

# przedstaw dane
print(f"Adres IP: {network_data[0]}\n"
      f"Maska podsieci: {network_data[1]}\n"
      f"Adres sieci: {network_address}\n"
      f"Adres rozgłoszeniowy sieci: {broadcast}\n"
      f"Maksymalna liczba hostów: {max_possible_hosts}")
