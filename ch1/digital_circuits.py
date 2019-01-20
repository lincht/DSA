from itertools import product


class LogicGate:
    """Simulation of logic gate."""
    
    def __init__(self, label):
        self.label = label
        self.output = None
    
    def get_label(self):
        """Identify gate."""
        return self.label
    
    def get_output(self):
        """Call method implemented in subclasses to produce output."""
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    """Logic gate with two input lines."""
    
    def __init__(self, label):
        
        # Call constructor of parent class
        super().__init__(label)
        
        # Add own distinguishing data
        self.pinA = None
        self.pinB = None
    
    def get_pinA(self):
        """Get input from pin A."""
        
        # If the input is not connected to anything, prompt for input
        if self.pinA is None:
            return int(input('Enter pin A input for gate {}: '.format(self.get_label())))
        
        # If there is a connection, get source gate's output through connector
        elif isinstance(self.pinA, Connector):
            
            # Connected to a gate with 1-bit output
            if self.pinA.cout is None:
                return self.pinA.get_from().get_output()
            else:
                # Connected to COUT of 2-bit output
                if self.pinA.cout:
                    return self.pinA.get_from().get_output()[1]
                # Connected to SUM of 2-bit output
                else:
                    return self.pinA.get_from().get_output()[0]
        
        # Otherwise get manually set value
        else:
            return self.pinA
    
    def get_pinB(self):
        """Get input from pin B."""
        
        if self.pinB is None:
            return int(input('Enter pin B input for gate {}: '.format(self.get_label())))
        elif isinstance(self.pinB, Connector):
            if self.pinB.cout is None:
                return self.pinB.get_from().get_output()
            else:
                if self.pinB.cout:
                    return self.pinB.get_from().get_output()[1]
                else:
                    return self.pinB.get_from().get_output()[0]
        else:
            return self.pinB
    
    def set_next_pin(self, source):
        """Connect one of the inputs to the specified source gate."""
        
        # Choose pin A by default
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError('No empty pins on this gate')


class TernaryGate(BinaryGate):
    """Logic gate with two input lines and an additional CIN input."""
    
    def __init__(self, label):
        super().__init__(label)
        self.C_in = None
    
    def get_C_in(self):        
        if self.C_in is None:
            return int(input('Enter CIN input for gate {}: '.format(self.get_label())))
        elif isinstance(self.C_in, Connector):
            if self.C_in.cout is None:
                return self.C_in.get_from().get_output()
            else:
                if self.C_in.cout:
                    return self.C_in.get_from().get_output()[1]
                else:
                    return self.C_in.get_from().get_output()[0]
        else:
            return self.C_in
    
    def set_C_in(self, source):
        """Connect CIN to the specified source gate."""
        
        if self.C_in is None:
            self.C_in = source
        else:
            raise RuntimeError('CIN already connected')


class UnaryGate(LogicGate):
    """Logic gate with one input line."""
    
    def __init__(self, label):
        super().__init__(label)
        self.pin = None
    
    def get_pin(self):
        if self.pin is None:
            return int(input('Enter pin input for gate {}:'.format(self.get_label())))
        elif isinstance(self.pin, Connector):
            return self.pin.get_from().get_output()
        else:
            return self.pin
    
    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError('No empty pins on this gate')


class AndGate(BinaryGate):
    
    def __init__(self, label):
        super().__init__(label)
    
    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if a==1 and b==1:
            return 1
        else:
            return 0


class NandGate(BinaryGate):
    
    def __init__(self, label):
        super().__init__(label)
    
    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if a==1 and b==1:
            return 0
        else:
            return 1


class OrGate(BinaryGate):
    
    def __init__(self, label):
        super().__init__(label)
    
    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if a==1 or b==1:
            return 1
        else:
            return 0


class NorGate(BinaryGate):
    
    def __init__(self, label):
        super().__init__(label)
    
    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if a==1 or b==1:
            return 0
        else:
            return 1


class XorGate(BinaryGate):
    
    def __init__(self, label):
        super().__init__(label)
    
    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if a == b:
            return 0
        else:
            return 1      


class NotGate(UnaryGate):
    
    def __init__(self, label):
        super().__init__(label)
    
    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class Connector:
    
    def __init__(self, fgate, tgate, cout=None, cin=False):
        """
        Parameters
        ----------
        cout : bool or None, default: None
            Whether to connect to fromgate's COUT, None if connecting to a gate with 1-bit output.
            If False, connect to fromgate's SUM.
        
        cin : bool, default: False
            Whether to connect to togate's CIN.
        """
        
        self.fromgate = fgate
        self.togate = tgate
        self.cout = cout
        
        if cin:
            tgate.set_C_in(self)
        else:
            tgate.set_next_pin(self)
    
    def get_from(self):
        return self.fromgate
    
    def get_to(self):
        return self.togate


class HalfAdder(BinaryGate):
    """Implementation of 1-bit half adder."""
    
    def __init__(self, label):
        super().__init__(label)
        self.XOR = XorGate(label + '_XOR')
        self.AND = AndGate(label + '_AND')
    
    def perform_gate_logic(self):
        # Store input for reuse
        A = self.get_pinA()
        B = self.get_pinB()
        self.XOR.pinA = self.AND.pinA = A
        self.XOR.pinB = self.AND.pinB = B
        
        SUM = self.XOR.get_output()
        C_out = self.AND.get_output()
        return SUM, C_out


class FullAdder(TernaryGate):
    """Implementation of 1-bit full adder."""
    
    def __init__(self, label):
        super().__init__(label)
        self.HA1 = HalfAdder(label + 'HA1')
        self.HA2 = HalfAdder(label + 'HA2')
        self.OR = OrGate(label + 'OR')
        c1 = Connector(self.HA1, self.HA2, cout=False)
        c2 = Connector(self.HA1, self.OR, cout=True)
        c3 = Connector(self.HA2, self.OR, cout=True)
        
    def perform_gate_logic(self):
        A = self.get_pinA()
        B = self.get_pinB()
        C_in = self.get_C_in()
        self.HA1.pinA = A
        self.HA1.pinB = B
        self.HA2.pinB = C_in
        
        SUM = self.HA2.get_output()[0]
        C_out = self.OR.get_output()
        return SUM, C_out


class EightBitFullAdder(TernaryGate):
    """Implementation of 8-bit full adder."""
    
    def __init__(self, label):
        super().__init__(label)
        # Use half adder for the first adder
        self.HA1 = HalfAdder('HA1')
        self.FA2 = FullAdder('FA2')
        self.FA3 = FullAdder('FA3')
        self.FA4 = FullAdder('FA4')
        self.FA5 = FullAdder('FA5')
        self.FA6 = FullAdder('FA6')
        self.FA7 = FullAdder('FA7')
        self.FA8 = FullAdder('FA8')
        c12 = Connector(self.HA1, self.FA2, cout=True, cin=True)
        c23 = Connector(self.FA2, self.FA3, cout=True, cin=True)
        c34 = Connector(self.FA3, self.FA4, cout=True, cin=True)
        c45 = Connector(self.FA4, self.FA5, cout=True, cin=True)
        c56 = Connector(self.FA5, self.FA6, cout=True, cin=True)
        c67 = Connector(self.FA6, self.FA7, cout=True, cin=True)
        c78 = Connector(self.FA7, self.FA8, cout=True, cin=True)
    
    def perform_gate_logic(self):
        
        # For readability, prompt for decimal inputs
        self.pinA = int(input('Enter input A (8-bit integer, 0-255): '))
        self.pinB = int(input('Enter input B (8-bit integer, 0-255): '))
        # Convert to binary string and reverse
        pinA_bits = str(bin(self.pinA))[2:].zfill(8)[::-1]
        pinB_bits = str(bin(self.pinB))[2:].zfill(8)[::-1]
        
        # Set inputs for all gates
        gates = ['HA1'] + ['FA'+str(i) for i in range(2, 9)]
        for g, A, B in zip(gates, pinA_bits, pinB_bits):
            getattr(self, g).pinA = int(A)
            getattr(self, g).pinB = int(B)
        
        # Concatenate outputs and reverse
        output = ''.join([str(getattr(self, g).get_output()[0]) for g in gates])[::-1]
        # Convert back to decimal
        output = int(eval('0b' + output))
        
        return output


def main():
    
    # NOT((A and B) or (C and D))
    g1 = AndGate('G1')
    g2 = AndGate('G2')
    g3 = OrGate('G3')
    g4 = NotGate('G4')
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    
    # NOT(A and B) and NOT(C and D)
    g5 = NandGate('G5')
    g6 = NandGate('G6')
    g7 = AndGate('G7')
    c4 = Connector(g5, g7)
    c5 = Connector(g6, g7)
    
    print('A B C D   Equal')
    for A, B, C, D in product(*[[0, 1]]*4):
        
        g1.pinA = g5.pinA = A
        g1.pinB = g5.pinB = B
        g2.pinA = g6.pinA = C
        g2.pinB = g6.pinB = D
        
        print('{} {} {} {} : {!s:>5}'.format(A, B, C, D, g4.get_output() == g7.get_output()))


if __name__ == '__main__':
    main()
