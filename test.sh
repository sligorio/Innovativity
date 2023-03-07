 #genera file dove ogni riga rappresenta ip e ora, di ogni tentativo fallito di log
awk '{print $1, $2, $3, $(NF-3)}' getFailedLog > ~/test1

