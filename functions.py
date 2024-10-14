import re


def fio(list_):
    for fio_ in list_[1:]:
        name_parts = ' '.join(fio_[:3]).split()

        match len(name_parts):
            case 3:
                fio_[0] = name_parts[0]
                fio_[1] = name_parts[1]
                fio_[2] = name_parts[2]
            case 2:
                fio_[0] = name_parts[0]
                fio_[1] = name_parts[1]
                fio_[2] = ''
            case 1:
                fio_[0] = name_parts[0]
                fio_[1] = ''
                fio_[2] = ''
    return list_


def phone_check(list_):
    phone_pattern = re.compile(
            r'(\+7|8)?\s*\(?(\d{3})\)?[-\s*]?(\d{3})[-\s*]?(\d{2})[-\s*]?(\d{2})(\s*)\(?(доб.?)?\s*(\d*)?\)?')
    phone_substitution = r'+7(\2)\3-\4-\5\6\7\8'

    for phone_ in list_[1:len(list_) - 1]:
        phone_[5] = phone_pattern.sub(phone_substitution, phone_[5])
    return list_


def delete_dub(list_):
    new_list = []
    for fio_1 in list_:
        for fio_2 in list_:
            if fio_1[0] == fio_2[0] and fio_1[1] == fio_2[1]:
                for idx in range(len(fio_1)):
                    if fio_1[idx] == '':
                        fio_1[idx] = fio_2[idx]
        if fio_1 not in new_list:
            new_list.append(fio_1)

    return new_list
