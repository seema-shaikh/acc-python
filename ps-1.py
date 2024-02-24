'''
PS 1:
Given the input Json, candidate need to write a python script to update
“AudioGroupId” key with its corresponding name modifier “NameModifier”
For e.g.: if NameModifier is AAC_BIH/AAC_BIH
Then AudioGroupId should be AAC_BIH
'''

'''
Result is stored in q1_output.json
'''
import json

json_file = open("src\q1_input.json")
settings = json.load(json_file)["settings"]

def split_name_modifier(name_mod):
    return name_mod.split("/")[0] 

'''
    This Loop modifies the JSON
'''
for op_grp in settings["OutputGroups"] :
    if "CustomName" in op_grp and op_grp["CustomName"] == "HLS-DRM":
        for op in op_grp["Outputs"]:
            if "NameModifier" in op:
                audio_grp_id = split_name_modifier(op["NameModifier"])
                output_settings = op.get("OutputSettings")
                hlssettings = output_settings.get("HlsSettings")
                hlssettings.update({
                    "AudioGroupId" : audio_grp_id
                })
                settings.update(hlssettings)
    else:
        continue 

'''
    This loop ic to check if modification is done correctly
'''
for op_grp in settings["OutputGroups"] :
    if "CustomName" in op_grp and op_grp["CustomName"] == "HLS-DRM":
        for op in op_grp["Outputs"]:
            if "NameModifier" in op:
                audio_grp_id = split_name_modifier(op["NameModifier"])
                output_settings = op.get("OutputSettings")
                hlssettings = output_settings.get("HlsSettings")
                print(f"Changed from {op['NameModifier']} to {hlssettings['AudioGroupId']}")
    else:
        continue 


json_object = json.dumps({
    "settings": settings
}, indent=4 )

with open("q1_output.json", "w") as outfile:
    outfile.write(json_object)

