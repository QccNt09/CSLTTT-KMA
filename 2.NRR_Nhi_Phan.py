
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
    print('1. đơn vị BIT')
    print('2. đơn vị HART')
    chon = int(input())
    print('p(a1) = ', pa1)
    print('p(a2) = ', pa2)
    print('p(b1) = ', pb1)
    print('p(b2) = ', pb2)
    print('-------------------------------------')
    print('p(a1/b1) = ', pa1_b1)
    print('p(a2/b1) = ', pa2_b1)
    print('p(a2/b2) = ', pa2_b2)
    print('p(a1/b2) = ', pa1_b2)
    if( chon == 1):
        print('-------------------------------------')
        print('I(a1/b1) = ', Ia1_b1_BIT, '[bit]')
        print('I(a1/b2) = ', Ia1_b2_BIT, '[bit]')
        print('I(a2/b2) = ', Ia2_b2_BIT, '[bit]')
        print('I(a2/b1) = ', Ia2_b1_BIT, '[bit]')
        print('-------------------------------------')
        print('I(AB) = ', IAB_BIT, '[bit]')
        print('-------------------------------------')
        print('I(a1b1) = ', Ia1b1_BIT, '[bit]')
        print('I(a2b2) = ', Ia2b2_BIT, '[bit]')
        print('-------------------------------------')
        print('I(A,b1) = ', Ia_b1_BIT, '[bit]')
        print('I(A,b2) = ', Ia_b2_BIT, '[bit]')
        print('-------------------------------------')
        print('H(A) = ', HA_BIT, '[bit]')
        print('H(B) = ', HB_BIT, '[bit]')
        print('--------------------------------------')
        print('H(A/B) = ', HA_B_BIT, '[bit]')
        print('H(B/A) = ', HB_A_BIT, '[bit]')
        print('-------------------------------------')
        print('H(AB) = ', HAB_BIT, '[bit]')
        print('--------------------------------------')
        print('H(A/b1) = ', HA_b1_BIT, '[bit]')
        print('H(A/b2) = ', HA_b2_BIT, '[bit]')
    else:
        print('----------------------------------------')
        print('I(a1/b1) = ', Ia1_b1_HART, '[Hart]')
        print('I(a1/b2) = ', Ia1_b2_HART, '[Hart]')
        print('I(a2/b2) = ', Ia2_b2_HART, '[Hart]')
        print('I(a2/b1) = ', Ia2_b1_HART, '[Hart]')
        print('-------------------------------------')
        print('I(AB) = ', IAB_HART, '[Hart]')
        print('--------------------------------------')
        print('I(a1b1) = ', Ia1b1_HART, '[Hart]')
        print('I(a2b2) = ', Ia2b2_HART, '[Hart]')
        print('--------------------------------------')
        print('I(A,b1) = ', Ia_b1_HART, '[Hart]')
        print('I(A,b2) = ', Ia_b2_HART, '[Hart]')
        print('-------------------------------------')
        print('H(A) = ', HA_HART, '[Hart]')
        print('H(B) = ', HB_HART, '[Hart]')
        print('H(AB) = ', HAB_HART, '[Hart]')
        print('--------------------------------------')
        print('H(A/B) = ', HA_B_HART, '[Hart]')
        print('H(B/A) = ', HB_A_HART, '[Hart]')
        print('--------------------------------------')
        print('H(A/b1) = ', HA_b1_HART, '[Hart]')
        print('H(A/b2) = ', HA_b2_HART, '[Hart]')


    # Tính thông lượng của kênh
    vk = float(input('Nhap Vk: '))
    c_phay = vk*(1-round(HB_A_BIT,5))
    print('Thong luong cua kenh la: ',c_phay)


if __name__ == '__main__':
    xs_pa1_tu=int(input('Nhap xs p(a1) Tu so = '))
    xs_pa1_mau=int(input('Nhap xs p(a1) Mau so = '))
    xsThuDung_tu=int(input('Nhap xs thu dung Tu so = '))
    xsThuDung_mau=int(input('Nhap xs thu dung Mau so = '))
    NRR_nhi_phan(xs_pa1_tu,xs_pa1_mau,xsThuDung_tu,xsThuDung_mau)