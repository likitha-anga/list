magic_square=[[8,3,5,2],
             [1,5,9,5],
            [6,7,2,2],
            [5,6,7,8]]
             
i=0
while i<len(magic_square):
    row=0
    column=0
    j=0
    while j<len(magic_square):
        row=row+magic_square[i][j]
        column=column+magic_square[j][i]
        d=0
        while d<len(magic_square):
            d1=0
            d2=0
            c=0
            while c<len(magic_square):
                d1=d1+magic_square[d][c]
                d2=d2+magic_square[c][d]
                d1=d2
                c+=1
            d+=1
        j+=1
    i+=1
print("row",row)
print("column",column)
print("decimal",d1)
if row==column==d1:
    print("it is a magic_square")
else:
    print("it is not a magic square")