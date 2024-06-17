from enum import Enum
from Guitar import Guitar, GuitarSpace
from inventory import Inventory


class Type(Enum):
    """
    This class is created to get rid of and ditch this annoying string comparison.
    """

    ACOUSTIC = "ACOUSTIC"
    ELECTRIC = "ELECTRIC"

    def to_string(self):
        return ACOUSTIC.Title(), ELECTRIC.Title()

    def __repr__(self):
        return "{} or {}".format(ACOUSTIC.Title(), ELECTRIC.Title())


class Builder(Enum):
    FENDER = "FENDER"
    MARTIN = "MARTIN"
    GIBSON = "GIBSON"

    def to_string(self):
        return FENDER.Title, GIBSON.Title(), MARTIN.Title()

    def __repr__(self):
        return "{}, {}, or {}".format(FENDER.Title, GIBSON.Title(), MARTIN.Title())


class Wood(Enum):
    CEDAR = "CEDAR"
    MAPLE = "MAPLE"
    COCOBOLO = "COCOBOLO"
    ALDER = "ALDER"

    def to_string(self):
        return CEDAR.Title(), ALDER.Title(), COCOBOLO.Title(), MAPLE.Title()

    def __repr__(self):
        return "{}, {}, {}, or {}".format(
            CEDAR.Title(), ALDER.Title(), COCOBOLO.Title(), MAPLE.Title()
        )


class FindGuitarTester:
    def __init__(self):
        self.inv = Inventory()

    def main(self):
        """
        The objective is to search for gts
        """
        ##self.initialize_inventory()
        new_guitar = Guitar(
            "",
            0,
            Builder.FENDER,
            "Sratocastor",
            Type.ELECTRIC,
            Wood.ALDER,
            Wood.ALDER,
            12,
        )
        guitar = self.inv.search_guitar(new_guitar)
        return self.inv.display_guitar(guitar) if guitar else "Not Found"

    def initialize_inventory(self):
        guitar_1 = Guitar(
            "",
            0,
            Builder.FENDER,
            "Sratocastor",
            Type.ELECTRIC,
            Wood.ALDER,
            Wood.ALDER,
            12,
        )
        guitar_2 = Guitar(
            "V95693",
            1499.95,
            Builder.FENDER,
            "Sratocastor",
            Type.ELECTRIC,
            Wood.ALDER,
            Wood.ALDER,
            12,
        )
        guitar_3 = Guitar(
            "V95123",
            1543.95,
            Builder.FENDER,
            "sratocastor",
            Type.ELECTRIC,
            Wood.ALDER,
            Wood.ALDER,
            12,
        )
        guitar_4 = Guitar(
            "V54312",
            1249.95,
            Builder.FENDER,
            "sratocastor",
            Type.ELECTRIC,
            Wood.ALDER,
            Wood.ALDER,
        )
        self.inv.add_guitar(guitar_1)
        self.inv.add_guitar(guitar_2)
        self.inv.add_guitar(guitar_3)
        self.inv.add_guitar(guitar_4)

        return self.inv.display_guitar()


obj = FindGuitarTester()
obj.initialize_inventory()
print(
    "------------------------------------------------Test main----------------------------------------"
)
obj.main()
