# 8. Napisati klasu koja opisuje iotUredjaj.
# Uredjaj sadrzi serijski broj, koji je jedinstven i id_na_cloudu.
# Overrajdovati str(Uredjaj) tako da prikazuje podatke odvojene zarezom.


class IOTUredjaj(object):
    """
    A class to represent a IOT device.

    Attributes
    ----------
    :param serijski_broj: unique serial number of the device
    :type serijski_broj: int
    :param id_na_cloudu: device identifier on the cloud
    :type id_na_cloudu: str

    Methods
    -------
    __init__(brojilac : serijski_broj: int, id_na_cloudu: str):
    Constructs all the necessary attributes for the IOTUredjaj object.
    :param serijski_broj: unique serial number of the device
    :param id_na_cloudu: device identifier on the cloud
    """
    serijski_broj = 0
    id_na_cloudu = ""

    def __init__(self, serijski_broj: int, id_na_cloudu: str):
        self.serijski_broj = serijski_broj
        self.id_na_cloudu = id_na_cloudu

    def __repr__(self):
        return {'Serijski broj': self.serijski_broj, 'id_na_cloudu': self.id_na_cloudu}

    def __str__(self):
        # return 'Serijski broj = ' + str(self.serijski_broj) + ', id_na_cloudu = ' + self.id_na_cloudu
        return str(self.serijski_broj) + ',' + self.id_na_cloudu


# print(IOTUredjaj.__doc__)
