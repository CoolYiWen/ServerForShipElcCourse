#算法
from beans.Output import Output

def NeedCoefficientMethod(data, input):
    output = Output(data)
    output.p4 = input.p1 / input.e
    output.p5 = input.num * output.p4
    output.k1 = input.pmax / input.p1

    output.k31 = output.k1 * input.k21
    output.pn1 = output.k31 * input.k01 * output.p5
    output.bRun = True

    output.k32 = output.k1 * input.k22
    output.pn2 = output.k32 * input.k02 * output.p5
    output.bStartBack = True

    output.k33 = output.k1 * input.k23
    output.pn3 = output.k33 * input.k03 * output.p5
    output.bWaterWork = True

    output.k34 = output.k1 * input.k24
    output.pn4 = output.k34 * input.k04 * output.p5
    output.bStop = True

    if (output.p4 <= 0 and output.p5 <= 0 and output.k1 <= 0):
        return None
    else:
        if (output.k31 <= 0 or output.pn1 <= 0):
            output.k31 = -1
            output.pn1 = -1
            output.bRun = False

        if (output.k32 <= 0 or output.pn2 <= 0):
            output.k32 = -1
            output.pn2 = -1
            output.bStartBack = False

        if (output.k33 <= 0 or output.pn3 <= 0):
            output.k33 = -1
            output.pn3 = -1
            output.bWaterWork = False

        if (output.k34 <= 0 or output.pn4 <= 0):
            output.k34 = -1
            output.pn4 = -1
            output.bStop = False

        return output






