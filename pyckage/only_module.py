import logging
import os
import glob
import shutil

def transform(loglevel, resources, args):
    HERE = os.getcwd()

    logging.debug('[DEBUG] Welcome in pyckage. Now in only_module.transform')
    logging.debug('[DEBUG] Parsed arguments = {}'.format(args))
    logging.debug('[DEBUG] loglevel : {}, resources located in {}'.format(loglevel,resources))

    src = os.path.join(resources,"NAME")
    dst = os.path.join(os.getcwd(),args["name"])
    shutil.copytree(src, dst)

    os.chdir(dst) # In the newly created repo

    src = "NAME"
    dst = args["name"]
    os.rename(src, dst) # Renaming the subdirectory where all submodules are

    tojoin = [os.getcwd(),args["name"],"launchers","NAME_launcher.py"]
    src = os.path.join(*tojoin)
    tojoin = [os.getcwd(),args["name"],"launchers","{}_launcher.py".format(args["name"])]
    dst = os.path.join(*tojoin)

    logging.debug("[DEBUG] Src = {}, dst = {}".format(src,dst))

    os.rename(src, dst)

    corresp_dict = {
        "[NAME]":args["name"],
        "[VERSION]":args["version"],
        "[YEAR]":args["year"],
        "[AUTHOR]":args["author"],
        "[EMAIL]": args["email"],
        "[DESCRIPTION]":args["description"],
        "[LONG_DESCRIPTION]":args["long_description"],
        "[URL]":args["URL"],
    }

    logging.debug("[DEBUG] Corresp dict = {}".format(corresp_dict))

    for filename in glob.iglob('**',recursive=True):
        if os.path.isfile(filename):
            logging.debug('[DEBUG] Reformating {}'.format(filename))

            filin = open(filename,"r").read()
            for key in corresp_dict:
                filin = filin.replace(key,str(corresp_dict[key]))
            filout = open(filename,"w")
            filout.write(filin)
            filout.close()



    os.chdir(HERE)

    return
