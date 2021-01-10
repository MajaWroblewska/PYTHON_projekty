BMI=20.703124999999996
print("Twoje BMI wynosi %f." % BMI)

print("Twoje BMI wynosi {:f}".format(BMI))

print("Twoje BMI wynosi", round(BMI,3))

print("1 po angielsku: {} \n2 po angielsku: {}".format('one', 'two'))
print("1 po angielsku: %s \n2 po angielsku: %s" % ('one', 'two'))

szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| %6.3f | %-16s | %-10s |" % (9.58, "Usain Bolt", "16.08.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Tyson Gay", "20.09.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Yohan Blake", "23.09.2012"))
print("| %-6.1f | %16s | %10s |" % (9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)

szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.58, "Usain Bolt", "16.08.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Tyson Gay", "20.09.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Yohan Blake", "23.09.2012"))
print("| {:6.1f} | {:16s} | {:10s} |" .format(9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)

print('{:,d}'.format(1234567890))
print('{:,f}'.format(1234567890))
print('{:,}'.format(1234567890))

print('{:,}'.format(528434682).replace(',', ' '))

print()
waluta = "dolar"
us = 1
pln = 4.08234915
print("Aktualnie %d %s kosztuje %.2f zł" % (us, waluta, pln))
print("Aktualnie %r %r kosztuje %r zł" % (us, waluta, pln))
print()

print("Rekord świata na 100m to {:.2f} ustanowił go {}".format(9.5877, 'Usain Bolt'))
print()

print("Moja {} o wadze {}g ma ok. {} kcal i {:.5f} węglowodanów".format('czekolada', 100, 545, 58.543210))

