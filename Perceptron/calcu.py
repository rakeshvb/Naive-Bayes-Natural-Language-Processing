Res = []

with open("per_output1.txt") as nbout:
    for line in nbout:
        #find space in file as space divides label and file path
        space = line.find(" ")
        predictLabel = line[0:space]
        filePath = line[space+1:]
        fileName = filePath[filePath.rfind("/")+1:]
        if "ham" in fileName:
            actualLabel = "ham"
        else:
            actualLabel = "spam"

        Res = Res + [(predictLabel,actualLabel)]
confusionMatrix = [[0,0],[0,0]]
for result in Res:
    if(result[0] == result[1] == "ham"):
        confusionMatrix[0][0] = confusionMatrix[0][0] + 1
    elif(result[0] == result[1] == "spam"):
        confusionMatrix[1][1] = confusionMatrix[1][1] + 1
    elif(result[0] == "ham" and result[1] == "spam"):
        confusionMatrix[1][0] = confusionMatrix[1][0] + 1
    else:
        confusionMatrix[0][1] = confusionMatrix[0][1] + 1

print(confusionMatrix)
denomPrecisionHam=(confusionMatrix[0][0] + confusionMatrix[1][0])
denomRecallHam=(confusionMatrix[0][0] + confusionMatrix[0][1])
precisionHam = confusionMatrix[0][0] / denomPrecisionHam
recallHam = confusionMatrix[0][0] / denomRecallHam
fscoreHam = 2 * precisionHam * recallHam / (precisionHam + recallHam)
print("[HAM]Precision:{0}".format(precisionHam))
print("[HAM]Recall:{0}".format(recallHam))
print("[HAM]Fscore:{0}".format(fscoreHam))



denomPrecisionSpam=(confusionMatrix[1][1] + confusionMatrix[0][1])
denomRecallSpam=(confusionMatrix[1][1] + confusionMatrix[1][0])
precisionSpam = confusionMatrix[1][1] / denomPrecisionSpam
recallSpam = confusionMatrix[1][1] / denomRecallSpam
fscoreSpam = 2 * precisionSpam * recallSpam / (precisionSpam + recallSpam)
print("[SPAM]Precision:{0}".format(precisionSpam))
print("[SPAM]Recall:{0}".format(recallSpam))
print("[SPAM]Fscore:{0}".format(fscoreSpam))