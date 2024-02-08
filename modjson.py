import os, json
import ndjson
from pathlib import Path

#cwd gets the script execution folder
path_to_json = Path.cwd()
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.ndjson')]
for json_file in json_files:
    print(json_file)
    file = open(json_file)
    pathToNewFile = str(path_to_json) + '/processed/' + str(json_file)

    if os.path.exists(pathToNewFile):
        os.remove(pathToNewFile)
    newFile = open(pathToNewFile, 'w')
    # print(path_to_json + '/proccessed/' + json_file)
    max_stroke_for_word = 0
    for line in file:
        quick_draw = json.loads(line)
        total_stroke_count = len(quick_draw['drawing'])
        if total_stroke_count > max_stroke_for_word:
            max_stroke_for_word = total_stroke_count
        for i in range(total_stroke_count):
            quick_draw['strokeX' + str(i)] = quick_draw['drawing'][i][0]
            quick_draw['strokeY' + str(i)] = quick_draw['drawing'][i][1]
        del quick_draw['drawing']
        json.dump(quick_draw, newFile)
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
    #         accessor = 'stroke' + str(i)
    #         if accessor in quick_draw:
    #             continue
    #         quick_draw[accessor] = None
    #     json.dump(quick_draw, newPaddedFile)
    #     newPaddedFile.write('\n')


        