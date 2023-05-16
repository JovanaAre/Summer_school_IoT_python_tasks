# 10. Napisati funkciju koja čita Sve Uredjaje u memoriju iz fajla.


import os


def read_txt() -> str:
    """
    Reads all IOT devices from the text file with devices (uredjaji_fajl.txt)
    and returns the read string

    :param: None
    :return: read string containing all read devices
    """
    with open(os.environ["FILE_PATH_1"], 'r') as f:
        lines = f.read()
    ioturedjaji = lines
    # ioturedjaji.strip()
    # serijski_brojevi = []
    # len(lines)
    # for line in lines:
    #     tmp = line[:6]     # serijski broj je int duzine 6
    #     print(tmp)
    #     serijski_brojevi.append(tmp)
    # print(str(ioturedjaji))
    # print(serijski_brojevi)
    return ioturedjaji


# print(read_txt.__doc__)
