import os


def get_upload_path(upload_path: str):
    while os.path.isfile(upload_path):
        if "_" in upload_path: 
            last_num = upload_path.split(".")[0].rsplit("_", 1)[-1]
            if last_num.isdigit(): # path ends with "_1" etc
                upload_path = upload_path.split(".")[0].rsplit("_", 1)[0] + f"_{int(last_num)+1}." + upload_path.split(".")[-1] 
            else:
                upload_path = upload_path.split(".")[0] + "_1." + upload_path.split(".")[-1]
        else: 
            upload_path = upload_path.split(".")[0] + "_1." + upload_path.split(".")[-1]
    return upload_path






    # if not os.path.isfile(upload_path):
    #     return upload_path
    # else:
    #     if "_" in upload_path:
    #         is_num = False

    #         end_num = upload_path.split(".")[0].rsplit("_", 1)[-1]
    #         try: 
    #             end_num = int(end_num) + 1
    #             is_num = True
    #         except:
    #             print("Not a end_num")
    #         if is_num:
                
            

