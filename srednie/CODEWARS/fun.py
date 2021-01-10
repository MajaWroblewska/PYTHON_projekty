TURKISH = """\
                               sıfırMbirMikiM
                         üçMdörtMbeşMaltıMyediMsekiz
                    MdokuzMonMon#birMon#ikiMon#üçMon#dör
                 tMon#beşMon#altıMon#yediMon#sekizMon#dokuz
               MyirmiMyirmi#birMyirmi#ik               iMyirmi
             #üçMyirmi#dörtMyirmi#                          be
           şMyirmi#altıMyirmi#y
         ediMyirmi#sekizMyir
        mi#dokuzMotuzMotuz
       #birMotuz#ikiMotu
      z#üçMotuz#dörtMot
     uz#beşMotuz#altıM                                   ot
    uz#yediMotuz#seki                                   zMot
    uz#dokuzMkırkMkı                                   rk#bir
   Mkırk#ikiMkırk#ü                                   çMkırk#d
   örtMkırk#beşMkır                           k#altıMkırk#yediMkırk#se
   kizMkırk#dokuzM                            elliMelli#birMelli#ikiMe
   lli#üçMelli#dör                             tMelli#beşMelli#altıMe
  lli#yediMelli#se                               kizMelli#dokuzMalt
   mışMaltmış#birM                                 altmış#ikiMalt
   mış#üçMaltmış#d                                 örtMaltmış#beş
   Maltmış#altıMalt                                mış#yediMaltmı
   ş#sekizMaltmış#d                               okuzMy    etmişM
    yetmiş#birMyetmi                              ş#            ik
    iMyetmiş#üçMyetmi
     ş#dörtMyetmiş#beş
      Myetmiş#altıMyetm
       iş#yediMyetmiş#sek
        izMyetmiş#dokuzMsek
         senMseksen#birMsekse
           n#ikiMseksen#üçMsekse                              n#
             dörtMseksen#beşMseksen#                      altıMs
               eksen#yediMseksen#sekizMsekse      n #dokuzMdok
                 sanMdoksan#birMdoksan#ikiMdoksan#üçMdoksan
                    #dörtMdoksan#beşMdoksan#altıMdoksan#
                        yediMdoksan#sekizMdoksan#dok
                               uzMMMMMMMMMMMM"""

print(get_turkish_number = TURKISH.replace(" ","").replace("\n","").replace("#"," ").strip().split("M").__getitem__)