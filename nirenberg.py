#U:0, C:1, A:2. G:3

#표준 염기 코드
geneticCode = [
    [['Phe','Phe','Leu','Leu'],['Ser','Ser','Ser','Ser'],['Tyr','Tyr','0','0'],['Cys','Cys','0','Trp']],
    [['Leu','Leu','Leu','Leu'],['Pro','Pro','Pro','Pro'],['His','His','Gln','Gln'],['Arg','Arg','Arg','Arg']],
    [['Ile','Ile','Ile','Met'],['Thr','Thr','Thr','Thr'],['Asn','Asn','Lys','Lys'],['Ser','Ser','Arg','Arg']],
    [['Val','Val','Val','Val'],['Ala','Ala','Ala','Ala'],['Asp','Asp','Glu','Glu'],['Gly','Gly','Gly','Gly']]
]

dna = input('DNA 주형가닥의 염기서열을 입력해주세요.\n')

dna = list(dna)

rna = []

#전사
for b in dna:
    #트리플렛코드->코돈
    if b == 'A':
        rna.append(0) #U
    elif b == 'T':
        rna.append(2) #A
    elif b == 'C':
        rna.append(3) #G
    elif b == 'G':
        rna.append(1) #C

polypeptideArr = []

#번역
for i in range(len(rna)):
    #RNA의 첫 염기를 잘라낸다.
    del rna[0]
    polypeptide = []
    #rna의 길이가 코돈의 길이보다 작으면 실험을 중단한다.
    if len(rna)>=3:
        for j in range(len(rna)//3):
            k = j+1
            #코돈에 해당하는 염기를 가져와 폴리펩타이드에 결합한다.
            polypeptide.append(geneticCode[rna[3*k-3]][rna[3*k-2]][rna[3*k-1]])
        polypeptideArr.append(polypeptide)

#결과 확인
for i in range(len(polypeptideArr)):
    print(str(i+1)+': ',end='')
    for j,k in zip(polypeptideArr[i],range(len(polypeptideArr[i]))):
        print(j, end='')
        if k!= len(polypeptideArr[i])-1:
            print('-', end='')
    print('')

