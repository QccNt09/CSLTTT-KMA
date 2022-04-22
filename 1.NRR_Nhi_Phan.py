
from fractions import Fraction
from math import log2,log10, perm
def NRR_nhi_phan(xs_pa1_tu,xs_pa1_mau,xsThuDung_tu,xsThuDung_mau):
    pa1 = Fraction(xs_pa1_tu,xs_pa1_mau)  # xs xuất hiện biến cố a1

    pa2 = 1-pa1

    

    pb1_a1 = pb2_a2 = Fraction(xsThuDung_tu,xsThuDung_mau)  # xs thu đúng
    pb1_a2 = pb2_a1 = 1-pb1_a1  # xs thu sai


    pa1_b1 = Fraction((pa1*pb1_a1), (pa1*pb1_a1)+(pa2*pb1_a2))  # p(a1/b1)


    pa2_b1 = 1-pa1_b1  # p(a2/b1)

    pa2_b2 = Fraction((pa2*pb2_a2), (pa1*pb2_a1)+(pa2*pb2_a2))  # p(a2/b2)


    pa1_b2 = 1-pa2_b2  # p(a1/b2)

    pa1b1 = pa1 * pb1_a1    # p(a1b1) 
    pa1b2 = pa1 * pb2_a1    # p(a1b2)
    pa2b1 = pa2 * pb1_a2    # p(a2b1)
    pa2b2 = pa2 * pb2_a2    # p(a2b2)

    pb1 = pa1*pb1_a1 + pa2*pb1_a2 #p(b1)
    pb2 = 1 - pb1                 #p(b2)

    Ia1_b1_BIT = -log2(pa1_b1) # I(a1/b1)
    Ia1_b2_BIT = -log2(pa1_b2) # I(a1/b2)
    Ia2_b2_BIT = -log2(pa2_b2) # I(a2/b2)
    Ia2_b1_BIT = -log2(pa2_b1) # I(a2/b1)

    Ia1b1_BIT = -log2(pa1/pa1_b1) # I(a1b1)
    Ia2b2_BIT = -log2(pa2/pa2_b2) # I(a2b2)

    Ia_b1_BIT = pa1_b1*log2(pa1_b1/pa1) + pa2_b1*log2(pa2_b1/pa2) #I(A,b1)
    Ia_b2_BIT = pa1_b2*log2(pa1_b2/pa1) + pa2_b2*log2(pa2_b2/pa2) #I(A,b2)



    Ia1_b1_HART = -log10(pa1_b1) # I(a1/b1)
    Ia1_b2_HART = -log10(pa1_b2) # I(a1/b2)
    Ia2_b2_HART = -log10(pa2_b2) # I(a2/b2)
    Ia2_b1_HART = -log10(pa2_b1) # I(a2/b1)

    Ia1b1_HART = -log10(pa1/pa1_b1) # I(a1b1)
    Ia2b2_HART = -log10(pa2/pa2_b2) # I(a2b2)

    Ia_b1_HART = pa1_b1*log10(pa1_b1/pa1) + pa2_b1*log10(pa2_b1/pa2) #I(A,b1)
    Ia_b2_HART = pa1_b2*log10(pa1_b2/pa1) + pa2_b2*log10(pa2_b2/pa2) #I(A,b2)

     

    HA_b1_BIT = -(pa1_b1*log2(pa1_b1)+pa2_b1*log2(pa2_b1))
    HA_b2_BIT = -(pa1_b2*log2(pa1_b2)+pa2_b2*log2(pa2_b2))
    HA_B_BIT=-(pa1b1*log2(pa1_b1)+pa1b2*log2(pa1_b2)+pa2b2*log2(pa2_b2)+pa2b1*log2(pa2_b1)) # H(A/B)
    HB_A_BIT=-(pa1b1*log2(pb1_a1)+pa1b2*log2(pb1_a2)+pa2b2*log2(pb2_a2)+pa2b1*log2(pb2_a1)) # H(B/A)

    HA_b1_HART = -(pa1_b1*log10(pa1_b1)+pa2_b1*log10(pa2_b1))
    HA_b2_HART = -(pa1_b2*log10(pa1_b2)+pa2_b2*log10(pa2_b2))
    HA_B_HART=-(pa1b1*log10(pa1_b1)+pa1b2*log10(pa1_b2)+pa2b2*log10(pa2_b2)+pa2b1*log10(pa2_b1)) # H(A/B)
    HB_A_HART=-(pa1b1*log10(pb1_a1)+pa1b2*log10(pb1_a2)+pa2b2*log10(pb2_a2)+pa2b1*log10(pb2_a1)) # H(B/A)
    
    HA_BIT = -(pa1*log2(pa1) + pa2*log2(pa2))
    HB_BIT = -(pb1*log2(pb1)+pb2*log2(pb2))

    HA_HART = -(pa1*log10(pa1) + pa2*log10(pa2))
    HB_HART = -(pb1*log10(pb1)+pb2*log10(pb2))

    IAB_BIT = HA_BIT - HA_B_BIT
    IAB_HART = HA_HART - HA_B_HART
    
    HAB_BIT = HA_BIT + HB_A_BIT
    HAB_HART = HA_HART + HB_A_HART

    print('p(a1) = ', pa1)
    print('p(a2) = ', pa2)
    print('p(b1) = ', pb1)
    print('p(b2) = ', pb2)
    print('-------------------------------------')
    print('p(a1/b1) = ',pa1_b1)
    print('p(a2/b1) = ',pa2_b1)
    print('p(a2/b2) = ',pa2_b2)
    print('p(a1/b2) = ',pa1_b2)
    print('-------------------------------------')
    print('p(a1b1) = ',pa1b1)
    print('p(a1b2) = ',pa1b2)
    print('p(a2b1) = ',pa2b1)
    print('p(a2b2) = ',pa2b2)
    print('-------------------------------------')
    print('I(a1/b1) don vi bit = ',Ia1_b1_BIT) 
    print('I(a1/b2) don vi bit = ',Ia1_b2_BIT) 
    print('I(a2/b2) don vi bit = ',Ia2_b2_BIT)
    print('I(a2/b1) don vi bit = ',Ia2_b1_BIT)
    print('-------------------------------------')
    print('I(AB) don vi bit = ',IAB_BIT) 
    print('I(AB) don vi hart = ',IAB_HART) 
    print('--------------------------------------')
    print('I(a1b1) don vi bit = ',Ia1b1_BIT) 
    print('I(a2b2) don vi bit = ',Ia2b2_BIT) 
    print('--------------------------------------')
    print('I(A,b1) don vi BIT = ', Ia_b1_BIT)
    print('I(A,b2) don vi BIT = ', Ia_b2_BIT)
    print('----------------------------------------')
    print('I(a1/b1) don vi hart = ',Ia1_b1_HART) 
    print('I(a1/b2) don vi hart = ',Ia1_b2_HART) 
    print('I(a2/b2) don vi hart = ',Ia2_b2_HART)
    print('I(a2/b1) don vi hart = ',Ia2_b1_HART)
    print('--------------------------------------')
    print('I(a1b1) don vi hart = ',Ia1b1_HART) 
    print('I(a2b2) don vi hart = ',Ia2b2_HART) 
    print('--------------------------------------')
    print('I(A,b1) don vi hart = ', Ia_b1_HART)
    print('I(A,b2) don vi hart = ', Ia_b2_HART)
    print('-------------------------------------')
    print('H(A) don vi BIT = ', HA_BIT)
    print('H(B) don vi BIT = ', HB_BIT)
    print('-------------------------------------')
    print('H(A) don vi HART = ', HA_HART)
    print('H(B) don vi HART = ', HB_HART)
    print('--------------------------------------')
    print('H(A/b1) don vi bit = ',HA_b1_BIT)
    print('H(A/b2) don vi bit = ',HA_b2_BIT)
    print('--------------------------------------')
    print('H(A/b1) don vi hart = ',HA_b1_HART)
    print('H(A/b2) don vi hart = ',HA_b2_HART)
    print('--------------------------------------')
    print('H(A/B) don vi bit = ',HA_B_BIT)
    print('H(B/A) don vi bit = ',HB_A_BIT)
    print('--------------------------------------')
    print('H(A/B) don vi hart = ',HA_B_HART)
    print('H(B/A) don vi hart = ',HB_A_HART)
    print('-------------------------------------')
    print('H(AB) don vi bit = ',HAB_BIT)
    print('H(AB) don vi hart = ',HAB_HART)
    
    
    
    

    # Tính thông lượng của cây
    # vk = float(input('Nhap Vk: '))
    # c_phay = vk*(1-round(HB_A_BIT,5))
    # print('Thong luong cua kenh la: ',c_phay)


if __name__ == '__main__':
    xs_pa1_tu=int(input('Nhap xs p(a1) Tu so = '))
    xs_pa1_mau=int(input('Nhap xs p(a1) Mau so = '))
    xsThuDung_tu=int(input('Nhap xs thu dung Tu so = '))
    xsThuDung_mau=int(input('Nhap xs thu dung Mau so = '))
    NRR_nhi_phan(xs_pa1_tu,xs_pa1_mau,xsThuDung_tu,xsThuDung_mau)