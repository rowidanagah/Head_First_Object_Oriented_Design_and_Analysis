from InstrumentSpec import *
from instrument import Instrument


# class Style:
#     def __init__(self, style):
#         self.style = style

#     def equal(self, otherStyle):
#         return otherStyle.style == self.style

#     def getStyle(self):
#         return self.style


class MandolinSpec(InstrumentSpec):
    def __init__(self, builder, type_of, model, backwood, topwood, style):
        super().__init__(builder, type_of, model, backwood, topwood)
        self.style = style

    def match(self, InsSpec):
        if not super().match(InsSpec):
            return False
        return (
            isinstance(InsSpec, MandolinSpec) and self.getStyle() == InsSpec.getStyle()
        )

    def getStyle(self):
        return self.style


class Mandolin(Instrument):
    def __init__(self, serialNumber, price, spec: MandolinSpec):
        super().__init__(serialNumber, price, spec)

    def __str__(self) -> str:
        return super().__str__() + "Mandolin"
