def actualise(indiceAction, messageServ):
    listeAction = []
    if not indiceAction == -2:
        indice = indiceAction
        chiffre = ""
        i = -1
        while messageServ[i] != '+':
            chiffre += messageServ[i]
            i -= 1
        chiffre = int(chiffre[::-1])
        chaineServ = messageServ[:i]

        if not int(indice) == chiffre:
            if indice == -2:
                chaineServ = chaineServ[0:]
            else:
                chaineServ = chaineServ[indice+1:]
            if len(chaineServ) > 2:
                if not chaineServ == '-':
                    if chaineServ[0] == '-':
                        chaineServ = chaineServ[1:]
                    txt = ""
                    for i in chaineServ:
                        if i == '-':
                            listeAction.append(txt)
                            txt = ""
                        else:
                            txt += i
        indiceAction = chiffre

    return listeAction, indiceAction

