import logging
import os
import glob
import shutil

def transform(loglevel, resources, args):
    HERE = os.getcwd()

    logging.debug('[DEBUG] Welcome in pyckage. Now in only_module.transform')
    logging.debug('[DEBUG] Parsed arguments = {}'.format(args))
    logging.debug('[DEBUG] loglevel : {}, resources located in {}'.format(loglevel,resources))

    src = os.path.join(resources,"[NAME]")
    dst = os.path.join(os.getcwd(),args["name"])
    shutil.copytree(src, dst)

    os.chdir(dst)
    src = "NAME"
    dst = args["name"]
    os.rename(src, dst)

    src = os.path.join("launchers","NAME_launcher.py")
    dst = os.path.join("launchers","{}_launcher.py".format(args["name"]))
    os.rename(src, dst)

    corresp_dict = {
        "[NAME]":args["name"],
        "[VERSION]":args["version"],
        "[YEAR]":args["year"],
        "[AUTHOR]":args["author"],
        "[EMAIL]": args["email"],
        "[DESCRIPTION]":args["description"],
        "[LONG_DESCRIPTION]":args["long_decription"],
        "[URL]":args["url"],
        "[REQUIRES]":args["requirements"]
    }

    logging.debug("[DEBUG] Corresp dict = {}".format(corresp_dict))

    for filename in glob.iglob('**'):
        filin = open(filename,"r").read()



    os.chdir(HERE)

    return
