from pyautocad import Autocad, APoint, aDouble

def main():

    acad = Autocad()
    doc = acad.ActiveDocument
    print(acad.doc.Name)

    acad.prompt("Hello Andrés, AutoCAD from Python\n")


    N = int(input("Número de bloques a dibujar: "))

    for i in range(N):

        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('')
        print('Bloque número {}'.format(i+1))

    # CREACIÓN DE LAYERS

        acad.doc.layers.Add("Ext1")
        Ext1 = acad.doc.layers.Item("Ext1")
        Ext1.color = 253

        acad.doc.layers.Add("Tub_Interf")
        Tub_Interf = acad.doc.layers.Item("Tub_Interf")
        Tub_Interf.color = 162

        acad.doc.layers.Add("Texto1")
        Texto1 = acad.doc.layers.Item("Texto1")
        Texto1.color = 18

    # CREACIÓN DE OBJETOS DE DIBUJO

        cE = aDouble(0,0,0,28,0,0,28,28,0,0,28,0,0,0,0)         # BORDE BLOQUE
        acad.model.AddPolyline(cE)

        t1 = APoint(9.91,24)            # ID
        text_head = int(input("Cruce número: "))
        acad.model.AddText(' CRUCE-1-%s' %text_head, t1, 1)

        t2 = APoint(11.39,17.80)            # DIAMETRO DE TUBERÍA 1
        text_tub = float(input("Diametro tubería 1: "))
        acad.model.AddText(' Ø%sm' %text_tub, t2, 1)

        t3 = APoint(9.84,16.01)            # RED
        text_red = "RED MATRIZ"
        acad.model.AddText(' %s' %text_red, t3, 1)

        t4 = APoint(10.39,14)           # TIPO DE RED EXISTENTE O PROYECTADO 1
        text_est = str(input("Tipo de red 1 (PROY o EXIST): "))
        acad.model.AddText(' %s' %text_est, t4, 1)

        t5 = APoint(11.46,7.15)            # DIAMETRO DE TUBERÍA 2
        text_tub2 = float(input("Diametro tubería 2: "))
        acad.model.AddText(' Ø%sm' %text_tub2, t5, 1)

        t6 = APoint(9.35,5.48)           # TIPO DE RED EXISTENTE O PROYECTADO 2
        text_est2 = str(input("Tipo de red 2 (PROY o EXIST): "))
        acad.model.AddText(' %s' %text_est2, t6, 1)

        t7 = APoint(11.16,3.81)           # TIPO DE SERVICIO - ESPECIALIDAD
        text_esp = str(input("Tipo de servicio - Especialidad: "))
        acad.model.AddText(' %s' %text_esp, t7, 1)

    # CREACIÓN DE TUBERÍAS

        pC1 = APoint(14,16.10)
        pC2 = APoint(14,16.10)
        acad.model.AddCircle(pC1,3.25)
        acad.model.AddCircle(pC2,3.45)
        # pC1.Offset(0.10)

        p1 = aDouble(8.48,9,0,19.52,9,0)
        p2 = aDouble(8.48,8.80,0,19.52,8.80,0)
        p3 = aDouble(8.48,3.23,0,19.52,3.23,0)
        p4 = aDouble(8.48,3,0,19.52,3,0)
        acad.model.AddPolyline(p1)
        acad.model.AddPolyline(p2)
        acad.model.AddPolyline(p3)
        acad.model.AddPolyline(p4)

        acad.model.AddSpline(aDouble([19.5200,8.8000,0.0000,19.0200,7.4000,0.0000,19.5200,6.0100,0.0000,20.0300,4.6200,0.0000,19.5200,3.2300,0.0000]), APoint(0,0), APoint(0,0))
        acad.model.AddSpline(aDouble([8.4700,8.8000,0.0000,7.9800,7.4000,0.0000,8.9000,4.6200,0.0000,8.4800,3.2300,0.0000]), APoint(0,0), APoint(0,0))


        # acad.model.AddDimAligned(APoint(14,19.35,0), APoint(14,8.8,0), APoint(20,20,0))
        # acad.model.AddDimAligned(APoint(14,12.65,0), APoint(14,9,0), APoint(14,10.82,0))



    print('')
    print('~~~~~~~~~~*******************~~~~~~~~~~~')
    print('Dibujo listo, por favor revise el AutoCAD ')
    print('----------\_____ (¬_¬) _____/----------')


if __name__ == '__main__':
    main()
