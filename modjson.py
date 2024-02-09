import os, json
from pathlib import Path

#cwd gets the script execution folder
path_to_json = Path.cwd()
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('snowman.ndjson')]

def transformJSON(line, max_strokes_count, max_stroke_length):
    # print(path_to_json + '/proccessed/' + json_file)
    quick_draw = json.loads(line)
    if quick_draw['recognized'] == False:
        return None        
    total_stroke_count = len(quick_draw['drawing'])
    if total_stroke_count > max_strokes_count:
        return None
    # For now, we will loop to the total_stroke_count limit for padding upto it
    for i in range(max_strokes_count):
        total_length_of_stroke = len(quick_draw['drawing'][0])
        if total_length_of_stroke > max_stroke_length:
            return None
        for j in range(max_stroke_length):
            xData = -1
            if i < total_stroke_count and j < total_length_of_stroke:
                xData = quick_draw['drawing'][i][0][j]
            yData = -1
            if i < total_stroke_count and j < total_length_of_stroke:
                yData = quick_draw['drawing'][i][1][j]
            quick_draw['strokeX' + str(i) + '_' + str(j)] = xData
            quick_draw['strokeY' + str(i) + '_' + str(j)] = yData
    del quick_draw['drawing']
    return quick_draw
   

for json_file in json_files:
    print(json_file)
    file = open(json_file)
    pathToNewFile = str(path_to_json) + '/processed/' + str(json_file)

    if os.path.exists(pathToNewFile):
        os.remove(pathToNewFile)
    newFile = open(pathToNewFile, 'w')
    for line in file:
        newJson = transformJSON(line, 10, 20)
        if newJson == None:
            continue
        json.dump(newJson, newFile)
        newFile.write('\n')
    newFile.close()

    # pathToNewPaddedFile = str(path_to_json) + '/processed_padded/' + str(json_file)
    # newFile = open(pathToNewFile)
    # if os.path.exists(pathToNewPaddedFile):
    #     os.remove(pathToNewPaddedFile)
    # newPaddedFile = open(pathToNewPaddedFile, 'w')
    # for line in newFile:
    #     quick_draw = json.loads(line)
    #     for i in range(max_stroke_for_word):
    #         for j in range(20):
    #             accessorX = 'strokeX' + str(i) + '_' + str(j)
    #             accessorY = 'strokeY' + str(i) + '_' + str(j)
    #             if accessorX in quick_draw:
    #                 continue
    #             quick_draw[accessorX] = -1
    #             quick_draw[accessorY] = -1
    #     json.dump(quick_draw, newPaddedFile)
    #     newPaddedFile.write('\n')


        