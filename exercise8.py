def vokon_zählen(wort):
    vokale = "aeiou"
    wort_lower = wort.lower
    bn = [i for i in wort.lower if i.isalpha]
    vn = [k for k in wort_lower if k in vokalen]
<    print (f"""Es gibt im Wort "{wort}" {len(vn)}Vokale und [len(bn) - ])
           
vokon_zählen("Berlin")