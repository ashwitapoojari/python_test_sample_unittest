class MathHelper:

    def calc(self, operation, n1, n2):
        switcher = {
            'addition': self._add(n1, n2),
            'subtraction': self._sub(n1, n2),
            'multiplication': self._mul(n1, n2),
            'division': self._div(n1, n2)
        }

        return switcher.get(operation, None)

    @staticmethod
    def _add(n1, n2):
        return n1 + n2

    @staticmethod
    def _sub(n1, n2):
        return n1 - n2

    @staticmethod
    def _mul(n1, n2):
        return n1 * n2

    @staticmethod
    def _div(n1, n2):
        return n1 / n2
